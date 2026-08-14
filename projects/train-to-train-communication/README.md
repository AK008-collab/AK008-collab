# 🚆 Train-to-Train Communication & Collision Prevention

> **Embedded wireless safety prototype using ESP32, ESP-NOW and RSSI-based proximity estimation.**

## 🎯 Objective

Build a model-train safety system in which two ESP32-controlled trains exchange wireless packets, estimate relative proximity, and trigger coordinated warnings and motor stopping when the trains enter a configurable danger zone.

## 🧠 System Architecture

```text
┌───────────────┐          ESP-NOW          ┌───────────────┐
│    Train A    │ ────────────────────────► │    Train B    │
│    ESP32      │ ◄──────────────────────── │    ESP32      │
└───────┬───────┘                           └───────┬───────┘
        │ RSSI / safety data                       │
        └────────────────┬─────────────────────────┘
                         ▼
                Proximity Estimation
                         │
                  Safety State Logic
                ┌────────┼────────┐
                ▼        ▼        ▼
              SAFE    WARNING    STOP
                         │
                  ┌──────┴──────┐
                  ▼             ▼
               Buzzer          LED
                  │
                  ▼
             Motor Control
                  │
                 L298N
```

## 🔧 Hardware

- 2 × ESP32 development boards
- L298N dual H-bridge motor driver
- DC motors / model train chassis
- IR / ultrasonic sensors where used by the physical prototype
- Buzzer and LED indicators
- Separate controller and motor power supplies

## 📡 Communication & RSSI

The prototype uses **ESP-NOW** for direct ESP32-to-ESP32 communication. RSSI is used as a relative proximity signal. Because RSSI changes with antenna orientation, obstacles, reflections and radio conditions, the distance model must be calibrated experimentally for the actual environment.

A practical implementation should treat the RSSI estimate as one input to the safety logic rather than as a precision ranging measurement.

## 🛑 Safety Logic

The system is designed around three states:

| State | Behaviour |
|---|---|
| 🟢 SAFE | Normal motor operation and safe-status reporting |
| 🟡 WARNING | Approaching threshold; warning indication is activated |
| 🔴 STOP | Motor outputs are disabled and alerts are activated |

Hysteresis is used between start/stop thresholds to reduce rapid state switching near a boundary.

## ⚙️ Motor Control

The ESP32 controls the L298N through its direction/enable inputs. The controller should also implement a communication timeout so that loss of the wireless link cannot leave the safety logic indefinitely dependent on stale data.

## 🌐 Monitoring Concept

A web dashboard can present:

- Train A / Train B status
- Estimated separation
- RSSI value
- Current safety state
- Warning / collision status
- Event history

## 🧪 Validation Plan

1. Verify ESP32-to-ESP32 communication.
2. Record RSSI at known physical distances.
3. Calibrate the RSSI model using measured samples.
4. Test warning and stop thresholds while stationary.
5. Test the system while trains approach at controlled speeds.
6. Verify hysteresis behaviour.
7. Test packet loss / communication timeout behaviour.
8. Record false positives and missed detections.

## 🚀 Future Improvements

- RSSI + ultrasonic sensor fusion
- Better filtering and calibration
- Independent emergency-stop path
- Communication-loss fail-safe
- Closed-loop braking rather than abrupt motor cut-off
- Real-time event logging
- Hardware-in-the-loop testing
- More robust ranging/localization technology

## 📁 Recommended Source Layout

```text
src/
├── main.ino
├── communication.ino
├── rssi_estimation.ino
├── safety_logic.ino
└── motor_control.ino
```

> **Documentation status:** This page records the verified project concept and engineering design. Actual source code, photographs, measurements and test results should be added from the physical implementation so the portfolio remains technically honest.
