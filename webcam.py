import cv2

def main():
    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)  # 0 represents the default webcam

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return

    # Loop to capture frames from the webcam
    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Check if the frame is successfully captured
        if not ret:
            print("Error: Failed to capture frame")
            break

        # Display the frame
        cv2.imshow('Webcam', frame)

        # Check for 'q' key to quit the program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoCapture object and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
