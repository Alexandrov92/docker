FROM ubuntu:22.04

RUN apt-get -y update
RUN apt-get -y install apache2

COPY . /var/www/html
WORKDIR /var/www/html


CMD ["/usr/sbin/apache2ctl", "-DFOREGROUND"]
EXPOSE 80

