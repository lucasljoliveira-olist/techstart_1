from flask import Flask, render_template, redirect
from back.controllers.category_controller import CategoryController
from front.web.routs.category_routs import category_bp

app = Flask(__name__)

app.register_blueprint(category_bp)


@app.route('/')
def index():
    return render_template('index.html')

