#!/bin/bash

echo "🧪 Testing Exact GitHub Actions CI Workflow Steps"
echo "=================================================="

# Simulate the exact environment and steps from .github/workflows/ci.yml

# Step 1: Checkout (simulated)
echo "✅ Step 1: Checkout repository and submodules"
echo "   (Simulated - we're already in the repo)"

# Step 2: Set up Bazel (simulated - we already have it)
echo "✅ Step 2: Set up Bazel"
bazel --version
if [ $? -eq 0 ]; then
    echo "   Bazel is available"
else
    echo "   ❌ Bazel not found"
    exit 1
fi

# Step 3: Build all targets (exact command from CI)
echo "✅ Step 3: Build all targets"
echo "   Running: bazel build //..."
bazel build //...
if [ $? -eq 0 ]; then
    echo "   Build successful"
else
    echo "   ❌ Build failed"
    exit 1
fi

# Step 4: Test all targets (exact command from CI)
echo "✅ Step 4: Test all targets"
echo "   Running: bazel test //..."
bazel test //...
if [ $? -eq 0 ]; then
    echo "   Tests passed"
else
    echo "   ❌ Tests failed"
    exit 1
fi

# Step 5: Set up Python (simulated - we already have it)
echo "✅ Step 5: Set up Python"
python --version
if [ $? -eq 0 ]; then
    echo "   Python is available"
else
    echo "   ❌ Python not found"
    exit 1
fi

# Step 6: Install Python dependencies and run tests (EXACT commands from CI)
echo "✅ Step 6: Install Python dependencies and run tests"
echo "   Running: pip install pytest"
pip install pytest
if [ $? -ne 0 ]; then
    echo "   ❌ Failed to install pytest"
    exit 1
fi

echo "   Running: pip install -e ."
pip install -e .
if [ $? -ne 0 ]; then
    echo "   ❌ Failed to install package with pip install -e ."
    exit 1
fi

echo "   Running: pytest tests/python"
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
