#! /usr/bin/env bash
set -x
set -e

cp $TGC_ROOT/requirements.txt $TGC_ROOT/docker/base
pushd $TGC_ROOT/docker/base
docker build -t tgc/tgc_base:0.0.1 -f Dockerfile.tgcbase .
# rm requirements.txt
popd