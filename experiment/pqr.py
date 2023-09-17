from pymongo import MongoClient

try:
    # Specify the database name in the connection string
    client = MongoClient(
        "mongodb+srv://saphia:saphia@cluster0.ey8zati.mongodb.net/mydb", tls=True
    )

    # Access the "mydb" database (it will be created if it doesn't exist)
    db = client.get_database("users")

    # Insert data into a collection within the "mydb" database
    media_collection = db["media"]

    # Sample media content
    # add image files to media used for presentation

    media1 = {"_id": 1, "title": "Anne With an E", "episode_count": 27}

    media2 = {"_id": 2, "title": "Attack on Titan", "episode_count": 88}

    media3 = {"_id": 3, "title": "1984", "episode_count": 24}

    media4 = {"_id": 4, "title": "Harry Potter", "episode_count": 25}

    media5 = {"_id": 5, "title": "To Kill a Mockingbird", "episode_count": 31}

    media6 = {"_id": 6, "title": "Breaking Bad", "episode_count": 125}

    media7 = {"_id": 7, "title": "Money Heist", "episode_count": 41}

    media8 = {"_id": 8, "title": "The Hobbit", "episode_count": 19}

    media9 = {"_id": 9, "title": "One Piece", "episode_count": 1075}

    media10 = {"_id": 10, "title": "The Lord of the Rings", "episode_count": 40}
    media_documents = [
        media1,
        media2,
        media3,
        media4,
        media5,
        media6,
        media7,
        media8,
        media9,
        media10,
    ]

    media_collection.insert_many(media_documents)
    # user collection sample data
    user_collection = db["users"]
    print("Connected to MongoDB")

except Exception as e:
    print(f"Error connecting to MongoDB: {str(e)}")
