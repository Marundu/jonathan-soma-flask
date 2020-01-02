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
def hello():
    print('The total number of schools is ', School.query.count())
    school=School.query.filter_by(LOC_CODE='X270').first()
    print('The school name is', school.SCHOOLNAME)
    
    zip_schools=School.query.filter_by(ZIP='10466').all()
    
    for zip_school in zip_schools:
        print(zip_school.SCHOOLNAME)
    
    return render_template('index.html')


@app.route('/about')
def about():
    print('The total number of schools is ', School.query.count())
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)
