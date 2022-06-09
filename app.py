from  flask import Flask, render_template ,request
import random
# db接続
import sqlite3

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

# 声かけランダム
@app.route('/word')
def word():
    word_list = ["１分でできることもいいね！","ずーっと気になってることやってみる？","１日１つもいいね！","カップラーメンできる間にやっちゃう？","深呼吸する時間意識してみる？","朝起きてコップ１杯の白湯いいらしいよ！","自分を褒めまくるのもいいね"]
    py_word = random.choice(word_list)
    return render_template("word.html",word = py_word)

# タスク入力
@app.route("/add",methods = ["GET"])
def add():
    return render_template("add.html")

@app.route("/add",methods = ["POST"])
def add_post():
    py_task = request.form.get("task")

    print(py_task)
    # py_user_id = session["user_id"]
    # py_task = request.form.get("task")

    # conn = sqlite3.connect('flasktest.db')
    # c = conn.cursor()
    # c.execute("INSERT INTO tasks (taks,user_id) VALUES(?,?)",(py_task,user_id))
    # conn.commit()
    # conn.close()
    # return redirect("/list")

# edit
@app.route('/edit')
def edit():
    return render_template("edit.html")

# list一覧
@app.route('/list')
def list():
    return render_template("list.html")

# login
@app.route('/login')
def login():
    return render_template("login.html")

# regist
@app.route('/regist')
def regist():
    return render_template("regist.html")

# 以下未使用
# @app.route('/')
# def ():
#     return render_template(".html")

# @app.route('/')
# def ():
#     return render_template(".html")

# @app.route('/')
# def ():
#     return render_template(".html")

# @app.route('/')
# def ():
#     return render_template(".html")

# @app.route('/')
# def ():
#     return render_template(".html")

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
