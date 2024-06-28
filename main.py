from app import app
from flask import Flask, render_template, url_for

from api.horoskop import blizanci




@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')



@app.route('/blizanci')
def bliz():
    return blizanci()








if __name__ == "__main__":
    app.run()
