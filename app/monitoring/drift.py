import numpy as np


class DriftCalculationError(Exception):
    pass


def population_stability_index(
    reference: np.ndarray,
    current: np.ndarray,
    bins: int = 10,
    epsilon: float = 1e-6,
) -> float:
    """
    Calculate Population Stability Index between
    reference and current feature distributions.

    PSI = Σ (current_pct - reference_pct)
              * ln(current_pct / reference_pct)
    """

    reference = np.asarray(
        reference,
        dtype=float,
    )

    current = np.asarray(
        current,
        dtype=float,
    )

    if reference.size == 0:
        raise DriftCalculationError(
            "Reference distribution cannot be empty"
        )

    if current.size == 0:
        raise DriftCalculationError(
            "Current distribution cannot be empty"
        )

    if bins < 2:
        raise DriftCalculationError(
            "At least two bins are required"
        )

    boundaries = np.quantile(
        reference,
        np.linspace(
            0,
            1,
            bins + 1,
        ),
    )

    # Avoid duplicated quantile boundaries.
    boundaries = np.unique(
        boundaries
    )

    if len(boundaries) < 3:
        raise DriftCalculationError(
            "Reference distribution does not "
            "contain enough variation"
        )

    boundaries[0] = -np.inf
    boundaries[-1] = np.inf

    reference_counts, _ = np.histogram(
        reference,
        bins=boundaries,
    )

    current_counts, _ = np.histogram(
        current,
        bins=boundaries,
    )

    reference_pct = (
        reference_counts
        / reference_counts.sum()
    )

    current_pct = (
        current_counts
        / current_counts.sum()
    )

    reference_pct = np.clip(
        reference_pct,
        epsilon,
        None,
    )

    current_pct = np.clip(
        current_pct,
        epsilon,
        None,
    )

    psi = np.sum(
        (current_pct - reference_pct)
        * np.log(
            current_pct / reference_pct
        )
    )

    return float(psi)
