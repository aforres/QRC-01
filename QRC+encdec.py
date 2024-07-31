# Core Pkgs
import streamlit as st 
import numpy as np
import os 
import time 
timestr = time.strftime("%Y%m%d-%H%M%S")
#import cv2


# For QR Code
import qrcode

qr = qrcode.QRCode(
    version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

from PIL import Image
# Function to Load Image
def load_image(img):
    im = Image.open(img)
    return im

st.title("Sagebrush Data Integrity")
st.write("draft example software only")
#st.header("Secure QRC+ technology")

# Application
def main():
    menu = ["Encode with QRC+","Decode with QRC+","About This Software"]

    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Encode with QRC+":
        st.subheader("Encode with QRC+")
        # Text input
        with st.form(key='myqr_form'):
            raw_text = st.text_area("Text Here")
            submit_button = st.form_submit_button("Generate QR code")

        # Layout
        if submit_button:

            col1,col2 = st.columns(2)

            with col1:
                # Add Data
                qr.add_data(raw_text)
                # Generate
                qr.make(fit=True)
                img = qr.make_image(fill_color='black',back_color='white')

                # Filename
                img_filename = 'QRC+_image_{}.png'.format(timestr)
                path_for_images = os.path.join('QRC01/image_folder/',img_filename)
                img.save(path_for_images)

                final_img = load_image(path_for_images)
                st.image(final_img)


            with col2:
                st.info("Original Text")
                st.write(raw_text)



    elif choice == "Decode with QRC+":
        st.subheader("Decode with QRC+")

        image_file = st.file_uploader("Upload Image",type=['jpg','png','jpeg'])

        if image_file is not None:
            # Method 1 : Display Image
            # img = load_image(image_file)
            # st.image(img)

            # Method 2: Using opencv * helps in decoding
            file_bytes = np.asarray(bytearray(image_file.read()),dtype=np.uint8)
            opencv_image = cv2.imdecode(file_bytes,1)

            c1,c2 = st.columns(2)
            with c1:

                st.image(opencv_image)

            with c2:
                st.info("Decoded QR code")
                det = cv2.QRCodeDetector()
                retval,points,straight_qrcode = det.detectAndDecode(opencv_image)

                # Retval is for the text
                st.write(retval)
                #st.write(points)
                #st.write(straight_qrcode)

    else:
        st.subheader("About this software")
        st.write("acknowledgements and attributions")




if __name__ == '__main__':
    main()
