from flask import (
  Flask,
  request,
  redirect,
  render_template)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer
from datetime import datetime
import pytz

#データベース---------------------------------------------------------------------------------------------------------
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data_list.db"
db.init_app(app)

class image_list(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    images = db.Column(db.String(100) ,nullable=False)
    color_name = db.Column(db.String(20) ,nullable=True)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.now(pytz.timezone('Asia/Tokyo')))

with app.app_context():
    db.create_all()


#ページ遷移----------------------------------------------------------------------------------------------------------------
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        images = request.form.get('images')
        color_name = request.form.get('color_name')

        lists = image_list(images=images, color_name=color_name)

        db.session.add(lists)
        db.session.commit()
        return redirect('/data_list')
    else:
        return render_template('home.html')

@app.route('/<int:id>/update', methods=['GET','POST'])
def update(id):
    lists = image_list.query.get(id)
    if request.method == 'GET':
        return render_template('update.html', lists=lists)
    else:
        lists.images = request.form.get('images')
        lists.color_name = request.form.get('color_name')

        db.session.commit()
        return redirect('/data_list')

@app.route('/<int:id>/delete', methods=['GET'])
def delete(id):
    lists = image_list.query.get(id)

    db.session.delete(lists)
    db.session.commit()
    return redirect('/data_list')

@app.route('/data_list', methods=['GET','POST'])
def list():
    if request.method == 'GET':
        all_lists = image_list.query.all()
        return render_template('data_list.html', all_lists=all_lists)

@app.route('/color_result')
def color():
    return render_template('color_result.html')

@app.route('/impression')
def impression():
    return render_template('impression.html')

@app.route('/coordination_result')
def coordination():
    return render_template('coordination_result.html')

if __name__ == "__main__":
    app.run(debug=True)