from app.schemas.common import AssistantCommand


def parse_command(cmd: AssistantCommand) -> dict:
    text = cmd.text.lower()
    if "start" in text and "train" in text:
        return {"action": "start_training", "args": {}}
    if "stop" in text and "train" in text:
        return {"action": "stop_training", "args": {}}
    if "compare" in text and "model" in text:
        return {"action": "compare_models", "args": {}}
    if "explain" in text and "metric" in text:
        return {"action": "explain_metrics", "args": {}}
    if "hyperparameter" in text or "learning rate" in text:
        return {"action": "suggest_hyperparameters", "args": {"tip": "Try lr=3e-4, cosine schedule"}}
    if "error" in text or "fail" in text:
        return {"action": "diagnose_error", "args": {"tip": "Inspect class imbalance and normalization"}}
    return {"action": "unknown", "args": {"message": "Could not parse command"}}
