import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from msal_streamlit_authentication import msal_authentication

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

login_token = msal_authentication(
    auth={
        "clientId": "aaaaaaa-bbbb-cccc-dddd-eeeeeeeeeee",
        "authority": "https://login.microsoftonline.com/bbbbbbbb-cccc-dddd-eeee-fffffffffff",
        "redirectUri": "/",
        "postLogoutRedirectUri": "/"
    }, # Corresponds to the 'auth' configuration for an MSAL Instance
    cache={
        "cacheLocation": "sessionStorage",
        "storeAuthStateInCookie": False
    }, # Corresponds to the 'cache' configuration for an MSAL Instance
    login_request={
        "scopes": ["aaaaaaa-bbbb-cccc-dddd-eeeeeeeeeee/.default"]
    }, # Optional
    logout_request={}, # Optional
    login_button_text="Login", # Optional, defaults to "Login"
    logout_button_text="Logout", # Optional, defaults to "Logout"
    class_name="css_button_class_selector", # Optional, defaults to None. Corresponds to HTML class.
    html_id="html_id_for_button", # Optional, defaults to None. Corresponds to HTML id.
    key=1 # Optional if only a single instance is needed
)

if login_token is not None:
    st.write("Recevied login token:", login_token)
    st.write("You are now logged in !")
    num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
    num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

    indices = np.linspace(0, 1, num_points)
    theta = 2 * np.pi * num_turns * indices
    radius = indices

    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    df = pd.DataFrame({
        "x": x,
        "y": y,
        "idx": indices,
        "rand": np.random.randn(num_points),
    })

    st.altair_chart(alt.Chart(df, height=700, width=700)
        .mark_point(filled=True)
        .encode(
            x=alt.X("x", axis=None),
            y=alt.Y("y", axis=None),
            color=alt.Color("idx", legend=None, scale=alt.Scale()),
            size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
        ))
