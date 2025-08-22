#include "my_robot_project/kinematics.hpp"

#include <stdexcept>

namespace my_robot_project {

Kinematics::Kinematics(int num_joints) : num_joints_(num_joints) {}

Pose Kinematics::forward(const std::vector<double>& joint_angles) {
    if (joint_angles.size() != num_joints_) {
        throw std::runtime_error("Invalid number of joint angles.");
    }
    // Placeholder implementation
    return {1.234, 0.0, 0.0};
}

std::vector<double> Kinematics::inverse(const Pose& pose) {
    // Placeholder implementation
    return std::vector<double>(num_joints_, 0.0);
}

int Kinematics::getNumJoints() const {
    return num_joints_;
}

} // namespace my_robot_project
