from nanoid import generate

class Post:
    def init(self, title, content):
        self.id = generate()
        self.title = title
        self.content = content