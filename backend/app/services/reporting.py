from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def generate_report(path: str, title: str, sections: dict[str, str]) -> str:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(path, pagesize=A4)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, title)
    y = 770
    c.setFont("Helvetica", 11)
    for k, v in sections.items():
        c.drawString(50, y, f"{k}: {v}")
        y -= 22
    c.save()
    return path
