FROM postgres:15.2

RUN apt-get update && apt-get -y install cron nano

COPY init/cron.sh /etc/cron.d/cron.sh

RUN chmod 0644 /etc/cron.d/cron.sh

RUN crontab /etc/cron.d/cron.sh