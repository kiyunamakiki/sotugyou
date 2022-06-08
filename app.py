from  flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'secret_key'

# --------ここから書く---------
@app.route('/')
def index():
    return '<h1>Hello Team Cookie</h1>'

@app.route('/top')
def template():
    py_name = "cookie"
    return render_template("index.html")

# @app.route("/list")
# def list():
#         py_user_id = session["user_id"]
#         conn = sqlite3.connect("flasktest.db")
#         c = conn.cursor()
#         c.execute("select id, task from tasks WHERE user_id = ?",(py_user_id,))
#         task_list = []
#         for row in c.fetchall():
#             task_list.append({"id":row[0],"task":row[1]})
#         c.close()
#         print(task_list)
#         return render_template("list.html",task_list = task_list )
#     else:
#         return redirect("/login")







# ---------ここまで書く----------

if __name__ == "__main__":
    app.run(debug=True)
