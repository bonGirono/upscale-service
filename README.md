## About The Project
Simple image upscale algorythm on python


### Built With

<img alt="Python" src="logo%2Fpython.png" width="200"/>
<img alt="FastApi" src="logo%2Ffastapi.png" width="200"/>
<img alt="Pillow" src="logo%2Fpillow.png" width="200"/>
<img alt="OpenCV" src="logo%2Fopencv.png" width="200"/>
<img alt="Redis" src="logo%2Fredis.png" width="200"/>
<img alt="Celery" src="logo%2Fcelery.png" width="200"/>


## Requirements
Install **ffmpeg, libsm6, libxext6** on your system **OR** use docker-compose

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
5. Install requirements
   ```sh
   cp .env.example ./app/.env
   cd app
   pip install -U pip
   pip install -r requirements.txt
   ```
6. Already run
   ```sh
   python main.py
   celery -A worker.celery worker --loglevel=info
   celery --broker=redis://redis:6379/0 flower --port=5555
   ```


## Roadmap

- [X] Endpoint for upload image or video
- [x] Upscale image


## Results
* Original 1000 x 600
   ![input.png](demo%2Finput.png)
* Up scale 2x 2000 x 1200
  ![output2x.png](demo%2Foutput2x.png)
* Up scale 8x 8000 x 4800
  ![output8x.png](demo%2Foutput8x.png)
