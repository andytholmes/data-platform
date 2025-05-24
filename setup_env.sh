#!/bin/bash

# Check if conda is installed
if ! command -v conda &> /dev/null; then
    echo "Conda is not installed. Please install Miniconda or Anaconda first."
    exit 1
fi

# Remove existing environment if it exists
echo "Removing existing environment if it exists..."
conda env remove -n data-platform

# Create conda environment from environment.yml
echo "Creating conda environment..."
conda env create -f environment.yml

# Activate the environment
echo "Activating environment..."
source $(conda info --base)/etc/profile.d/conda.sh
conda activate data-platform

# Verify Python version
echo "Verifying Python version..."
python --version

# Verify installation
echo "Verifying installation..."
python -c "import pyspark; print(f'PySpark version: {pyspark.__version__}')"
python -c "import pytest; print('pytest installed')"
python -c "import pandas; print('pandas installed')"
python -c "import numpy; print('numpy installed')"
python -c "import jupyter; print('jupyter installed')"

echo "Setup complete! You can now activate the environment with: conda activate data-platform" 