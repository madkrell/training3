from src.database import Database
import uuid
from datetime import datetime, timedelta

class Blog(object):
    def __init__(self, title, description, content, author, date=datetime.utcnow() + timedelta(hours=1), _id=None):
        self.title = title,
        self.description = description,
        self.content = content,
        self.author = author,
        self.date = date,
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_to_mongo(self):
        Database.insert(collection='blogs', data=self.json())

    def json(self):
        return {
            'title': self.title,
            'description': self.description,
            'content': self.content,
            'author': self.author,
            'date': self.date,
            '_id': self._id
        }

    @classmethod
    def get_data(cls):
        blog_data = Database.find(collection='blogs', query={})
        return blog_data

    @classmethod
    def get_by_author(cls, author):
        single_blog = Database.find_one(collection='blogs', query={'author': author})
        return cls(**single_blog)

    @staticmethod
    def list_comp():
        nums = [(x, x**2) for x in range(0, 10, 2) if x >= 0]
        return nums




