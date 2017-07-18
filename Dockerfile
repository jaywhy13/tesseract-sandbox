FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN apt-get update && \
    apt-get -y --no-install-recommends install python3-dev python3-setuptools \
    libtiff5-dev libjpeg-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev \
    tesseract-ocr
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt