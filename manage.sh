#!/bin/bash

argument=$1

if [ $argument = "up" ]; then
    echo "Model File compressing..."
    gzip -d ko_w2v_model.gz
    echo "Model File compressing complete!"
fi