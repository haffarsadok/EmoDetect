# Real-Time Emotion Detection App

This project is a **Real-Time Emotion Detection** application built with Python, OpenCV, and Keras. It captures video from a webcam, detects faces, and classifies emotions in real-time, specifically tracking "happy" expressions for a duration of approximately 3 seconds. When a "happy" face is detected continuously for this threshold, a message is displayed on the video feed.

## Features

- **Face Detection**: Uses OpenCV's Haar Cascade Classifier to detect faces in real-time.
- **Emotion Classification**: Classifies emotions into predefined categories: "Angry," "Disgust," "Fear," "Happy," "Neutral," "Sad," and "Surprise" using a pre-trained model.
- **Consecutive Happy Detection**: Counts consecutive frames with a "happy" expression. If "happy" is detected for ~3 seconds, a message is displayed.
- **Real-Time Video Display**: Continuously displays the video feed, showing emotions and tracking the duration of "happy" detections.
- **Simple Exit Control**: User can end the program by pressing the `q` key.

## Requirements

To run this project, you need the following libraries:

- **Python 3.x**
- **OpenCV**
- **Keras**
- **TensorFlow**
- **NumPy**

Install dependencies with:

```bash
pip install opencv-python keras tensorflow numpy
```

## File Structure

- **`emotion_detection.py`**: Main script for running the emotion detection application.
- **`haarcascade_frontalface_default.xml`**: Haar Cascade Classifier file for face detection.
- **`model.h5`**: Pre-trained model for emotion classification.

## Usage

### Clone the Repository

```bash
git clone https://github.com/haffarsadok/EmoDetect.git
cd emotion-detection-app
```

## Interact with the Application

- The app will open a real-time video feed from your webcam.
- It will display detected emotions for each face.
- If a "happy" face is detected for ~3 seconds, a message "Happy detected for 3 seconds!" will appear on the screen.
- Press the `q` key to exit the application.

## Model Details

The emotion detection model is a convolutional neural network (CNN) trained on facial emotion datasets. It classifies emotions into the following categories:

- Angry
- Disgust
- Fear
- Happy
- Neutral
- Sad
- Surprise

## Customization

To adjust the duration for which a "happy" expression must be detected, modify the `happy_duration_threshold` variable in `emotion_detection.py`.


## Contributing

We welcome contributions! Feel free to open issues or submit pull requests for improvements or additional features.

## License

This project is licensed under the MIT License.

