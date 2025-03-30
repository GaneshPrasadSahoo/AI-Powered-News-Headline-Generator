# AI-Powered News Headline Generator

![AI-Powered News Headline Generator](Screenshot%202025-03-30%20125440.png)

## 📌 Overview
The **AI-Powered News Headline Generator** is a Streamlit-based web application that leverages AI agents to retrieve the latest news on a given topic and generate engaging headlines. This tool uses **SerpAPI** and **Crawl4AI** for news extraction and **Groq's deepseek-r1-distill-llama-70b model** for headline generation.

## 🚀 Features
- **Automated News Retrieval**: Fetches the most relevant and recent articles based on the given topic.
- **AI-Generated Headlines**: Produces engaging and concise headlines for the retrieved news.
- **User-Friendly Interface**: Simple Streamlit-based UI for seamless interaction.
- **Structured Output**: Delivers headlines in a clear and readable format.

## 📽️ Demo Video
Watch how the AI-Powered News Headline Generator works:
[Click here to watch the demo](https://github.com/GaneshPrasadSahoo/AI-Powered-News-Headline-Generator/blob/main/Untitled%20video%20-%20Made%20with%20Clipchamp%20(2).mp4)

## 🛠️ Installation
To set up the project on your local machine, follow these steps:

### 1️⃣ Clone the Repository
```bash
 git clone https://github.com/GaneshPrasadSahoo/AI-Powered-News-Headline-Generator.git
 cd AI-Powered-News-Headline-Generator
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
 python -m venv venv
 source venv/bin/activate   # On MacOS/Linux
 venv\Scripts\activate     # On Windows
```

### 3️⃣ Install Dependencies
```bash
 pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file in the project directory and add your API keys:
```env
SERPAPI_API_KEY=your_serpapi_api_key_here
```

### 5️⃣ Run the Application
```bash
 streamlit run app.py
```

## 🏗️ How It Works
1. **Enter a news topic** in the input field (e.g., "Latest advancements in AI").
2. **Click on 'Generate News Headline'**.
3. The **news researcher agent** fetches relevant news articles.
4. The **headline generator agent** creates engaging headlines.
5. The results are displayed in the Streamlit UI.

## 📸 Screenshots
_Provide screenshots here for better visualization._

## 🤝 Contributing
Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.


---
**Developed by [Ganesh Prasad Sahoo](https://github.com/GaneshPrasadSahoo)**

