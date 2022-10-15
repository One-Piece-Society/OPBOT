# from PIL import Image
    
# image=Image.open('Anjo.jpg')

# imageBox = image.getbbox()
# cropped = image.crop(imageBox)
# cropped.save('Anjo_cropped.png')


import cv2
image = cv2.imread("Anjo.jpg")

y=0
x=0
h=300
w=510
crop_image = image[x:w, y:h]
cv2.imshow("Cropped", crop_image)
cv2.waitKey(0)

