# Create the Python extension module.
# The first argument is the name of the module as it will be imported in Python.
# The subsequent arguments are the C++ source files containing the binding code.
pybind11_add_module(_bindings
   src/bindings.cpp
)

# Link the Python module against the C++ libraries it exposes.
# This demonstrates the power of the target-based system: the Python module
# is just another target that consumes our C++ library, automatically
# inheriting its usage requirements (e.g., include directories).
target_link_libraries(_bindings
   PRIVATE
       kinematics
)
