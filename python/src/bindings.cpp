// /python/src/bindings.cpp

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <my_robot_project/kinematics.hpp> // Include the C++ header to be bound

namespace py = pybind11;

// The PYBIND11_MODULE macro creates a function that will be called when
// the Python module is imported. The module name (my_robot_py) must match
// the name given to pybind_extension in Bazel.
PYBIND11_MODULE(my_robot_py, m) {
   // Optional: Add a docstring for the module
   m.doc() = "Python bindings for the MyRobotProject C++ library";

   // Bind the Kinematics C++ class to a Python class named "Kinematics"
   py::class_<my_robot_project::Kinematics>(m, "Kinematics")
       // Bind the constructor that takes the number of joints
      .def(py::init<int>())

       // Bind the 'forward' method. pybind11 automatically handles
       // conversions for standard types like std::vector.
      .def("forward", &my_robot_project::Kinematics::forward, "Calculate forward kinematics")

       // Bind the 'inverse' method
      .def("inverse", &my_robot_project::Kinematics::inverse, "Calculate inverse kinematics")

       // Expose the 'num_joints' public member variable as a read-only property
      .def_property_readonly("num_joints", &my_robot_project::Kinematics::getNumJoints);

    py::class_<my_robot_project::Pose>(m, "Pose")
        .def(py::init<>())
        .def_readwrite("x", &my_robot_project::Pose::x)
        .def_readwrite("y", &my_robot_project::Pose::y)
        .def_readwrite("z", &my_robot_project::Pose::z);
}
