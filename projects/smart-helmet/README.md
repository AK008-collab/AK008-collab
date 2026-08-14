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
- IoT monitoring dashboard concept

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

`Embedded C` `ESP8266` `ESP32` `MPU6050` `GPS` `GSM` `IoT` `Sensors` `Automation`

## System Flow

```text
Sensors
   ↓
ESP Controller
   ├── Helmet / Alcohol Safety Check → Ignition Control
   └── Motion / Crash Detection → GPS → GSM Emergency Alert
```

## Engineering Value

The project demonstrates how embedded systems can combine multiple sensor inputs with actuator control and communication to create a practical safety-oriented IoT system.

## Future Improvements

- Better crash classification using sensor fusion
- Mobile application for emergency contacts
- Cloud event logging
- Battery-health monitoring
- Secure communication
- GNSS improvements for better positioning
- Field testing with controlled safety scenarios
