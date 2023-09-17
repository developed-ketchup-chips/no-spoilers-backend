# object that save users information
# ex Profile that has:  Name and Id.
from dataclasses import dataclass

@dataclass
class User:
    email: str
    name: str
    id: str
    token: str
