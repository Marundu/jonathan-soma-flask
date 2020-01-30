from flask import render_template

from app import app, db
from app.models import School


# routes

@app.route('/')
def index():
    school_count=School.query.count()
    zip_schools=School.query.all()  
    return render_template('list.html', count=school_count, schools=zip_schools, location='New York City')


@app.route('/schools/<slug>')
def schools(slug):
    school=School.query.filter_by(LOC_CODE=slug).first()
    return render_template('schools.html', school=school)


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
    # convert all cities to title case
    cities=[city[0].title() for city in cities]
    # remove duplicates and sort
    cities=sorted(list(set(cities)))
    return render_template('cities.html', count=len(cities), cities=cities)


@app.route('/zip')
def zip_list():
    zips=School.query.with_entities(School.ZIP).distinct().all()
    zips=[zipcode[0] for zipcode in zips]
    return render_template('zips.html', zips=zips)

