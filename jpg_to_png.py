import cv2

image = cv2.imread('fix_img.jpg')
# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Threshold the grayscale image to create a binary mask
_, mask = cv2.threshold(gray_image, 230, 255, cv2.THRESH_BINARY)
# Invert the mask
mask = cv2.bitwise_not(mask)
# Convert the image to BGR format (if it's not already in BGR)
if len(image.shape) == 2 or image.shape[2] == 1:
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
# Split the image into RGB channels
b, g, r = cv2.split(image)
# Set the alpha channel to the inverted mask
a = mask.copy()
# Merge the RGB channels with the alpha channel
rgba_image = cv2.merge((b, g, r, a))
# Save the resulting image as PNG with transparency
cv2.imwrite('output_image.png', rgba_image)
# Display the result
cv2.imshow('Result', rgba_image)    
cv2.waitKey(0)
cv2.destroyAllWindows()
