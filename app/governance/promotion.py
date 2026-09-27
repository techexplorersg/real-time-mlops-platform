from dataclasses import dataclass


@dataclass(frozen=True)
class ModelMetrics:
    accuracy: float
    p95_latency_ms: float
    error_rate: float


@dataclass(frozen=True)
class PromotionPolicy:
    max_accuracy_regression: float = 0.01
    max_latency_increase_pct: float = 20.0
    max_error_rate: float = 0.02


@dataclass(frozen=True)
class PromotionDecision:
    approved: bool
    reasons: tuple[str, ...]


def evaluate_candidate(
    champion: ModelMetrics,
    challenger: ModelMetrics,
    policy: PromotionPolicy,
) -> PromotionDecision:

    reasons = []

    accuracy_delta = (
        challenger.accuracy
        - champion.accuracy
    )

    if (
        accuracy_delta
        < -policy.max_accuracy_regression
    ):
        reasons.append(
            "Accuracy regression exceeds policy."
        )

    if champion.p95_latency_ms > 0:

        latency_increase = (
            (
                challenger.p95_latency_ms
                - champion.p95_latency_ms
            )
            / champion.p95_latency_ms
        ) * 100

        if (
            latency_increase
            > policy.max_latency_increase_pct
        ):
            reasons.append(
                "P95 latency increase exceeds policy."
            )

    if (
        challenger.error_rate
        > policy.max_error_rate
    ):
        reasons.append(
            "Error rate exceeds policy."
        )

    return PromotionDecision(
        approved=not reasons,
        reasons=tuple(reasons),
    )
