
# Importing the OpenCV library
import cv2
# Reading the image using imread() function
image = cv2.imread(r'introduction_to_opencv.py\image.jpg')

# Extracting the height and width of an image
h, w = image.shape[:2]
# Displaying the height and width
print("Height = {},  Width = {}".format(h, w))
print(image.shape)


# We will calculate the region of interest 
# by slicing the pixels of the image
roi = image[100 : 500, 200 : 700]


# Calculating the ratio
ratio = 800 / w
  
# Creating a tuple containing width and height
dim = (800, int(h * ratio))
  
# Resizing the image
resize_aspect = cv2.resize(image, dim)
print(dir(image))


# Calculating the center of the image
center = (w // 2, h // 2)
  
# Generating a rotation matrix
matrix = cv2.getRotationMatrix2D(center, -45, 1.0) 
  
# Performing the affine transformation
rotated = cv2.warpAffine(image, matrix, (w, h))


cv2.imshow('sdasdas',rotated)


output = image.copy()
  
# Using the rectangle() function to create a rectangle.
rectangle = cv2.rectangle(output, (1500,900),(600,400),(0,0,0),5)

text = cv2.putText(output, 'OpenCV Demo', (600, 380),cv2.FONT_HERSHEY_TRIPLEX, 4, (255, 0, 255), 9)

cv2.imshow('rec',output)
cv2.waitKey(0)