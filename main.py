import cv2
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

img = cv2.imread("screenshot.png")
cv2.waitKey(1000)

cv2.destroyAllWindows() 

# detecting faces
print("running")

faces = face_cascade.detectMultiScale(img, 1.1, 4)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

cv2.imshow("Detect Faces", img)
cv2.waitKey()

