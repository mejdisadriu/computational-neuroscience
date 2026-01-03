"""
Threshold Neuron - The Simplest Spiking Model
==============================================
Pure Python + Matplotlib for visualization

Voltage rises with input. When it hits threshold:  SPIKE!
"""

import matplotlib.pyplot as plt

# =============================================================================
# SETTINGS
# =============================================================================

voltage = -70           # Start voltage (mV)
threshold = -55         # Spike threshold (mV)
input_current = 0.5     # Input strength
time_total = 100        # Simulation time (ms)

# =============================================================================
# STORAGE
# =============================================================================

spike_times = []
voltage_history = []
time_history = []

# =============================================================================
# SIMULATION
# =============================================================================

print("\n" + "="*60)
print("THRESHOLD NEURON SIMULATION")
print("="*60)
print(f"Input: {input_current} | Threshold: {threshold}mV\n")

for t in range(time_total):
    
    # Add input
    voltage = voltage + input_current
    
    # Check threshold
    if voltage >= threshold:
        print(f"⚡ SPIKE at {t}ms (voltage: {voltage:.1f}mV)")
        spike_times.append(t)
        voltage = -70  # Reset
    elif t % 10 == 0:
        print(f"t={t}ms: {voltage:.1f}mV")
    
    # Store for plotting
    voltage_history.append(voltage)
    time_history.append(t)

# =============================================================================
# RESULTS
# =============================================================================

print(f"\n{'='*60}")
print(f"Total spikes: {len(spike_times)}")
if spike_times:
    rate = len(spike_times) / (time_total/1000)
    print(f"Firing rate: {rate:.1f} Hz")
print("="*60 + "\n")

# =============================================================================
# VISUALIZATION
# =============================================================================

plt.figure(figsize=(12, 6))

# Plot voltage
plt.plot(time_history, voltage_history, linewidth=2, color='blue', 
         label='Voltage')

# Plot threshold line
plt.axhline(y=threshold, color='red', linestyle='--', linewidth=2, 
            label=f'Threshold ({threshold}mV)')

# Mark spikes
for spike_t in spike_times:
    plt.axvline(x=spike_t, color='orange', alpha=0.5, linewidth=2)

# Labels and formatting
plt.xlabel('Time (ms)', fontsize=12, fontweight='bold')
plt.ylabel('Voltage (mV)', fontsize=12, fontweight='bold')
plt.title('Threshold Neuron Model', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.ylim(-75, -50)

# Add spike count on plot
if spike_times:
    plt.text(5, -52, f'{len(spike_times)} spikes | {rate:.1f} Hz',
             fontsize=11, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

plt.tight_layout()
plt.show()

print("Try changing 'input_current' to 1.0 and run again!")
