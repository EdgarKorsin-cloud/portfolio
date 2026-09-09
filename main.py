from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
