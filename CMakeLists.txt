# Require a modern version of CMake
cmake_minimum_required(VERSION 3.14)

# Define the project name, version, and languages
project(MyRobotProject VERSION 1.0.0 LANGUAGES CXX)

# Enforce modern C++ standard across all targets
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# --- Best Practices ---

# Require out-of-source builds to keep the source directory clean
# This prevents mixing source files with build artifacts.
file(TO_CMAKE_PATH "${PROJECT_BINARY_DIR}/CMakeLists.txt" LOC_PATH)
if(EXISTS "${LOC_PATH}")
   message(FATAL_ERROR "You cannot build in a source directory. Please create a separate build directory.")
endif()

# Add our custom cmake module directory to the search path
list(APPEND CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake")

# --- Dependencies ---

# Add pybind11 from the submodule
add_subdirectory(extern/pybind11)

# Add GoogleTest via FetchContent
include(FetchContent)
FetchContent_Declare(
   googletest
   URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

# --- Include Sub-components ---

# Add the core C++ libraries
add_subdirectory(src)

# Add the C++ applications
add_subdirectory(apps)

# Add the Python bindings
add_subdirectory(python)

# Enable testing and add the test suite
enable_testing()
add_subdirectory(tests)
