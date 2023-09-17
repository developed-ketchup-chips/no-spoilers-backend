# Information about the show or book, including episode list

from media_type import MediaType
from user import User

class Comment():
    def __init__(self, user, comment):
        if not comment.strip():  # Check if comment is blank or contains only whitespace
            raise ValueError("Comment cannot be blank.")
        self.user = user
        self.comment = comment
        
class CommentList():
    def __init__(self):
        self.comment_list = []

    def add_comment(self, comment:Comment):
        self.comment_list.append()

    def remove_comment(self, comment:Comment):
        self.comment_list.remove()

class Episode():
    def __init__(self, name, commentList):
        self.name = name,
        self.status = False, #status is automatically false(incomplete)
        self.commentList = commentList

class Media():
    def __init__(self, name, type:MediaType, length, episodeList):
        self.name = name,
        self.type = type,
        self.length = length,
        self.episodeList = episodeList #episode list is a collection of Episode objects