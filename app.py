from flask import Flask, render_template

app = Flask(__name__)


config = {
    "DEBUG": True  # run app in debug mode
}

# Flask to use the above defined config
app.config.from_mapping(config)

#
# @app.route('/')
# def hello_world():  # put application's code here
#     return render_template('index.html')



#
# if __name__ == '__main__':
#     app.run()
