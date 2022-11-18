from flask import Flask
from flask import render_template, request
import requests


api_url = "https://jsonplaceholder.typicode.com/"

app = Flask(__name__)

@app.route("/")
def index():
    template = "index.html"
    return render_template(template)

@app.route("/users", methods=['GET', 'POST'])
def users():
    template = "users.html"
    users = requests.get(api_url + "users").json()

    if request.method == 'POST':
        id_user_delete = request.form.get('id_user_delete')
        url_delete = api_url + "users/" + id_user_delete
        if requests.get(url_delete).status_code == 200:
            requests.delete(url_delete)
            users = requests.get(api_url + "users").json()
            return render_template(template, users=users, message="Usuário apagado com sucesso!", class_alert="alert-success")
        else:
            print("User not found")
            return render_template(template, users=users, message="Erro ao apagar usuário, talvez o usuário não exista! ", class_alert="alert-danger")

    return render_template(template, users=users)

@app.route("/users/<int:user_id>")
def user_details(user_id):
    template = "user_details.html"
    # Get user details
    user = requests.get(api_url + "users/{}".format(user_id)).json()
    # Get user posts
    posts = requests.get(api_url + "posts?userId={}".format(user_id)).json()
    # Get user albums
    albums = requests.get(api_url + "albums?userId={}".format(user_id)).json()
    #Get user todos
    todos = requests.get(api_url + "todos?userId={}".format(user_id)).json()
    return render_template(template, user=user, posts=posts, albums=albums, todos=todos)
    

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    template = "posts.html"
    posts = requests.get(api_url + "posts").json()

    if request.method == 'POST':
        id_posts = request.form.get("id_post_delete")
        url = api_url + "posts/{}".format(id_posts)
        if requests.get(url).status_code == 200:        
            requests.delete(url)
            print(requests.delete(url).status_code)
            return render_template(template, posts=posts, message="Post apagado com sucesso!", class_alert="alert-success")
        else:
            print('Erro ao apagar post!')
            print(requests.delete(url).status_code)
            return render_template(template, posts=posts, message="Erro ao apagar post, talvez o post não exista! ", class_alert="alert-danger")

    return render_template(template, posts=posts)


@app.route("/posts/new", methods=['GET', 'POST'])
def new_post():
    template = "new_post.html"

    if request.method == 'POST':
        title = request.form.get("title")
        body = request.form.get("body")
        user_id = request.form.get("user_id")
        data = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        response = requests.post(api_url + "posts", data=data)
        if response.status_code == 201:
            print(response.status_code)
            return render_template(template, message="Post criado com sucesso!", class_alert="alert-success")
        else:
            print('Erro ao criar post!')
            print(response.status_code)
            return render_template(template, message="Erro ao criar post!", class_alert="alert-danger")

    return render_template(template)

@app.route("/tarefas", methods=['GET', 'POST'])
def todos():
    template = "tarefas.html"
    tarefas = requests.get(api_url + "todos").json()
    return render_template(template, tarefas=tarefas)

@app.route("/tarefas/new", methods=['GET', 'POST'])
def new_tarefa():
    template = "new_tarefa.html"

    if request.method == 'POST':
        title = request.form.get("title")
        completed = request.form.get("description")
        status = request.form.get("status")
        user_id = request.form.get("user_id")
        data = {
            "title": title,
            "completed": completed,
            "status": status,
            "userId": user_id
        }
        response = requests.post(api_url + "todos", data=data)
        if response.status_code == 201:
            print(response.status_code)
            return render_template(template, message="Tarefa criada com sucesso!", class_alert="alert-success")
        else:
            print('Erro ao criar tarefa!')
            print(response.status_code)
            return render_template(template, message="Erro ao criar tarefa!", class_alert="alert-danger")

    return render_template(template)

@app.route("/tarefas/<int:tarefa_id>/delete", methods=['GET', 'POST'])
def delete_tarefa(tarefa_id):
    template = "tarefas.html"
    tarefas = requests.get(api_url + "todos").json()
    url = api_url + "todos/{}".format(tarefa_id)
    if requests.get(url).status_code == 200:
        requests.delete(url)
        print(requests.delete(url).status_code)
        return render_template(template, tarefas=tarefas, message="Tarefa apagada com sucesso!", class_alert="alert-success")
    else:
        print('Erro ao apagar tarefa!')
        print(requests.delete(url).status_code)
        return render_template(template, tarefas=tarefas, message="Erro ao apagar tarefa, talvez a tarefa não exista! ", class_alert="alert-danger")

@app.route("/comments")
def comments():
    template = "comments.html"
    comments = requests.get(api_url + "comments").json()
    return render_template(template, comments=comments)





if __name__ == "__main__":
    app.secret_key = "jsonplaceholder"
    app.run(debug=True)
