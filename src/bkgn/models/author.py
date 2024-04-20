class Author:
    def __init__(self, name: str, bio: str):
        self.name = name
        self.bio = bio

    def __str__(self):
        return f"{self.name} - {self.bio}"