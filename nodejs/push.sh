#!/bin/bash

docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PWD
docker push $DOCKERHUB_USERNAME/$NODE_JS_DIR:latest
