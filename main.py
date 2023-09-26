from flask import Flask, render_template, jsonify, request, redirect
from pymongo import MongoClient
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder='templates', static_folder='static')
mongo_client = MongoClient(
    os.getenv("DATABASE_URL"))
db = mongo_client.thedevsdiaries


@app.get('/<path:page_path>')
def get_page_not_found(page_path):
    return render_template('404.html')


@app.get('/')
def get_home():
    cards = sorted(list(db.posts.find()),
                   key=lambda x: x['created_at'], reverse=True)
    return render_template('index.html', cards=cards)


@app.post('/posts')
def set_post():
    now = datetime.datetime.now()
    now_formated = now.strftime("%d/%m/%Y %H:%M:%S")
    data = request.get_json()

    db.posts.insert_one({'title': data.get('title'), 'content': data.get(
        'message'), 'author': data.get('email'), 'created_at': now_formated})

    return redirect('/')


@app.get('/creator')
def get_creator():
    return jsonify(url='https://github.com/julioreisdev')


@app.get('/ping')
def get_ping():
    return 'pong'


if __name__ == '__main__':
    app.debug = True
    app.run()
