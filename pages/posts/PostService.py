from database.database import posts

class PostService:
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
            filteredPosts = PostService.getPostsByState(state)
        else:
            filteredPosts = posts
        hotPosts = []
        for post in filteredPosts:
            if post.isHot == True:
                hotPosts.append(post)
        return hotPosts