#!/bin/sh
docker system prune -f
docker-compose build && docker-compose up
