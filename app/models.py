from app import app, db

db.Model.metadata.reflect(db.engine)


class School(db.Model):
    __tablename__='schools'
    __table_args__={'extend_existing': True}
    LOC_CODE=db.Column(db.Text, primary_key=True)
