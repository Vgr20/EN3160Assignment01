# Initialize the mask (1s for sure foreground, 0s for sure background)
mask = np.zeros(image.shape[:2], np.uint8)
# Define the rectangular region of interest for initial segmentation
rect = (35, 35, image.shape[1] - 25, image.shape[0] - 25)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
cv.grabCut(image, mask, rect, bgdModel, fgdModel, 5, cv.GC_INIT_WITH_RECT)

# Modify the mask to create a binary foreground mask
foreground_mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
foreground_image = image * foreground_mask[:, :, np.newaxis]
background_image = image * (1 - foreground_mask[:, :, np.newaxis])