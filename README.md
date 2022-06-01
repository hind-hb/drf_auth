# Lab 33: Authentication & Production Server
## Feature Tasks and Requirements
Features - Django

Add JWT Authentication to your API.

Install needed libraries in project configuration and/or site settings.

Keep any pre-existing authentication so DRF Browsable API still usable.

Install needed libraries in project configuration and/or site settings.

## Features - Docker

Create a boilerplate Dockerfile and docker-compose.yml so you don’t need to start from scratch each time.

E.g. as a VS Code snippet, or a gist.

## Steps :
```
# Djang
$ pip install django
pip install django_rest_framework

# env
$ python -m venv django_env
$ source ./django_env/bin/activate

# requirements
$ poetry export -f requirements.txt --output requirements.txt

```

install docker

```
sudo apt-get update
sudo apt-get upgrade
sudo apt install docker.io
systemctl start docker
systemctl enable docker
docker --version
```


## PR : [LINK](https://github.com/hind-hb/drf_auth/pull/1/commits/29239284be71c712f0ae432c149b2625d7c4832f)
