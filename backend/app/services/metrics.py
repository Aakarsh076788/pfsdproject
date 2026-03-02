from __future__ import annotations
import math
from typing import Dict


def compute_rsi(clean_acc: float, noise_robustness: float, adv_stability: float, calibration_reliability: float, uncertainty_consistency: float) -> float:
    weights = {
        "clean_acc": 0.25,
        "noise": 0.2,
        "adv": 0.2,
        "calib": 0.2,
        "uncertainty": 0.15,
    }
    score = (
        clean_acc * weights["clean_acc"]
        + noise_robustness * weights["noise"]
        + adv_stability * weights["adv"]
        + calibration_reliability * weights["calib"]
        + uncertainty_consistency * weights["uncertainty"]
    )
    return round(score * 100, 2)


def expected_calibration_error(confidences: list[float], accuracies: list[int], bins: int = 10) -> Dict[str, float | list[float]]:
    ece = 0.0
    n = len(confidences)
    hist = []
    for b in range(bins):
        lo, hi = b / bins, (b + 1) / bins
        idx = [i for i, c in enumerate(confidences) if lo <= c < hi]
        if not idx:
            hist.append(0)
            continue
        bin_acc = sum(accuracies[i] for i in idx) / len(idx)
        bin_conf = sum(confidences[i] for i in idx) / len(idx)
        ece += abs(bin_acc - bin_conf) * (len(idx) / n)
        hist.append(len(idx))
    return {"ece": round(ece, 4), "histogram": hist}


def kl_drift(p: list[float], q: list[float]) -> float:
    eps = 1e-8
    return float(sum(pi * math.log((pi + eps) / (qi + eps)) for pi, qi in zip(p, q)))
