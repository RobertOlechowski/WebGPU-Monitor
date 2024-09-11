class SmiConfig:
    def __init__(self, query, target=None):
        self.query = query
        self.target = target or self.query
