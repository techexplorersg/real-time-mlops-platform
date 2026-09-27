from app.governance.promotion import (
    ModelMetrics,
    PromotionPolicy,
    evaluate_candidate,
)


def test_good_challenger_is_approved():

    champion = ModelMetrics(
        accuracy=0.88,
        p95_latency_ms=100,
        error_rate=0.01,
    )

    challenger = ModelMetrics(
        accuracy=0.90,
        p95_latency_ms=105,
        error_rate=0.01,
    )

    decision = evaluate_candidate(
        champion,
        challenger,
        PromotionPolicy(),
    )

    assert decision.approved


def test_slow_challenger_is_rejected():

    champion = ModelMetrics(
        accuracy=0.88,
        p95_latency_ms=100,
        error_rate=0.01,
    )

    challenger = ModelMetrics(
        accuracy=0.91,
        p95_latency_ms=150,
        error_rate=0.01,
    )

    decision = evaluate_candidate(
        champion,
        challenger,
        PromotionPolicy(),
    )

    assert not decision.approved

    assert (
        "P95 latency increase exceeds policy."
        in decision.reasons
    )
