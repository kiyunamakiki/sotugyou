from  flask import Flask

app = Flask(__name__)
app.secret_key = 'secret_key'

# --------ここから書く---------
@app.route("")







# ---------ここまで書く----------

if __name__ == "__main__":
    app.run(debug=True)