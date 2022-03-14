from nanoid import generate

class Post:
    def __init__(self, title, content, isHot, state):
        self.id = generate()
        self.title = title
        self.content = content
        self.isHot = isHot
        self.state = state