# MNIST Classification Sample App
This model demonstrates the deployment of a python app using docker. 

To build the docker container run 

```
$ docker-compose up
```

<!-- ```
docker build -t flask_keras_docker:latest .

docker run -d -p 8000:8000 flask_keras_docker
``` -->

This project uses MongoDB to track when and what users submit to the neural network.

Currently there is an issue with Mongo client that clashes with bson which means this project will not be able to read anything inserted into the database.