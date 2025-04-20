# 🤖 Meeting Insights AI — Multilingual Meeting Transcript & Insight Generator

**Meeting Insights AI** is a powerful Python tool that converts audio meetings into **structured business summaries**, **action items**, and **decisions** — all powered by **Whisper** and **LLMs** like **LLaMA 3.2 (via Ollama)** or **Azure OpenAI**.

🎯 Ideal for professionals and teams who want instant, intelligent summaries from meeting recordings — in **any language**.

---

**🌐 Key Features**

✅ Multilingual Support using Whisper Large V3  
✅ Extracts:

- Meeting Title, Date, Participants
- Bullet-pointed MoM
- Action Items with deadlines
- Key Decisions & Summary

✅ Works fully offline with LLaMA 3.2 (via Ollama) or with Azure OpenAI  
✅ Lightweight & Fast — runs on CPU, GPU, or Apple Silicon  
✅ Audio format support: `.mp3`, `.wav`, `.m4a`, etc.

---

**📁 Project Structure**

meeting-insights-ai/  
├── main.py → Entrypoint to transcribe & analyze  
├── whisper_transcribe.py → Whisper transcription logic  
├── llm_analysis.py → Insight generation via Ollama or Azure  
├── requirements.txt → Python dependencies  
├── sample_audio/ → Add audio files here  
├── outputs/ → Transcripts + insights stored here  
└── .gitignore

---

**🚀 Getting Started**

1️⃣ Install Dependencies:  
`pip install -r requirements.txt`

2️⃣ Run Ollama (for local inference):  
`ollama run llama3`

3️⃣ Transcribe + Analyze:  
`python main.py sample_audio/meeting.wav --use ollama`  
or  
`python main.py sample_audio/meeting.wav --use azure`

---

**🔐 Environment Variables (for Azure OpenAI)**

AZURE_AI_ENDPOINT=  
AZURE_AI_KEY=  
AZURE_AI_DEPLOYMENT=

(You can also use a `.env` file with python-dotenv)

---

**🧪 Sample Output**

Meeting Summary:

- Discussed Q2 roadmap
- Alice confirmed launch date: May 5
- Team raised concerns on API stability

✅ Decisions:

- Delay frontend update until API v2

📌 Next Actions:

- Bob to finalize sprint plan by Monday

---

**🧠 LLMs Behind the Scenes**

- Whisper Large V3 for multilingual speech-to-text
- LLaMA 3.2 (via Ollama) for local/private insight generation
- Azure OpenAI (GPT-4) for enterprise-grade analysis

---

**✨ Use Cases**

- Corporate meeting summaries
- Async standup analysis
- Interview review
- Academic lecture insights
- Podcast show notes

---

**💡 Future Plans**

- Microsoft Teams integration
- Language auto-detection & translation
- PDF/HTML report generation
- Email summary delivery

---

**👨‍💻 Author**

Built with ❤️ by [YourName]  
Connect on LinkedIn: https://www.linkedin.com/in/rahulm28/

---

**🪄 Want to contribute?**

Star ⭐ the repo, fork it, and send a PR!  
Have ideas or feedback? Drop them in the GitHub issues tab!
