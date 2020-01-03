from flask import (
    Flask,
    render_template,
)

from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///schools.db'
db=SQLAlchemy(app)

db.Model.metadata.reflect(db.engine)


class School(db.Model):
    __tablename__='schools'
    __table_args__={'extend_existing': True}
    LOC_CODE=db.Column(db.Text, primary_key=True)


@app.route('/')
def index():
    school_count=School.query.count()
    zip_schools=School.query.all()  
    return render_template('list.html', count=school_count, schools=zip_schools, location='New York City')


@app.route('/schools/<slug>')
def detail(slug):
    school=School.query.filter_by(LOC_CODE=slug).first()
    return render_template('detail.html', school=school)


@app.route('/city/<cityname>')
def city(cityname):
    cityname=cityname.replace('-', ' ')
    schools=School.query.filter_by(city=cityname.upper()).all()
    return render_template('city.html', schools=schools, count=len(schools), location=cityname)


@app.route('/zip/<zipcode>')
def zip(zipcode):
    schools=School.query.filter_by(ZIP=zipcode).all()
    return render_template('zip.html', schools=schools, count=len(schools), location=zipcode)


@app.route('/city')
def city_list():
    cities=School.query.with_entities(School.city).distinct().all()
    cities=[city[0] for city in cities]
    return render_template('cities.html', count=len(cities), cities=cities)


if __name__=='__main__':
    app.run(debug=True)
