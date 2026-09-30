import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="Aznikaa AI", page_icon="🤖", layout="wide")

# App Header
st.title("🤖 Welcome to Aznikaa AI")
st.caption("Your Free AI Assistant for IT, Education & Entertainment")

# Fetch API Key from Streamlit Secrets or Sidebar
api_key = st.secrets.get("GEMINI_API_KEY", "")

# Sidebar Configuration
st.sidebar.title("⚙️ Aznikaa AI Settings")

if not api_key:
    api_key = st.sidebar.text_input("Enter your Free API Key:", type="password")

# Category Selection
mode = st.sidebar.radio(
    "Choose Service / Category:",
    [
        "💻 IT & Coding Helper",
        "📚 Education & Notes Tutor",
        "🎭 Entertainment & Fun Chat"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Aznikaa AI is 100% Free to use!")

# User Input Section
user_query = st.text_area("Ask Aznikaa AI anything:", height=150, placeholder="Type your code, question, or topic here...")

if st.button("🚀 Ask Aznikaa AI"):
    if not api_key:
        st.error("⚠️ Baraye meherbani pehle Sidebar mein apni API Key daalein aur Enter press karein!")
    elif not user_query.strip():
        st.warning("⚠️ Baraye meherbani koi sawal ya prompt enter karein!")
    else:
        with st.spinner("Aznikaa AI is thinking..."):
            try:
                # Configure Gemini API
                genai.configure(api_key=api_key.strip())
                
                # Model Setup
                model = genai.GenerativeModel('gemini-1.5-flash-latest')
                
                # Custom System Prompts
                if mode == "💻 IT & Coding Helper":
                    prompt = f"You are Aznikaa AI, an expert IT instructor. Explain concepts clearly, write clean code, or fix bugs for: {user_query}"
                elif mode == "📚 Education & Notes Tutor":
                    prompt = f"You are Aznikaa AI, a patient academic tutor. Provide clear notes, step-by-step summaries, and easy explanations for: {user_query}"
                else:
                    prompt = f"You are Aznikaa AI, a fun, friendly, and witty companion. Provide funny stories, jokes, or creative chat for: {user_query}"

                # Fetch AI response
                response = model.generate_content(prompt)
                
                # Display output
                st.success("Aznikaa AI Response:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
