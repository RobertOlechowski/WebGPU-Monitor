# WebGPU Monitor

## Description
This web application enables real-time monitoring and management of GPU cards, offering an web interface to `nvidia-smi`.
It is designed to display essential statistics and performance metrics of graphics cards.

## Features
- Web-based interface to `nvidia-smi` accessible from any device
- Display of GPU usage, temperature, and other critical metrics

## Run docker container
### Requirements
Before you start, make sure to install the NVIDIA Toolkit for Docker to ensure compatibility with Docker containers managing GPU resources. 
Follow these steps to install the NVIDIA Toolkit or read more [Installing the NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list


sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit

sudo systemctl restart docker
```

```bash
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```

### Verify Nvidia docker configuration
```bash
docker run -it --gpus all nvidia/cuda:12.1.0-base-ubuntu22.04 nvidia-smi
```

### Run app in docker container
```bash
docker pull ghcr.io/robertolechowski/webgpu-monitor:latest
docker run -p 8000:8000 -it --gpus all ghcr.io/robertolechowski/webgpu-monitor:latest
```

### Run app with docker composer
```bash
git clone https://github.com/RobertOlechowski/WebGPU-Monitor.git
cd WebGPU-Monitor/docker
docker compose up -d
```

## Run app without docker
```bash
git clone https://github.com/RobertOlechowski/WebGPU-Monitor.git
cd WebGPU-Monitor
uvicorn main:app --host 0.0.0.0 --port 8000
# open web browser http://127.0.0.1:8000
```

## Configuration
Edit the `config/config.yaml` file to specify your preferences

## TODO and known bugs
 - Improve documentation, add screenshot

 - Auto refresh data
 - Add more info about given GPU. number of cores, etc
 - Add agent mode and collect data from other hosts
 - Keep historical data
 - Add conditional formating of cells like red clor when high temperature


## About the Author
This project is developed and maintained by **Robert Olechowski**. 
I encourage you to report any issues or bugs you encounter, and I'm always open to any suggestions for improvements. 
Please feel free to reach out via email or submit an issue on GitHub if you have any questions or need support. 
Your contributions and feedback are highly valued and play a crucial role in the continuous enhancement of this project.

- **Email:** [robertolechowski@gmail.com](mailto:robertolechowski@gmail.com)
- **Website:** [robertolechowski.com](https://robertolechowski.com/)
