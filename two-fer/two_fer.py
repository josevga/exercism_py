def two_fer(name):
    """Returns string: one for [name/you], one for me."""
    if not name:
        name = "you"
    return f"One for {name}, one for me."
