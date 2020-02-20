FROM ubuntu:18.04
RUN adduser --quiet --disabled-password qtuser
RUN apt-get update \
    && apt-get install -y \
      python3 \
      python3-pyqt5 \
      python3-pip \
      netcat
RUN pip3 install mysql-connector-python
RUN mkdir /newwishlist
WORKDIR /newwishlist
COPY . /newwishlist
RUN chmod +x ./wait-for-mysql.sh