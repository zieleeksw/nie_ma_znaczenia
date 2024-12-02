import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def preprocess_image(image, method: str):
    """Zastosuj wybraną metodę przetwarzania obrazu."""
    if method == "median_blur":
        return cv2.medianBlur(image, 3)
    elif method == "gaussian_threshold":
        blurred = cv2.GaussianBlur(image, (5, 5), 0)
        return cv2.threshold(blurred,
                     0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    elif method == "bilateral_threshold":
        filtered = cv2.bilateralFilter(image, 5, 75, 75)
        return cv2.threshold(filtered,
                     0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    elif method == "adaptive_gaussian":
        blurred = cv2.GaussianBlur(image, (5, 5), 0)
        return cv2.adaptiveThreshold(blurred,
                  255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    elif method == "adaptive_bilateral":
        filtered = cv2.bilateralFilter(image, 9, 75, 75)
        return cv2.adaptiveThreshold(filtered,
                  255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    elif method == "adaptive_median":
        blurred = cv2.medianBlur(image, 3)
        return cv2.adaptiveThreshold(blurred,
                255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    else:
        raise ValueError(f"Nieznana metoda przetwarzania: {method}")


def read_text_from_image(image_path: str, method: str) -> str:
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    processed_image = preprocess_image(gray_image, method)
    text = pytesseract.image_to_string(processed_image)
    return text


if __name__ == "__main__":
    test_images = [
        "test_image1.png",
        "test_image2.png"
    ]

    methods = [
        "median_blur",
        "gaussian_threshold",
        "bilateral_threshold",
        "adaptive_gaussian",
        "adaptive_bilateral",
        "adaptive_median"
    ]

    for image_path in test_images:
        print(f"Rezultaty dla obrazu: {image_path}")
        for method in methods:
            print(f"Metoda: {method}")
            try:
                result = read_text_from_image(image_path, method)
                print(result)
            except Exception as e:
                print(f"Błąd dla metody {method}: {e}")
            print("-" * 30)
