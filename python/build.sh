#!/bin/bash

git clone $PYTHON_REPO
cd $PYTHON_APP
docker build -t $DOCKERHUB_USERNAME/$PYTHON_APP:latest .
cd ..
rm -r $PYTHON_APP
