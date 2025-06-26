import cv2

# Read the image
img = cv2.imread("C:\\Users\\DELL\\Downloads\\Black Minimal Motivation Quote LinkedIn Banner.png")

# Add a border to the image (top, bottom, left, right, color in BGR format)
border_color = (0, 255, 0)  # Green border
bordered_img = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=border_color)

# Display the image with the border
cv2.imshow('Image with Border', bordered_img)

# Wait until a key is pressed
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()