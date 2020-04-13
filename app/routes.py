from flask import request
from flask import current_app as app

from app.Users import controllers


@app.route('/user/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
@app.route('/user', methods=['GET', 'POST'])
def create_user(user_id=None):
    """User crud """
    if request.method == "GET" and not user_id:
        return controllers.get_all_user()
    elif request.method == "POST":
        return controllers.add_user(request)
    elif request.method == "GET" and user_id:
        return controllers.get_user(user_id)
    elif request.method == "PUT" and user_id:
        return controllers.edit_user(request, user_id)
    elif request.method == "DELETE" and user_id:
        return controllers.delete_user(user_id)
    else:
        return {"Please check the request URL and Request Type"}


@app.route('/hello', methods=['GET'])
def say_hello():
    return "hello"
