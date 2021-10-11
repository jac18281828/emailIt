#!/usr/bin/env bash

docker build . -t email:1 && docker run --rm -i -t email:1
