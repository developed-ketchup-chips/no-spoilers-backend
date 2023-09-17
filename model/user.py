# object that save users information
# ex Profile that has:  Name and Id.
@dataclass
class User:
    email: str
    name: str
    id: str
    token: str
