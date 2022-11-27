import cv2
import matplotlib.pyplot as plt

crop_img = cv2.imread("./cropped_img.jpeg")
img_final = crop_img[691:1888,201:1620]

images = [
    "./1.jpeg","./5.jpeg","./3.jpeg","./4.jpeg","./5.jpeg","./6.jpeg","./7.jpeg","./8.jpeg","./9.jpeg","./10.jpeg", 
]
matching = []
for img in images:
    image = cv2.imread(img)
    img_final_test = image[714:2228,341:1420]
    plt.imshow(img_final_test)
    plt.show()
    X = img_final_test - img_final
    ssd = sum(X[:]**2)
    matching.append(ssd)

print(matching)
cv2.imshow("image",img_final)
plt.imshow(img_final)
plt.show()
