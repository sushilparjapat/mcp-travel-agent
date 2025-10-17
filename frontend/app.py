import streamlit as st
import asyncio
from mcp_use import MCPAgent, MCPClient
from config import config
from system_prompt import SYSTEM_PROMPT
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

# Load environment variables (like OPENAI_API_KEY)
load_dotenv()

# ---------- BASIC CONFIG ----------
MODEL_NAME = "gpt-5-nano"

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="MCP Agent Chatbot", page_icon="🤖", layout="centered")

# ---------- HEADER IMAGE ----------
st.image("/Users/sushil/Desktop/Projects/mcp-travel-agent/frontend/image/MCP Travel Header.gif", width='stretch')
st.markdown(
    """
    <h2 style='text-align:center; color:#1F4E79;'>
        🌍 MCP Travel Agent — Your AI-Powered Travel Companion
    </h2>
    <p style='text-align:center; color:gray;'>
        Ask anything related to flights, hotels, events, weather, and finance for your trips.
    </p>
    """,
    unsafe_allow_html=True
)

# ---------- SESSION STATE ----------
if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

# ---------- DISPLAY PREVIOUS MESSAGES ----------
for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------- CHAT INPUT ----------
user_input = st.chat_input("Type your travel request here...")

# ---------- ASYNC AGENT FUNCTION ----------
async def get_agent_response(user_message: str):
    """Run MCPAgent asynchronously and return the final result."""
    client = MCPClient.from_dict(config)
    llm = init_chat_model(MODEL_NAME, model_provider="openai")

    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=30,
        system_prompt=SYSTEM_PROMPT,
    )

    result = await agent.run(user_message, max_steps=30)
    return result

# ---------- MAIN CHAT LOGIC ----------
if user_input:
    # Show user message
    st.session_state["message_history"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Show assistant placeholder
    with st.chat_message("assistant"):
        with st.spinner("🤔 Thinking..."):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            result = loop.run_until_complete(get_agent_response(user_input))

        st.markdown(result)
        st.session_state["message_history"].append({"role": "assistant", "content": result})
