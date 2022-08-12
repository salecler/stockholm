#!/usr/bin/env bash
docker build -t stockholm .

docker run -v "$PWD"/venv:/home/admin -it --name c_stockholm -p 80:80 stockholm
