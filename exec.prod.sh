#!/bin/zsh

docker-compose -f docker-compose.prod.yml exec web python manage.py "$@"