from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from optical_systems.transceiver.pam4 import (
    generate_pam4_symbols,
    generate_pam4_waveform,
)
from optical_systems.transceiver.channel import rc_lowpass

# Experiment configuration
RS = 50e9
SPS = 8 
N_SYMBOLS = 8192
BANDWIDTH = [12.5e9, 25e9, 40e9]
LEVELS = np.array([-3, -1, 1, 3])

_, symbols = generate_pam4_symbols(N_SYMBOLS, seed = 2026)
_, tx = generate_pam4_waveform(symbols, RS, SPS)

fs = RS * SPS
discard = 100 # exclude initial symbols

fig, axes = plt.subplots(
    1, 3, figsize = (11, 3.5),
    sharex = True, sharey = True,
    layout = "constrained",
)

for ax, bandwidth in zip(axes, BANDWIDTH):
    rx = rc_lowpass(tx, fs, bandwidth)

    # The current RC implementation reports the output
    # at the end of each sample-and-hold interval.
    # Index SPS//2 -1 corresponds to the UI midpoint.
    sampled = rx[SPS//2 - 1 :: SPS]

    a = symbols[discard:]
    y = sampled[discard:]

    eye_gaps = [
        np.min(y[a==LEVELS[i+1]])
        - np.max(y[a==LEVELS[i]])
        for i in range(3)
    ]

    min_eye = min(eye_gaps)

    print(
        f"BW = {bandwidth / 1e9:4.1f} GHz |"
        f"Eye clearances = {np.round(eye_gaps, 3)} |"
        f"Minmum = {min_eye: .3f}"
    )

    # Overlay 120 two-UI waveform segments
    eye_time = (np.arange(2*SPS)+1)/SPS

    for k in range(discard, discard+ 120):
        segment = rx[k*SPS:(k+2)*SPS]
        ax.plot(
            eye_time, segment,
            color = "#1879A9",
            alpha = 0.12,
            linewidth = 0.6
        )

    ax.set_title(f"Bandwidth = {bandwidth/1e9:g}GHz")
    ax.set_xlabel("Time (UI)")
    ax.set_xlim(0,2)
    ax.set_ylim(-3.8,3.8)
    ax.set_xticks([0,0.5,1,1.5,2])
    ax.grid(alpha = 0.2)

axes[0].set_ylabel("Normalized PAM4 amplitude")

output = Path("02_imdd_pam4_interconnect/figures")
output.mkdir(parents=True, exist_ok=True)

fig.savefig(output / "pam4_bandwidth_sweep.png", dpi = 300)
fig.savefig(output / "pam4_bandwidth_sweep.svg")

plt.show()
