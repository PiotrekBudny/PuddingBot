class JokeSinglePartResponse:
    def __init__(self, error, category, type, joke, flags, id, safe, lang):
        self.error = error
        self.category = category
        self.type = type
        self.joke = joke
        self.flags = flags
        self.id = id
        self.safe = safe
        self.lang = lang