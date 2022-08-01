FROM debian:latest

RUN apt-get update -y && apt-get upgrade -y
RUN apt install -y openssh-server &&\
	apt install -y python3-pip &&\
	apt install -y sudo &&\
	apt install -y vim &&\
	apt install -y git

RUN pip install --upgrade pip
RUN pip install cryptography

RUN useradd -m admin
RUN usermod -s /bin/bash admin
RUN usermod -aG sudo admin

RUN echo "admin:42madrid" | chpasswd

RUN mkdir -p /home/admin/

#USER admin

ENTRYPOINT service ssh start; bash;
