import numpy as np

from app.monitoring.drift import (
    DriftStatus,
    classify_drift,
    population_stability_index,
)


def test_similar_distributions_have_low_drift():

    rng = np.random.default_rng(42)

    reference = rng.normal(
        0,
        1,
        5000,
    )

    current = rng.normal(
        0,
        1,
        5000,
    )

    psi = population_stability_index(
        reference,
        current,
    )

    assert psi >= 0

    assert classify_drift(
        psi
    ) in {
        DriftStatus.STABLE,
        DriftStatus.WARNING,
    }


def test_shifted_distribution_increases_psi():

    rng = np.random.default_rng(42)

    reference = rng.normal(
        0,
        1,
        5000,
    )

    current = rng.normal(
        3,
        1,
        5000,
    )

    psi = population_stability_index(
        reference,
        current,
    )

    assert psi > 0.25

    assert (
        classify_drift(psi)
        == DriftStatus.DRIFTED
    )
