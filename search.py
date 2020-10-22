import re

def check_trigger(text):
    """Checks if the text matches a trigger, and if so, returns the username.

    String -> String
    """
    # List of pattern matches that signify a trigger.
    triggers = [r'/u/(\w+)\s+((is|seems|looks|be|so|too)\s+)?sus\b', r'\bsus\s+/u/(\w+)']
   
    # Go through all triggers and see if one matches.
    for trigger in triggers:
        if result := re.search(trigger, text, re.IGNORECASE):
            return result.group(1)

    return None
