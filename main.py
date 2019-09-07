from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>hello flask!</h1>'


## 动态路由
@app.route('/user/<yourname>')
def user(yourname):
    return '<h1>hello {yourname}</h1>'.format(yourname=yourname)


if __name__ == "__main__":
    app.run(debug=True)
