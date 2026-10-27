# Optical Systems Portfolio
## High-Speed Optical Communication \| PAM4 \| Transceivers \| System Validation

A Python-based engineering portfolio focused on optical link modeling, high-speed IM/DD transceiver simulation, signal integrity, and automated performance validation.

## Overview

This repository develops reusable tools and simulation workflows for optical communication systems, with an emphasis on bridging communication theory and practical transceiver engineering.

The primary goal is to build and characterize a **high-speed PAM4 optical transceiver**, analyze the physical limitations of the link, and develop systematic methods for performance evaluation and validation.

The portfolio combines:

* Physics-based optical communication models
* Digital signal processing and equalization
* Eye diagram, BER, and receiver performance analysis
* Link-budget and signal-integrity evaluation
* Reproducible Python simulations and automated testing

## Projects

| Project | Scope | Status |
|---|---|---|
| [01 Optical System Validation](01_optical_system_validation/) | Optical link budget, power loss, receiver sensitivity threshold, and engineering margin | Baseline implemented |
| [02 High-Speed PAM4 Optical Transceiver](02_imdd_pam4_interconnect/) | PAM4 transmitter, optical channel, receiver, eye diagrams, and BER | In progress |
| [03 High-Speed Signal Integrity & DSP](03_laser_and_receiver_analysis/) | Frequency response, S-parameters, bandwidth limitations, and equalization | Planned |
| [04 Automated Transceiver Characterization](04_coherent_800zr_link/) | Receiver sensitivity, performance sweeps, pass/fail criteria, and validation reports | Planned |

## Technologies

- **Core**: Python, NumPy, pytest
- **Optical communication simulation**: OptiCommPy
- **Planned analysis and visualization**: SciPy, Matplotlib, scikit-rf

OptiCommPy provides established optical communication and DSP models, while this repository focuses on system integration, model validation, performance characterization, and engineering analysis.

## Testing
Run from the repository root with the required dependencies installed:

` python -m pytest -q `

Individual components are developed and tested incrementally to maintain reproducibility.

## Repository Structure



## Current Status

The repository is under active development.

Completed and tested:

* Configurable point-to-point optical link-budget model
* Fiber attenuation and insertion-loss calculations
* Received-power and engineering-margin evaluation
* Link-budget pass/fail logic
* PAM4 Gray-coded symbol-mapping verification
* Automated unit tests using pytest

Current test status: 4 passing tests 

