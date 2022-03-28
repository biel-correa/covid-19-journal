from nanoid import generate

class Post:
    def __init__(self, title, content, isHot, state, imageUrl=None):
        self.id = generate()
        self.title = title
        self.content = content
        self.isHot = isHot
        self.state = state
        self.imageUrl = imageUrl