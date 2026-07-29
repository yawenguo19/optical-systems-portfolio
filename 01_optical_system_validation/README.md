# 01 — Optical System Validation

## Overview

This project implements a Python toolkit for validating optical communication links.

The current version focuses on point-to-point link budget analysis and provides reusable modules for evaluating receiver power, system margin, and pass/fail conditions.

Future extensions will include amplifier modeling, OSNR analysis, receiver sensitivity, and end-to-end optical system validation.

## Features

- Optical link budget calculation
- Fiber attenuation modeling
- Connector loss modeling
- Receiver sensitivity evaluation
- System margin calculation
- Pass / Fail validation

## System Model
<p align="center">
  <img src="figures/system_model.svg" width="700">
</p>

The received optical power is computed by subtracting the accumulated insertion loss from the transmitted optical power.

## Example

tx_power = 3
fiber_length = 40
attenuation = 0.22
connector_loss = 1

Output: 
Receiver Power : -7.8 dBm
System Margin : 8.2 dB
PASS

## Repository Structure
link_budget.py
validation.py
example_link.py

## Future Work

- EDFA modeling
- ASE noise
- OSNR estimation
- Receiver noise
- BER prediction


