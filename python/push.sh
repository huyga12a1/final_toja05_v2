#!/bin/bash

docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PWD
docker push $DOCKERHUB_USERNAME/$PYTHON_APP:latest