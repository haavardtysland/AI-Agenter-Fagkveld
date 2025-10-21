from agents import function_tool
import asyncio
from tools import get_favorite_person
from openai import AzureOpenAI

from config import Config
from prompt import get_system_prompt

# Setup
Config.validate()

tools = [
    {
        "type": "function",
        "function": {
            "name": get_favorite_person.__name__,
            "description": get_favorite_person.__doc__ or "",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    }
]
print("Available tools:", tools)
thinking_prompt = f"""Think hard about the next steps you need to take. """

deployment = "gpt-5-mini"

api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=Config.AZURE_OPENAI_ENDPOINT,
    api_key=Config.AZURE_OPENAI_API_KEY,
)
messages=[
    {
        "role": "system",
        "content": thinking_prompt,
    }
    ]

def call_llm(message: str):
    messages.append(
            {
                "role": "user",
                "content": message,
            }
        )
    response = client.chat.completions.create(
            messages=messages,
        max_completion_tokens=16384,
        temperature=1.0,
        top_p=1.0,
        model=deployment,
        tools=tools,
    )
    print("FULL RESP:", response)
    print("LLM RESP:", response.choices[0].message.content)

    return response

def process_tool_calls(tool_calls):
    results = []
    for tool_call_list in tool_calls:
        if tool_call_list:
            for tool_call in tool_call_list:
                function_name = tool_call.function.name
                # Call the function dynamically by name
                results.append(globals()[function_name]())
                print(f"\033[91mTool result: {results}\033[0m")
    return results

while True:
    response = call_llm("Hvem er din favorittperson?")
    tool_calls = [choice.message.tool_calls for choice in response.choices if hasattr(choice.message, 'tool_calls')]
    tool_results = process_tool_calls(tool_calls)

    messages.append({
            "role": "assistant",
            "content": response.choices[0].message.content,
            "tool_calls": response.choices[0].message.tool_calls
        })
        # Add tool results
    if response.choices[0].message.tool_calls:
        for tool_call, result in zip(response.choices[0].message.tool_calls, tool_results):
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
        
            })

    call_llm(f"Verktøyresultater: {tool_results}")
