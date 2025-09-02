# 👁️‍🗨️ Vision-Based Indoor Navigation Assistant for the Visually Impaired

An **affordable, real-time wearable assistive system** that combines **computer vision** and **audio feedback** to enhance independent indoor navigation for the visually impaired.  
Built around a **Raspberry Pi**, **USB webcam**, **OpenCV MobileNet-SSD**, and **text-to-speech**, the system detects obstacles and provides **directional audio guidance**.

---

## 🌟 About The Project
Visually impaired individuals face challenges navigating indoor spaces such as homes, offices, hospitals, and schools.  
Traditional aids like **white canes** and **guide dogs** are helpful but limited.  

This project introduces a **vision-based wearable navigation assistant** that provides:
- 🧭 **Obstacle detection** using MobileNet-SSD (OpenCV DNN).  
- 🔊 **Real-time audio feedback** via text-to-speech.  
- 💡 **Context-aware spatial guidance** (left, center, right).  
- ⚡ Portable design powered by a **5V power bank**.  

---

## 🛠️ Built With
### Hardware
- Raspberry Pi 4 Model B (8GB RAM)  
- USB Webcam  
- Aux / Bluetooth Speaker  
- 5V Power Bank  

### Software
- Python 3.9  
- OpenCV (Computer Vision Library)  
- MobileNet-SSD (Pre-trained Object Detection Model)  
- pyttsx3 (Offline Text-to-Speech)  
- ALSA (Audio configuration for Raspberry Pi)  

---


## ⚡ Features
- Real-time **object detection** with MobileNet-SSD.  
- **Audio prompts** based on obstacle position.  
- **Offline operation** (no cloud dependency).  
- **Headless deployment** with auto-start on boot.  
- Low-cost and **portable design** for indoor use.  

---

## 🚀 Installation & Setup
### 1️⃣ OS Setup
Install **Raspberry Pi OS (32-bit, Bullseye recommended)**.  

### 2️⃣ Package Installation
```bash
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install python3-opencv alsa-utils
pip3 install pyttsx3 imutils
