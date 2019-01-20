from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def create_app():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

# when you execute python assigns the name "main" to the file
# so then line 9 will be true! 





  
  

  