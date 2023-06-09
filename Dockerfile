ARG BASE_IMAGE=daisukekobayashi/darknet:gpu-cv
FROM $BASE_IMAGE
ENV DEBIAN_FRONTEND noninteractive
ARG SERVER_FONFIG
ENV SERVER_CONFIG ${SERVER_CONFIG:-./config.py}

RUN apt update \
    && apt search opencv-highgui | grep opencv-highgui | apt install -y - \
    && apt install -y python3 python3-dev \
        python3-pip vim wget curl wget opencv3-python

WORKDIR /config

COPY requirements.txt .
COPY app.py .
COPY demo.py .

RUN pip3 install -r requirements.txt && which python3

CMD ['python3', 'app.py']