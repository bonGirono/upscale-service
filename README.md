## About The Project
Simple image upscale algorythm on python


### Built With

<img alt="Python" src="logo%2Fpython.png" width="200"/>
<img alt="FastApi" src="logo%2Ffastapi.png" width="200"/>
<img alt="Tortoise ORM" src="logo%2Ftortoise.png" width="200"/>
<img alt="PostgreSQL" src="logo%2Fpostgresql.png" width="200"/>
<img alt="Redis" src="logo%2Fredis.png" width="200"/>


## Requirements
Install **ffmpeg, libsm6, libxext6** on your system

## Installation

_Instruction_

1. Clone the repo
   ```sh
   git clone https://github.com/bonGirono/upscale-service.git
   cd upscale-service
   ```
2. Run with docker-compose **OR** follow the steps below 
   ```sh
   cp .env.example.docker_compose ./app/.env
   docker-compose up --build -d
   ```
3. Install python 3.11 from [official site](https://www.python.org) or with package manager on your os
4. Install redis from [official site](https://redis.io) or with package manager on your os and up service
   * on linux with systemctl
   ```sh
   sudo systemctl start redis.service
   ```
5. Install postgresql from [official site](https://www.postgresql.org) or with package manager on your os and up service
   * on linux with systemctl
   ```sh
   sudo systemctl start postgresql
   ```
7. Install requirements
   ```sh
   cp .env.example ./app/.env
   cd app
   pip install -U pip
   pip install -r requirements.txt
   ```
8. Already run
   ```sh
   python main.py
   celery -A worker.celery worker --loglevel=info
   celery --broker=redis://redis:6379/0 flower --port=5555
   ```


<!-- ROADMAP -->
## Roadmap

- [X] Endpoint for upload image or video
- [x] Upscale image
