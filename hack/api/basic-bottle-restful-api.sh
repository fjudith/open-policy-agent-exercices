#!/bin/bash
docker-compose \
--file ./api/basic-bottle-restful-api/docker-compose.yaml \
build && \
docker-compose \
--file ./api/basic-bottle-restful-api/docker-compose.yaml \
up