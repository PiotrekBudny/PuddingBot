class JokeTwoPartResponse:
    def __init__(self, error, category, type, setup, delivery, flags, id, safe, lang):
        self.error = error
        self.category = category
        self.type = type
        self.setup = setup
        self.delivery = delivery
        self.flags = flags
        self.id = id
        self.safe = safe
        self.lang = lang