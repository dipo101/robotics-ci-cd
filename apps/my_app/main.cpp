#include <iostream>
#include <vector>
#include "my_robot_project/kinematics.hpp"

int main() {
    my_robot_project::Kinematics kinematics(6);
    std::cout << "Kinematics object created for a " << kinematics.getNumJoints() << "-DOF arm." << std::endl;

    std::vector<double> joint_angles = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
    my_robot_project::Pose pose = kinematics.forward(joint_angles);

    std::cout << "Forward kinematics result: " << std::endl;
    std::cout << "x: " << pose.x << ", y: " << pose.y << ", z: " << pose.z << std::endl;

    return 0;
}
