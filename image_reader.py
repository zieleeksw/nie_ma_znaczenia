import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def read_text_from_image(image_path: str) -> str:
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    processed_image = cv2.medianBlur(gray_image, 5)
    text = pytesseract.image_to_string(processed_image)
    return text


if __name__ == "__main__":
    test_images = [
        "test_image1.jpg",
        "test_image2.jpg",
        "test_image3.jpg",
        "test_image4.jpg",
        "test_image5.jpg"
    ]

    for i, image_path in enumerate(test_images):
        print(f"Rezultat dla obrazu {i + 1}:")
        try:
            result = read_text_from_image(image_path)
            print(result)
        except Exception as e:
            print(f"Błąd odczytu obrazu: {e}")
