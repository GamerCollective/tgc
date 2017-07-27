#!/usr/bin/env bash

pushd $TGC_ROOT
docker build -t tgc/tgc_app:0.0.1 -f Dockerfile.tgc .
popd
