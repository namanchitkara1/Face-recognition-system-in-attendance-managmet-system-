import streamlit as st
import base64


def app():
    # Function to change the background of the page
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

    set_jpg_as_page_bg('Images/blue bg 1.jpg')
    st.markdown("<h1 style='text-align: center; color: blue;'>Developers</h1>", unsafe_allow_html=True)
    # s2.title('Developers')
    st.markdown("""
        <style>
        .dev-font {
            text-align: center ;
            font-family: sans-serif !important;
            margin-bottom: 35px ;
            font-style: oblique ;
            font-size: x-large ; 
        }
        </style>
        """, unsafe_allow_html=True)
    st.markdown('<p class="dev-font">If debugging is the process of removing software bugs, then programming must be '
                'the process of putting '
                'them in.</p>', unsafe_allow_html=True)
    # st.write('If debugging is the process of removing software bugs, then programming must be the process of putting '
    #          'them in.')
    c1, c2, c3 = st.beta_columns((1, 1, 1))
    c1.image("Images/pp21321.jfif")
    c1.title('Naman Chitkara')
    
    # c1.markdown('<p class="big-font">Naman</p>', unsafe_allow_html=True)
    #c2.image("Images/Eevee7.png")
    # c2.markdown("""
    # <p><a href="https://www.w3schools.com">
    # <img src="img.png" alt="W3Schools.com" width="100" height="132">
    # </a></p>
    # """, unsafe_allow_html=True)
    #c3.image("Images/Psyduck7.png")