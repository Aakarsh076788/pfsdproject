import numpy as np

def apply_gaussian_noise(img: np.ndarray, sigma: float) -> np.ndarray:
    noise = np.random.normal(0, sigma, img.shape)
    return np.clip(img + noise, 0, 1)
