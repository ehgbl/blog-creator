
class Post:
    def __init__(self, title, author, content):
        self.title = title
        self.content = content
        self.author = author

    def json(self):
        pass


#does the test depend only on itself or anything else
def json(self):
    return {'title': self.title, 'author': self.author, 'content': self.content}

