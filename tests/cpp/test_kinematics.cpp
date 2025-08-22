#include <gtest/gtest.h>
#include <my_robot_project/kinematics.hpp>

// Test fixture for the Kinematics class
class KinematicsTest : public ::testing::Test {
protected:
   my_robot_project::Kinematics kinematics_{6}; // 6-DOF arm
};

// Test the constructor
TEST_F(KinematicsTest, Constructor) {
   EXPECT_EQ(kinematics_.getNumJoints(), 6);
}

// Test a basic forward kinematics calculation
TEST_F(KinematicsTest, ForwardKinematics) {
   std::vector<double> joint_angles = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
   auto pose = kinematics_.forward(joint_angles);
   // Basic assertion: Expect two values to be equal
   EXPECT_DOUBLE_EQ(pose.x, 1.234); // Expected value for home position
}
