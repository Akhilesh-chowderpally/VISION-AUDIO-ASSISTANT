import cv2
import pyttsx3
import time

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Load the MobileNetSSD model (use correct filenames)
net = cv2.dnn.readNetFromCaffe("deploy.prototxt", "mobilenet_iter_73000.caffemodel")

# Define object class labels MobileNetSSD recognizes
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

# Open the webcam
cap = cv2.VideoCapture(0)

# Track last announcement time and last announced object
last_said = time.time()
last_announced_object = ""

print("[INFO] Starting video stream...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]

    # Prepare the image as a blob for the network
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
                                 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    # If 3 seconds have passed since last audio message
    if (time.time() - last_said) > 3:
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:
                idx = int(detections[0, 0, i, 1])
                label = CLASSES[idx]

                if label == "background":
                    continue

                # Get the bounding box coordinates
                box = detections[0, 0, i, 3:7] * [w, h, w, h]
                (startX, startY, endX, endY) = box.astype("int")

                # Draw rectangle and label text
                cv2.rectangle(frame, (startX, startY), (endX, endY),
                              (0, 255, 0), 2)
                y = startY - 15 if startY - 15 > 15 else startY + 15
                cv2.putText(frame, label, (startX, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                # Determine horizontal position: left / center / right
                centerX = (startX + endX) // 2
                if centerX < w / 3:
                    position = "on your left. Move slightly right."
                elif centerX > 2 * w / 3:
                    position = "on your right. Move slightly left."
                else:
                    position = "ahead. Move carefully."

                # Announce only if object is new or after time delay
                if label != last_announced_object:
                    message = f"{label} {position}"
                    print("[INFO]", message)
                    engine.say(message)
                    engine.runAndWait()

                    last_announced_object = label
                    last_said = time.time()
                    break  # Speak one object at a time

    # Display the video frame
    cv2.imshow("Camera Feed", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()


# RUN COMMAND python3 vision_audio_assistant.py

