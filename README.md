# DevOps Flask CI Demo

A small educational project: a simple Python web application packaged
with Docker and checked automatically by a GitHub Actions pipeline.

## Tech stack

- Python 3.12, Flask
- Docker, Docker Compose
- GitHub Actions
- unittest

## Run locally with Docker Compose

Build and start the application:

    docker compose up --build -d

Open http://localhost:5000

Health endpoint: http://localhost:5000/health

Stop the application:

    docker compose down

## Run tests locally

    pip install -r requirements.txt
    python -m unittest discover -s tests -v

## CI pipeline

On every push and pull request, GitHub Actions:

1. installs dependencies and runs unit tests,
2. builds the Docker image,
3. lints the Dockerfile (hadolint),
4. starts the container and runs a smoke test on `/health`,
5. scans the image for known vulnerabilities (Trivy, report only).

## Security notes

- The container runs as a non-root user.
- The image is based on `python:3.12-slim`.
- The container has a health check.