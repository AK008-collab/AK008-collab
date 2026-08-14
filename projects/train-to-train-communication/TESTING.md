# Train-to-Train Communication — Testing Checklist

## Communication

- [ ] Both ESP32 boards boot correctly
- [ ] ESP-NOW peer communication verified
- [ ] Packets received consistently
- [ ] RSSI values recorded
- [ ] Communication timeout tested

## Distance Calibration

Record multiple RSSI samples at known distances in the actual test environment.

| Distance | RSSI samples | Mean RSSI | Notes |
|---:|---:|---:|---|
| 0.25 m |  |  |  |
| 0.50 m |  |  |  |
| 0.75 m |  |  |  |
| 1.00 m |  |  |  |
| 1.50 m |  |  |  |
| 2.00 m |  |  |  |

## Safety Behaviour

- [ ] Safe state verified
- [ ] Warning state verified
- [ ] Stop state verified
- [ ] Hysteresis verified
- [ ] Motors remain stopped during danger state
- [ ] Recovery behaviour verified after separation increases
- [ ] Packet-loss behaviour verified

## Evidence to Add

When available, add real evidence to this repository:

- Hardware photographs
- Wiring diagram
- Serial-monitor logs
- RSSI calibration data
- Test videos
- Measured response time
- Final source code

Do not add estimated measurements as if they were experimentally measured results.
