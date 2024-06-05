from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    area = db.Column(db.Integer, nullable=False)
    population = db.Column(db.Integer, nullable=False)
    density = db.Column(db.Float, nullable=False)
    gdp = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Country {self.name}>'
