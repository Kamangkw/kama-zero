from flask import Flask, render_template, request, redirect, url_for
import todo_core

app = Flask(__name__)

@app.route('/')
def index():
    tasks = todo_core.load_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    if task:
        todo_core.save_task(task)
    return redirect(url_for('index'))

@app.route('/delete/<task_to_delete>', methods=['POST'])
def delete_task(task_to_delete):
    todo_core.delete_task(task_to_delete)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
