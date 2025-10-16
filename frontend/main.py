import asyncio
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient
from dotenv import load_dotenv
from config import config
load_dotenv()
async def main():
    # Configure MCP server


    client = MCPClient.from_dict(config)
    llm = ChatOpenAI(model="gpt-5-nano")
    agent = MCPAgent(llm=llm, client=client,max_steps=30 ,system_prompt="You can use multiple MCP servers.")
    user_input = """Plan a weekend trip from San Francisco to Port land, Oregon for next weekend. 
    We want to visit breweries, food trucks, and outdoor markets. Budget is $1500 
    for 2 people. Find flights leaving Friday evening and returning Sunday night."""

 
    print("\n--- Streaming Agent Output ---\n")

    # async for chunk in agent.stream(user_input):
    #     if isinstance(chunk, tuple):
    #         action, message = chunk
    #         print(f"\n[Action] {action}\n")
    #         print(f"[Message] {message}\n")
    #     else:
    #         print(chunk)
    result = await agent.run(user_input , max_steps=30)
    print("\n--- Final Output ---\n")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())