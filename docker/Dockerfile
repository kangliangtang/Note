FROM registry.steam.crcloud.com/docker/library/python:3.5.6

RUN mkdir /usr/local/java
ADD jdk-8u221-linux-x64.tar.gz /usr/local/java/

RUN ln -s /usr/local/java/jdk1.8.0_221 /usr/local/java/jdk

# set environment variables
ENV JAVA_HOME /usr/local/java/jdk
ENV JRE_HOME ${JAVA_HOME}/jre
ENV CLASSPATH .:${JAVA_HOME}/lib:${JRE_HOME}/lib
ENV PATH ${JAVA_HOME}/bin:$PATH


RUN mkdir -p /usr/local/node
WORKDIR /usr/local/node
COPY . /usr/local/node
#RUN openjdk-8-jdk
RUN ln -s /usr/local/node/node-v10.16.3-linux-x64/bin/node /usr/local/bin/node
RUN ln -s /usr/local/node/node-v10.16.3-linux-x64/bin/npm /usr/local/bin/npm
EXPOSE 3000

