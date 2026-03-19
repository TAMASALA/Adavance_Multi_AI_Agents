def detect_intent(text):

    text = text.lower()

    if any(x in text for x in ["code", "python", "script", "program"]):
        return "code"

    if any(x in text for x in ["flight", "ticket", "travel", "goa"]):
        return "flight"

    if any(x in text for x in ["generate", "image", "draw", "picture"]):
        return "image"

    return "info"
