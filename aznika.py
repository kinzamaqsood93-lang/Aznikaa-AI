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
                try:
                    # Preferred models list in priority order
                    preferred_models = [
                        "models/gemini-3.8-flash",
                        "models/gemini-2.5-flash",
                        "models/gemini-2.0-flash",
                        "models/gemini-1.5-flash"
                    ]
                    
                    # Get available models for this key
                    available_models = [
                        m.name for m in genai.list_models() 
                        if 'generateContent' in m.supported_generation_methods
                    ]
                    
                    # Find the first available matching model
                    selected_model = None
                    for model_name in preferred_models:
                        if model_name in available_models:
                            selected_model = model_name
                            break
                    
                    if not selected_model and available_models:
                        selected_model = available_models[0]
                    
                    if selected_model:
                        model = genai.GenerativeModel(selected_model)
                        response = model.generate_content(user_input)
                        
                        st.write("### AI ka Jawab:")
                        st.write(response.text)
                        st.caption(f"Active Model: {selected_model}")
                    else:
                        st.error("Koi working Gemini model nahi mila. Key status check karein.")

                except Exception as e:
                    st.error(f"Error aagaya: {e}")
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
