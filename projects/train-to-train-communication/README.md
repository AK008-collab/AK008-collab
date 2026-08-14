# 🚆 Train-to-Train Communication & Collision Prevention

## Overview

An ESP32-based prototype designed to improve railway safety by detecting the relative proximity of two moving train models and triggering coordinated alerts and motor stopping when a configurable safety threshold is reached.

## System Concept

**Train A ↔ Wireless Communication ↔ Train B**

The prototype uses ESP32 wireless communication and RSSI measurements to estimate relative proximity. The controller combines the wireless measurement with motor-control logic and safety hysteresis so that the trains can stop when they approach the defined danger zone.

## Main Features

- ESP32-based control
- ESP-NOW wireless communication
- RSSI-based proximity estimation
- Motor control using L298N
- Buzzer and LED warning system
- Configurable safe / warning / stop thresholds
- Hysteresis to reduce rapid start-stop switching
- Web dashboard concept for distance and safety status

## Hardware

- 2 × ESP32
- L298N motor driver
- DC motors / train model chassis
- IR / ultrasonic sensing where required by the prototype
- Buzzer
- LED indicators
- Separate power supply for controller and motor system

## Software / Technologies

`Embedded C` `ESP32` `ESP-NOW` `RSSI` `L298N` `IoT` `Wireless Communication`

## Safety Logic

The prototype uses three conceptual states:

| State | Prototype behavior |
|---|---|
| Safe | Trains continue operation and system reports safe status |
| Warning | System indicates that the trains are approaching |
| Stop | Motors are commanded to stop and alerts are activated |

The exact RSSI-to-distance relationship depends on environment, antenna orientation, channel conditions and calibration. Therefore, RSSI is treated as a relative proximity indicator rather than a precision ranging sensor.

## Engineering Value

This project combines embedded control, wireless communication, sensing, motor control and real-time monitoring into one mechatronics safety prototype.

## Future Improvements

- Sensor fusion using RSSI + ultrasonic sensing
- Better calibration across different environments
- Fail-safe communication timeout handling
- Independent emergency-stop path
- Improved dashboard and data logging
- Hardware-in-the-loop testing
- More robust localization / ranging technology
