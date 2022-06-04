from nanoid import generate

class Post:
    def __init__(self, title, content, isHot, state, imageUrl=None, likes=0, dislikes=0):
        self.id = generate()
        self.title = title
        self.content = content
        self.isHot = isHot
        self.state = state
        self.imageUrl = imageUrl
        self.likes = likes
        self.dislikes = dislikes

    @classmethod
    def getAllPosts(cls):
        return posts
    
    @classmethod
    def getAllStates(cls):
        return states
    
    @classmethod
    def getPostById(cls, postId):
        for post in posts:
            if post.id == postId:
                return post
        return None
    
    @classmethod
    def getPostsByState(cls, state):
        postsByState = []
        for post in posts:
            if post.state == state:
                postsByState.append(post)
        return postsByState
    
    @classmethod
    def getHotPosts(cls, state=None):
        if state:
            filteredPosts = Post.getPostsByState(state)
        else:
            filteredPosts = posts
        hotPosts = []
        for post in filteredPosts:
            if post.isHot == True:
                hotPosts.append(post)
        return hotPosts
    
    @classmethod
    def likePost(cls, postId):
        post = Post.getPostById(postId)
        post.likes += 1
        post.editPost(post)
        return post
    
    @classmethod
    def dislikePost(cls, postId):
        post = Post.getPostById(postId)
        post.dislikes += 1
        post.editPost(post)
        return post
    
    def editPost(self, newPost):
        self.title = newPost.title
        self.content = newPost.content
        self.isHot = newPost.isHot
        self.state = newPost.state
        self.imageUrl = newPost.imageUrl
        self.likes = newPost.likes
        self.dislikes = newPost.dislikes

        for item in posts:
            if item.id == self.id:
                item = self
                break
        return self

posts = [
        Post('First post', 'This is the first post', False, 'AC', None, 10, 5),
        Post('Second post', 'This is the second post', True, 'AC', 'https://picsum.photos/400/300', 10, 5),
        Post('Third post', 'This is the third post', False, 'AL', 'https://picsum.photos/400/300', 10, 5),
]

states = {
    'AC': 'Acre',
    'AL': 'Alagoas',
    'AP': 'Amapá',
    'AM': 'Amazonas',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'DF': 'Distrito Federal',
    'ES': 'Espírito Santo',
    'GO': 'Goiás',
    'MA': 'Maranhão',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais',
    'PA': 'Pará',
    'PB': 'Paraíba',
    'PR': 'Paraná',
    'PE': 'Pernambuco',
    'PI': 'Piauí',
    'RJ': 'Rio de Janeiro',
    'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul',
    'RO': 'Rondônia',
    'RR': 'Roraima',
    'SC': 'Santa Catarina',
    'SP': 'São Paulo',
    'SE': 'Sergipe',
    'TO': 'Tocantins'
}