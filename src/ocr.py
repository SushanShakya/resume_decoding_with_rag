from src.utils import Utils
from PIL import Image
import pytesseract


class OCR:
    def __init__(self, docpath=None):
        self.docpath = (
            docpath if docpath is not None else Utils.asset_path("europass_resume.jpg")
        )

    def extract_text(self):
        image = Image.open(self.docpath).convert("RGB")
        text = pytesseract.image_to_string(image)
        return text
