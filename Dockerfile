ARG BASE_IMAGE=daisukekobayashi/darknet:gpu-cv
FROM $BASE_IMAGE
ENV DEBIAN_FRONTEND noninteractive
ARG SERVER_FONFIG
ENV SERVER_CONFIG ${SERVER_CONFIG:-./config.py}

RUN apt update \
    apt install python3 python3-dev python3-pip python-highgui \
    vim wget curl

WORKDIR /config

COPY requirements.txt .
COPY app.py .
COPY demo.py .

RUN pip3 install -r requirements.txt

CMD ['python3', 'app.py']