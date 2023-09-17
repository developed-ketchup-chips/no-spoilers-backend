from dataclasses import dataclass
from typing import List
from pymongo import MongoClient
from pymongo.collection import Collection

client = MongoClient("mongodb+srv://mihiri:mihiri@cluster0.ey8zati.mongodb.net/")

db = client["no-spoilers"]
rooms = db["rooms"]
media_collection = db["media"]

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

    def create_room(cls, media_title, membership_list):
    # Find a document in the collection that matches the given media title
        media_document = media_collection.find_one({"title": media_title})

        # Check if a document was found
        if media_document:
            # Convert the MongoDB document to a Python dictionary
            media_info = {
                "title": media_document["title"],
                "episode_count": media_document["episode_count"],
                "media_type" : media_document["media_type"]
            }

            # Create an instance of Room using the media_info
            room = cls(media_info, members=membership_list)
            rooms.insert_one(room.__dict__)

            return media_info
        else:
            return None

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