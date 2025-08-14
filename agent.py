"""
Minimal Weather Agent Demo - OpenAI Agents SDK Version
=====================================================
Shows the new OpenAI Agents SDK in action with Azure OpenAI.
"""

import asyncio

from agent_trace import get_trace, start_run
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
from openai import AsyncAzureOpenAI, OpenAIError

from config import Config
from prompt import get_system_prompt
from tools import (
    get_activities,
    get_foursquare_categories,
    get_weather,
    search_location,
)

# Setup
Config.validate()

# Disable tracing since we're using Azure OpenAI
set_tracing_disabled(disabled=True)

async def create_agent():
    """Create the agent with Azure OpenAI configuration"""
    try:
        # Create the Async Azure OpenAI client
        client = AsyncAzureOpenAI(
            api_key=Config.AZURE_OPENAI_API_KEY,
            api_version=Config.AZURE_OPENAI_API_VERSION,
            azure_endpoint=Config.AZURE_OPENAI_ENDPOINT
        )

        # Configure the agent with Azure OpenAI
        agent = Agent(
            name="NorskAktivitetsAssistent",
            instructions=get_system_prompt(),
            tools=[search_location, get_weather, get_activities, get_foursquare_categories],
            model=OpenAIChatCompletionsModel(
                model=Config.AZURE_DEPLOYMENT_NAME,
                openai_client=client,
            )
        )
        
        return agent
        
    except OpenAIError as e:
        print(f"❌ OpenAI API-feil: {str(e)}")
        return None
    except Exception as e:
        print(f"❌ Uventet feil oppstod: {str(e)}")
        return None

async def run_agent():
    """Run the weather agent"""
    print("🤖 Norsk Aktivitetsassistent er klar!")
    print("Spør meg om aktiviteter i en by, f.eks: 'Aktiviteter i Oslo kl 17:00?'")
    print("Skriv 'exit' for å avslutte.\n")
    
    agent = await create_agent()
    if not agent:
        print("❌ Kunne ikke opprette agent. Sjekk konfigurasjonen.")
        return

    while True:
        try:
            user_input = input("Du: ").strip()
            
            if user_input.lower() in ['exit', 'quit', 'bye', 'ha det']:
                print("👋 Ha det!")
                break
            
            if not user_input:
                continue
                
            print("\n🤖 Assistent:")
            print(f"📝 BRUKER: '{user_input}'")
            print("🧠 AGENTEN TENKER: Analyserer forespørsel og planlegger verktøybruk...")
            start_run()
            
            # Run the agent with the user's input
            result = await Runner.run(agent, user_input)
            print("💬 ENDELIG SVAR:")
            print(result.final_output)
            # Vis kort spor om ønskelig
            trace = get_trace()
            if trace:
                print("\n🧾 Kort verktøyspor:")
                for i, event in enumerate(trace, start=1):
                    etype = event.get("type")
                    tool = event.get("payload", {}).get("tool")
                    summary = {k: v for k, v in event.get("payload", {}).items() if k != "tool"}
                    print(f"  {i}. {etype} – {tool}: {summary}")
            print()
            
        except KeyboardInterrupt:
            print("\n👋 Ha det!")
            break
        except Exception as e:
            print(f"❌ Feil: {str(e)}")
            print("Prøv igjen eller skriv 'exit' for å avslutte.\n")

def main():
    """Main entry point"""
    asyncio.run(run_agent())

if __name__ == "__main__":
    main()