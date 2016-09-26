from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return 'Home page'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello_page(name=None):
    return render_template('hello_page.html', name=name)


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


if __name__ == '__main__':
    app.run()
