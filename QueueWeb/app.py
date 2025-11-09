from flask import Flask, render_template, request, redirect
from queue_ds import Queue
import os

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates"),
    static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), "static"),
)

# instantiate queue as an object
queue = Queue()

@app.route("/")
def index():
    return render_template("index.html", queue=queue.get_all(), front=queue.peek())

@app.route("/enqueue", methods=["POST"])
def enqueue():
    value = request.form.get("value")
    if value:
        queue.enqueue(value)
    return redirect("/")

@app.route("/dequeue")
def dequeue():
    queue.dequeue()
    return redirect("/")

@app.route("/clear")
def clear():
    # reset queue object
    global queue
    queue = Queue()
    return redirect("/")

@app.route("/members")
def members():
    return render_template("members.html")

@app.route("/rafael")
def rafael():
    # Puwede kang magpadala ng data sa template
    my_profile = {
        "name": "Rafael L. Pillejera",
        "age": 19,
        "status": "Regular",
        "bio": "hi phoe",
        
    }
    return render_template("rafael.html", rafael=my_profile)


if __name__ == "__main__":
    app.run(debug=True)
