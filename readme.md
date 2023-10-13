# Pokenum

The Pokenum web project is a FastAPI-based application that provides an API for the Pokenum tool. Pokenum is a poker hand evaluator and calculator that helps users analyze poker hands and calculate winning probabilities, uses poker-eval lib.

## Prerequisites

To run the Pokenum web project using Docker, you need to have Docker installed on your system. You can download Docker from the official website:

- [Docker for Windows](https://docs.docker.com/docker-for-windows/install/)
- [Docker for Mac](https://docs.docker.com/docker-for-mac/install/)
- [Docker for Linux](https://docs.docker.com/engine/install/)

## Installation docker

1. Clone the Pokenum project repository:

   ```
   git clone https://github.com/jejellyroll-fr/pokenum.git
   ```

2. Change to the project directory:

   ```
   cd pokenum
   ```

3. Build the Docker image using the provided Dockerfile:

   ```
   docker build -t pokenum .
   ```


## Running the Pokenum Project Docker

1. Run the Docker container:

   ```
   docker run -p 8080:8080 -p 8000:8000 pokenum
   ```


## Using cluster Kubernetes
1. install Kubernetes locally or on cloud and deploy services
   
   ```
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   ```
   if you want more replica: edit deployment.yaml
   or use auto scaler

2. Access the Pokenum front at `http://localhost:8080` or the Pokenum API at `http://localhost:8000`

## Usage

1. see example in the repo FPDB-3