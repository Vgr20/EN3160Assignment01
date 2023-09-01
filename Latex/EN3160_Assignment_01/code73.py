# Defining the kernels
kernel1 = np.array([[1], [2], [1]])
kernel2 = np.array([[1, 0, -1]])

# Applying the convolutions
# kernel = kernel1 * kernel2
conv = cv.filter2D(img, cv.CV_64F, kernel1)
conv = cv.filter2D(conv, cv.CV_64F , kernel2)