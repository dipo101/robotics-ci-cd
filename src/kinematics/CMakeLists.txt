# Define the library target from its source files
add_library(kinematics
   kinematics.cpp
)

# Specify the public include directory for this library.
# Consumers of this library will automatically get this include path.
target_include_directories(kinematics
   PUBLIC
       # The path to the public headers for this component
       $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
       # The path for installed headers
       $<INSTALL_INTERFACE:include>
)
