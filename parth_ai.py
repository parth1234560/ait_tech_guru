import streamlit as st
st.subheader("2.🧠Parth's Generative AI Projects")
x = st.selectbox(
    "🧠 How do you want AI to work for you?",
    [
        "🧑‍🏫 As a Tech Guru (for coding & projects)",
        "❤️ As a Love Guru (relationship tips desi style)",
        "💃 As your Female Partner (sweet, caring, supportive)",
        "🕺 As your Male Partner (funny, protective, filmy)",
        "👨‍🍳 As a Desi Chef (cooking advice like maa ke haath ka khana)",
        "👴 As your Indian Grandpa (old wisdom, life lessons)",
        "👵 As your Indian Grandma (stories, emotional bonding)",
        "🧙‍♂️ As a Bollywood Baba (filmy gyaan + drama)",
        "🎓 As an Exam Guru (study help, tips, motivation)",
        "📿 As a Spiritual Guru (inner peace, Indian traditions)",
        "💼 As your Career Coach (interview prep, resume, job advice)"
        ]
)

st.markdown(f"### ✨ You selected: `{x}`")
key = 'AIzaSyD7ShfsF9OnKXH-ZzOxdiXaTSvI-GWq0IY'
if "Tech Guru" in x:
    system_prompt = "🧑‍💻 Expert in tech, coding, AI, ML. Help with clear answers, debug, and guidance."
elif "Love Guru" in x:
    system_prompt = "❤️ Give desi-style relationship advice with humor and respect."
elif "Female Partner" in x:
    system_prompt = "💃 Respond like a sweet, emotional, and caring girlfriend."
elif "Male Partner" in x:
    system_prompt = "🕺 Respond like a fun, protective boyfriend with filmy style."
elif "Desi Chef" in x:
        system_prompt = "👨‍🍳 Give Indian recipes and cooking advice like maa ke haath ka khana."
else:
    system_prompt = "🧠 Default friendly assistant."
from openai import OpenAI

gemini_model=OpenAI(
        api_key=key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
def techguru_llm(my_prompt):
        my_message=[
            {"role":"system", "content": system_prompt },
            {"role":"user","content":my_prompt}
        ]
        answer=gemini_model.chat.completions.create(model="gemini-2.5-flash",messages=my_message)
        return(answer.choices[0].message.content)
x=st.text_area("💬 Enter your question here")
if st.button("🚀 Submit"):
        ai_response = techguru_llm(x)

        # Display AI response in a styled container
        with st.container():
            st.markdown("""
            <div style="
                    background-color: #1e1e1e;
                    padding: 20px;
                    border-radius: 15px;
                    border: 2px solid #2196F3;
                    box-shadow: 0 0 10px rgba(33, 150, 243, 0.3);
                    color: white;
                    font-size: 16px;
                ">
                    🤖 <b>AI Response:</b><br><br>
                    {}
                </div>
            """.format(ai_response), unsafe_allow_html=True)
else:
    st.warning("Please enter a question before submitting.")