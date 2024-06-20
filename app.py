from src.utils import detect_text

from src.logger import logger

image_path = "data\purpose-final_small.jpg"
logger.info(f"Image path: {image_path}")


if __name__ == '__main__':
    text = detect_text(image_path)
    output=[]
    for line in text:
        output.append(line)
    logger.info(f"OCR text: {''.join(text)}")