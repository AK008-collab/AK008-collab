import unittest

from campus_courier_mission.state_machine import MissionState, MissionStateMachine


class TestMissionStateMachine(unittest.TestCase):
    def setUp(self):
        self.machine = MissionStateMachine()

    def test_accept_start_complete(self):
        accepted, message = self.machine.submit_goal("LAB_A")
        self.assertTrue(accepted)
        self.assertEqual(message, "ACCEPTED: LAB_A")
        self.assertEqual(self.machine.state, MissionState.ACCEPTED)
        self.assertEqual(self.machine.start(), "IN_PROGRESS: LAB_A")
        self.assertEqual(self.machine.state, MissionState.IN_PROGRESS)
        self.assertEqual(
            self.machine.complete_demo(), "COMPLETED_DEMO_ONLY: LAB_A"
        )
        self.assertEqual(self.machine.state, MissionState.COMPLETED_DEMO_ONLY)

    def test_reject_empty_destination(self):
        accepted, message = self.machine.submit_goal("  ")
        self.assertFalse(accepted)
        self.assertIn("must not be empty", message)
        self.assertEqual(self.machine.state, MissionState.IDLE)

    def test_reject_second_goal_while_active(self):
        self.machine.submit_goal("LAB_A")
        self.machine.start()
        accepted, message = self.machine.submit_goal("ROOM_B")
        self.assertFalse(accepted)
        self.assertIn("already active", message)
        self.assertEqual(self.machine.destination, "LAB_A")

    def test_cannot_complete_before_start(self):
        self.machine.submit_goal("LAB_A")
        with self.assertRaises(RuntimeError):
            self.machine.complete_demo()


if __name__ == '__main__':
    unittest.main()
