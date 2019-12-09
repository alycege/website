
from flask import Flask, render_template

app = Flask(__name__)

templates_dir = '/home/age/scripts/website/templates/'

@app.route('/')
def test():
    return render_template(templates_dir + 'homepage.html')

