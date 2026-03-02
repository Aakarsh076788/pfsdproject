from app.services.metrics import compute_rsi, expected_calibration_error


def test_rsi_range():
    score = compute_rsi(0.8, 0.7, 0.75, 0.85, 0.65)
    assert 0 <= score <= 100


def test_ece():
    out = expected_calibration_error([0.1, 0.9], [0, 1])
    assert "ece" in out
