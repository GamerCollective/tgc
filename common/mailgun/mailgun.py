from __future__ import unicode_literals

import logging

from django.conf import settings
from django.template.loader import get_template
import requests


logger = logging.getLogger(__name__)


API_AUTH = ("api", settings.MAILGUN_API_KEY)
PUB_AUTH = ("api", "pubkey-8efe21120b21f848a874747c075c6183")


class Domain(object):
    _base_url = "https://api.mailgun.net/v3/{domain}/"

    def __init__(self, domain, *args, **kwargs):
        """
        Args:
            domain (str): The domain name to send the email from (email.offerup.com, etc.).
            args (list): variable list of arguments
            kwargs (dict): variable dictionary of keyword arguments
        """
        self.domain = domain
        _url = self._base_url.format(domain=domain)
        self.messages = _url + "messages"
        self.events = _url + "events"
        self.stats = _url + "stats"
        self.stats_total = self.stats + "/total"
        self.tags = _url + "tags"
        self.blocking_flag_ids = kwargs.get('blocking_flag_ids', set())

    @staticmethod
    def is_valid_header(key):
        return key.startswith('h:')

    @staticmethod
    def is_valid_custom_json(key):
        return key.startswith('v:')

    @staticmethod
    def is_valid_param(key):
        valid_mailgun_params = {
            "from", "to", "cc", "bcc", "subject", "text", "html", "attachment", "inline", "o:tag", "o:campaign",
            "o:dkim", "o:deliverytime", "o:testmode", "o:tracking", "o:tracking-clicks", "o:tracking-opens",
            "o:require-tls", "o:skip-verification"
        }
        return key in valid_mailgun_params

    def is_valid_key(self, key):
        return any((self.is_valid_custom_json(key), self.is_valid_header(key), self.is_valid_param(key)))

    def validate_data(self, data):
        for key, _ in data.items():
            if not self.is_valid_key(key):
                raise ValueError('Passed invalid field for message: {}'.format(key))
        for required in ['to', 'from', 'subject', 'html']:
            if required not in data:
                raise ValueError('Missing required field: {}'.format(required))

    @staticmethod
    def _format_message_body(template, context):
        t = get_template(template)
        return t.render(context)

    def format_message_body(self, data, context):
        if "text" in data:
            data["text"] = self._format_message_body(data["text"], context)
        data["html"] = self._format_message_body(data["html"], context)
        return data

    def send_complex_message(self, data, context):
        """
        Simple wrapper function for sending an email via the Mailgun API. This function is for sending emails that
        require rendering of the email template (it has some of {{these}}).

        Args:
            data (dict): Dictionary containing relevant info for sending the email. Note that the ``text`` and ``html``
                fields are paths to templates that will be rendered. If this isn't what you need i.e. You are sending a
                completely static email (there are none of {{these}} in the template) use ``send_simple_message()``.

                    data = {
                        "to": "ian.auld@offerupnow.com",
                        "from": "Sender sender@email.com",
                        "subject": "Join Me on OfferUp",
                        "text": "emails/invite_email.txt",
                        "html": "emails/invite_email.html",
                        "v:userID": 1234
                    }

            context (dict): A standard Django style context dict. Contains keys/values ot be inserted into templates.

        Returns:
            requests.Response
        """
        self.validate_data(data)
        data = self.format_message_body(data, context)
        return self._send(data)

    def send_simple_message(self, data):
        """
        Wrapper function for sending a static email via the Mailgun API. This function is for sending emails that are
        static and require no rendering (they have none of {{these}})

        Args:
            data (dict): Dictionary containing relevant info for sending the email. Note that the ``text`` and ``html``
                fields are the full content fo the body. If this isn't what you need i.e. You are sending a
                dynamic email (there are some of {{these}} in the template) use ``send_complex_message()`` instead.

                    data = {
                        "to": "ian.auld@offerupnow.com",
                        "from": "invite@offerup.com",
                        "subject": "Join Me on OfferUp",
                        "text": "The body of your email goes here!",
                        "html": "<html>HTML version of the body</html>",
                        "v:userID": 1234
                    }

        Returns:
            requests.Response
        """
        self.validate_data(data)
        return self._send(data)

    @staticmethod
    def _is_active_user(user_id):
        """
        Checks if a user is active (not banned/disabled).

        Returns:
            bool
        """
        return True

    def user_id_can_receive_emails(self, user_id):
        """
        Returns a boolean indicating whether or not the user can receive emails.
        Args:
            user_id (int): User ID

        Returns:
            bool
        """
        return self._is_active_user(user_id)

    @staticmethod
    def _respond_with_403(msg):
        resp = requests.Response()
        resp.status_code, resp._content = 403, msg
        return resp

    def _send(self, data):
        """
        Does the actual sending of data to the Mailgun API. Ensures the recipient is not blocked from receiving email.

        Args:
            data (dict): A dictionary containing all pertinent data

        Returns:
            requests.Response
        """
        if all(API_AUTH):
            user_id = data.get("v:userID")
            if self.user_id_can_receive_emails(user_id):
                try:
                    return requests.post(self.messages, auth=API_AUTH, data=data)
                except requests.ConnectionError as err:
                    msg = "coudn't send mail: %s" % err
                    logger.error(msg)
            else:
                msg = 'user %s has blocking email flags. Mail not sent!'
                logger.warn(msg, user_id)
        else:
            msg = "Couldn't send email. Missing API authentication key!"
            logger.error(msg)
        return self._respond_with_403(msg)

    def get_tags(self):
        resp = requests.get(self.tags, auth=API_AUTH)
        return resp.json()

    def get_tag(self, tag):
        """
        Returns a given tag.

        Args:
            tag (str): The tag name

        Returns:
            (dict)
        """
        url = self.tags + "/{}".format(tag)
        resp = requests.get(url, auth=API_AUTH)
        return resp.json()

    def update_tag(self, tag, description):
        """
        Updates a given tag with the information provided.

        Args:
            tag (str): The tag name
            description (str): The new description for the tag

        Returns:
            dict
        """
        url = self.tags + "/{}".format(tag)
        data = {'description': description}
        resp = requests.put(url, auth=API_AUTH, data=data)
        return resp.json()

    def get_tag_stats(self, tag, params):
        """
        Returns statistics for a given tag.

        Args:
            tag (str): The tag name
            params (dict): A dictionary of parameters to filter stats:
                {
                    "event": (Required) The type of the event. For a complete list of all events written to the log see
                             the Event Types table here: https://documentation.mailgun.com/api-tags.html#event-types
                    "start": The starting time. Should be in RFC 2822 or unix epoch format.
                             Default: 7 days from the current time.
                    "end": The ending date. Should be in RFC 2822 or unix epoch time in seconds. Default: current time.
                    "resolution": Can be either hour, day or month. Default: day
                    "duration": Period of time with resolution encoded. See Duration for more info. If provided,
                                overwrites the start date and resolution.
                }

        Returns:
            dict
        """
        url = self.tags + "/{}/stats".format(tag)
        resp = requests.get(url, auth=API_AUTH, params=params)
        return resp.json()
