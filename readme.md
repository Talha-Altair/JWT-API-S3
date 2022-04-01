# JWT-API-S3

A Simple Flask server which provides an API for interacting with S3.

## Installation

### Docker

```
docker-compose up
```

### Standalone

```
pip install -r requirements.txt
python app.py
```

Visit http://localhost:8000/ to see the API routes.

## Non Functional requirements

- [x] Unit tests using moto or similar library to mock AWS services

- [x] Lint and prettier configurations

- [x] Dockerise the application

- [x] Readme file on how to deploy and run the service. 

## Testing

### Login

```
curl -X POST -H "Content-Type: application/json" -d '{"username":"altair","password":"1234"}' http://localhost:8000/login

```

```
export JWT="<enter access token here>"
```

### Test Access

```
curl -X GET -H "Authorization: Bearer $JWT" http://localhost:8000/ping
```

### Create

```
curl -X POST -H "Authorization: Bearer $JWT" -H "Content-Type: application/json" -d '{"sample":"data","lorem":"ipsum"}' http://localhost:8000/create
```

copy the uuid

### Read

```
curl -X POST -H "Authorization: Bearer $JWT" -H "Content-Type: application/json" -d '{"uuid": "<uuid>"}' http://localhost:8000/read
```

### Update

```
curl -X POST -H "Authorization: Bearer $JWT" -H "Content-Type: application/json" -d '{"uuid": "<uuid>","body":{"sample":"data2","lorem2":"ipsum3"}}' http://localhost:8000/update
```

### Delete

```
curl -X POST -H "Authorization: Bearer $JWT" -H "Content-Type: application/json" -d '{"uuid": "<uuid>"}' http://localhost:8000/delete
```
