import pytest
from my_robot_py import Kinematics, Pose

def test_kinematics_instantiation():
   """Test that the Kinematics class can be created from Python."""
   kin = Kinematics(7) # Create a 7-DOF kinematics object
   assert kin.num_joints == 7

def test_kinematics_forward_pass():
   """Test calling a bound method with Python types."""
   kin = Kinematics(6)
   # Pass a Python list, which pybind11 should convert to std::vector<double>
   joint_angles = [0.0] * 6
   pose = kin.forward(joint_angles)
   
   # Assert on the result, which should be a bound struct or class
   assert isinstance(pose, Pose)
   assert isinstance(pose.x, float)
   assert pose.x == pytest.approx(1.234)
