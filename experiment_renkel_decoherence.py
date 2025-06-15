# experiment_renkel_decoherence.py

import numpy as np
import matplotlib.pyplot as plt
import os

from observer_simulator_decoherence import (
    simulate_original_observer as simulate_observer,
    simulate_decoherence_observer
)
from visualization_decoherence import (
    plot_entropy,
    plot_entropy_comparison,
    plot_collapse
)
import config_decoherence as cfg  # <- импорт конфигурации


def main(steps=cfg.STEPS, seed_decoherence=cfg.SEED_DECOHERENCE, seed_original=cfg.SEED_ORIGINAL):
    """
    Run the simulation and plot entropy curves and collapse probabilities.
    Outputs are saved as high-resolution figures.

    Parameters:
        steps (int): Number of stochastic samples per λ.
        seed_decoherence (int): Random seed for decoherence model.
        seed_original (int): Random seed for original observer model.
    """
    lambdas = np.linspace(0.5, 2.5, 50)

    print("Simulating observer (decoherence model)...")
    entropies_new = simulate_decoherence_observer(
        lambdas, steps=steps, seed=seed_decoherence
    )

    print("Simulating observer (original model)...")
    entropies_old = simulate_observer(
        lambdas, steps=steps, seed=seed_original
    )

    collapse_probs = 0.5 + 0.5 * np.tanh(lambdas - 1.0)

    os.makedirs("results", exist_ok=True)

    plot_entropy(lambdas, entropies_new, "results")
    plot_entropy_comparison(lambdas, entropies_old, entropies_new, "results")
    plot_collapse(lambdas, collapse_probs, "results")

    # Summary plot
    plt.figure(figsize=(10, 6))
    plt.plot(lambdas, collapse_probs, label="Collapse probability", color="red", linewidth=2)
    plt.plot(lambdas, entropies_new, label="Observer entropy (decoherence)", color="blue", linestyle="--")
    plt.plot(lambdas, entropies_old, label="Observer entropy (original)", color="green", linestyle="-.")

    plt.xlabel("λ (scale of distinguishability)")
    plt.ylabel("Entropy / Collapse Probability")
    plt.title("Decoherence Model vs Original Observer Model")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("results/decoherence_effects.pdf", dpi=600)
    plt.savefig("results/decoherence_effects.png", dpi=600)
    plt.show()


if __name__ == "__main__":
    main()
