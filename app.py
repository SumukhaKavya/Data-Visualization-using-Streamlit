import streamlit as st

st.title("Innomatics Data App")
st.snow()

# btn_clik = st.btn("Click Me!")
# There is an error in the above statement in creating a button 
btn_clik=st.button("Click Me!")

#if btn_click == True:
    # There is an error in the variable name it should be btn_clik
if btn_clik==True:
    st.subheader("You clicked me :cry:")
    st.balloons()