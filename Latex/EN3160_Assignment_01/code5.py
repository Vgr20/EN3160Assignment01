#Calculate the histogram of the image
hist,bins = np.histogram(img.ravel(),256,[0,256])
# find probabilities for each intensity level
probabilities = hist / np.sum(hist)
# find cumulative sum of pixels
cumsum=np.zeros(256)

for i in range(len(cumsum)):
    cumsum[i] = np.sum(hist[:i])
equalized_cumsum = np.zeros(256)
for x in range(len(equalized_cumsum)):
    equalized_cumsum[x] = (cumsum[x] * 255) / img.size

equalized_cumsum = equalized_cumsum.astype('uint8')
equalized_image = np.zeros(img.shape)
for i in range(len(img)):
    for j in range(len(img[i])):
        equalized_image[i][j] = equalized_cumsum[img[i][j]]
equalized_image = equalized_image.astype('uint8')

array1 = np.arange(256)
array2 = hist
array3 = probabilities
array4 = cumsum
array5 = equalized_cumsum

# Combine arrays into a list of tuples
combined_data = list(zip(array1, array2, array3,array4,array5))
# Define headers for the columns
headers = ['r_k', 'n_k', 'Pr(r_k)','Cumulative n_k','equalized rounded']
# Print the combined data using tabulate
table = tabulate(combined_data, headers=headers, tablefmt='grid')