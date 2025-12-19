from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

TASKS = [
    {"title": "Finish OM 3020 homework", "done": False},
    {"title": "Push Flask app to GitHub", "done": True},
]

@app.route("/")
def index():
    total = len(TASKS)
    done = sum(1 for t in TASKS if t["done"])
    return render_template("index.html", total=total, done=done)

@app.route("/tasks", methods=["GET", "POST"])
def tasks():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        if title:
            TASKS.append({"title": title, "done": False})
        return redirect(url_for("tasks"))
    return render_template("tasks.html", tasks=TASKS)

@app.route("/toggle/<int:task_id>")
def toggle(task_id):
    if 0 <= task_id < len(TASKS):
        TASKS[task_id]["done"] = not TASKS[task_id]["done"]
    return redirect(url_for("tasks"))

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)