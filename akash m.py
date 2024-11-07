import cv2
import numpy as np

image = cv2.imread('C:/Users/akash/OneDrive/Documents/akash m.jpg') 
if image is None:
    print("Error: Image not found or unable to open the file.")
    exit()  

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, threshold1=100, threshold2=200)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
min_area = 100  
max_area = 10000 
for contour in contours:
    area = cv2.contourArea(contour)
    if min_area < area < max_area:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, 'Unwanted Object', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
cv2.imshow('Detected Unwanted Objects', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('detected_objects.jpg', image)
print("Output saved as detected_objects.jpg")
