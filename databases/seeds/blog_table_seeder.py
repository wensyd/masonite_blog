"""BlogTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Blog import Blog


class BlogTableSeeder(Seeder):
    def run(self):
        Blog.create({"title": "New Post", "body": "this is all new post..."})
        Blog.create({"title": "New Post2", "body": "this is all new post 2..."})
        Blog.create({"title": "New Post3", "body": "this is all new post 3..."})