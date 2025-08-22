#!/bin/bash

echo "🧪 Testing CI Workflow Steps Locally"
echo "===================================="

# Step 1: Checkout (simulated)
echo "✅ Step 1: Checkout repository and submodules"
echo "   (Simulated - we're already in the repo)"

# Step 2: Set up Bazel
echo "✅ Step 2: Set up Bazel"
bazel --version
if [ $? -eq 0 ]; then
    echo "   Bazel is available"
else
    echo "   ❌ Bazel not found"
    exit 1
fi

# Step 3: Build all targets
echo "✅ Step 3: Build all targets"
bazel build //... --compilation_mode=opt
if [ $? -eq 0 ]; then
    echo "   Build successful"
else
    echo "   ❌ Build failed"
    exit 1
fi

# Step 4: Test all targets
echo "✅ Step 4: Test all targets"
bazel test //... --compilation_mode=opt
if [ $? -eq 0 ]; then
    echo "   Tests passed"
else
    echo "   ❌ Tests failed"
    exit 1
fi

# Step 5: Set up Python
echo "✅ Step 5: Set up Python"
python --version
if [ $? -eq 0 ]; then
    echo "   Python is available"
else
    echo "   ❌ Python not found"
    exit 1
fi

# Step 6: Install Python dependencies and run tests
echo "✅ Step 6: Install Python dependencies and run tests"
pip install pytest
python setup.py install
pytest tests/python/
if [ $? -eq 0 ]; then
    echo "   Python tests passed"
else
    echo "   ❌ Python tests failed"
    exit 1
fi

echo ""
echo "🎉 All CI workflow steps passed locally!"
echo "The workflow should work in GitHub Actions."
