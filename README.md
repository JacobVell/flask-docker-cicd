# Flask Docker CI/CD Pipeline

This project demonstrates a simple CI/CD pipeline using GitHub Actions, Docker, and a Python Flask app.

## Features

- Simple Flask app
- Pytest for testing
- Dockerfile to build image
- GitHub Actions workflow to run tests, build and push Docker image to Docker Hub

## Setup

1. Create a repository on GitHub and push this project.
2. Create a Docker Hub account if you don't have one.
3. Create a Docker Hub access token:
   - Go to Docker Hub -> Settings -> Security -> New Access Token
4. In your GitHub repo, go to Settings -> Secrets and add:
   - `DOCKERHUB_USERNAME` - your Docker Hub username
   - `DOCKERHUB_TOKEN` - your Docker Hub access token
5. Push changes to the `main` branch to trigger CI/CD pipeline.

## How it works

- On every push to `main`, GitHub Actions:
  - Runs tests with pytest
  - Builds Docker image
  - Pushes the image to Docker Hub under your username

## Run locally

```bash
docker build -t flask-docker-cicd .
docker run -p 5000:5000 flask-docker-cicd
```

Open http://localhost:5000 to see the app.

