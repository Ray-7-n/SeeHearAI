import streamlit as st

from vision import analyze_image
from speech import speak


st.set_page_config(
    page_title="SeeHear AI",
    page_icon="👁️"
)

st.title("👁️ SeeHear AI")
st.subheader("AI Accessibility Assistant")

st.write(
    "Take a picture and let AI describe what is visible."
)

image = st.camera_input("📷 Take a picture")


if image is not None:

    st.image(
        image,
        caption="Captured Image",
        use_container_width=True
    )

    if st.button("🔍 Analyze Image"):

        with st.spinner("AI is analyzing the image..."):

            description = analyze_image(image)

        st.subheader("👁️ What I See")

        st.write(description)

        if st.button("🔊 Read Aloud"):

            speak(description)
