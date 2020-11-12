from flask import g

db = g.db


def productFromJson(data):
    return Product(
               name=data['name'],
               category=data['category']
           )


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255))

    def __repr__(self):
        return dict(id=self.id, name=self.name, category=self.category)
