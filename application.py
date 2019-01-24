from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
# from flask_bootstrap import Bootstrap

app = Flask(__name__)
# bootstrap = Bootstrap(app)

@app.route('/')
def create_app():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


  
  

  
