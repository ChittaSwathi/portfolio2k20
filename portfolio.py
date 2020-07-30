from flask import Flask, url_for, render_template

app = Flask(__name__)
print('app', app)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/projects/')
@app.route('/projects/<name>')
def projects(name=None):
    if not name:
        return render_template('projects.html')
    else:
        return render_template('project_details.html', name=name)

# with app.test_request_context():
#     print(url_for('projects'))




if __name__ == '__main__':
    print('app in main', app)
    app.run()