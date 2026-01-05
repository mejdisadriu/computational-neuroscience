# Basic Neuron Models

This directory contains implementations of fundamental neuron models, progressing from simplest to more realistic.

## Models

### 1. Basic Integrate Fire Neuron    (`basic-integrate-fire-neuron.py`)
The absolute simplest model - voltage accumulates until threshold.

**Key Concepts:**
- Voltage accumulation
- Threshold crossing
- Reset mechanism



### 2. Integrate-and-Fire (`integrate_and_fire.py`)
Classic I&F model with proper time discretization.

**New Concepts:**
- Time step (`dt`)
- Numerical integration
- Continuous time simulation



### 3. Leaky Integrate-and-Fire (`leaky_integrate_fire.py`)
Adds membrane leak - voltage decays without input.

**New Concepts:**
- Membrane time constant (`tau`)
- Exponential decay
- Resting potential


## Notebooks

Interactive Jupyter notebooks for exploration:
- `01_threshold_neuron.ipynb` - Step-by-step explanation
- `02_integrate_fire.ipynb` - Comparing parameters
- `03_leaky_IF.ipynb` - Understanding membrane dynamics


