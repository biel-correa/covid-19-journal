from nanoid import generate

from pages.comments.Comment import Comment

class Post:
    def __init__(self, title, content, isHot, state, imageUrl=None, likes=0, dislikes=0, comments=[]):
        self.id = generate()
        self.title = title
        self.content = content
        self.isHot = isHot
        self.state = state
        self.imageUrl = imageUrl
        self.likes = likes
        self.dislikes = dislikes
        self.comments = comments

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
    
    @classmethod
    def commentPost(self, post_id, data):
        for item in posts:
            if item.id == post_id:
                item.comments.append(data)
                return item
        return None
    
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
        Post('Second post', 'This is the second post', True, 'AC', 'https://picsum.photos/400/300', 10, 5, [Comment('John', 'teste@teste.com', 'This is the first comment')]),
        Post('Third post', 'This is the third post', False, 'AL', 'https://picsum.photos/400/300', 10, 5),
]

states = {
    'AC': 'Acre',
    'AL': 'Alagoas',
    'AP': 'Amap??',
    'AM': 'Amazonas',
    'BA': 'Bahia',
    'CE': 'Cear??',
    'DF': 'Distrito Federal',
    'ES': 'Esp??rito Santo',
    'GO': 'Goi??s',
    'MA': 'Maranh??o',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais',
    'PA': 'Par??',
    'PB': 'Para??ba',
    'PR': 'Paran??',
    'PE': 'Pernambuco',
    'PI': 'Piau??',
    'RJ': 'Rio de Janeiro',
    'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul',
    'RO': 'Rond??nia',
    'RR': 'Roraima',
    'SC': 'Santa Catarina',
    'SP': 'S??o Paulo',
    'SE': 'Sergipe',
    'TO': 'Tocantins'
}