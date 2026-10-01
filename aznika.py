import streamlit as st
import requests
import time

st.title("Aznikaa AI")

keys_raw = st.secrets.get("GEMINI_API_KEYS", "")
api_keys = [k.strip() for k in keys_raw.split(",") if k.strip()]

if not api_keys and st.secrets.get("GEMINI_API_KEY"):
    api_keys = [st.secrets.get("GEMINI_API_KEY")]

if not api_keys:
    st.error("API Key nahi mili! Streamlit Secrets check karein.")
else:
    user_input = st.text_input("Aap ka sawal:")

    if st.button("Bhejein"):
        if user_input:
            models_to_try = ["gemini-3.8-flash", "gemini-1.5-flash"]
            success = False
            
            with st.spinner("AI response generate kar raha hai..."):
                for key in api_keys:
                    for model in models_to_try:
                        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
                        headers = {"Content-Type": "application/json"}
                        payload = {"contents": [{"parts": [{"text": user_input}]}]}
                        
                        response = requests.post(url, json=payload, headers=headers)
                        
                        if response.status_code == 200:
                            data = response.json()
                            answer = data['candidates'][0]['content']['parts'][0]['text']
                            st.write("### AI ka Jawab:")
                            st.write(answer)
                            success = True
                            break
                        elif response.status_code == 429:
                            # Direct key skip karke agli try karein
                            continue
                            
                    if success:
                        break
                
                if not success:
                    st.warning("⚠️ Daily Free Tier quota limit complete ho gayi hai. Kisi doosre Gmail account se nayi API Key bana kar Secrets mein update karein, ya thodi der baad try karein!")
        else:
            st.warning("Pehle koi sawal toh likhein!")

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
