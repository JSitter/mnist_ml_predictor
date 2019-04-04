# Dockerfile - this is the Dockerfile stuff for doing things using python.
FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ['python']
CMD ['app.py']