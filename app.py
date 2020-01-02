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
    school_count=School.query.count()
    zip_schools=School.query.filter_by(ZIP='10466').all()  
    return render_template('index.html', count=school_count, schools=zip_schools)


@app.route('/about')
def about():
    print('The total number of schools is ', School.query.count())
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)
