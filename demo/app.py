#!/usr/bin/env python

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request

from datetime import datetime

import riak

app = Flask(__name__)

@app.route('/')
def index():

    client = riak.RiakClient()
    bucket = client.bucket('blogs')

    # get a list of keys that point to blog entries
    blogs = bucket.get_keys()

    posts = [
            {'blog_id': 'philipps_crazy_blog', 'title': 'lala', 'timestamp': 123456},
            {'blog_id': 'felix_crazy_blog', 'title': 'foo', 'timestamp': 123456},
            {'blog_id': 'philipps_cray_blog', 'title': 'bar', 'timestamp': 123456}
            ]

    return render_template('index.html', blogs=blogs, posts=posts)

@app.route('/blogs/<blog_id>/')
def blogs(blog_id):
    client = riak.RiakClient()

    blogs = client.bucket('blogs')
    blog = blogs.get(blog_id)
    links = blog.get_links()
    print links
    posts = [link.get().get_data() for link in links]
    print posts
    blog = {
      'id': blog_id,
      'posts' : posts
    }

    return render_template('blog.html', blog=blog)

@app.route('/users/<username>/')
def users(username):
    return render_template('user.html', username=username)

@app.route('/blogs/<blog_id>/posts/', methods=['POST'])
@app.route('/blogs/<blog_id>/posts/<post_id>/')
def posts(blog_id, post_id=None):

    if request.method == 'POST':
        id = request.form['id']
        body = request.form['body']
        if id!= None and body != None:
            client = riak.RiakClient()

            bucket = client.bucket('posts')
            post = bucket.new(blog_id+"_"+id,
              data={
                'id': id,
                'body': body
              })

            blogs = client.bucket('blogs')
            blog = blogs.get(blog_id)
            blog.add_link(post)

            post.add_link(blog)

            blog.store()
            post.store()
            return redirect("/blogs/"+blog_id)
        else:
            #TODO Fehlermeldung
            return redirect("/blogs/"+blog_id)
    else:
        client = riak.RiakClient()
        posts = client.bucket('posts')
        post = posts.get(blog_id+"_"+post_id)
        return render_template('post.html', post=post.get_data())

if __name__ == '__main__':

    app.debug = True
    app.run()



# classes & models

class Post(object):

    def __init__(self, title, body, blog):
        self.blog = blog
        self.title = title
        self.body = body

class Blog(object):

    def __init__(self, title, author=None):
        self.title = title
        self.author = author

    def getPosts(self):
        pass
