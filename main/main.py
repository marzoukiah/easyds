from dataclasses import dataclass
from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
import requests

from producer import publish

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)


@dataclass
class Job(db.Model):
    id: int
    job_title: str
    job_type: str
    job_description: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    job_title = db.Column(db.String(200))
    job_type = db.Column(db.String(200))
    job_description = db.Column(db.String(200))


@dataclass
class JobUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    job_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'job_id', name='user_job_unique')


@app.route('/api/jobs')
def index():
    return jsonify(Job.query.all())


'''@app.route('/api/jobs/<int:id>/like', methods=['POST'])
def like(id):
    req = requests.get('http://docker.for.mac.localhost:8000/api/user')
    json = req.json()

    try:
        productUser = ProductUser(user_id=json['id'], product_id=id)
        db.session.add(productUser)
        db.session.commit()

        publish('product_liked', id)
    except:
        abort(400, 'You already liked this product')

    return jsonify({
        'message': 'success'
    })
'''
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')