#!/bin/bash

docker volume rm "jupyterhub_jupyterhub_data"
docker-compose build
