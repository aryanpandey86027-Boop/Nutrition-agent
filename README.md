# 🥗 NutriAI – Your Personal AI Nutrition Coach

An intelligent, AI-powered nutrition assistant built with **Flask** (Python backend) and vanilla HTML/CSS/JS frontend, using the **Groq API** for fast LLM inference.

---

## 🚀 Features

- 🤖 **AI Chat Coach** – Ask anything about nutrition, macros, meal timing, and fitness goals
- 🍽 **Meal Analyzer** – Describe a meal and get an instant nutrition breakdown (calories, protein, carbs, fat, fiber, health score)
- 📅 **Meal Planner** – Generate a full personalized daily meal plan based on your profile
- 👤 **User Profile** – Set age, weight, height, activity level, goal, diet type, and allergies
- 📊 **Dashboard** – View your daily calorie, protein, carbs, fat, and water targets
- 🌙 **Dark / Light Mode** – Full theme toggle
- 💾 **Local Storage** – Chat history and profile saved in browser

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3, Flask |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| AI Model | Groq API (`openai/gpt-oss-20b`) |
| Styling | Custom CSS with CSS variables (dark/light themes) |

---

## 📁 Project Structure

```
NUTRITION-AGENT/
├── app.py              # Flask backend — serves UI & proxies Groq API calls
├── index.html          # Main frontend (single-page app)
├── style.css           # All styles (extracted from HTML)
├── requirements.txt    # Python dependencies
├── env.example         # Environment variable template
└── README.md           # This file
```

---

## ⚙️ Setup & Run

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/nutrition-agent.git
cd nutrition-agent
```

### 2. Create your `.env` file
```bash
cp env.example .env
```
Edit `.env` and add your Groq API key:
```
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=openai/gpt-oss-20b
GROQ_URL=https://api.groq.com/openai/v1/chat/completions
```
Get a free API key at: https://console.groq.com

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
python app.py
```

Open **http://127.0.0.1:5000** in your browser.

---

## 🔐 Security

The Groq API key is stored in `.env` (never committed to Git) and all AI requests are proxied through the Flask backend — the key is **never exposed** to the browser.

---

## 📌 Problem Statement

NutriAI addresses the challenge of accessible, personalized nutrition guidance. Most people lack easy access to dietitians or tools that give real-time, context-aware food advice. NutriAI uses AI to bridge this gap — providing instant, personalized nutrition analysis, meal planning, and coaching for free.

---

## 🏫 Project Info

- **Domain:** AI / Health & Wellness  
- **Tech Event:** IBM AI Agent Hackathon  
- **Team:** NutriAI Team
