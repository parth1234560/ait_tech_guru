import streamlit as st
from openai import OpenAI

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
elif "Indian Grandpa" in x:
    system_prompt = "👴 Speak with Indian grandpa vibes: traditional wisdom, desi stories, and life advice."
elif "Indian Grandma" in x:
    system_prompt = "👵 Speak like an Indian nani/daadi with warmth, care, and emotional stories."
elif "Bollywood Baba" in x:
    system_prompt = "🧙‍♂️ Be a dramatic Bollywood Baba giving quirky advice with filmy gyaan."
elif "Exam Guru" in x:
    system_prompt = "🎓 Help with exams, motivation, tips, tricks, and study hacks."
elif "Spiritual Guru" in x:
    system_prompt = "📿 Speak with inner peace, Indian traditions, spiritual calm, and life detachment."
elif "Career Coach" in x:
    system_prompt = "💼 Help with interview preparation, resume advice, job search guidance and confidence."
else:
    system_prompt = "🧠 Default friendly assistant."

# Set up model
gemini_model = OpenAI(
    api_key=key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Function to call LLM
def techguru_llm(my_prompt):
    my_message = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": my_prompt}
    ]
    answer = gemini_model.chat.completions.create(
        model="gemini-2.5-flash",
        messages=my_message
    )
    return answer.choices[0].message.content

# UI: Text area and submit
x_input = st.text_area("💬 Enter your question here")

if st.button("🚀 Submit"):
    ai_response = techguru_llm(x_input)
    with st.container():
        st.markdown(f"""
        <div style="
