FROM ubuntu:22.04

#NOTE ADD NAOQI FOLDER TO FOLDER WITH DOCKERFILE. TOO LARGE FOR GITHUB
COPY pynaoqi-python2.7-2.5.7.1-linux64.tar.gz /root/

RUN apt update

#Python 2 Setup
RUN apt -y install python2.7
RUN apt -y install python2.7-dev

#naoqi Setup
#RUN tar -xvzf pynaoqi-python2.7-2.5.7.1-linux64.tar.gz


#Python 3 Setup
