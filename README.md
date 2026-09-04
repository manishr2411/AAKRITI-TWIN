# Aakriti Twin
### AI-Powered Environment Mapping and Digital Twin System

<p align="center">
  <b>Low-Cost Real-Time Environment Understanding using Ultrasonic Sensing, Computer Vision, Sensor Fusion, IoT and Digital Twin Visualization</b>
</p>

---

## 📌 Overview

**Aakriti Twin** is an AI-powered real-time environment mapping and digital twin system designed to understand and digitally represent a physical environment.

The system combines:

- Ultrasonic distance sensing
- Servo-based directional scanning
- ESP32 embedded control
- Webcam-based computer vision
- YOLO object detection
- Sensor fusion
- Firebase cloud connectivity
- 2D spatial mapping
- Streamlit dashboard visualization

The ultrasonic sensor determines **where an object is and approximately how far it is**, while the camera-based AI determines **what the object is**.

These outputs are fused together and displayed as a live digital representation of the physical environment.

> **In simple terms:**  
> The system scans the real environment, detects objects using AI, combines object identity with spatial information, sends data through the cloud, and displays the environment as a live digital twin.

---

## 🎯 Problem Statement

Many environments such as:

- Warehouses
- Factories
- Industrial work areas
- Indoor monitoring spaces
- Robotics environments
- Smart surveillance areas

require information about:

- What objects are present
- Where the objects are located
- How far the objects are
- How the environment is changing
- How this information can be visualized digitally in real time

Advanced solutions such as LiDAR, industrial vision systems and high-end robotics sensors can provide sophisticated environment perception, but they can also be expensive for low-cost prototyping and educational applications.

### Our Approach

Aakriti Twin addresses this problem using affordable and accessible components:

- Ultrasonic sensor
- Servo motor
- ESP32
- Webcam
- Laptop
- Cloud backend
- AI-based object detection

The objective is to create a low-cost system capable of:

**Sensing → Understanding → Fusing → Mapping → Visualizing**

---

# 💡 Core Idea

The system uses two complementary sensing approaches.

### 1. Ultrasonic Sensing

The ultrasonic sensor provides:

- Distance information
- Directional information

The sensor is mounted on a servo motor that rotates through different angles.

This produces angle-distance measurements of the surrounding environment.

### 2. Camera-Based AI

A webcam captures the same environment.

A YOLO object detection model processes the camera frames and provides:

- Object class
- Confidence score
- Bounding box
- Approximate image position

### 3. Sensor Fusion

The two outputs are combined.

The ultrasonic sensor provides:

> **Where + How far**

The camera AI provides:

> **What**

Together, they provide:

> **What + Where + How Far**

The resulting information is then visualized as a 2D digital twin.

---

# 🏗️ System Architecture

```text
                 PHYSICAL ENVIRONMENT
                         │
                         ▼
              ┌─────────────────────┐
              │ Ultrasonic Sensor   │
              │ + Servo Motor       │
              └──────────┬──────────┘
                         │
                  Angle + Distance
                         │
                         ▼
                  ┌─────────────┐
                  │    ESP32    │
                  └──────┬──────┘
                         │
                    Serial / USB
                         │
                         ▼
                ┌──────────────────┐
                │ Serial Collector │
                └───────┬──────────┘
                        │
             ┌──────────┴──────────┐
             │                     │
             ▼                     ▼
      Local JSON Data       Firebase Cloud
             │                     │
             │                     │
             └──────────┬──────────┘
                        │
                        │
                        ▼
                ┌────────────────┐
                │ Sensor Scan    │
                │ Processing     │
                └───────┬────────┘
                        │
                        │
       ┌────────────────┴────────────────┐
       │                                 │
       ▼                                 ▼
┌───────────────┐                ┌────────────────┐
│ Webcam        │                │ Scan Data      │
│ Feed          │                │ Angle/Distance │
└───────┬───────┘                └───────┬────────┘
        │                                │
        ▼                                │
┌────────────────┐                       │
│ YOLO Object    │                       │
│ Detection      │                       │
└───────┬────────┘                       │
        │                                │
        │ Object Class                   │
        │ Confidence                     │
        │ Bounding Box                   │
        │                                │
        └──────────────┬─────────────────┘
                       ▼
              ┌─────────────────┐
              │ Sensor Fusion   │
              └────────┬────────┘
                       │
                Object + Position
                       │
                       ▼
              ┌─────────────────┐
              │ 2D Coordinate   │
              │ Mapping         │
              └────────┬────────┘
                       │
                       ▼
             ┌────────────────────┐
             │ Streamlit          │
             │ Digital Twin       │
             │ Dashboard          │
             └─────────┬──────────┘
                       │
                       ▼
              REAL-TIME DIGITAL
                 REPRESENTATION
```

---

## 📁 Repository Structure

```text
AAKRITI-TWIN/
│
├── Images/
│   ├── Hardware/
│   ├── Circuit_Diagram/
│   ├── AI_Training/
│   ├── Results/
│   └── Team/
│
├── Source_code/
│   ├── Person1_ESP32/
│   │   └── aakriti_twin_scanner.ino
│   │
│   ├── Person2_Firebase/
│   │   └── upload_serial_to_firebase.py
│   │
│   ├── Person3_AI/
│   │   ├── auto_capture.py
│   │   ├── best.pt
│   │   ├── classes.txt
│   │   ├── hybrid_detect_cam.py
│   │   ├── test_custom_cam.py
│   │   ├── train_custom.py
│   │   └── yolo11n.pt
│   │
│   └── Person4_Dashboard/
│       ├── data/
│       ├── pages/
│       ├── src/
│       ├── tests/
│       ├── app.py
│       ├── object_fusion_collector.py
│       ├── requirements.txt
│       └── serial_collector.py│
│       └── yolo11n.pt
│
├── Videos/
│   ├── Hardware_Demo/
│   └── System_Demo/
│
└── README.md
