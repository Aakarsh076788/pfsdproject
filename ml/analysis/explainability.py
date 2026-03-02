"""Explainability stubs for Grad-CAM, saliency, and activation maps."""

def grad_cam(image_path: str, model_path: str) -> str:
    return "artifacts/gradcam.png"

def saliency_map(image_path: str, model_path: str) -> str:
    return "artifacts/saliency.png"

def activation_map(image_path: str, model_path: str) -> str:
    return "artifacts/activation.png"
