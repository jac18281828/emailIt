ARG VERSION=stable-slim

FROM debian:${VERSION} 

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt update && \
    apt -y install python3 python3-pip

# build project
ARG PROJECT=emailalert
WORKDIR /workspaces/${PROJECT}

COPY requirements.txt .
COPY emailit.py .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
ENV PYTHONPATH=.
CMD python3 emailit.py done
