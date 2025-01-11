FROM nginx:latest

COPY ./typer/index.html /usr/share/nginx/html/index.html