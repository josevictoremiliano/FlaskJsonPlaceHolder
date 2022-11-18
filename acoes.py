from flask import request
import requests

api_url = "https://jsonplaceholder.typicode.com/"

class delete_post:
    def __init__(self, id):
        self.id = id

    def delete(self):
        id_posts = request.form.get("id_post_delete")
        url = api_url + "posts/{}".format(id_posts)
        response = requests.delete(url)
        if response.status_code == 200:
            return response.status_code
        else:
            print('Erro ao apagar post!')
        return response.status_code
        