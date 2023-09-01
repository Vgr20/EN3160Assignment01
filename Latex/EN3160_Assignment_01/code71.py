# Creating the kernel(2d convolution matrix)
kernel1 = np.array([[1,0,-1],[2,0,-2],[1,0,-1]]) 
# Applying the filter2D() function
img_filtered = cv.filter2D(img,cv.CV_64F,kernel1)