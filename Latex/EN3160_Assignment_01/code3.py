def apply_gamma_correction(image_lab, gamma):

    global L,L_corrected
    # Split the LAB image into L*, a*, and b* channels
    L, a, b = cv.split(image_lab)

    # Apply gamma correction to the L* channel
    L_corrected = np.power(L / 255.0, gamma) * 255.0

    # Ensure the corrected L* channel is in the appropriate data range
    L_corrected = np.clip(L_corrected, 0, 255).astype('uint8')

    # Merge the corrected L* channel with the original a* and b* channels
    corrected_lab = cv.merge([L_corrected, a, b])

    return corrected_lab

# Convert the image to LAB color space
image_lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# Set the desired gamma value
gamma = 0.7
# Apply gamma correction to the LAB image
corrected_image_lab = apply_gamma_correction(image_lab, gamma)
# Convert the corrected LAB image back to BGR color space
corrected_image_bgr = cv.cvtColor(corrected_image_lab, cv.COLOR_LAB2BGR)