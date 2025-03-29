---

# 🎤 My Behavioral Voice Bot

A personalized voice-based chatbot that answers behavioral interview questions using real context about my background, projects, and personality traits. Built with **Streamlit**, **OpenAI APIs**, and **audio streaming**, this assistant speaks in **first person** — as *me* — and is capable of giving natural, situation-specific answers based on my professional journey.

---

## 🚀 Live Demo

🌐 [Try the app on Streamlit Cloud](https://mybehavioralvoicebot.streamlit.app/)

---

## 📂 Project Overview

This project was developed as part of an assignment for a job interview. It showcases:

- ✅ **Voice-to-Text Input** using microphone recording
- ✅ **Personalized Context Injection** from a `my_story.json` file (resume-like content)
- ✅ **Behavioral Question Handling** in real-time
- ✅ **Text-to-Speech Output** for smooth audio playback
- ✅ **First-Person Conversational Tone** tailored to my personality and work history

---

## 🧠 How It Works

1. **Audio Recorder**: User speaks into a mic to ask a behavioral question.
2. **Whisper API**: Converts spoken input to text.
3. **OpenAI Chat API**: Generates personalized responses using context from `my_story.json`.
4. **TTS API**: Converts response to speech using OpenAI's `tts-1` model.
5. **Streamlit Interface**: Displays the chat and plays the audio automatically.

---

## 📸 Sample Questions You Can Try

- "Tell me about a time you resolved a conflict with your manager."
- "How do you handle pressure or tight deadlines?"
- "What motivates you to take initiative?"
- "Can you describe your biggest strength?"
- "What was your role at Outlier AI?"

---

## 🛠️ Tech Stack

| Tech/Tool       | Purpose                                |
|-----------------|----------------------------------------|
| `streamlit`     | Web interface                          |
| `openai`        | LLM + Whisper + TTS APIs               |
| `audio-recorder-streamlit` | Mic input from user               |
| `streamlit-float` | Floating UI elements                  |
| `dotenv / st.secrets` | API key management (locally & on cloud) |

---

## 🧪 Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/saimanojbera/My_Behavioral_Voice_Bot.git
cd My_Behavioral_Voice_Bot
```

2. **Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Add your OpenAI API key**

- Create a `.env` file with:
  ```
  OPENAI_API_KEY=your_api_key_here
  ```

*(Or use `st.secrets` if deploying on Streamlit Cloud)*

5. **Run the app**
```bash
streamlit run app.py
```

---

## 📁 Folder Structure

```
├── app.py                # Main Streamlit app
├── utils.py              # Utility functions (TTS, STT, Chat)
├── my_story.json         # Context file with resume-like data
├── requirements.txt      # Python dependencies
```

---

## 📢 About Me

I’m **Saimanoj Bera**, an AI Engineer with a passion for building intelligent, human-centric systems.  
Connect with me:

- 🔗 [LinkedIn](https://www.linkedin.com/in/saimanoj-bera-044831150)
- 🌐 [Portfolio](https://saimanojbera.github.io/)
- 📫 saimanoj2509@gmail.com

---

## 📝 License

This project is for demonstration purposes and not intended for commercial use. Feel free to fork and adapt with your own story!

---