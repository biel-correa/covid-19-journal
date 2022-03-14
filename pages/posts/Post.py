from nanoid import generate

class Post:
    def __init__(self, title, content, isHot):
        self.id = generate()
        self.title = title
        self.content = content
        self.isHot = isHot