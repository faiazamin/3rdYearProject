from flask import Flask, render_template, request, url_for


app = Flask(__name__)
TITLE = "ROJ"

# main page
@app.route('/')
def index_page():
    return render_template('index.html', title=TITLE)

# # practice page
# @app.route('/practice')
# def practice():
#     return 'Hello, World!'

# # sign up page
# @app.route('/signup')
# def signup():
#     return 'Hello, World!'

# # signin page
# @app.route('/signin')
# def signin():
#     return 'Hello, World!'

# # practice page
# @app.route('/practice')
# def problem():
#     return 'Hello, World!'

# # practice page
# @app.route('/practice')
# def practice():
#     return 'Hello, World!'


if __name__ == "__main__":
	app.run()