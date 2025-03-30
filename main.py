from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.serpapi_tools import SerpApiTools
from phi.tools.crawl4ai_tools import Crawl4aiTools
import streamlit as st
import os

# Load API keys from environment
load_dotenv()
serpapi_api_key = os.getenv("SERPAPI_API_KEY")

if not serpapi_api_key:
    st.error("⚠️ SERPAPI API Key is missing! Please check your .env file.")
    st.stop()

# Initialize tools
serpapi_tools = SerpApiTools(api_key=serpapi_api_key)
crawl4ai_tools = Crawl4aiTools()

# News Research Agent
news_researcher = Agent(
    name="news_researcher",
    role="News Research Agent",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[serpapi_tools, crawl4ai_tools],
    show_tool_calls=True,
    markdown=True,
    instruction=[
        "Retrieve the most relevant and recent news articles on the given topic.",
        "Strictly adhere to the given topic without altering or expanding it.",
        "Use SerpAPI or Crawl4AI to fetch only the most recent, reliable articles.",
        "Ensure articles are directly related to the topic and not about unrelated subjects.",
        "Provide results in a structured format for summarization."
    ],
    debug_mode=False
)

# Headline Generator Agent
headline_generator = Agent(
    name="headline_generator",
    role="Headline Generator",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[],
    show_tool_calls=False,
    markdown=True,
    instruction=[
        "Generate at least three different engaging headlines based on the given news content.",
        "Each headline should be concise (8-15 words) and in an active voice.",
        "Provide the headlines in a bullet-point format (• or -).",
        "DO NOT summarize or rewrite the content, only generate relevant headlines."
    ],
    debug_mode=False
)

# Streamlit UI
st.title("📰 AI-Powered News Headline Generator")
topic = st.text_input("Enter a news topic (e.g., 'Recent developments in quantum computing'):", "").strip()

def process_news(topic):
    if not topic:
        st.warning("⚠️ Please enter a valid topic!")
        return None

    with st.spinner("🔍 Searching for relevant news..."):
        news_data = news_researcher.run(topic)
        if not news_data or not news_data.content.strip():
            st.error("❌ No relevant news found. Try a different topic.")
            return None

    with st.spinner("📰 Generating headlines..."):
        news_headlines = headline_generator.run(news_data.content)
        if not news_headlines or not news_headlines.content.strip():
            st.error("❌ Headline generation failed.")
            return None

    return {"headlines": news_headlines.content}

if st.button("Generate News Headline"):
    result = process_news(topic)

    if result:
        st.subheader("📰 Generated Headlines:")
        st.markdown(result["headlines"])
