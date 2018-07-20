STRICTNESS_FREE = 0
STRICTNESS_EXPAND = 1
STRICTNESS_SET = 2

class Field:
    def __init__(self, name, strictness=STRICTNESS_EXPAND, color="ffffff", tags=[]):
        self.name = name
        self.strictness = strictness
        self.color = color
        self.tags = tags