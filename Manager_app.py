from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory task list (acts like a temporary database)
tasks = []

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

# Create task
@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        tasks.append(task)
    return redirect(url_for("index"))

# Update task
@app.route("/edit/<int:task_id>", methods=["POST"])
def edit(task_id):
    new_task = request.form.get("task")
    if 0 <= task_id < len(tasks):
        tasks[task_id] = new_task
    return redirect(url_for("index"))

# Delete task
@app.route("/delete/<int:task_id>")
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
