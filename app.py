from flask import Flask, request, render_template, \
                  flash, g, session, redirect, url_for

app = Flask(__name__, template_folder="templates")

@app.route('/')
def create_app():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)