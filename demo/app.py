#!/usr/bin/env python

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request

from time import time

import riak

app = Flask(__name__)

@app.route('/')
def index():

    client = riak.RiakClient()
    bucket = client.bucket('blogs')

    # get a list of keys that point to blog entries
    blogs = bucket.get_keys()

    end_time = int(time())
    start_time = end_time - 60*5

    # use a secondary index to fetch blog posts in the last 5 minutes
    post_links = client.index('posts', 'timestamp_int', start_time, end_time).run()

    posts = [link.get().get_data() for link in post_links]

    return render_template('index.html', blogs=blogs, posts=posts)

@app.route('/blogs/<blog_id>/')
def blogs(blog_id):
    client = riak.RiakClient()

    blogs = client.bucket('blogs')
    blog = blogs.get(blog_id)
    links = blog.get_links()
    # fetch all blog posts via link walking
    posts = [link.get().get_data() for link in links]
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
                'body': body,
                'blog_id': blog_id
              })

            # add timestamp index for post
            post.add_index('timestamp_int', int(time()))

            blogs = client.bucket('blogs')
            blog = blogs.get(blog_id)
            # add a link from blog to post
            blog.add_link(post)
            # add a link from post to blog
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
