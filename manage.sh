#!/bin/bash

argument=$1

if [ $argument = "start" ]; then
    echo "Creating infrastructure..."
    sleep 3
    gzip -d ko_w2v_model.gz
    sleep 3
    docker build -t 'w2v_model_api' .
    sleep 3
    docker run -d --name 'Model-API' -p '80':'5000' 'w2v_model_api'
elif [ $argument = "stop" ]; then
    echo "Deleting infrastructure..."
    docker stop 'Model-API'
    docker rm 'Model-API'
fi