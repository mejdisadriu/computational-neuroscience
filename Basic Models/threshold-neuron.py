"""
Threshold Neuron- The Simplest Spiking Model
==============================================
Pure Python + Matplotlib for visualization

Voltage rises with input. When it hits threshold:  SPIKE!
"""

import matplotlib.pyplot as plt


voltage = -70           # Start voltage (mV)
threshold = -55         # Spike threshold (mV)
input_current = 0.5     # Input per timestep
time_total = 100        # Total simulation time (ms)
voltage_history = []
time_history = []
spike_times = []


for t in range(time_total):
    # Increase voltage by input (simple addition, no integration)
    voltage += input_current

    # Check for spike
    if voltage >= threshold:
        spike_times.append(t)
        voltage = -70  # Reset after spike

    # Store for plotting
    voltage_history.append(voltage)
    time_history.append(t)


plt.figure(figsize=(10,5))
plt.plot(time_history, voltage_history, label='Voltage', color='blue', linewidth=2)
plt.axhline(y=threshold, color='red', linestyle='--', linewidth=2, label=f'Threshold ({threshold} mV)')

# Mark spikes
for spike in spike_times:
    plt.axvline(spike, color='orange', alpha=0.5, linewidth=2)

plt.xlabel('Time (ms)', fontsize=12, fontweight='bold')
plt.ylabel('Voltage (mV)', fontsize=12, fontweight='bold')
plt.title('Threshold Neuron Model', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(alpha=0.3)
plt.ylim(-75, -50)

plt.show()

# Print summary
print(f"Total spikes: {len(spike_times)}")
if time_total > 0:
    firing_rate = len(spike_times) / (time_total/1000)
    print(f"Firing rate: {firing_rate:.1f} Hz")
