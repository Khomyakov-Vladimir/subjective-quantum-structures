# Subjective Quantum Structures — Decoherence and Observer Collapse Simulation
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15670260.svg)](https://doi.org/10.5281/zenodo.15670260)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> 📌 **Note:** A newer version of the related article is available:  
> **Version 3.0 – June 2025**: [https://doi.org/10.5281/zenodo.15706835](https://doi.org/10.5281/zenodo.15706835)  
> Please consider referring to this updated version for the most recent results and clarifications.

> 📌 **Note:** This model complements the simulator-based framework described in  
> **Cognitive Simulator and Subjective Physics – Version 6.0 (June 2025)**  
> [https://doi.org/10.5281/zenodo.15705869](https://doi.org/10.5281/zenodo.15705869)

This repository contains the simulation code and visualizations accompanying the second study on subjective quantum structures, observer decoherence, and categorical collapse models in the context of cognitive quantum physics. This work extends the simulation framework introduced in the previous publication:

**Khomyakov, V. (2025). Subjective Quantum Structures: A Categorical Model of Observer Collapse.**
Zenodo. [https://doi.org/10.5281/zenodo.15670260](https://doi.org/10.5281/zenodo.15670260)

---

## Overview

The project includes the following Python modules:

* **`experiment_renkel_decoherence.py`**
  Main simulation script modeling entropy dynamics and collapse probabilities under observer decoherence.

* **`observer_simulator_decoherence.py`**
  Core logic for cognitive observers, modeling decoherence as emergent instability in subjective phase space.

* **`visualization_decoherence.py`**
  Plotting and figure generation for all results used in the publication.

* **`test_visualization.py`**
  Unit tests to ensure correctness and consistency of generated visualizations.

* **`config_decoherence.py`**
  Stores default parameters and simulation constants (step count, seeds, thresholds) for reproducible experiments.

All plots are saved to the `results/` directory in both `.pdf` and `.png` formats.

---

## Directory Structure

```
decoherence_experiment/
├── LICENSE
├── .gitignore
├── README.md
├── requirements.txt
├── config_decoherence.py
├── experiment_renkel_decoherence.py
├── observer_simulator_decoherence.py
├── visualization_decoherence.py
├── test_visualization.py
├── results/
│   ├── ...
└── figures/
    ├── decoherence_effects.pdf
    ├── decoherence_effects.png
    ├── plot_collapse.pdf
    ├── plot_collapse.png
    ├── plot_decoherence.pdf
    ├── plot_decoherence.png
    ├── plot_entropy.pdf
    ├── plot_entropy.png
    ├── plot_entropy_comparison.pdf
    └── plot_entropy_comparison.png
```

---

## Requirements

This project uses the following Python libraries:

* `numpy`
* `matplotlib`
* `tqdm`
* `pytest`

Install them with:

```bash
pip install -r requirements.txt
```

---

## Usage

To run the simulation:

```bash
python experiment_renkel_decoherence.py
```

Generated plots will be saved in the `results/` directory. The script automatically creates the directory if it doesn't exist.

To generate visualizations independently:

```bash
python visualization_decoherence.py
```

To test plot generation:

```bash
python test_visualization.py
```

---

## Output figures

* `decoherence_effects.pdf/png`  
  **Summary plot combining all key dynamics.**  
  Integrates entropy, collapse probability, and decoherence effects.

* `plot_collapse.pdf/png`  
  **Observer collapse probability vs. λ (state distinguishability).**

* `plot_entropy_comparison.pdf/png`  
  **Comparison of entropy: decoherence vs original.**

* `plot_entropy.pdf/png`  
  **Cognitive entropy as a function of resolution ε.**  
  Shows quantized entropy transitions during cognitive differentiation.

* `plot_decoherence.pdf/png`  
  **Decoherence effect on state-space trajectories.**

---

## Configuration

Simulation parameters are defined in `config_decoherence.py`. By default:

```python
STEPS = 100
SEED_DECOHERENCE = 42
SEED_ORIGINAL = 123
```

These can be overridden directly in the script or extended via CLI in future versions.

---

## License

This project is licensed under the terms of the MIT License.

---

## Citation

🔓 Open access publication available at [Zenodo](https://doi.org/10.5281/zenodo.15670260).

If you use this code or refer to the associated research, please cite:

```bibtex
@misc{khomyakov2025subjective_quantum_structures,
  author       = {Khomyakov, Vladimir},
  title        = {Subjective Quantum Structures: A Categorical Model of Observer Collapse},
  year         = 2025,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.15670260},
  url          = {https://doi.org/10.5281/zenodo.15670260},
  note         = {Available at Zenodo; open source code at \url{https://github.com/Khomyakov-Vladimir/subjective-quantum-structures}}
}
```

---

## Related Publications

* 📘 [Cognitive Distinguishability and Quantum Observer Simulation — A Phase Transition Perspective](https://doi.org/10.5281/zenodo.15571107)
* 🧐 Based on the formalism of categorical observers and subjective decoherence in emergent quantum cognition
