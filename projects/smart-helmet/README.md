# 🪖 IoT-Based Smart Helmet for Rider Safety

## Overview

This project is positioned first and foremost as an **emergency-response system for two-wheeler riders**. Its main value is to help communicate a rider’s location and send emergency alerts when a possible accident is detected. Alcohol detection is an **additional preventive safety feature**, not the primary reason to use the helmet.

The goal is to support riders and their families with timely emergency information while keeping the rider-facing experience straightforward.

## Primary Value: Emergency Response

- Detect a possible accident using motion/impact sensing.
- Acquire the rider’s GPS location.
- Send an emergency notification through GSM communication.
- Provide a companion web/app interface for viewing status and location information.

These are intended capabilities; detection reliability, alert delivery and location accuracy must be validated through controlled testing before making performance claims.

## Additional Safety Features

- **Alcohol detection:** an additional preventive check.
- **Helmet-use detection:** detects whether the helmet is being worn, according to the prototype’s sensor/input design.
- **Ignition control:** relay-based control, where implemented and validated.
- **Buzzer/indicators:** local warnings and status feedback.

## Hardware

- ESP8266 / ESP32 controller
- MPU6050 accelerometer/gyroscope for motion sensing
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
Motion / Impact Sensors
          ↓
    ESP Controller
          ↓
  Possible Accident Event
          ↓
    Obtain GPS Location
          ↓
     GSM Alert Message
          ↓
Emergency Contact / Dashboard

Additional safety inputs:
Alcohol Sensor · Helmet-use Input · Optional Relay Control
```

## 🌐 Web Backend & Dashboard

The project repository includes prototype backend and frontend source code:

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
- OpenStreetMap/Leaflet location map
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

## Rider-Centred Design Principle

The helmet should be presented as a familiar riding product with **emergency support as the main benefit**, rather than as a device focused on checking or monitoring the rider. Alcohol detection remains a supporting safety feature.

## Validation Priorities

- Test possible-accident detection and reduce false alerts.
- Verify GPS location accuracy in different environments.
- Test GSM message delivery and response time.
- Evaluate usability and comfort with rider feedback.
- Validate helmet-use and alcohol-sensor behavior independently.
- Review electrical safety, helmet compliance and manufacturing requirements before deployment.

## Future Improvements

- Better crash classification using sensor fusion
- Mobile application for emergency contacts
- Cloud event logging
- Battery-health monitoring
- Secure authenticated API
- HTTPS deployment
- GNSS improvements for better positioning
- Controlled field testing and documented results
