from flask import (
  Flask,
  request,
  redirect,
  render_template)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String,Integer
from datetime import datetime
import pytz
import re
from color_model1 import find_closest_color
from color_model1 import extract_dominant_color
from color_model1 import get_dominant_color_name
from impression import impression1
from impression import impression2
from coordination_model import find_sub_color
from coordination_model import find_sub_color_eng
from coordination_model import main_color_eng

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  #JSONレスポンスをUTF-8でエンコードする

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
def home():
    if request.method == 'POST':
        image_path = request.form.get('images')
        the_closest_color_name = get_dominant_color_name(image_path)
        lists = image_list(images=image_path, color_name=the_closest_color_name)
        db.session.add(lists)
        db.session.commit()

        main_color = the_closest_color_name
        main_color_eng_result = main_color_eng(main_color)
        return render_template('color_result.html', image_path = image_path, color_name = the_closest_color_name, main_color_eng_result=main_color_eng_result)
    else:
        return render_template('home.html')


@app.route('/color_result')
def color():
        return render_template('color_result.html')


@app.route('/data_list')
def list():
        all_lists = image_list.query.all()
        return render_template('data_list.html', all_lists=all_lists)


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


@app.route('/<int:id>/impression', methods=['GET','POST'])
def id_impression(id):
    if request.method == 'GET':
        user = image_list.query.filter(image_list.id == id).first()
        user_image = user.images
        user_color = user.color_name
        colors = impression2(user_color)
        return render_template('impression.html', user_image=user_image, colors=colors)
    else:
        user = image_list.query.get(id)
        user_color = user.color_name
        main_color = user_color
        impression = request.form.get('imp') 
        result_sub_color = find_sub_color(main_color,impression)
        result_sub_color_eng = find_sub_color_eng(main_color,impression)
        return render_template('coordination_result.html', result_sub_color=result_sub_color, result_sub_color_eng=result_sub_color_eng)


@app.route('/impression')
def impression():
    return render_template('impression.html')


@app.route('/coordination_result')
def coordination():
    return render_template('coordination_result.html')

if __name__ == "__main__":
    app.run(debug=True)


# if isinstance(id_image, list):
#             id_image = id_image[0]
#         elif isinstance(id_image, str):
#             user_image = re.sub(r"/\d+/", "/", id_image)
#         else:
#             user_image = None
