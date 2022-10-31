import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import glob
import base64
from PIL import Image
from io import BytesIO
import streamlit_authenticator as stauth # VERSION 0.15 WORKS OTHERWISE CHECK THE SYNTAX FOR THE NEW V
from other_misc import database as db


def show_table():
    HtmlFile = open("pages/tamplates/table.html", 'r+', encoding='utf-8')
    source_code = HtmlFile.read()
    print(source_code)
    components.html(source_code,height=700,width=600,scrolling=True)




def authentication():
    users= db.fetch_all_users()
    usernames =[user["key"]for user in users]
    names = [user["name"]for user in users]
    hashed_passwords = [user["password"] for user in users]

    authenticator = stauth.Authenticate(
        names,
        usernames,
        hashed_passwords,
        "usr_ath",
        "astftlgltsda",
        cookie_expiry_days=30
    )
    name, authenticaton_status, username = authenticator.login("Login", "main")

    if authenticaton_status == False:
        st.error("usr / pass incorect ")

    if authenticaton_status == None:
        st.warning("please enter your username and password")

    if authenticaton_status:
        authenticator.login("LOGOUT","sidebar")
        st.sidebar.title(f"Wellcome {name}")
        st.header(f"Wellcome {name}")
        authenticator.logout("Logout","sidebar")



def get_thumbnail(path: str) -> Image:
    img = Image.open(path)
    img.thumbnail((100, 100))
    return img

def image_to_base64(img_path: str) -> str:
    img = get_thumbnail(img_path)
    with BytesIO() as buffer:
        img.save(buffer, 'png') # or 'jpeg'
        return base64.b64encode(buffer.getvalue()).decode()

def image_formatter(img_path: str) -> str:
    return f'<img src="data:pages/tamplates/assets/to_show_func/png;base64,{image_to_base64(img_path)}">'



@st.cache
def convert_df(input_df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return input_df.to_html(escape=False, formatters=dict(thumbnail=image_formatter),show_dimensions=False)


def streamlit_table_pictures():

    images = glob.glob('pages/tamplates/assets/to_show_func/*.png')
    df = pd.DataFrame({  'thumbnail': images},index=["parameter","parameter","parameter","parameter","parameter","parameter","parameter","parameter"])
    html = convert_df(df)
    st.markdown(
        html,

        unsafe_allow_html=True

    )



def streamlit_table_data():


    data_to_be_represented =  {'20 ':[2,3,4,5,6,7],'40':[2,3,4,5,6,7],'60':[2,3,4,5,6,7],'80':[2,3,4,5,6,7],\
                               '90':[2,3,4,5,6,7],'160':[2,3,4,5,6,7]}
    df = pd.DataFrame(data=data_to_be_represented,index=["parameter","parameter","parameter","parameter","parameter","parameter"])
    st.table(df)




def menus():
    add_selectbox_material = st.sidebar.selectbox('Choose material', (
        'Home', "Maximum permissible exposure (MPE)", "Nominal Ocular Hazard Distance (NOHD)",
        "Nominal Hazard Zone (NHZ)"))
    add_selectbox_operation = st.sidebar.selectbox('Choose operation', (
        'Home', "Maximum permissible exposure (MPE)", "Nominal Ocular Hazard Distance (NOHD)",
        "Nominal Hazard Zone (NHZ)"))





menus()









