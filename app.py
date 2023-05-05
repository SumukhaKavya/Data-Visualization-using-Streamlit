import streamlit as st

st.title("Innomatics Data App")
st.snow()
 
btn_clik=st.button("Click Me!")

if btn_clik==True:
    st.subheader("You clicked me :cry:")
    st.balloons()
