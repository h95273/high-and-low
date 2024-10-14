from flask import Flask, render_template
import random

app = Flask(__name__)

# トップページ
@app.route('/')
def index():
    # トップページの処理
    #  なにもしない。
    # 表示するhtmlのページ
    return render_template('index.html')

# Highのページ
@app.route('/high')
def high():
    # Highを選んだときのページの処理を書く。
    # 正解の数字
    correct_number = random.randint(1, 10)
    # 正解かどうか
    if correct_number >= 6:
      output = "正解！"
    else:
      output = "はずれ"
    # 表示するhtmlのページ
    return render_template('high.html',
      correct_number=correct_number,
      output=output)

# Lowのページ
#high等を参考にしてください。

app.run(host='0.0.0.0')

