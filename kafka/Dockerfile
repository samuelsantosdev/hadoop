FROM python:3.7-alpine
MAINTAINER Samuel Santos <samuelsantosdev@gmail.com>

COPY entrypoint.sh /entrypoint.sh
COPY app/requirements.txt /requirements.txt

# Java Version
ENV JAVA_VERSION_MAJOR 8
ENV JAVA_VERSION_MINOR 121
ENV JAVA_VERSION_BUILD 13
ENV JAVA_PACKAGE       jdk
ENV JAVA_SHA256_SUM    97e30203f1aef324a07c94d9d078f5d19bb6c50e638e4492722debca588210bc
ENV JAVA_URL_ELEMENT   e9e7ea248e2c4826b92b3f075a80e441

RUN apk update && apk add --no-cache wget curl && wget -O /tmp/glibc-2.21-r2.apk https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.21-r2/glibc-2.21-r2.apk &&\
apk add --allow-untrusted /tmp/glibc-2.21-r2.apk

RUN mkdir -p /opt &&\
    wget  -O java.tar.gz --header "Cookie: oraclelicense=accept-securebackup-cookie"\
    http://mirror.cnop.net/jdk/linux/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz &&\
    echo "$JAVA_SHA256_SUM  java.tar.gz" | sha256sum -c -

RUN gunzip -c java.tar.gz | tar -xf - -C /opt && rm -f java.tar.gz
RUN mv /opt/jdk1.8.0_121 /opt/jdk
RUN ln -s /opt/jdk/jre /opt/jre

RUN apk update && apk add --no-cache gcc python3-dev bash curl musl-dev && mkdir /app && \
chmod +x /entrypoint.sh && pip install -r /requirements.txt && rm /requirements.txt

RUN rm -rf /opt/jre/lib/plugin.jar \
     /opt/jre/lib/ext/jfxrt.jar \
     /opt/jre/bin/javaws \
     /opt/jre/lib/javaws.jar \
     /opt/jre/lib/desktop \
     /opt/jre/plugin \
     /opt/jre/lib/deploy* \
     /opt/jre/lib/*javafx* \
     /opt/jre/lib/*jfx* \
     /opt/jre/lib/amd64/libdecora_sse.so \
     /opt/jre/lib/amd64/libprism_*.so \
     /opt/jre/lib/amd64/libfxplugins.so \
     /opt/jre/lib/amd64/libglass.so \
     /opt/jre/lib/amd64/libgstreamer-lite.so \
     /opt/jre/lib/amd64/libjavafx*.so \
     /opt/jre/lib/amd64/libjfx*.so &&\
  apk del curl &&\
  rm -rf /var/cache/apk/*


ENV JAVA_HOME /opt/jre
ENV PATH ${PATH}:${JAVA_HOME}/bin

WORKDIR /app