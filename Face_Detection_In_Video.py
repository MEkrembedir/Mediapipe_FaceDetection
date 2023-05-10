import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Open the video file.
cap = cv2.VideoCapture('video.mp4')

# Create an output video writer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width, frame_height))

# Process video frames with MediaPipe Face Detection.
with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    while cap.isOpened():
        # Read a frame from the video.
        success, image = cap.read()
        if not success:
            print("Unable to read a frame from the video.")
            break
        
        # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
        results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        
        # Draw face detections of each face.
        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(image, detection)

        # Write the processed frame to the output video.
        out.write(image)
        
        # Display the frame.
        cv2.imshow('MediaPipe Face Detection', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break

# Release the resources.
cap.release()
out.release()
cv2.destroyAllWindows()
