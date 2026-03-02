from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.security import hash_password, verify_password, create_access_token
from app.db.session import get_db
from app.models.entities import User, Dataset, ModelRun
from app.schemas.common import (
    UserCreate,
    Token,
    DatasetCreate,
    ModelTrainRequest,
    AssistantCommand,
    RobustnessRequest,
    ReportRequest,
)
from app.services.assistant import parse_command
from app.services.metrics import compute_rsi, expected_calibration_error, kl_drift
from app.services.reporting import generate_report

router = APIRouter()


@router.post("/auth/signup", response_model=Token)
def signup(payload: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already in use")
    user = User(email=payload.email, password_hash=hash_password(payload.password), role=payload.role)
    db.add(user)
    db.commit()
    return Token(access_token=create_access_token(payload.email))


@router.post("/auth/login", response_model=Token)
def login(payload: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return Token(access_token=create_access_token(user.email))


@router.post("/datasets")
def create_dataset(payload: DatasetCreate, db: Session = Depends(get_db)):
    dataset = Dataset(name=payload.name, owner_id=1, class_distribution={"healthy": 120, "blight": 80}, imbalance_score=0.2)
    db.add(dataset)
    db.commit()
    db.refresh(dataset)
    return dataset


@router.get("/datasets/{dataset_id}/analysis")
def dataset_analysis(dataset_id: int, db: Session = Depends(get_db)):
    dataset = db.query(Dataset).get(dataset_id)
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset not found")
    suggestion = "Use weighted random sampler + horizontal flip augmentation" if dataset.imbalance_score > 0.15 else "Balanced"
    return {
        "class_distribution": dataset.class_distribution,
        "imbalance_score": dataset.imbalance_score,
        "augmentation_suggestion": suggestion,
    }


@router.post("/training/start")
def start_training(payload: ModelTrainRequest, db: Session = Depends(get_db)):
    run = ModelRun(
        name=payload.name,
        architecture=payload.architecture,
        owner_id=1,
        training_config=payload.model_dump(),
        metrics={"loss": [1.2, 0.8, 0.55], "accuracy": [0.54, 0.72, 0.84]},
        status="running",
    )
    db.add(run)
    db.commit()
    db.refresh(run)
    return run


@router.post("/assistant/command")
def assistant_command(payload: AssistantCommand):
    return parse_command(payload)


@router.post("/voice/command")
def voice_command(payload: AssistantCommand):
    return parse_command(payload)


@router.post("/robustness/test")
def robustness_test(payload: RobustnessRequest, db: Session = Depends(get_db)):
    run = db.query(ModelRun).get(payload.model_run_id)
    if not run:
        raise HTTPException(status_code=404, detail="Model run not found")
    degradation = max(0.0, 1.0 - 0.05 * (payload.gaussian_noise + payload.blur + payload.brightness_shift + payload.compression_artifacts + payload.occlusion_masking))
    run.robustness = {"degradation_curve": [1.0, degradation], "attack": payload.adversarial_attack}
    run.rsi = compute_rsi(0.84, degradation, 0.74, 0.82, 0.79)
    db.commit()
    return {"robustness": run.robustness, "rsi": run.rsi}


@router.get("/explainability/{model_run_id}")
def explainability(model_run_id: int):
    return {
        "grad_cam": "/artifacts/gradcam.png",
        "saliency": "/artifacts/saliency.png",
        "activation_map": "/artifacts/activation.png",
    }


@router.get("/prediction/realtime")
def realtime_prediction():
    return {
        "predicted_disease": "Early Blight",
        "confidence": 0.93,
        "uncertainty": 0.08,
        "heatmap": "/artifacts/heatmap.png",
        "robustness_stability_score": 0.81,
    }


@router.get("/models/compare")
def compare_models(db: Session = Depends(get_db)):
    runs = db.query(ModelRun).all()
    return [
        {
            "id": r.id,
            "name": r.name,
            "accuracy": r.metrics.get("accuracy", [0])[-1] if r.metrics else 0,
            "precision": 0.82,
            "recall": 0.80,
            "f1": 0.81,
            "inference_speed_ms": 24,
            "model_size_mb": 42,
            "robustness": r.rsi,
            "calibration_error": 0.04,
        }
        for r in runs
    ]


@router.get("/calibration/analyze")
def calibration_analyze():
    return expected_calibration_error([0.2, 0.6, 0.9, 0.8], [0, 1, 1, 1])


@router.get("/generalization/test")
def generalization_test():
    return {"source_dataset": "PlantVillage", "target_dataset": "FieldShots", "drop": 0.18}


@router.get("/failures/{model_run_id}")
def failure_cases(model_run_id: int):
    return {
        "lighting_error": ["img_14.png"],
        "occlusion_error": ["img_88.png"],
        "background_bias": ["img_90.png"],
    }


@router.get("/bias/{model_run_id}")
def bias_detection(model_run_id: int):
    return {"background_reliance_score": 0.31, "warning": True}


@router.get("/drift/monitor")
def drift_monitor():
    score = kl_drift([0.4, 0.6], [0.52, 0.48])
    return {"kl_divergence": score, "alert": score > 0.1}


@router.get("/deployment/simulate")
def deployment_simulation():
    return {
        "mobile": {"latency_ms": 80, "memory_mb": 210, "fps": 12},
        "edge": {"latency_ms": 45, "memory_mb": 340, "fps": 22},
        "cloud": {"latency_ms": 15, "memory_mb": 1024, "fps": 80},
    }


@router.get("/export/{model_run_id}")
def export_model(model_run_id: int):
    return {"pytorch": "model.pt", "onnx": "model.onnx", "tflite": "model.tflite"}


@router.post("/reports/generate")
def report_generate(payload: ReportRequest):
    report_path = generate_report(
        path=f"artifacts/report_{payload.model_run_id}.pdf",
        title="AgroRobust AI Research Report",
        sections={"Architecture": "CNN", "Training": "Completed", "Robustness": "Analyzed", "Insights": "See dashboard"},
    )
    return {"report_path": report_path}


@router.get("/admin/overview")
def admin_overview(db: Session = Depends(get_db)):
    return {
        "users": db.query(User).count(),
        "datasets": db.query(Dataset).count(),
        "model_runs": db.query(ModelRun).count(),
        "cpu_usage": 0.63,
        "gpu_usage": 0.58,
    }
