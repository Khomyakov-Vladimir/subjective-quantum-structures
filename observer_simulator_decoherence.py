# observer_simulator_decoherence.py
# Observer simulation with and without decoherence
# Part of the Cognitive Observer framework

import numpy as np
from tqdm import tqdm


def simulate_decoherence_observer(lambda_values, steps=100, seed=42):
    """
    Simulates the observer's entropy under a decoherence-based probabilistic model.

    Parameters:
        lambda_values (array-like): Input values of λ (scale of distinguishability).
        steps (int): Number of stochastic samples per λ.
        seed (int): Random seed for reproducibility.

    Returns:
        np.ndarray: Estimated entropy values for each λ.
    """
    np.random.seed(seed)
    entropy_values = []

    for lam in tqdm(lambda_values, desc="Simulating Decoherence"):
        prob = 0.5 + 0.5 * np.tanh(lam - 1.0)
        samples = np.random.binomial(1, prob, size=steps)
        p = np.mean(samples)
        entropy = -p * np.log(p + 1e-9) - (1 - p) * np.log(1 - p + 1e-9)
        entropy_values.append(entropy)

    return np.array(entropy_values)


def simulate_original_observer(lambda_values, steps=100, seed=123):
    """
    Simulates the observer's entropy using the original sigmoid-based model.

    Parameters:
        lambda_values (array-like): Input values of λ (scale of distinguishability).
        steps (int): Number of stochastic samples per λ.
        seed (int): Random seed for reproducibility.

    Returns:
        np.ndarray: Estimated entropy values for each λ.
    """
    np.random.seed(seed)
    entropy_values = []

    for lam in tqdm(lambda_values, desc="Simulating Original Observer"):
        prob = 1.0 / (1.0 + np.exp(-lam))
        samples = np.random.binomial(1, prob, size=steps)
        p = np.mean(samples)
        entropy = -p * np.log(p + 1e-9) - (1 - p) * np.log(1 - p + 1e-9)
        entropy_values.append(entropy)

    return np.array(entropy_values)


def compute_collapse_probability(lambda_values):
    """
    Computes the phenomenological collapse probability.

    Parameters:
        lambda_values (array-like): Input values of λ.

    Returns:
        np.ndarray: Collapse probabilities corresponding to each λ.
    """
    return 0.5 + 0.5 * np.tanh(lambda_values - 1.0)

if __name__ == "__main__":
    lambdas = np.linspace(0.5, 2.5, 10)
    entropies_dec = simulate_decoherence_observer(lambdas)
    entropies_orig = simulate_original_observer(lambdas)
    print("Decoherence entropies:", entropies_dec)
    print("Original entropies:", entropies_orig)
