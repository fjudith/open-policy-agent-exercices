# Open Policy Agent Examples

The Open Policy Agent (OPA , pronounced "oh-pa") is an open source, general-purpose policy engin that unifies policy enforcement across the stack.

This repository centralize various static and dynamic based policies to demonstrate the power of OPA.

### Running exercises

Clone this repostory

```bash
git clone https://github.com/fjudith/open-policy-agent-exercices opa-exercices
cd opa-exercices
```

Create a Python virtual environment

```bash
virtualenv .venv
./.venv/bin/activate
```

## API

<img src="./docs/media/flask.png" alt="Flask" width="80px"/> [based basic RESTFul API](./api/01_basic_flask_restful_api/)

```bash
pushd "./api/01_basic_flask_restful_api"
pip install -r ./requirements.txt
opa run -s "./apiserver.rego" & \
python "./apiserver.py"
```

<img src="./docs/media/bottlepy.png" alt="Bottlepy" width="80px"/> [based basic RESTFul API](./api/01_basic_flask_restful_api/)

```bash
pushd "./api/01_basic_bottle_restful_api"
pip install -r ./requirements.txt
opa run -s "./apiserver.rego" & \
python "./apiserver.py"
```
