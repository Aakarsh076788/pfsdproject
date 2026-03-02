from datetime import datetime
from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: str = "user"


class UserOut(BaseModel):
    id: int
    email: EmailStr
    role: str
    created_at: datetime

    class Config:
        from_attributes = True


class DatasetCreate(BaseModel):
    name: str


class ModelTrainRequest(BaseModel):
    name: str
    architecture: str
    dataset_id: int
    learning_rate: float
    batch_size: int
    epochs: int
    optimizer: str
    loss_function: str
    augmentations: list[str] = []


class AssistantCommand(BaseModel):
    text: str


class RobustnessRequest(BaseModel):
    model_run_id: int
    gaussian_noise: float = 0.0
    blur: float = 0.0
    brightness_shift: float = 0.0
    rotation: float = 0.0
    scaling: float = 1.0
    compression_artifacts: float = 0.0
    occlusion_masking: float = 0.0
    adversarial_attack: str = "fgsm"


class ReportRequest(BaseModel):
    model_run_id: int
