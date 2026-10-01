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
            with st.spinner("Aznikaa AI response generate kar raha hai..."):
                try:
                    # Key ke liye active text-generation models dynamically fetch honge
                    active_models = []
                    for m in genai.list_models():
                        if 'generateContent' in m.supported_generation_methods:
                            active_models.append(m.name)
                    
                    if not active_models:
                        st.error("Aapki API key ke sath koi valid text model active nahi hai. Key check karein!")
                    else:
                        # Pehla working model choose karega
                        success = False
                        last_err = ""
                        
                        for model_name in active_models:
                            # Preferred model resolution
                            try:
                                model = genai.GenerativeModel(model_name)
                                response = model.generate_content(user_input)
                                
                                st.write("### AI ka Jawab:")
                                st.write(response.text)
                                st.caption(f"Active Model: {model_name}")
                                success = True
                                break
                            except Exception as model_err:
                                last_err = str(model_err)
                                continue
                        
                        if not success:
                            st.error(f"Error: {last_err}")
                            st.info("Tip: Agar 429 Rate Limit error ho, toh Google AI Studio se 1 new API Key bana kar Streamlit Secrets mein update karein.")

                except Exception as e:
                    st.error(f"Connection Error: {e}")
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
