import numpy as np 
import matplotlib.pyplot as plt
import cv2 


img = cv2.imread('image.png')

# img2 = np.where(img < 80, 0, np.where(img < 180, 128, 255)).astype('uint8')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

x = np.arange(gray.shape[0])
y = np.arange(gray.shape[1])

X, Y = np.meshgrid(x, y)
Z = gray


fig = plt.figure(figsize=(12,8))
ax = plt.axes(projection="3d")
# ax.plot_wireframe(X, Y, gray, color='green')
ax.plot_surface(X, Y, Z, cmap="gray")
ax.set_title('surface');
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
