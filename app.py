from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Keeey'

bootstrap = Bootstrap(app)

app_name = 'myapp'



@app.route("/")
def homepage():
    return render_template('user.html')

@app.route('/base')
def base_page():
    return render_template('base.html')

@app.route('/Syllabus')
def index_page():
    return render_template('Pages/Syllabus.html')

if __name__ == '__main__':
    app.run()

