import cv2
import pytesseract
import numpy as np

# Path to the image
image_path = './line_5.png'

# Load the image using OpenCV
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply some preprocessing
# You can tweak these parameters to get better results
# Resize the image (optional)
# image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# Apply thresholding (if needed)
_, image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)

# Optionally, you can use other preprocessing steps like erosion, dilation, etc.
# For example:
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
image = cv2.morphologyEx(image, cv2.MORPH_CLOSE,kernel)

# Display the preprocessed image (optional)
cv2.imshow("Preprocessed Image", image)
cv2.waitKey(0)

# Use pytesseract to extract text
extracted_text = pytesseract.image_to_string(image, config='--psm 6')0

# Print the extracted text
print("Extracted Text:")
print(extracted_text)