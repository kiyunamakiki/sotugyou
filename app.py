from  flask import Flask ,render_template ,request ,redirect, session
import random
# db接続
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret_key'

# --------ここから書く---------
@app.route('/')
def index():
    return '<h1>Hello Team Cookie</h1>'

@app.route('/greet/<name>')
def greet(name):
    return name + 'さん、こんにちは！' 

@app.route('/template')
def template():
    py_name = "SUNABACO"
    return render_template("index.html",name = py_name)

# login
@app.route('/add',methods = ["GET"])
def add():
    if "user_id" in session:
        return render_template("add.html")
    else:
        return redirect("/login")

@app.route('/add',methods = ["POST"])
def add_post():
    py_user_id = session["user_id"]
    py_task = request.form.get("task")
    conn = sqlite3.connect('cookie.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (task,user_id) VALUES(?,?)",(py_task,py_user_id))
    conn.commit()
    conn.close()
    return redirect("/list")

# タスクをｄｂについか
@app.route("/regist")
def regist():
    return render_template("regist.html")


@app.route("/regist",methods = ["POST"])
def regist_post():
    py_name = request.form.get("member_name")
    py_password = request.form.get("member_password")
    conn = sqlite3.connect('cookie.db')
    c = conn.cursor()
    c.execute("INSERT INTO members VALUES(null,?,?)",(py_name,py_password))
    conn.commit()
    conn.close()
    return "登録しました"   

# タスクリスト表示
@app.route("/list")
def list():
    if "user_id" in session:
        # DB接続
        py_user_id = session["user_id"]
        conn = sqlite3.connect("cookie.db")
        # DBを操作できるようにする
        c = conn.cursor()
        # 実行したいSQL文を書く
        c.execute("select id, task from tasks WHERE user_id = ?",(py_user_id,))
        # タスクリストを入れる配列を定義
        task_list = []
        for row in c.fetchall():
            task_list.append({"id":row[0],"task":row[1]})
        # DB接続終了
        c.close()
        print(task_list)
        return render_template("list.html",task_list = task_list)

    else:
        return redirect("/login")

# 編集機能
@app.route("/edit/<int:id>")
def edit(id):
    if "user_id" in session:
        conn = sqlite3.connect("flasktest.db")
        c = conn.cursor()
        c.execute("SELECT task FROM tasks WHERE id = ?;",(id,))
        task = c.fetchone()
        c.close()
        print(task)

        if task == None:
            return redirect("/list")
        else:
            return render_template("edit.html",task_id = id,task = task)
    else:
        return redirect("/login")

@app.route("/edit",methods = ["POST"])
def edit_post():
    # 入力フォームからデータを受け取る
    py_task = request.form.get("task")
    py_id = request.form.get("task_id")
    # DB接続
    conn = sqlite3.connect("cookie.db")
    # DBを操作できるようにする
    c = conn.cursor()
    # 実行したいSQL文を書く
    print(py_task)
    # breakpoint()
    c.execute("UPDATE tasks SET task= ? where id =?",(py_task,py_id))
    conn.commit()
    conn.close()
    print(py_task)
    return redirect("/list")

# 削除機能をつくっていくよー
@app.route("/del/<int:id>")
def del_get(id):
    # 入力フォームからデータを受け取る
    conn = sqlite3.connect("cookie.db")
    # DBを操作できるようにする
    c = conn.cursor()
    # 実行したいSQL文を書く
    c.execute("DELETE FROM tasks WHERE id = ?",(id,))
    conn.commit()
    conn.close()
    return redirect("/list")

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/login",methods = ["POST"])
def login_post():
    # フォームから送られてきたデータを取得する
    # request.form.get("名前") タスクの内容を取得する
    py_name = request.form.get("member_name")
    py_password = request.form.get("member_password")
    
    # Dbに接続する
    conn = sqlite3.connect('cookie.db')
    # カーソルを取得する
    c = conn.cursor()
    # SQL
    c.execute("SELECT id FROM members WHERE name = ? AND password = ?",(py_name,py_password))
    # データを取得する
    user_id = c.fetchone()
    # DBを閉じる
    conn.close()
    
    if user_id == None:
        message = "ユーザー名かパスワードが間違っています"
        return render_template("login.html",message = message)
    
    else:
        session["user_id"] = user_id[0]
        return redirect("/list")


@app.route("/logout")
def logout():
    session.pop("user_id",None)
    return redirect("/login")


# -------いったん隠しー－－－－－－－－－－－
# @app.route('/top')
# def template():
#     py_name = "cookie"
#     return render_template("index.html")

# # 声かけランダム
# @app.route('/word')
# def word():
#     word_list = ["１分でできることもいいね！","ずーっと気になってることやってみる？","１日１つもいいね！","カップラーメンできる間にやっちゃう？","深呼吸する時間意識してみる？","朝起きてコップ１杯の白湯いいらしいよ！","自分を褒めまくるのもいいね"]
#     py_word = random.choice(word_list)
#     return render_template("word.html",word = py_word)

# # タスク入力
# @app.route("/add",methods = ["GET"])
# def add():
#     return render_template("add.html")

# @app.route("/add",methods = ["POST"])
# def add_post():
#     py_task = request.form.get("task")

#     print(py_task)
#     # py_user_id = session["user_id"]
#     # py_task = request.form.get("task")

#     # conn = sqlite3.connect('flasktest.db')
#     # c = conn.cursor()
#     # c.execute("INSERT INTO tasks (taks,user_id) VALUES(?,?)",(py_task,user_id))
#     # conn.commit()
#     # conn.close()
#     # return redirect("/list")

# # edit
# @app.route('/edit')
# def edit():
#     return render_template("edit.html")

# # list一覧
# @app.route('/list')
# def list():
#     return render_template("list.html")

# # login
# @app.route('/login')
# def login():
#     return render_template("login.html")

# # regist
# @app.route('/regist')
# def regist():
#     return render_template("regist.html")

# # 以下未使用
# # @app.route('/')
# # def ():
# #     return render_template(".html")

# # @app.route('/')
# # def ():
# #     return render_template(".html")

# # @app.route('/')
# # def ():
# #     return render_template(".html")

# # @app.route('/')
# # def ():
# #     return render_template(".html")

# # @app.route('/')
# # def ():
# #     return render_template(".html")

# # @app.route("/list")
# # def list():
# #         py_user_id = session["user_id"]
# #         conn = sqlite3.connect("flasktest.db")
# #         c = conn.cursor()
# #         c.execute("select id, task from tasks WHERE user_id = ?",(py_user_id,))
# #         task_list = []
# #         for row in c.fetchall():
# #             task_list.append({"id":row[0],"task":row[1]})
# #         c.close()
# #         print(task_list)
# #         return render_template("list.html",task_list = task_list )
# #     else:
# #         return redirect("/login")







# ---------ここまで書く----------

if __name__ == "__main__":
    app.run(debug=True)
