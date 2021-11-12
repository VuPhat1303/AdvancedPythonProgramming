from flask import Flask, render_template
app = Flask(__name__)

@app.route("/index.html")
def trangchu():
    return render_template("index.html")

@app.route("/tintuc.html")
def tintuc():
    return render_template("tintuc.html")

@app.route("/sanpham.html")
def sanpham():
    return render_template("sanpham.html")

if __name__ == "__main__":
    app.run(debug=True)