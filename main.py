from flask import Flask
from flask import render_template, request
import requests

api_url = "https://jsonplaceholder.typicode.com/"

app = Flask(__name__)

@app.route("/")
def index():
    template = "index.html"
    return render_template(template)

@app.route("/users")
def users():
    template = "users.html"
    users = requests.get(api_url + "users").json()
    return render_template(template, users=users)

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    template = "posts.html"
    posts = requests.get(api_url + "posts").json()

    id_posts = request.form.get("id_post_delete")

    if delete_post == 200:
        requests.delete(api_url + "posts/" + id_posts).json()
        data = {}
        data["msg"] = "Post foi apagado com sucesso!"
        data['class'] = 'alert-success'
        return render_template(template, posts=posts, data=data)
    else:
        data = {}
        data["msg"] = "Erro ao apagar post!"
        data['class'] = 'alert-danger'
        return render_template(template, posts=posts, data=data)
    
    return render_template(template, posts=posts)

@app.route("/posts/new")
def new_post():
    template = "new_post.html"
    return render_template(template)

@app.route("/albums")
def albums():
    template = "albums.html"
    albums = requests.get(api_url + "albums").json()
    return render_template(template, albums=albums)

@app.route("/photos")
def photos():
    template = "photos.html"
    photos = requests.get(api_url + "photos").json()
    return render_template(template, photos=photos)

@app.route("/todos")
def todos():
    template = "todos.html"
    todos = requests.get(api_url + "todos").json()
    return render_template(template, todos=todos)

@app.route("/comments")
def comments():
    template = "comments.html"
    comments = requests.get(api_url + "comments").json()
    return render_template(template, comments=comments)





if __name__ == "__main__":
    app.secret_key = "jsonplaceholder"
    app.run(debug=True)
