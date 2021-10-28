#!/usr/bin/env bash

VERSION=$(date +%m%d%y)

docker build . -t email:${VERSION} && docker run --rm -i -t email:${VERSION}
