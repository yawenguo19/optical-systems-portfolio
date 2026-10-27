# 01 — Optical System Validation
## Optical Link Budget \| Receiver Power \| Engineering Margin

A Python-based optical link-budget model for evaluating received optical power, link losses, and system margin.

## Overview

Optical link budgeting is a fundamental step in communication system design and validation.

This project implements a configurable point-to-point optical link-budget calculator that estimates received power and evaluates whether a link meets specified receiver sensitivity and engineering-margin requirements.

The implementation emphasizes reusable Python components, transparent calculations, and automated testing.

## System Model
<p align="center">
  <img
    src="figures/system_model.svg"
    alt="Point-to-point optical link model"
    width="900"
  >
</p>

The baseline model includes:

* Optical transmitter power
* Fiber attenuation and propagation distance
* Additional insertion losses
* Receiver sensitivity threshold
* Required engineering margin

## Mathematical Model

Fiber attenuation is calculated as:

$$
L_{\mathrm{fiber}} = \alpha L
$$

where $\alpha$ is the attenuation coefficient in dB/km and $L$ is the fiber length in km.

The total link loss is:

$$
L_{\mathrm{total}} = L_{\mathrm{fiber}} + L_{\mathrm{other}}
$$

Received optical power is:

$$
P_{\mathrm{RX}} = P_{\mathrm{TX}} - L_{\mathrm{total}}
$$

where optical powers are expressed in dBm and losses in dB.

Available link margin:

$$
M_{\mathrm{available}} = P_{\mathrm{RX}} - P_{\mathrm{sensitivity}}
$$

Net engineering margin:

$$
M_{\mathrm{net}} = M_{\mathrm{available}} - M_{\mathrm{required}}
$$

The link passes the power-budget check when:

$$
M_{\mathrm{net}} \geq 0
$$


## Example Validation
The example uses the following configuration:

|Parameter | Value|
| :---|:--- |
|Fiber length |40km|
|Fiber attenuation| 0.22dB/km|
|Transimission power| 3dBm|
|Additional insertion loss| 1dB|
|Receiver sensitivity| -16dBm|
|Required engineering margin| 3dB|

## Example Results

```text
fiber loss :        8.80 dB
Total loss :        9.80 dB
Receiver Power:     -6.80 dBm
available margin:   9.20 dB
net margin:         6.20 dB
Status:             PASS
```

The model predicts 6.2 dB of net margin beyond the specified engineering-margin requirement.

This is a power-budget result, not a measured BER or a complete link-performance qualification.

## Implementation
The model and example are organized as follows:
```text
optical-systems-portfolio/
├── optical_systems/
│   └── validation/
│       └── link_budget.py
├── 01_optical_system_validation/
│   ├── README.md
│   ├── examples/
│   │   └── basic_link.py
│   └── figures/
│       └── system_model.svg
└── tests/
    └── test_link_budget.py
```


## Testing
Run the link-budget unit tests from the repository root:

` python -m pytest tests/test_link_budget.py -q`

The project uses pytest to verify model behavior and expected calculations.


## Planned Extensions

* Optical power budget versus fiber distance
* Maximum supported distance estimation
* Component-level loss visualization
* Automated parameter sweeps
* Structured validation reports

Future integration with the PAM4 transceiver simulator will allow link-budget results to be compared with simulated receiver and BER performance.

