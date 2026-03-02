import numpy as np

def mc_dropout_predict(probs_samples: list[list[float]]) -> dict:
    arr = np.array(probs_samples)
    return {"mean": arr.mean(axis=0).tolist(), "uncertainty": arr.var(axis=0).mean().item()}
