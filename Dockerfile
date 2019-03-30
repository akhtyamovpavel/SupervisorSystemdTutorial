from ubuntu:bionic

label maintainer=akhtyamovpavel@gmail.com

run apt-get update && apt-get install -y python python-dev python-pip openssh-server vim curl cron
run apt-get install -y openssh-server

run pip install supervisor

expose 22

run pip install jupyter

cmd supervisord -c /etc/supervisor/supervisord.conf && bash
