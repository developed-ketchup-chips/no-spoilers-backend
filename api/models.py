from dataclasses import dataclass
from typing import List


@dataclass
class User:
    email: str
    name: str
    token: str


@dataclass
class RoomMember(User):
    progress: int


# Create an instance of room
@dataclass
class Room:
    name: str
    type: str
    length: int
    members: List[RoomMember]

# Information about the show or book, including episode list

class Comment:
    def __init__(self, user, comment):
        if not comment.strip():  # Check if comment is blank or contains only whitespace
            raise ValueError("Comment cannot be blank.")
        self.user = user
        self.comment = comment


class CommentList:
    def __init__(self):
        self.comment_list = []

    def add_comment(self, comment: Comment):
        self.comment_list.append()

    def remove_comment(self, comment: Comment):
        self.comment_list.remove()


class Episode:
    def __init__(self, name, commentList):
        self.name = (name,)
        self.status = (False,)  # status is automatically false(incomplete)
        self.commentList = commentList


class Media:
    def __init__(self, name, type, length, episodeList):
        self.name = (name,)
        self.type = (type,)
        self.length = (length,)
        self.episodeList = (
            episodeList  # episode list is a collection of Episode objects
        )

# Room: a show or book the user is participating in with multiple other users.
# Call rooms associated with the user to display after the login page.


# Create a membership list for a room
class FriendList(object):
    def __init__(self):
        self.friends = []

    def add_friend(self, friend: User):
        self.friends.append(friend)

    def remove_friend(self, friend: User):
        self.friends.remove(friend)