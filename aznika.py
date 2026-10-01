import streamlit as st
import streamlit.components.v1 as components
import requests

st.title("Aznikaa AI")

# Streamlit Secrets se single API key read ho rahi hai
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("API Key nahi mili! Streamlit Secrets check karein.")
else:
    user_input = st.text_input("Aap ka sawal:")

    if st.button("Bhejein"):
        if user_input:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key={api_key}"
            headers = {"Content-Type": "application/json"}
            payload = {"contents": [{"parts": [{"text": user_input}]}]}
            
            with st.spinner("AI response generate kar raha hai..."):
                response = requests.post(url, json=payload, headers=headers)
                
                if response.status_code == 200:
                    data = response.json()
                    answer = data['candidates'][0]['content']['parts'][0]['text']
                    st.write("### AI ka Jawab:")
                    st.write(answer)
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
        else:
            st.warning("Pehle koi sawal toh likhein!")

# AdMob / AdSense Banner Integration
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
