# RoboticsCiCd

Python bindings for the toy MyRobotProject C++ library.

This project is a Continuous Integration, Continuous Delivery (CI/CD), and Release pipeline tailored for robotics applications. It's deliberately a modular monorepo to make sure it's maintainable and easy to understand. The project demonstrates a modern Bazel-based build system for hybrid C++/Python robotics projects.

## Architecture

This project uses **Bazel** as the primary build system, providing:
- **Fast, incremental builds** and some precise dependency tracking
- **Hermetic builds** that work consistently across different environments
- **Multi-language support** for C++ and Python in a single build system

## End-to-End Development Flow

1. **Development**: A developer pushes a commit to a feature branch or opens a pull request against the main branch.
2. **CI Trigger**: This action automatically triggers the CI workflow on GitHub Actions.
3. **Matrix Build**: The CI workflow initiates a matrix of parallel jobs, building and testing the code across multiple configurations (Linux and macOS).
4. **Dependency Resolution**: Each job fetches and installs the necessary external dependencies using Bazel's dependency management.
5. **Compilation**: The project is compiled using the Bazel build system.
6. **C++ Unit Testing**: A suite of C++ unit tests, written using the GoogleTest framework, is executed to validate the core logic of individual components.
7. **Python Integration Testing**: Python tests, run via pytest, are executed to validate the correctness of the pybind11 bindings and any pure Python logic.
8. **Quality Gates**: Static analysis and code formatting checks are run to enforce code quality and style consistency.
9. **Release Trigger**: Upon successful integration into the main branch, a developer creates a versioned Git tag (e.g., v1.0.0) to signify a release.
10. **Release Workflow**: The creation of this tag automatically triggers a separate Release workflow.
11. **Python Packaging**: The workflow builds a Python wheel package, which includes the compiled C++ extension module. This package is then published to the Python Package Index (PyPI).
12. **C++ Artifact Packaging**: The workflow also packages the compiled C++ libraries, executables, and public header files into an archive (.tar.gz). This archive is attached to the corresponding GitHub Release.

## Quick Start

### Prerequisites/FYI
- Bazel 7.2.1 or later
- Python 3.10 or later
- C++17 compatible compiler

### Building and Testing
```bash
# Build all targets
bazel build //...

# Run all tests
bazel test //...

# Build and run specific targets
bazel run //apps/my_app:my_app
```

### Python Development
```bash
# Install the package in development mode
pip install -e .

# Run Python tests
pytest tests/python
```

## Project Structure (for now)

```
robotics-ci-cd/
├── apps/                    # C++ executable applications
├── include/                 # Public C++ headers
├── models/                  # Simulation models and assets
├── python/                  # Python bindings and pure Python code
├── src/                     # C++ library sources
├── tests/                   # Test suites (C++ and Python)
├── BUILD.bazel             # Root Bazel build file
├── MODULE.bazel            # Bazel module configuration
└── pyproject.toml          # Python packaging configuration
```

## Technology Stack

- **Build System**: Bazel
- **C++/Python Bridge**: pybind11 (via bzlmod)
- **C++ Testing**: GoogleTest
- **Python Testing**: pytest
- **CI/CD**: GitHub Actions
- **Python Packaging**: setuptools with Bazel integration

This project serves as a reference implementation for modern robotics software development practices, demonstrating how to build maintainable, testable, and distributable hybrid C++/Python projects using Bazel.