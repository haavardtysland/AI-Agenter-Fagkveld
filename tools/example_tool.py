from agents import function_tool


@function_tool
def get_favorite_person() -> str:
    """
    Use this tool when asked who your favorite person is
    """
    return "Håvard"
    