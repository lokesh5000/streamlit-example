import streamlit as st
import cv2
from streamlit_webrtc import webrtc_streamer

# Function to capture video frames
def video_frame_callback(frame):
    # Convert BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return frame

# Title for Streamlit app
st.title("Live Webcam Stream")

# Create a WebRTC video stream
webrtc_streamer(key="example", video_frame_callback=video_frame_callback)
