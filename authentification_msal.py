import streamlit as st
from msal_streamlit_authentication import msal_authentication


login_token = msal_authentication(
    auth={
        "clientId": "032f9021-9dad-49df-8c4a-748426176605",
        "authority": "https://login.microsoftonline.com/032f9021-9dad-49df-8c4a-748426176605",
        "redirectUri": "/",
        "postLogoutRedirectUri": "/"
    }, # Corresponds to the 'auth' configuration for an MSAL Instance
    cache={
        "cacheLocation": "sessionStorage",
        "storeAuthStateInCookie": False
    }, # Corresponds to the 'cache' configuration for an MSAL Instance
    login_request={
        "scopes": ["032f9021-9dad-49df-8c4a-748426176605/.default"]
    }, # Optional
    logout_request={}, # Optional
    login_button_text="Login", # Optional, defaults to "Login"
    logout_button_text="Logout", # Optional, defaults to "Logout"
    key=1 # Optional if only a single instance is needed
)
st.write("Recevied login token:", login_token)