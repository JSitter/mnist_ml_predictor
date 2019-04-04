To build docker thing.

```
docker build -t flask_keras_docker:latest .

docker run -d -p 8000:8000 flask_keras_docker
```