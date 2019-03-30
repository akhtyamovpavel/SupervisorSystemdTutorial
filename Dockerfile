from ubuntu:bionic

label maintainer=akhtyamovpavel@gmail.com

run apt-get update && apt-get install -y python python-dev python-pip openssh-server vim curl cron
run apt-get install -y openssh-server

run pip install supervisor

expose 22

run pip install jupyter

run useradd --create-home --shell /bin/bash test
run pip install requests
user test

add credentials.py /home/test/credentials.py
add check_jupyter.py /home/test/check_jupyter.py
expose 2288
user root
cmd supervisord -c /etc/supervisor/supervisord.conf && bash
