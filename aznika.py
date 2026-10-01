import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="Aznikaa AI", page_icon="🤖", layout="wide")

# App Header
st.title("🤖 Welcome to Aznikaa AI")
st.caption("Your Free AI Assistant for IT, Education & Entertainment")

# Fetch API Key automatically from Streamlit Secrets
api_key = st.secrets.get("GEMINI_API_KEY")
# Category Selection Sidebar
st.sidebar.title("⚙️ Aznikaa AI Settings")
mode = st.sidebar.radio(
    "Choose Service / Category:",
    [
        "💻 IT & Coding Helper",
        "📚 Education & Notes Tutor",
        "🎭 Entertainment & Fun Chat"
    ]
)

# User Input Box
user_query = st.text_area("Ask Aznikaa AI anything:", height=120)

if st.button("🚀 Ask Aznikaa AI"):
    if not api_key:
        st.error("⚠️ Backend API Key setup nahi hua! Streamlit Secrets mein GEMINI_API_KEY add karein.")
    elif not user_query.strip():
        st.warning("⚠️ Baraye meherbani koi sawal ya prompt enter karein!")
    else:
     with st.spinner("Aznikaa AI is thinking..."):
            try:
                genai.configure(api_key=api_key.strip())
                model = genai.GenerativeModel("gemini-3.8-flash")

                if mode == "💻 IT & Coding Helper":
                    prompt = f"You are Aznikaa AI, an expert IT instructor. Explain concepts clearly, write clean code, or fix bugs for: {user_query}"
                elif mode == "📚 Education & Notes Tutor":
                    prompt = f"You are Aznikaa AI, a patient academic tutor. Provide clear notes, step-by-step summaries, and easy explanations for: {user_query}"
                else:
                    prompt = f"You are Aznikaa AI, a friendly and smart AI assistant. Answer clearly and helpfully to: {user_query}"

                response = model.generate_content(prompt)
                st.success("Aznikaa AI Response:")
                st.write(response.text)

            except Exception as e:
                error_msg = str(e).lower()
                if "429" in error_msg or "quota" in error_msg:
                    st.warning("⏳ AI server busy hai. Baraye meharbani 30 seconds baad dubara message bhejein!")
                else:
                    st.error(f"Error: {e}")

import streamlit.components.v1 as components

# AdMob Banner Integration (Free Method)
admob_html = """
<div style="text-align: center; margin-top: 20px;">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7585166010772057"
            crossorigin="anonymous"></script>
    <!-- Aznikaa Banner -->
    <ins class="adsbygoogle"
         style="display:inline-block;width:320px;height:50px"
         data-ad-client="ca-pub-7585166010772057"
         data-ad-slot="777795"></ins>
    <script>
         (adsbygoogle = window.adsbygoogle || []).push({});
    </script>
</div>
"""

components.html(admob_html, height=70)
