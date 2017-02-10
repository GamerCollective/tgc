FROM python:2.7
MAINTAINER Ian Auld <imauld@gmail.com>


RUN apt-get update && apt-get install -y \
    git \
    python-dev \
    python-setuptools \
    nginx \
    supervisor \
    sqlite3 \
  && rm -rf /var/lib/apt/lists/*

# install uwsgi now because it takes a little while
RUN pip install uwsgi

# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY nginx-app.conf /etc/nginx/sites-available/default
COPY supervisor-app.conf /etc/supervisor/conf.d/

# COPY requirements.txt and RUN pip install BEFORE adding the rest of your code, this will cause Docker's caching mechanism
# to prevent re-installing (all your) dependencies when you change a line or two in your app.
COPY requirements.txt /home/docker/tgc/
RUN pip install -r /home/docker/tgc/requirements.txt

# add (the rest of) our code
COPY . /tgc

EXPOSE 80
CMD ["supervisord", "-n"]
