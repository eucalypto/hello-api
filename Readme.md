# hello-api

A minimal REST API built with [FastAPI](https://fastapi.tiangolo.com/), packaged as a Docker image. Created as a learning project for Docker and Azure container hosting.

## Endpoints

| Method | Path     | Response                              |
|--------|----------|---------------------------------------|
| GET    | `/hello` | `{"message": "Hello from Docker!"}`   |
| GET    | `/health`| `{"status": "ok"}`                    |
| GET    | `/docs`  | Interactive API documentation         |

## Run with Docker

Build the image:

```bash
docker build -t hello-api .
```

Run the container:

```bash
docker run --rm --name hello-api -p 8080:8080 hello-api
```

Test it:

```bash
curl http://localhost:8080/hello
curl http://localhost:8080/health
```

If Docker runs in a VM, replace `localhost` with the VM's IP address and use `http://`, not `https://`.

## Build for Azure

Azure runs amd64 (x86) containers. On an Apple Silicon (arm64) machine, build with an explicit platform:

```bash
docker build --platform linux/amd64 -t hello-api .
```

## Project layout

```
.
├── main.py            # FastAPI application
├── requirements.txt   # Python dependencies
├── Dockerfile         # Image definition
├── .dockerignore      # Files excluded from the Docker build
└── .gitignore         # Files excluded from Git
```
