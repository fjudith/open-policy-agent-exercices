#!/bin/bash
docker-compose \
--file ./api/flask-restful-api-rethinkdb/docker-compose.yaml \
build && \
docker-compose \
--file ./api/flask-restful-api-rethinkdb/docker-compose.yaml \
up