"""Pure-Python mission state machine; no ROS dependency."""
from dataclasses import dataclass
from enum import Enum


class MissionState(str, Enum):
    IDLE = "IDLE"
    ACCEPTED = "ACCEPTED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED_DEMO_ONLY = "COMPLETED_DEMO_ONLY"


@dataclass
class MissionStateMachine:
    """Tracks one demo mission at a time; does not control robot motion."""
    state: MissionState = MissionState.IDLE
    destination: str = ""

    def submit_goal(self, destination: str) -> tuple[bool, str]:
        destination = destination.strip()
        if not destination:
            return False, "REJECTED: destination must not be empty"
        if self.state in (MissionState.ACCEPTED, MissionState.IN_PROGRESS):
            return False, f"REJECTED: mission to {self.destination} is already active"
        self.destination = destination
        self.state = MissionState.ACCEPTED
        return True, f"ACCEPTED: {destination}"

    def start(self) -> str:
        if self.state != MissionState.ACCEPTED:
            raise RuntimeError("Only an accepted mission can be started")
        self.state = MissionState.IN_PROGRESS
        return f"IN_PROGRESS: {self.destination}"

    def complete_demo(self) -> str:
        if self.state != MissionState.IN_PROGRESS:
            raise RuntimeError("Only an in-progress mission can be completed")
        self.state = MissionState.COMPLETED_DEMO_ONLY
        return f"COMPLETED_DEMO_ONLY: {self.destination}"
