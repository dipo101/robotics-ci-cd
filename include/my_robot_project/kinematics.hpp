#pragma once

#include <vector>

namespace my_robot_project {

// A placeholder struct for robot pose.
struct Pose {
    double x = 0.0;
    double y = 0.0;
    double z = 0.0;
};

class Kinematics {
public:
    explicit Kinematics(int num_joints);

    Pose forward(const std::vector<double>& joint_angles);

    std::vector<double> inverse(const Pose& pose);

    int getNumJoints() const;

private:
    int num_joints_;
};

} // namespace my_robot_project
