from flask import Flask,render_template
app= Flask(__name__)

@app.route('/play')
def index():
    return render_template("index.html", times=3,shade="blue")
@app.route('/play/<num>')
def many(num):
    return render_template("index.html", times=int(num), shade="blue")
@app.route('/play/<num>/<color>')
def colorful(num,color):
    return render_template("index.html", times=int(num), shade=color)
if __name__=="__main__":
    app.run(debug=True)