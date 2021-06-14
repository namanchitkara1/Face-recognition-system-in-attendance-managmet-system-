import streamlit as st
import stream_app
import Developers
import base64

st.set_page_config(layout="wide")


@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_jpg_as_page_bg(jpg_file):
    bin_str = get_base64_of_bin_file(jpg_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/jpg;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)
    return


def set_jpg_as_sidebar_bg(jpg_file):
    bin_str = get_base64_of_bin_file(jpg_file)
    sidebar_bg_img = '''
    <style>
    body {
    background-image: url("data:image/jpg;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str

    st.sidebar.markdown(sidebar_bg_img, unsafe_allow_html=True)
    return


bg_color_sidebar = """
<style>
.sidebar .sidebar-content {
    background-image: linear-gradient(#ffafbd,#ffc3a0);
    color: red;
}
</style>
"""

set_jpg_as_page_bg('Images/BG.jpg')
set_jpg_as_sidebar_bg('Images/sb.jpeg')
st.sidebar.image("Images/Logo.jpg")
st.markdown(bg_color_sidebar, unsafe_allow_html=True)

PAGES = {
    "Home": stream_app,
    "Developers": Developers
}

# if st.sidebar.button("Home"):
#     page = PAGES["Home"]
#     page.app()
#
# if st.sidebar.button("Developers"):
#     page = PAGES["Developers"]
#     page.app()

selection = st.sidebar.radio(" ", list(PAGES.keys()))
page = PAGES[selection]
page.app()
