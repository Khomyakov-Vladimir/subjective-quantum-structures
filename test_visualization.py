# test_visualization.py

import numpy as np
import visualization_decoherence as viz

# Synthetic test data
Lambda_values = np.linspace(0.5, 2.5, 50)
entropy_new = np.sin(Lambda_values) + 1.5  # synthetic entropy curve (new model)
entropy_old = np.cos(Lambda_values) + 1.5  # synthetic entropy curve (old model)
collapse_probs = 0.5 + 0.5 * np.tanh(Lambda_values - 1.0)

# Output directory for results
results_dir = "results"

# Function calls for plotting
viz.plot_entropy(Lambda_values, entropy_new, results_dir)
viz.plot_collapse(Lambda_values, collapse_probs, results_dir)
viz.plot_decoherence_effect(Lambda_values, entropy_new, entropy_old, results_dir)
viz.plot_entropy_comparison(Lambda_values, entropy_new, entropy_old, results_dir)
