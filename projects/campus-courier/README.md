# CampusCourier — Autonomous Indoor Delivery Robot

**Status:** Milestone 1 — ROS 2 delivery mission manager (navigation not yet integrated)

CampusCourier is a simulation-first robotics portfolio project for an indoor delivery robot intended for college buildings, laboratories, and hospitals.

## Roadmap
- [x] M1: Mission manager and pure-Python unit tests
- [ ] M2: Differential-drive robot model and indoor simulation world
- [ ] M3: Simulated LiDAR, mapping, and localization
- [ ] M4: Nav2 goal execution and obstacle avoidance
- [ ] M5: Repeatable evaluation, evidence, and demo video

## Milestone 1 scope

The ROS 2 node subscribes to `/delivery/goal` (`std_msgs/msg/String`) and publishes mission status to `/delivery/status`. It demonstrates the mission workflow only.

**It does not move a robot, plan paths, localize, or avoid obstacles.** A configurable demonstration timer marks a mission complete; this is not evidence of physical or simulated delivery.

## Requirements
- Ubuntu 22.04
- ROS 2 Humble
- Python 3
- `colcon`

## Build

Place this package folder under `~/campus_courier_ws/src/campus_courier_mission`:

```bash
source /opt/ros/humble/setup.bash
mkdir -p ~/campus_courier_ws/src
cd ~/campus_courier_ws
colcon build --packages-select campus_courier_mission
source install/setup.bash
```

## Run

Terminal 1:

```bash
source /opt/ros/humble/setup.bash
source ~/campus_courier_ws/install/setup.bash
ros2 run campus_courier_mission mission_manager
```

Terminal 2 — submit a destination:

```bash
source /opt/ros/humble/setup.bash
ros2 topic pub --once /delivery/goal std_msgs/msg/String "{data: 'LAB_A'}"
```

Terminal 3 — monitor mission status:

```bash
source /opt/ros/humble/setup.bash
ros2 topic echo /delivery/status
```

Expected status sequence for an accepted goal:
- `ACCEPTED: LAB_A`
- `IN_PROGRESS: LAB_A`
- `COMPLETED_DEMO_ONLY: LAB_A`

The default demo duration is 5 seconds. It can be changed with:

```bash
ros2 run campus_courier_mission mission_manager --ros-args -p demo_duration_sec:=5.0
```

A goal submitted while another mission is active is rejected.

## Unit tests

From the package root, with Python 3:

```bash
PYTHONPATH=. python3 -m unittest discover -s test -v
```

The state machine is kept separate from ROS so its logic can be tested without a ROS installation. ROS build/runtime testing must still be performed on Ubuntu 22.04 with ROS 2 Humble.

## Package layout

```text
campus_courier_mission/
├── campus_courier_mission/
│   ├── __init__.py
│   ├── mission_manager.py
│   └── state_machine.py
├── resource/campus_courier_mission
├── test/test_state_machine.py
├── package.xml
├── setup.cfg
└── setup.py
```

## Current limitations
- Destination labels are not mapped to coordinates.
- Completion is timer-based demonstration logic, not robot feedback.
- No robot model, simulator, SLAM, localization, Nav2, or obstacle avoidance is included in M1.
- No navigation performance metrics have been measured.

## Evidence checklist
- [ ] ROS build output
- [ ] Unit-test output
- [ ] `/delivery/status` terminal capture
- [ ] Simulation screenshots after M2
- [ ] Navigation test table with conditions and measured results
- [ ] Demo video

## License
MIT
