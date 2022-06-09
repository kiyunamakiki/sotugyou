from  flask import Flask, render_template
import random

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
    word_list = ["１分でできることもいいね！","ずーっと気になってることやってみる？","１日１つもいいね！","カップラーメンやってる間にやっちゃう？","深呼吸する時間はどう？","朝起きてコップ１杯のの白湯いいらしいよ！","自分を褒めまくるのもいいね"]
    py_word = random.choice(word_list)
    return render_template("word.html",word = py_word)

# add タスク入力   
@app.route('/add')
def add():
    return render_template("add.html")

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
