# WebGPU Monitor

## Description
This web application enables real-time monitoring and management of GPU cards, offering an web interface to `nvidia-smi`.
It is designed to display essential statistics and performance metrics of graphics cards.

## Features
- Web-based interface to `nvidia-smi` accessible from any device
- Display of GPU usage, temperature, and other critical metrics

## Requirements
Before you start, make sure to install the NVIDIA Toolkit for Docker to ensure compatibility with Docker containers managing GPU resources. 

### Installing NVIDIA Toolkit for Docker
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

## Run docker container

```bash
docker pull ghcr.io/robertolechowski/webgpu-monitor:latest

docker run -p 8000:8000 -it --gpus all ghcr.io/robertolechowski/webgpu-monitor:latest
```

## Configuration
Edit the `config/config.yaml` file to specify your preferences

## Usefully config
```
git config --global core.autocrlf true
```

## ToDo
 - Improve presentation: CSS, HTML, columns, font
 - Auto refresh data
 - Add docker composer example
 - Links to GitHub page in main page. Show version number and build time in UI
 - Improve documentation, add screenshot
 - Add more info about given GPU. number of cores, etc
 - Add agent mode and collect data from other hosts
 - Keep historical data
 - Add conditional formating of cells like red clor when high temperature
 - Promote project, reddit 