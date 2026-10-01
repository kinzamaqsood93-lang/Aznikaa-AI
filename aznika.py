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
            with st.spinner("Aznikaa AI aap ka jawab tayar kar raha hai..."):
                # Working exact Google SDK model paths
                fallback_models = [
                    "models/gemini-2.5-flash",
                    "models/gemini-1.5-flash",
                    "gemini-2.5-flash",
                    "gemini-1.5-flash"
                ]
                
                success = False
                last_error = ""
                
                for model_name in fallback_models:
                    try:
                        model = genai.GenerativeModel(model_name)
                        response = model.generate_content(user_input)
                        
                        st.write("### AI ka Jawab:")
                        st.write(response.text)
                        st.caption(f"Powered by: {model_name}")
                        success = True
                        break
                    except Exception as e:
                        last_error = str(e)
                        continue
                
                if not success:
                    st.error(f"Error: {last_error}")
                    st.info("Tip: Agar Quota Limit 429 aa raha hai, toh Google AI Studio se 1 nayi key bana kar Streamlit Secrets mein update karein!")
        else:
            st.warning("Pehle koi sawal toh likhein!")

# AdMob / AdSense Banner Integration
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
