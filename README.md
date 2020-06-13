# trivia-mania-api

Dockerizing application: https://stavshamir.github.io/python/dockerizing-a-flask-mysql-app-with-docker-compose/

Requirements: Docker, docker-compose

Start application: ```docker-compose up```

Visit "[hello world](http://127.0.0.1/)" page

To find IP of mysql docker container so it can be used with mysql workbench: 

```docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name_or_id```
