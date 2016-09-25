from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def home_page():
    return 'Home page'


@app.route('/hello')
def hello_page():
    return 'Hello page'


@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post №%d' % post_id


@app.route('/projects/')
def show_projects():
    return 'Projects page'


@app.route('/about')
def about_page():
    return 'about page'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass


with app.test_request_context():
    print(url_for('home_page', next='/'))

if __name__ == '__main__':
    app.run()
