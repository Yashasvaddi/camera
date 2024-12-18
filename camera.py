import streamlit as st
import cv2

# Title of the app
st.title("Webcam Stream Example")

# Open the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    st.error("Could not open webcam.")
else:
    # Start the webcam feed
    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to grab frame.")
            break
        
        # Convert the frame from BGR to RGB (OpenCV uses BGR)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Display the frame in the Streamlit app
        st.image(frame_rgb, channels="RGB", use_column_width=True)

    # Release the webcam when done
    cap.release()
