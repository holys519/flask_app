#coding: utf-8

from flask import Flask, render_template

# appという名前でFlaskオブジェクトをインスタンス化
app = Flask(__name__)

@app.route('/')
def index():
    # return 'Hello Workd!'
    return render_template('index.html')

# エントリーポイント
if __name__ == '__main__':
    app.run()