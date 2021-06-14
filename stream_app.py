import streamlit as st
import cv2 as cv
import base64
import Att
import Register
import pandas as pd


def app():
    # @st.cache(allow_output_mutation=True)
    # def get_base64_of_bin_file(bin_file):
    #     with open(bin_file, 'rb') as f:
    #         data = f.read()
    #     return base64.b64encode(data).decode()
    #
    # def set_jpg_as_page_bg(jpg_file):
    #     bin_str = get_base64_of_bin_file(jpg_file)
    #     page_bg_img = '''
    #     <style>
    #     body {
    #     background-image: url("data:image/jpg;base64,%s");
    #     background-size: cover;
    #     }
    #     </style>
    #     ''' % bin_str
    #
    #     st.markdown(page_bg_img, unsafe_allow_html=True)
    #     return

    # def set_jpg_as_sidebar_bg(jpg_file):
    #     bin_str = get_base64_of_bin_file(jpg_file)
    #     sidebar_bg_img = '''
    #     <style>
    #     body {
    #     background-image: url("data:image/jpg;base64,%s");
    #     background-size: cover;
    #     }
    #     </style>
    #     ''' % bin_str
    #
    #     st.sidebar.markdown(sidebar_bg_img, unsafe_allow_html=True)
    #     return

    # set_jpg_as_page_bg('Images/BG.jpg')

    text_markdown = '''
    <p style='text-align: center; font-size: 25px; font-family: serif;'>
    Face Recognition in Attendance Management System
    </p>
    '''

    img = cv.imread("Images/logo3.jpeg")

    st.image(img, channels='BGR')

    # st.markdown(text_markdown, unsafe_allow_html=True)

    c1, c2, c3, c4, c5 = st.beta_columns((1, 1, 1.2, 1, 1))

    if c3.button("Register + Train"):
        Register.run()
    if c3.button("Recognize + Attendance"):
        Att.run()

    def get_table_download_link(df):
        """Generates a link allowing the data in a given panda dataframe to be downloaded
            in:  dataframe
            out: href string
            """
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
        href = f'<a href="data:file/csv;base64,{b64}" download="Attendance.csv">Download csv file</a>'
        return href

    att = c3.button("Display Attendance Sheet")
    if att:
        date = c3.text_input("Date", "13-04-2021")
        sheet_path = 'Attendance/Attendance_' + str(date) + ".csv"
        file = pd.read_csv(sheet_path)
        c3.markdown(get_table_download_link(file), unsafe_allow_html=True)

    # set_jpg_as_sidebar_bg('Images/sb.jpeg')

    # st.sidebar.image("Images/Logo.jpg")

    # Buttons for testing
    # if st.sidebar.button("Contact Us"):
    #     # email = st.sidebar.button("Email")
    #     # no = st.sidebar.button("Phone no.")
    #     # if email:
    #     st.sidebar.write("Email: abc@gmail.com")
    #     # if no:
    #     st.sidebar.write("Phone no: 7009278101")
    # st.sidebar.button("Feedback")
