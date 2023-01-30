# Our platform
FROM python:3.10.4-slim

# Copy the project directory into a Docker directory named "app". Ignore files started in .dockerignore
COPY . /app
# Set Docker working directory to "/app"
WORKDIR /app


RUN python -m venv /opt/venv

RUN pip install pip --upgrade && \
    /opt/venv/bin/pip install -r requirements.txt
# runs Docker equivalent of /home/charlie/Documents/Django-K8S/venv/bin/python manage.py runserver
RUN chmod +x entrypoint.sh

CMD ["/app/entrypoint.sh"]