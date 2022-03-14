# https://www.youtube.com/watch?v=e4ax90XmUBc
# https://www.youtube.com/watch?v=QXjU9qTsYCc&t=204s

""" Interpreter :
  一邊翻譯一邊執行程式碼，
  讀一行程式碼後就立馬翻譯成 Machine 後並執行
  inter 指介於程式碼 & 電腦之間來回

  優點：你可以知道錯在第幾行 code
  缺點：執行效率低

  Python 為 Interpreter language
"""

""" Compiler :
  將程式語言一次翻譯成 Machine Code 後再執行，

  優點：執行很快
  缺點：你只知道最後無法順利執行，不知道問題出在哪裡
"""

import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
  return jsonify({
    'name': 'Benson Chen',
    'email': 'benson_chen@trendmicro.com'
  })

app.run()