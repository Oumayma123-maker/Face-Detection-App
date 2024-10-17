# import libraries
 import cv2
 import streamlit as st
 import numpy as np
 from PIL import Image

# # Load the Haar Cascade file for face detection
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
 
# # Function to detect faces in the image
def detect_faces(img):
   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert image to grayscale
   faces = face_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
# 
# 
   for (x, y, w, h) in faces:
      cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw rectangle around detected face
   return img, len(faces)
# 
# 
# # Set a colorful background using HTML and CSS
page_bg_img = '''
 <style>
 body {
     background-color: #f0f8ff;
    background-image: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
     color: #ffffff;
 }
h1 {
     font-family: 'Courier New', Courier, monospace;
     color: #ff6347;  /* Change title color to a more vibrant shade */
     font-size: 3em;  /* Make the title larger */
     text-align: center;  /* Center the title */
    text-shadow: 2px 2px 4px #000000;  /* Add a slight shadow for emphasis */
 }
 </style>
 '''
 
 
# # Display the background
st.markdown(page_bg_img, unsafe_allow_html=True)
# 
# 
# # Title and emojis with more color!
st.markdown("<h1>🎉 Face Detection App 😊💻</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #4682B4;'>👤 Upload an image or use the webcam to detect faces! 📸😎</p>", unsafe_allow_html=True)
# 
# 
# # Option to upload an image file
uploaded_file = st.file_uploader("Choose an image... (jpg, png, jpeg)", type=["jpg", "png", "jpeg"])
# 
# 
if uploaded_file is not None:
# # Convert the uploaded file to an OpenCV image
     image = np.array(Image.open(uploaded_file))
     result_img, faces_detected = detect_faces(image)
# 
# 
# # Display the result with faces detected
      st.image(result_img, caption=f"✨ Processed Image with {faces_detected} face(s) detected! 😀🤖", use_column_width=True)
# 
# 
# # Initialize session state to manage webcam activation
 if 'webcam_active' not in st.session_state:
     st.session_state.webcam_active = False
 if 'picture_taken' not in st.session_state:
     st.session_state.picture_taken = False
# 
# 
# # Button to activate the webcam
 if st.button("🎥 Use Webcam") or st.session_state.webcam_active:
    st.session_state.webcam_active = True
    st.markdown("<h3 style='color: #ff6347;'>🎦Starting webcam... Smile! 😊📷</h3>", unsafe_allow_html=True)
# 
# 
# # Use the camera input to capture image
     camera_image = st.camera_input("Take a picture!")
# 
# 
     if camera_image is not None:
         st.session_state.picture_taken = True
         st.session_state.webcam_active = False  # Deactivate webcam after picture is taken
 
# 
# # Convert the captured image to a format suitable for OpenCV (BGR)
         image = Image.open(camera_image)
         image = np.array(image)  # Convert PIL image to NumPy array (RGB format)
# 
# 
#         # Convert the image from RGB to BGR for OpenCV
         image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
# 
# 
# # Detect faces and draw rectangles
         result_img, faces_detected = detect_faces(image_bgr)
# 
# 
# # Convert BGR (OpenCV format) back to RGB to display in Streamlit
         result_img_rgb = cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB)
# 
# 
# # Display the result with faces detected
         st.image(result_img_rgb, caption=f"📷 Detected {faces_detected} face(s)! 😎🎉", use_column_width=True)
# 
# 
#         # Show the "Take Another Picture" button after the picture is taken
         if st.button("📸 Take Another Picture"):
             st.session_state.picture_taken = False
             st.session_state.webcam_active = True  # Reactivate webcam to allow taking another picture
# 
# 
st.markdown("<p style='color: #32cd32;'>✅ Capture your face for detection! 🛑</p>", unsafe_allow_html=True)
# 
# 
# # Footer message
st.markdown("<p style='text-align: center; color: #ff69b4;'>🚀 Created with 💖 and Streamlit! 🎨</p>", unsafe_allow_html=True)
# 
# 
# 
# 
#
