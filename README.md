# MNIST Classification Sample App
This model demonstrates the deployment of a python app using docker. 

To build the docker container.

```
docker build -t flask_keras_docker:latest .

docker run -d -p 8000:8000 flask_keras_docker
```

