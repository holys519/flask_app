# 必要なモジュールをインポート
from crypt import methods
from flask import Flask, request, render_template
from wtforms import Form, StringField, validators, SubmitField

# app という変数名でFlaskオブジェクトをインスタンス化
app = Flask(__name__)

# WTForm を使い、index.htmlがわで表示させるフォームを構築
class InputForm(Form):
    InputFormTest = StringField('文字を入力してください', [validators.InputRequired()])

    # html側で表示する、submitボタンの表示
    submit = SubmitField('送信')

# URLにアクセスがあった場合の挙動
@app.route('/', methods = ['GET', 'POST'])
def input():
    # WTforms で構築したフォームをインスタンス化
    form = InputForm(request.form)
    # POSTメソッドの条件の定義
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('index.html', forms=form)
        # 条件に当てはまる場合の処理を実行を定義
        outputname_ = request.form['InputFormTest']
        return render_template('result.html', outputname=outputname_)

    # GETめそどの条件の定義
    elif request.method == 'GET':
        return render_template('index.html', forms=form)

# アプリケーションに実行の定義
if __name__ == '__main__':
    app.run(debug=True)
