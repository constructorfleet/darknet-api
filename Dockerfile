ARG BASE_IMAGE=daisukekobayashi/darknet:gpu-cv
ENV DEBIAN_FRONTEND noninteractive
ARG SERVER_FONFIG
ENV SERVER_CONFIG ${SERVER_CONFIG:-./config.py}

WORKDIR /config

COPY requirements.txt .
COPY app.py .
COPY demo.py .

RUN pip3 install -r requirements.txt

CMD ['python3', 'app.py']