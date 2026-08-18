# 🪖 Smart Helmet Safety System

## Overview

An IoT-based two-wheeler safety prototype that combines helmet-use detection, alcohol detection, motion sensing, ignition control and emergency communication.

## Core Idea

The system is designed to prevent unsafe vehicle operation and respond to accident conditions. Sensor data is processed by an ESP8266/ESP32 controller, while GPS/GSM communication can provide location-based emergency alerts.

## Main Features

- Helmet-wearing detection
- Alcohol detection
- Accelerometer-based crash detection
- Ignition control through relay
- GPS location acquisition
- GSM emergency notification
- IoT monitoring dashboard

## Hardware

- ESP8266 / ESP32
- MPU6050 accelerometer
- Alcohol detection sensor
- Push-button / helmet detection input
- GPS module
- GSM module
- Relay module
- Buzzer / indicators

## Software / Technologies

`Embedded C` `ESP8266` `ESP32` `MPU6050` `GPS` `GSM` `Flask` `Python` `HTML` `CSS` `JavaScript` `Leaflet` `IoT`

## System Flow

```text
Sensors
   ↓
ESP Controller
   ├── Helmet / Alcohol Safety Check → Ignition Control
   └── Motion / Crash Detection → GPS → GSM Emergency Alert
                                      ↓
                                  Flask API
                                      ↓
                              Live Web Dashboard
```

## 🌐 Web Backend & Dashboard

The project now includes the **actual web/backend source code** supplied for the prototype:

👉 **[Open Smart Helmet Source Code](source/)**

### Backend

- Flask REST API
- `POST /update` for incoming telemetry
- `GET /status` for current helmet data
- Crash-alert state handling
- CORS enabled for prototype development

### Frontend

- Live status dashboard
- GPS coordinate display
- OpenStreetMap/Leaflet live location map
- Automatic polling for updated data

## Local Setup

```bash
cd source
python -m venv .venv
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python app.py
```

The prototype Flask server listens on port `5000`.

## Example Telemetry

```json
{
  "status": 1,
  "latitude": 11.9795,
  "longitude": 79.832199
}
```

The current prototype treats `status = -1` as a crash-alert condition.

## Engineering Value

The project demonstrates how embedded systems can combine multiple sensor inputs with actuator control, wireless communication, GPS/GSM emergency communication and a web-based monitoring layer.

## Future Improvements

- Better crash classification using sensor fusion
- Mobile application for emergency contacts
- Cloud event logging
- Battery-health monitoring
- Secure authenticated API
- HTTPS deployment
- GNSS improvements for better positioning
- Field testing with controlled safety scenarios
