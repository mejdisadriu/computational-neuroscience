# Basic Neuron Models

This directory contains implementations of fundamental neuron models, progressing from simplest to more realistic.

## Models

### 1. Basic Integrate Fire Neuron    (`basic-integrate-fire-neuron.py`)
The absolute simplest model - voltage accumulates until threshold.

**Key Concepts:**
- Voltage accumulation
- Threshold crossing
- Reset mechanism

**Run:**
```bash
python basic-integrate-fire-neuron.py
```

**Parameters to experiment with:**
- `input_current`: Try 0.5, 1.0, 2.0
- `threshold`: Try -55, -50, -45

### 2. Integrate-and-Fire (`integrate_and_fire.py`)
Classic I&F model with proper time discretization.

**New Concepts:**
- Time step (`dt`)
- Numerical integration
- Continuous time simulation

**Run:**
```bash
python integrate_and_fire.py --input 20 --dt 0.1
```

### 3. Leaky Integrate-and-Fire (`leaky_integrate_fire.py`)
Adds membrane leak - voltage decays without input.

**New Concepts:**
- Membrane time constant (`tau`)
- Exponential decay
- Resting potential

**Mathematical Model:**
```
τ dV/dt = -(V - V_rest) + R*I
```

**Run:**
```bash
python leaky_integrate_fire.py --tau 10 --input 1.5
```

## Notebooks

Interactive Jupyter notebooks for exploration:
- `01_threshold_neuron.ipynb` - Step-by-step explanation
- `02_integrate_fire.ipynb` - Comparing parameters
- `03_leaky_IF.ipynb` - Understanding membrane dynamics

## Figures

All generated plots are saved in `figures/` directory.

## Next Steps

After mastering these models, proceed to:
- `02-advanced-models/` for Hodgkin-Huxley
- `03-network-dynamics/` for multi-neuron systems
