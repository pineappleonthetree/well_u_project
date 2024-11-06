from flask import Flask,render_template,request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/objective")
def objective():
    return render_template("objective.html")

@app.route("/page3")
def page3():
    return render_template("page3.html",)

@app.route('/submit', methods=['POST'])
def submit():
    user_name = request.form['username']
    user_age = request.form['age']
    return redirect(url_for('page4', username=user_name,age=user_age))

@app.route("/page4/<username>/<age>")
def page4(username,age):
    return render_template("page4.html",username=username,age=age)

@app.route("/page5/<username>")
def page5(username):
    return render_template("page5.html",username=username)

@app.route("/page6/<username>")
def page6(username):
    return render_template("page6.html",username=username)

@app.route("/page7/<username>")
def page7(username):
    return render_template("page7.html",username=username)

@app.route("/page8/<username>")
def page8(username):
    return render_template("page8.html",username=username)

@app.route("/page9")
def page9():
    return render_template("page9.html")

@app.route("/page10")
def page10():
    return render_template("page10.html")

if __name__ == "__main__":
    app.run(port=8000,debug=True)
