# 🌍 Aakriti Twin
### AI-Powered Environment Mapping & Digital Twin System

An intelligent low-cost Digital Twin system that combines **embedded sensing**, **computer vision**, **sensor fusion**, **cloud connectivity**, and **real-time visualization** to understand and digitally represent physical environments. The system scans its surroundings, detects objects using AI, fuses sensor data, and displays a live 2D digital twin through an interactive dashboard. :contentReference[oaicite:0]{index=0}

---

## 📖 Overview

Aakriti Twin is designed to bridge the gap between the physical and digital worlds by creating a live virtual representation of indoor environments.

The system integrates:

- 📡 Ultrasonic distance sensing
- 🔄 Servo-based environmental scanning
- 🤖 AI-powered object detection (YOLO)
- ☁️ Cloud connectivity (Firebase)
- 🧠 Sensor Fusion
- 📊 Streamlit Digital Twin Dashboard

Unlike traditional systems that rely only on cameras or only on sensors, Aakriti Twin combines both to determine:

- What an object is
- Where it is located
- How far it is
- How the environment changes in real time

---

# 🚀 Features

- Real-time environment scanning
- AI object detection using webcam
- Sensor fusion for object localization
- Live 2D Digital Twin visualization
- Firebase cloud integration
- Real-time dashboard monitoring
- Raw sensor data visualization
- System health monitoring
- Modular architecture

---

# 🏗️ System Architecture

```
                Physical Environment
                        │
        ┌───────────────┴───────────────┐
        │                               │
 Ultrasonic Sensor                Webcam
        │                               │
 Servo Motor                  YOLO Object Detection
        │                               │
 Distance Scan              Object Classification
        └───────────────┬───────────────┘
                        │
                  Sensor Fusion
                        │
              Position Estimation
                        │
          Firebase + Local Storage
                        │
                Streamlit Dashboard
                        │
                 Digital Twin View
```

---

# 🛠 Hardware

- ESP32
- Ultrasonic Sensor
- Servo Motor
- LCD Display
- USB Communication
- Laptop
- Webcam

---

# 💻 Software Stack

| Category | Technology |
|----------|------------|
| Programming | Python |
| Embedded | ESP32 |
| AI | YOLO |
| Computer Vision | OpenCV |
| Dashboard | Streamlit |
| Cloud | Firebase Realtime Database |
| Data Format | JSON |

---

# ⚙️ Workflow

### Step 1

The ultrasonic sensor scans the surroundings by rotating across multiple angles.

### Step 2

Distance measurements are collected continuously.

### Step 3

The ESP32 sends scan packets to the laptop.

### Step 4

The serial collector stores scan data locally and uploads it to Firebase.

### Step 5

The webcam captures live video.

### Step 6

YOLO detects visible objects.

### Step 7

Sensor Fusion combines:

- Object Label
- Angle
- Distance
- Position

### Step 8

The Streamlit dashboard visualizes the environment as a Digital Twin.

This creates a complete real-time pipeline from sensing to visualization. :contentReference[oaicite:1]{index=1}

---


# 📊 Dashboard

The dashboard provides:

- 🗺 Live Digital Twin Map
- 📷 Camera View
- 📦 Detected Objects
- 📈 Scan Visualization
- 📋 Raw JSON Data
- ☁ Cloud Status
- 📊 System Health

---

# 🧠 Sensor Fusion

The project combines:

**Ultrasonic Sensor**

- Distance
- Direction

**Camera AI**

- Object Detection
- Object Classification

Both outputs are fused to estimate:

- Object Position
- Distance
- Angle
- 2D Coordinates
  
---

# 🌐 Applications

- Smart Warehouses
- Indoor Mapping
- Robotics
- Industrial Monitoring
- Smart Surveillance
- Digital Twin Demonstrations
- Educational Research
- Intelligent Environment Monitoring

---

# 🔮 Future Improvements

- Improved sensor fusion
- Better object localization
- Custom-trained AI models
- Enhanced cloud synchronization
- Advanced Digital Twin UI
- Alert and automation system
- Indoor navigation support

---

# 📄 License

This project is licensed under the MIT License.

---

# 👥 Contributors

**Manish R**

**Chirag B N**

**Likhith Gowda H R**

**Bharani J S**

----
