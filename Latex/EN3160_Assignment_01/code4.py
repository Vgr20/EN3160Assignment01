# Convert the image to HSV color space
image_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# Spliting image to HSV planes
hue, saturation, value = cv.split(image_hsv)
# Define the Saturation Transformer
def satIntensityTransformer(x,alpha,zigma):
    
    transformer = x +(alpha*128)*np.exp((-(x-128)**2)/(2*(zigma**2)))

    return min(transformer,255)

# Define the new array after transformation
transformed_saturation= np.zeros(saturation.shape)
# perform transformation
for i in range(len(saturation)):
    for j in range(len(saturation[i])):
        transformed_saturation[i][j] = satIntensityTransformer(saturation[i][j],0.7,70)
# make sure the values are in the range of 0 to 255
transformed_saturation=transformed_saturation.astype('uint8')