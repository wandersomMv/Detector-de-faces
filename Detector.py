import cv2
import sys

# Get user supplied values
#imagePath = sys.argv[1]
cascPath = "haarcascade_frontalface_default.xml"

# IMPORTANDO A IMAGEM



faceCascade = cv2.CascadeClassifier(cascPath)
# Read the image
image = cv2.imread('1 (1).jpg')
gray = image
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5,
    minSize=(30, 30)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
)

print("Encontradas {0}".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (35, 255, 0), 2)

cv2.imshow("Faces encontradas", image)
cv2.waitKey(0)













# USANDO WEBCAN

# import cv2
#
# cap = cv2.VideoCapture(0)
#
# 
# um = 'haarcascade_eye_tree_eyeglasses.xml'
# dois ='haarcascade_frontalface_default.xml'
# faceCascade = cv2.CascadeClassifier(dois)
#
# while(True):
# 	# Capture frame-by-frame
# 	ret, frame = cap.read()
#
# 	# Our operations on the frame come here
# 	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
# 	# Detect faces in the image
# 	faces = faceCascade.detectMultiScale(
# 		gray,
# 		scaleFactor=1.1,
# 		minNeighbors=3,
# 		minSize=(20, 20)
# 		#flags = cv2.CV_HAAR_SCALE_IMAGE
# 	)
#
# 	print(" faces encontradas {0}!".format(len(faces)))
#
# 	# Draw a rectangle around the faces
# 	for (x, y, w, h) in faces:
# 		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
#
#
# 	# Display the resulting frame
# 	cv2.imshow('Webcam', frame)
# 	if cv2.waitKey(1) & 0xFF == ord('q'):
# 		break
#
# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()
