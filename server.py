from logging import debug
from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def index():
    return "Go to /play to get started"

# * Single Template == play_num_color.html  >  Change num and color in return line
@app.route('/play')
def play():
    return render_template("play_num_color.html", num=7, color="red")

# * -------------------- Using multiple templates --------------------
# @app.route('/play/<int:num>')
# def play_num(num):
#     return render_template("play_num.html", num=num)

# @app.route('/play/<int:num>/<string:color>')
# def play_num_color(num, color):
#     return render_template("play_num_color.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)