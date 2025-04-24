#!/bin/bash

model_path=$PWD/<PATH_TO_YOUR_MODEL>  # Path to your model directory
volume=$PWD/data # Share a volume with the Docker container to avoid downloading weights every run

sudo docker run --cpus 2 --shm-size 1g -p 8080:80 \
    -v $model_path:/model -v $volume:/data \
    ghcr.io/huggingface/text-generation-inference:3.1.0 \
    --model-id /model

