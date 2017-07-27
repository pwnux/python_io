# khainguyen
# Dockerfile
#
FROM ubuntu:14.04
MAINTAINER khainguyen "khainguyenptiter@gmail.com"

RUN apt-get -y update

RUN apt-get install -y gcc g++ python3-dev libssl-dev \
    libxml2-dev libxslt1-dev libffi-dev \
    libmysqlclient-dev python3-pip\
    libtiff5-dev libjpeg8-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev \
    tcl8.6-dev tk8.6-dev python3-tk wget

RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 -C /usr/local/share/
RUN ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
WORKDIR /crawl_training
CMD scrapy crawl hust

