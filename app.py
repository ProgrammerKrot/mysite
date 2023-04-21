from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/en")
def home_en():
    return render_template("index_en.html")

@app.route("/bel")
def home_bel():
    return render_template("index_bel.html")

@app.route("/ru")
def home_ru():
    return render_template("index_ru.html")

@app.route("/por")
def home_por():
    return render_template("index_por.html")




if __name__ == '__main__':
    app.run(debug=True)