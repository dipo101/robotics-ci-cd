# Create an executable for the kinematics tests
add_executable(kinematics_test
   test_kinematics.cpp
)

# Link the test executable against the library it is testing ('kinematics')
# and the GoogleTest main library. GTest::gtest_main provides a main()
# function and initializes GoogleTest.
target_link_libraries(kinematics_test
   PRIVATE
       kinematics
       GTest::gtest_main
)

# Use the GoogleTest CMake module to automatically discover tests
include(GoogleTest)
gtest_discover_tests(kinematics_test)
