# Real time barcode scanner      
import cv2
import numpy as np
import streamlit as st
from camera_input_live import camera_input_live

"# Barcode Scanner"
"## Try holding a barcode in front of your webcam"

if "found_barcode" not in st.session_state:
    st.session_state.found_barcode = False

if "barcode_image" not in st.session_state:
    st.session_state.barcode_image = None

if not st.session_state["found_barcode"]:
    image = camera_input_live()
else:
    image = st.session_state.barcode_image

if image is not None:
    st.image(image)
    bytes_data = image.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    detector = cv2.barcode.BarcodeDetector()

    data, bbox, straight_barcode = detector.detectAndDecode(cv2_img)

    if data:
        st.session_state["found_barcode"] = True
        st.session_state["barcode_image"] = image
        st.write("# Found barcode")
        st.write(data)
        if st.button("Restart Scanner"):
            st.session_state["found_barcode"] = False
            st.session_state["barcode_image"] = None
            st.rerun()
        
        
