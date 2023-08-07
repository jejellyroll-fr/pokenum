# Pokenum

The Pokenum web project is a FastAPI-based application that provides an API for the Pokenum tool. Pokenum is a poker hand evaluator and calculator that helps users analyze poker hands and calculate winning probabilities, uses poker-eval lib.

## Prerequisites

To run the Pokenum web project using Docker, you need to have Docker installed on your system. You can download Docker from the official website:

- [Docker for Windows](https://docs.docker.com/docker-for-windows/install/)
- [Docker for Mac](https://docs.docker.com/docker-for-mac/install/)
- [Docker for Linux](https://docs.docker.com/engine/install/)

## Installation

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


## Running the Pokenum Project

1. Run the Docker container:

   ```
   docker run -p 8080:8080 -p 8000:8000 pokenum
   ```



2. Access the Pokenum front at `http://localhost:8080` or the Pokenum API at `http://localhost:8000`

## Usage

1. Examples from command line:
```
$ pokenum -h Ac 7c - 5s 4s - Ks Kd
$ pokenum -h Ac 7c 5s 4s Ks Kd
$ pokenum -h Ac 7c 5s 4s Ks Kd -- 7h 2c 3h

$ pokenum -o As Kh Qs Jh - 8h 8d 7h 6d
$ pokenum -o As Kh Qs Jh 8h 8d 7h 6d
$ pokenum -o As Kh Qs Jh 8h 8d 7h 6d -- 8s Ts Jc
$ pokenum -mc 1000000 -o85 As Kh Qs Jh Ts - 8h 8d 7h 6d 9c
$ pokenum -mc 1000000 -o5 As Kh Qs Jh Ts - 8h 8d 7h 6d 9c
$ pokenum -mc 1000000 -o6 As Kh Qs Jh Ts 9d - 8h 8d 7h 6d 9c 6c

$ pokenum -7s As Ah Ts Th 8h 8d - Kc Qc Jc Td 3c 2d
$ pokenum -7s As Ah Ts Th 8h 8d - Kc Qc Jc Td 3c 2d / 5c 6c 2s Jh

$ pokenum -l 7h 5s 3d Xx / Kd - 9s 8h 6d 4c / 8c
$ pokenum -l27 5h 4h 3h 2h / 5s - 9s 8h 6d 4c / Kd
$ pokenum -mc 10000 -l27 5h 4h 3h / 5s Qd - 9s 8h 6d / Ks Kh
```

2. API doc

`http://127.0.0.1:8000/redoc`