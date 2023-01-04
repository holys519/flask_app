from flask import Flask

# Flask をインスタンス化
app = Flask(__name__)

# ルートディレクトリにアクセスが会った時の処理
@app.route('/')
def hello():
    return 'Hello World'

# エントリーポイント
if __name__ == '__main__':
    app.run()