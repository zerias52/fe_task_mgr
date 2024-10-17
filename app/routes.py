from flask import (
    Flask,
    render_template,
    request as req
)
import requests

BACKEND_URL = "http://127.0.0.1:5000/tasks"

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")


@app.get("/tasks")
def view_tasks():
    response = requests.get(BACKEND_URL)
    if response.status_code == 200:
        task_list = response.json().get("tasks")
        return render_template("list.html", tasks=task_list)
    return (
        render_template("error.html", error=response.status_code),
        response.status_code
    )