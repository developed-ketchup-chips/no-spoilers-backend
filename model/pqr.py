from pymongo import MongoClient
from media_type import MediaType
client = MongoClient("mongodb+srv://mihiri:mihiri@cluster0.ey8zati.mongodb.net/")

# Access the "mydb" database (it will be created if it doesn't exist)
db = client["no-spoilers"]

#Sample Room Content

room_collection = db['rooms']

room1 = {
    "title": "Serial Experiments Lain",
    "episode_count": 12,
    "media_type": "TV Show",
    "user_progress": [
        {"name": "John", "progress": 6},  # User 1 has watched 6 episodes
        {"name": "Jake", "progress": 6},  # User 2 has watched 2 episodes
    ]
}

client.close()

#Sample media content
#add image files to media used for presentation

# media1 = {
#     "title" : "Anne With an E",
#     "episode_count" : 27,
#     "media_type" : "TV Show "
# }

# media2 = {
#     "title" : "Attack on Titan",
#     "episode_count" : 88,
#     "media_type" : "TV Show "
# }

# media3 = {
#     "title" : "1984",
#     "episode_count" : 24,
#     "media_type" : "Book"
# }

# media4 = {
#     "title" : "Harry Potter",
#     "episode_count" : 25,
#     "media_type" : "Book"
# }

# media5 = {
#     "title" : "To Kill a Mockingbird",
#     "episode_count" : 31,
#     "media_type" : "Book"
# }

# media6 = {
#     "title" : "Breaking Bad",
#     "episode_count" : 125,
#     "media_type" : "TV Show"
# }

# media7 = {
#     "title" : "Money Heist",
#     "episode_count" : 41,
#     "media_type" : "TV Show"
# }

# media8 = {
#     "title" : "The Hobbit",
#     "episode_count" : 19,
#     "media_type" : "Book"
# }

# media9 = {
#     "title" : "One Piece",
#     "episode_count" : 1075,
#     "media_type" : "TV Show"
# }

# media_collection.insert_many([media1, media2, media3, media4, media5, media6, media7, media8, media9])



