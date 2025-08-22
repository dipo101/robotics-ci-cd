# Define the executable target from its main source file
add_executable(my_app
   main.cpp
)

# Link the application against the libraries it needs.
# The linkage is PRIVATE because the application is a final product;
# no other target will link against 'my_app'. The usage requirements
# (include directories, etc.) from 'kinematics' will be correctly
# propagated to 'my_app'.
target_link_libraries(my_app
   PRIVATE
       kinematics
)
