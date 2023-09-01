# Sobel kernels
sobel_kernel_x = np.array([[-1, 0, 1],
                          [-2, 0, 2],
                          [-1, 0, 1]])
# Convolution operation
gradient_x = np.zeros_like(img, dtype=float)
for y in range(1, img.shape[0] - 1):
    for x in range(1, img.shape[1] - 1):
        window = img[y-1:y+2, x-1:x+2]
        gradient_x[y, x] = np.sum(window * sobel_kernel_x)

# Compute gradient magnitude
gradient_magnitude = np.abs(gradient_x)
# gradient_magnitude = (gradient_magnitude / np.max(gradient_magnitude)) * 255 
gradient_magnitude = gradient_magnitude.astype(np.uint8)