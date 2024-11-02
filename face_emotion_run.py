import numpy as np
from keras.models import load_model
import cv2
from keras.preprocessing.image import img_to_array
import time

# Load pre-trained model and face classifier
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
classifier = load_model('model.h5')

# Define emotion labels
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

# Initialize variables
consecutive_happy_count = 0
happy_duration_threshold = 90  # Set for ~3 seconds at 30fps

# Start video capture
cap = cv2.VideoCapture(0)

try:
    while True:
        # Read each frame
        ret, frame = cap.read()
        if not ret:
            break  # Exit loop if no frame is captured

        # Convert frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_classifier.detectMultiScale(gray)

        # Flag to indicate if a happy face is detected
        happy_detected = False

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float') / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)

                # Make emotion prediction
                prediction = classifier.predict(roi)[0]
                label = emotion_labels[prediction.argmax()]
                
                # Display the emotion label on the video frame
                label_position = (x, y - 10)
                cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                if label == 'Happy':
                    happy_detected = True
                    break  # Exit loop if happy face is detected

        # Update happy face counter
        if happy_detected:
            consecutive_happy_count += 1
        else:
            consecutive_happy_count = 0

        # Check if "Happy" has been detected for ~3 seconds
        if consecutive_happy_count >= happy_duration_threshold:
            cv2.putText(frame, "Happy detected for 3 seconds!", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            consecutive_happy_count = 0  # Reset the counter after detection

        # Display the counter for consecutive happy detections
        cv2.putText(frame, f"Happy Count: {consecutive_happy_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # Show the frame with detected face and emotion
        cv2.imshow('Emotion Detection', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Optional delay to control the frame rate
        time.sleep(0.1)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Release the video capture and close all windows
    if cap is not None:
        cap.release()
    cv2.destroyAllWindows()
