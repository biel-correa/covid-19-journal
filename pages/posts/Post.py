from nanoid import generate

class Post:
    def __init__(self, title, content):
        self.id = generate()
        self.title = title
        self.content = content