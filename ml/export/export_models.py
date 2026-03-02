"""Export model to PyTorch, ONNX, and TFLite placeholders."""
from pathlib import Path

def export_all(base='artifacts/model'):
    Path('artifacts').mkdir(exist_ok=True)
    for ext in ('pt','onnx','tflite'):
        Path(f'{base}.{ext}').write_text('placeholder')

if __name__ == '__main__':
    export_all()
