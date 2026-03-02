# AgroRobust AI

Production-ready full-stack platform for robustness analysis of CNN-based crop disease detection.

## Modules Included
- Landing interface with motion-driven scientific UI
- Authentication + role scaffolding
- Dataset manager (distribution + imbalance suggestions)
- Training lab (ResNet, EfficientNet, MobileNet, DenseNet)
- Conversational & voice command assistant
- Robustness testing (noise, blur, brightness, rotation, scaling, compression, occlusion, FGSM/PGD)
- Explainability center (Grad-CAM, saliency, activation)
- Real-time prediction engine
- Model comparison dashboard
- Calibration analyzer (ECE)
- Uncertainty estimation (MC Dropout helper)
- Cross-dataset generalization endpoint
- Failure case explorer
- Bias detection module
- Drift monitor (KL divergence)
- Deployment simulation lab
- Custom RSI metric
- Export system (PT/ONNX/TFLite placeholders)
- Research report generator endpoint
- Admin panel overview

## Run locally
```bash
cd infra
docker compose up --build
```
Frontend: http://localhost:5173
Backend: http://localhost:8000/docs

## Dev run
```bash
cd backend && pip install -r requirements.txt && uvicorn app.main:app --reload
cd frontend && npm install && npm run dev
```

## Testing
```bash
cd backend && pytest
```
