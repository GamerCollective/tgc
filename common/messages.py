from __future__ import unicode_literals

from collections import namedtuple
from django.contrib import messages


# Correspond to CSS classes for bootstrap
ALERT_SUCCESS = "alert-success"
ALERT_INFO = "alert-info"
ALERT_WARNING = "alert-warning"
ALERT_DANGER = "alert-danger"

alert_levels = namedtuple("AlertLevels", ["success", "info", "warning", "danger"])(
    ALERT_SUCCESS,
    ALERT_INFO,
    ALERT_WARNING,
    ALERT_DANGER,
)


def success(request, message, **kwargs):
    messages.success(request, message, extra_tags=alert_levels.success)


def info(request, message, **kwargs):
    messages.success(request, message, extra_tags=alert_levels.info)


def warning(request, message, **kwargs):
    messages.success(request, message, extra_tags=alert_levels.warning)


def danger(request, message, **kwargs):
    messages.success(request, message, extra_tags=alert_levels.danger)


def strong(text):
    return "<strong>{}</strong>".format(text)


def anchor(href, text):
    return "<a href=\"{}\">{}</a>".format(href, text)
