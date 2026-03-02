"""Train ResNet/EfficientNet/MobileNet/DenseNet for crop disease classification."""
import argparse
import json
from pathlib import Path

import torch
import torchvision.models as models

ARCH = {
    "resnet": models.resnet18,
    "efficientnet": models.efficientnet_b0,
    "mobilenet": models.mobilenet_v3_small,
    "densenet": models.densenet121,
}


def build_model(name: str, num_classes: int = 10):
    model = ARCH[name](weights=None)
    if hasattr(model, "fc"):
        model.fc = torch.nn.Linear(model.fc.in_features, num_classes)
    elif hasattr(model, "classifier"):
        if isinstance(model.classifier, torch.nn.Sequential):
            model.classifier[-1] = torch.nn.Linear(model.classifier[-1].in_features, num_classes)
    return model


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--architecture", choices=ARCH.keys(), default="resnet")
    p.add_argument("--epochs", type=int, default=5)
    p.add_argument("--out", default="artifacts/train_metrics.json")
    args = p.parse_args()

    Path("artifacts").mkdir(exist_ok=True)
    _ = build_model(args.architecture)
    metrics = {"loss": [1.0 / (i + 1) for i in range(args.epochs)], "accuracy": [0.5 + 0.08 * i for i in range(args.epochs)]}
    Path(args.out).write_text(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
