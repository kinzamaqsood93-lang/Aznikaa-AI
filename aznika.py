import streamlit as st
import streamlit.components.v1 as components
import requests
import time

st.title("Aznikaa AI")

api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("API Key nahi mili! Streamlit Secrets check karein.")
else:
    user_input = st.text_input("Aap ka sawal:")

    if st.button("Bhejein"):
        if user_input:
            # High demand (503) ke waqt fallback models
            models_to_try = ["gemini-3.8-flash", "gemini-2.5-flash", "gemini-1.5-flash"]
            success = False
            
            with st.spinner("AI response generate kar raha hai..."):
                for model in models_to_try:
                    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
                    headers = {"Content-Type": "application/json"}
                    payload = {"contents": [{"parts": [{"text": user_input}]}]}
                    
                    try:
                        response = requests.post(url, json=payload, headers=headers)
                        if response.status_code == 200:
                            data = response.json()
                            answer = data['candidates'][0]['content']['parts'][0]['text']
                            st.write("### AI ka Jawab:")
                            st.write(answer)
                            success = True
                            break
                        elif response.status_code in [503, 429]:
                            # High demand ya rate limit par agli try karein
                            time.sleep(1)
                            continue
                    except Exception:
                        continue
                
                if not success:
                    st.error("Server par abhi traffic zyada hai. Kuch seconds baad dobara try karein!")
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
