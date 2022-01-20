#!/bin/bash

docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PWD
docker stop $PYTHON_APP
docker pull $DOCKERHUB_USERNAME/$PYTHON_APP:latest
docker run --rm -d -p 5000:5000 -e APP_VERSION=latest -e APP_HOST=$HOSTNAME --name=$PYTHON_APP $DOCKERHUB_USERNAME/$PYTHON_APP:latest
