from  flask import Flask ,render_template ,request ,redirect, session
import random
# db接続
import sqlite3
# 日付
import datetime
# できた！ボタンを押したら日付を取得したい
today = datetime.date.today()
print(today)

app = Flask(__name__)
app.secret_key = 'sunabaco'

# --------ここから書く---------
# top画面
@app.route('/')
def top():
    return render_template("index.html")

# まだやってない　できとらん6/14_22:43時点
@app.route('/greet/<name>')
def greet(name):
    return name + 'さん、こんにちは！' 

# まだやってない　できとらん6/14_22:43時点
@app.route('/template')
def template():
    py_name = "SUNABACO"
    return render_template("index.html",name = py_name)

# login画面用＿残す
@app.route("/login")
def login():
    return render_template("login.html")

# login‗登録済みの方
@app.route("/login",methods = ["POST"])
def login_post():
        py_name = request.form.get("member_name")
        py_password = request.form.get("member_password") 
        # Dbに接続
        conn = sqlite3.connect('cookie.db')
        c = conn.cursor()
        c.execute("SELECT id FROM members WHERE name = ? AND password = ?",(py_name,py_password))
        user_id = c.fetchone()
        conn.close()
        
        if user_id == None:
            message = "ユーザー名かパスワードが間違っています"
            return render_template("login.html",message = message)    
        else:
            session["user_id"] = user_id[0]
            return redirect("/list")


# task追加
@app.route('/add', methods = ["GET"])
def add():
    if "user_id" in session:
        return render_template("add.html")
    else:
        return redirect("/add")

@app.route('/add',methods = ["POST"])
def add_post():
    py_user_id = session["user_id"]
    py_task = request.form.get("task")
    # db
    conn = sqlite3.connect('cookie.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (task,user_id) VALUES(?,?)",(py_task,py_user_id))
    conn.commit()
    conn.close()
    return redirect("/list")

# 新規ユーザー登録
@app.route("/regist")
def regist():
    return render_template("regist.html")

@app.route("/regist",methods = ["POST"])
def regist_post():
        py_name = request.form.get("member_name")
        py_password = request.form.get("member_password")
        # db
        conn = sqlite3.connect('cookie.db')
        c = conn.cursor()
        c.execute("INSERT INTO members VALUES(null,?,?)",(py_name,py_password))
        conn.commit()
        conn.close()
        return redirect("/list")

# タスクリスト
@app.route("/list")
def list():
    if "user_id" in session:
        # DB接続
        py_user_id = session["user_id"]
        conn = sqlite3.connect("cookie.db")
        c = conn.cursor()
        c.execute("SELECT id, task FROM tasks WHERE user_id = ?",(py_user_id,))
        # タスクリストを入れる配列を定義
        task_list = []
        for row in c.fetchall():
            task_list.append({"id":row[0],"task":row[1]})
        c.close()
        print(task_list)
        word_list = ["１分でできることもいいね！","ずーっと気になってることやってみる？","１日１つのタスクもいいね！","カップラーメンできる間にやっちゃう？","深呼吸する時間意識してみる？","朝起きてコップ１杯の白湯いいらしいよ！","自分を褒めまくるのもいいね"]
        py_word = random.choice(word_list)
        return render_template("list.html",task_list = task_list, word = py_word)

    else:
        return redirect("/login")


# 編集機能
@app.route("/edit/<int:id>")
def edit(id):
    if "user_id" in session:
        conn = sqlite3.connect("cookie.db")
        c = conn.cursor()
        c.execute("SELECT task FROM tasks WHERE id = ?;",(id,))
        task = c.fetchone()
        c.close()
        if task is not None:
            task = task[0]
        else:
            return "タスクがないよ"
        item = {"id":id, "task":task} 
        return render_template("edit.html",item = item)
   
    else:
        return redirect("/login")

# タスクの内容を編集（更新）する機能
@app.route("/edit", methods = ["POST"])
def edit_post():
    # 入力フォームからデータを受け取る
    task = request.form.get("task")
    task_id = request.form.get("task_id")
    # DB接続
    conn = sqlite3.connect("cookie.db")
    c = conn.cursor()
    # breakpoint()
    c.execute("UPDATE tasks SET task= ? WHERE id =?",(task,task_id))
    conn.commit()
    conn.close()
    return redirect("/list")

# 削除機能をつくっていくよー
@app.route("/del/<int:id>")
def del_get(id):
    # 入力フォームからデータを受け取る
    conn = sqlite3.connect("cookie.db")
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?",(id,))
    conn.commit()
    conn.close()
    return redirect("/list")

# ログアウト
@app.route("/logout")
def logout():
    session.pop("user_id",None)
    return redirect("/")

# ４０３
@app.errorhandler(403)
def mistake403(code):
    return 'There is a mistake in your url!'

# ４０４
@app.errorhandler(404)
def notfound404(code):
    return render_template("notf.html")

# -------コピペ用ー－－－－－－－－－－－

# @app.route('/')
# def ():
#     return render_template(".html")

# -------ー－－－－－－－－－－－

# ---------ここまで書く、以下消さない----------

if __name__ == "__main__":
    app.run(debug=True)
