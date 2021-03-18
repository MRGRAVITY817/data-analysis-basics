FROM ubuntu:20.04
LABEL AUTHOR="Wee Seong Hoon:<mrgravity817@gmail.com>"

RUN sed -i 's/kr.archive.ubuntu.com/mirror.kakao.com/g' /etc/apt/sources.list
ADD pip.conf /root/.pip/pip.conf

RUN apt-get update && \ 
  apt-get install -y python3-pip python3-dev && \
  apt-get clean && \
  pip3 install --upgrade pip

RUN pip3 install numpy


CMD ["python3"]