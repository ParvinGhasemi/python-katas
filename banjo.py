"""
DESCRIPTION:
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:
name + " plays banjo" 
name + " does not play banjo"
Names given are always valid strings.
"""

def areYouPlayingBanjo(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError("The Input must be a string.")
    if not name:
        raise ValueError("The name cannot be empty.")

    return f"{name} plays banjo" if name.lower().startswith("r") else f"{name} does not play banjo"