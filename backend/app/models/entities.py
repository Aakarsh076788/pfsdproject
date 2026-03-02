from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, JSON, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.db.session import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, default="user", nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class Dataset(Base):
    __tablename__ = "datasets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    class_distribution = Column(JSON, default={})
    imbalance_score = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)


class ModelRun(Base):
    __tablename__ = "model_runs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    architecture = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    training_config = Column(JSON, default={})
    metrics = Column(JSON, default={})
    robustness = Column(JSON, default={})
    rsi = Column(Float, default=0.0)
    model_path = Column(String, default="")
    status = Column(String, default="queued")
    created_at = Column(DateTime, default=datetime.utcnow)


class PredictionLog(Base):
    __tablename__ = "prediction_logs"
    id = Column(Integer, primary_key=True, index=True)
    model_run_id = Column(Integer, ForeignKey("model_runs.id"))
    image_path = Column(String, nullable=False)
    predicted_label = Column(String, nullable=False)
    confidence = Column(Float, default=0.0)
    uncertainty = Column(Float, default=0.0)
    drift_flag = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True, index=True)
    actor_id = Column(Integer, ForeignKey("users.id"))
    action = Column(String, nullable=False)
    payload = Column(JSON, default={})
    created_at = Column(DateTime, default=datetime.utcnow)
