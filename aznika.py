import streamlit as st
import google.generativeai as genai
import streamlit.components.v1 as components

st.title("Aznikaa AI")

api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("API Key nahi mili! Streamlit Secrets check karein.")
else:
    genai.configure(api_key=api_key)
    
    user_input = st.text_input("Aap ka sawal:")

    if st.button("Bhejein"):
        if user_input:
            with st.spinner("AI response generate kar raha hai..."):
                try:
                    # Official Gemini SDK model configuration
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    response = model.generate_content(user_input)
                    
                    st.write("### AI ka Jawab:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error aagaya: {e}")
        else:
            st.warning("Pehle koi sawal toh likhein!")

# AdMob Banner Integration
admob_html = """
<div style="text-align: center; margin-top: 20px;">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7585166010772057"
     crossorigin="anonymous"></script>
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
