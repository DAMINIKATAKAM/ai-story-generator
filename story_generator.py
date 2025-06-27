import streamlit as st
import google.generativeai as genai

# Replace this with your valid Gemini API key from makersuite.google.com
genai.configure(api_key="AIzaSyDf6yqorHvp3ETHiboDd65pZTboOtWQbjI")

# Use a supported model (list_models will usually show this as available)
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Streamlit app UI
st.set_page_config(page_title="AI Story Generator", page_icon="📖")
st.title("📖 AI Story Generator")
st.write("Enter a story prompt and let AI write a creative short story!")

# User input
prompt = st.text_area("Enter your story prompt:", height=100)

if st.button("Generate Story") and prompt.strip():
    with st.spinner("Generating your story..."):
        try:
            response = model.generate_content(
                f"Write a short, creative, and engaging story based on the prompt:\n{prompt}"
            )
            st.subheader("📝 Generated Story")
            st.write(response.text)
        except Exception as e:
            st.error(f"❌ Error: {e}")
else:
    st.info("Please enter a prompt above and click the button to generate a story.")

