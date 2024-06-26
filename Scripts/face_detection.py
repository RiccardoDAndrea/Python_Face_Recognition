# import cv2

# # Load the cascade
# face_cascade = cv2.CascadeClassifier('/Users/riccardo/Desktop/Repositorys_Github/Python_Face_Recognition/Scripts/models/haarcascade_frontalface_default.xml')
# # Read the input image
# img = cv2.imread('/Users/riccardo/Desktop/Repositorys_Github/Python_Face_Recognition/Scripts/data/group_pic_2.jpeg')
# # Convert into grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # Detect faces
# faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# # Draw rectangle around the faces
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# # Display the output
# cv2.imshow('img', img)
# cv2.waitKey()
# cv2.destroyAllWindows()

import cv2

# Load the cascade
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open the video capture device
video_capture = cv2.VideoCapture(0)

# Function to detect faces and draw bounding boxes
def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces

while True:
    # Read the frame
    result, video_frame = video_capture.read()
    if not result:
        break
    
    # Detect faces
    faces = detect_bounding_box(video_frame)
    
    # Display the frame with bounding boxes
    cv2.imshow("My Face Detection Project", video_frame)
    
    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture device and close the windows
video_capture.release()
cv2.destroyAllWindows()
