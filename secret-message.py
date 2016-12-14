def find_message(text):
    """Find a secret message"""
    return ''.join([c for c in text if c.isupper()])
