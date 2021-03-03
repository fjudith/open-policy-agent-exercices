# Hack guidelines

This document describes how you can use the scripts from the `hack` directory and gives a brief introduction and explanation of these scripts.

## Overview

the `hack` directory contains many scripts that ensure continuous development of the project, enhance the robustness of the code, improve development efficiency, etc. The explanations and descriptions of the scripts are helpful for contributors. For details, refer to the following guidelines.

# Key scripts

* [`hack/api/01_basic_flask_restful_api.sh`](api/01_basic_flask_restful_api.sh): This scripts boots a Docker-Compose stack running a simple RESTful API running from Flask and an OPA server to demonstrate how OPA Authorization module filters HTTP request `Authorization` header.
* [`hack/api/02_basic_bottle_restful_api.sh`](api/02_basic_bottle_restful_api.sh): This scripts boots a Docker-Compose stack running a simple RESTful API running from Bottle and an OPA server to demonstrate how OPA Authorization module filters HTTP requests based on the `Authorization` header.
