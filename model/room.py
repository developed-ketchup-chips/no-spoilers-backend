# Room: a show or book the user is participating in with multiple other users. 
# Call rooms associated with the user to display after the login page.

from user import User
from media import Media

#Create a membership list for a room
class FriendList(object):
    def __init__(self):
        self.friends = []
    
    def add_friend(self, friend:User):
        self.friends.append(friend)
    
    def remove_friend(self, friend:User):
        self.friends.remove(friend)
    
#Create an instance of room
class Room(object):
    def __init__(self, media:Media, progress, friends:FriendList):
        self.media = media
        self.type = type,
        self.progress = progress, #int
        self.friends = friends



        