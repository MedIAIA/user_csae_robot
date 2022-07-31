import pytest
from robot import *


class TestRobotObject:
	@staticmethod
	def test_robot_object(mocker):
		
		# Given
		
		mocked_talk = mocker.patch("robot.Androides.talk")
		
		# When
		
		robot = Robot(serial_number=1111, fabricant="honda")
		androide = Androides(serial_number=1111, fabricant="honda", firstname="alix", family_name="Tesla")
		
		# Then
		
		assert isinstance(robot, Robot)
		assert isinstance(androide, Androides)
		assert mocked_talk.called
		


class TestRobot:
    @staticmethod
    def test_power_on():
        assert 1 == 1

