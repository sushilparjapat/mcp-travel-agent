import streamlit as st
import asyncio
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient
from config import config
from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
# Load environment variables (like OPENAI_API_KEY)
load_dotenv()

# ---------- BASIC CONFIG ----------
SYSTEM_PROMPT = "You can use multiple MCP servers."
MODEL_NAME = "gpt-5-nano"

# ---------- SESSION STATE ----------
if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

# ---------- UI ----------
st.set_page_config(page_title="MCP Agent Chatbot", page_icon="🤖")
st.title("🌍 Travel Assistant")

# Display previous chat messages
for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------- CHAT INPUT ----------
user_input = st.chat_input("Type your message here...")

# ---------- ASYNC AGENT FUNCTION ----------
async def get_agent_response(user_message: str):
    """Run MCPAgent asynchronously and return the final result."""
      # Add MCP config if nee
    client = MCPClient.from_dict(config)

    llm = init_chat_model(MODEL_NAME, model_provider="openai")
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=30,
        system_prompt=SYSTEM_PROMPT,
    )
    # Run the agent and get the final output
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
            # Run agent asynchronously
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            result = loop.run_until_complete(get_agent_response(user_input))

        # Display final result once done
        st.markdown(result)


    # Save assistant message
    st.session_state["message_history"].append({"role": "assistant", "content": result})
