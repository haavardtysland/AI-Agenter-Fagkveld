from datetime import datetime


def get_system_prompt():
    """Get system prompt with current date context for OpenAI Agents SDK"""
    current_date = datetime.now().strftime("%A %d. %B %Y")
    current_iso = datetime.now().strftime("%Y-%m-%d")
    
    return f"""Du er en norsk agent. I dag er {current_date} ({current_iso}).
    
    Svar på alle spørsmål brukeren har"""