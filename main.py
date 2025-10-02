from flask import Flask,redirect,render_template

app = Flask(__name__)

@app.route("/")
def main_page():

    return render_template("index.html")

@app.route("/registr_page")
def registr():
    return None



if __name__ == '__main__':
    app.run(debug=True)

