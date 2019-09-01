FROM python:3.7-alpine

ENV PYTHONIOENCODING utf-8
WORKDIR /app

RUN apk add --update \
        wget \
    # Add chromium and dependences
        udev \
        ttf-freefont \
        chromium \
        chromium-chromedriver \
    # Add Japanese font
    && mkdir noto \
    && wget -P /app/noto https://noto-website.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip \
    && unzip /app/noto/NotoSansCJKjp-hinted.zip -d /app/noto \
    && mkdir -p /usr/share/fonts/noto \
    && cp /app/noto/*.otf /usr/share/fonts/noto \
    && chmod 644 -R /usr/share/fonts/noto/ \
    && fc-cache -fv \
    && rm -rf /app/noto \
    # Add selenium
    && pip install selenium
