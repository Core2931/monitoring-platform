class DuplicateCodeError(Exception):
    def __init__(self, code: str):
        super().__init__(f"hospital code already exists: {code}")
        self.code = code
