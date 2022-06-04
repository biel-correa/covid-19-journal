from nanoid import generate

class Comment:
    def __init__(self, name, email, content):
        self.id = generate()
        self.name = name
        self.email = email
        self.content = content
