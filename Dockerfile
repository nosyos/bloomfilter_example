FROM python:3.10-alpine

COPY requirements.txt .

RUN apk add --no-cache build-base curl binutils \
  && curl -sL https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub -o /etc/apk/keys/sgerrand.rsa.pub \
  && curl -sLO https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.33-r0/glibc-2.33-r0.apk \
  && curl -sLO https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.33-r0/glibc-bin-2.33-r0.apk \
  && apk add --no-cache glibc-2.33-r0.apk glibc-bin-2.33-r0.apk \
  && pip install --upgrade pip \
  && pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt \ 
  && apk del build-base

WORKDIR /app
