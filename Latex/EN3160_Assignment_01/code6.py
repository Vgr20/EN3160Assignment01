threshold_value = 11
_,foreground_mask=cv.threshold(saturation, threshold_value, 255, cv.THRESH_BINARY)
foreground_mask = cv.morphologyEx(foreground_mask, cv.MORPH_CLOSE, cv.getStructuringElement(cv.MORPH_ELLIPSE, (80, 80)))
#masking operation using bitwise_and 
foreground = cv.bitwise_and(img, img,mask=foreground_mask)
# Convert the foreground to grayscale for histogram calculation
foreground_gray = cv.cvtColor(foreground, cv.COLOR_BGR2GRAY)
# Extract the background
gray_image = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
background_image = gray_image - foreground_gray