#!/bin/bash
docker-compose \
--file ./api/basic-flask-restful-api/docker-compose.yaml \
build && \
docker-compose \
--file ./api/basic-flask-restful-api/docker-compose.yaml \
up