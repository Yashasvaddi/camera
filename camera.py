import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av

# Function to process video frames
def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")  # Convert to a NumPy array (BGR format)
    # Process the frame if needed (e.g., apply filters or draw overlays)
    return av.VideoFrame.from_ndarray(img, format="bgr24")

# Streamlit app layout
st.title("WebRTC Video Stream")
st.write("This is a real-time video stream example using WebRTC.")

# Initialize WebRTC streamer
webrtc_streamer(
    key="example",
    video_frame_callback=video_frame_callback,
    media_stream_constraints={"video": True, "audio": False},
)
