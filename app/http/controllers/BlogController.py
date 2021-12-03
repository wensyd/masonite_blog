""" A BlogController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Blog import Blog


class BlogController(Controller):
    """Class Docstring Description
    """

    def __init__(self, request: Request):
        self.request = request

    def show(self):
        id = self.request.param("id")
        return Blog.where("id", id).get()

    def index(self):
        return Blog.all()
        

    def create(self):
        title = self.request.input("title")
        body = self.request.input("body")
        blog = Blog.create({"title": title, "body": body})
        return blog

    def update(self):
        title = self.request.input("title")
        body = self.request.input("body") 
        id = self.request.param("id")
        Blog.where("id", id).update({"title": title, "body": body})
        return Blog.where("id", id).get()

    def destroy(self):
        id = self.request.param("id")
        blog = Blog.where("id", id).get()
        Blog.where("id", id).delete()
        return blog