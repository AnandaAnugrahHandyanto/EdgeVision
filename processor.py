import cv2
import numpy as np

def canny_edge_detection(image: np.ndarray, low_threshold: int = 50, high_threshold: int = 150) -> np.ndarray:
    """Apply Canny edge detection."""
    return cv2.Canny(image, low_threshold, high_threshold)

def sobel_operator(image: np.ndarray, dx: int = 1, dy: int = 1) -> np.ndarray:
    """Apply Sobel operator."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
    sobelx = cv2.Sobel(gray, cv2.CV_64F, dx, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, dy, ksize=3)
    return cv2.magnitude(sobelx, sobely)

def prewitt_operator(image: np.ndarray) -> np.ndarray:
    """Apply Prewitt operator."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
    kernelx = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
    kernely = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    img_prewittx = cv2.filter2D(gray, -1, kernelx)
    img_prewitty = cv2.filter2D(gray, -1, kernely)
    return cv2.addWeighted(img_prewittx, 0.5, img_prewitty, 0.5, 0)

def laplacian_edge_detection(image: np.ndarray) -> np.ndarray:
    """Apply Laplacian edge detection."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
    return cv2.Laplacian(gray, cv2.CV_64F)

def hsv_color_segmentation(image: np.ndarray, lower_bound: np.ndarray, upper_bound: np.ndarray) -> np.ndarray:
    """Apply HSV color segmentation."""
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    return cv2.bitwise_and(image, image, mask=mask)
