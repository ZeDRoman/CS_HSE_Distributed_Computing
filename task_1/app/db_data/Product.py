from app import db


def productFromForm(form):
    return Product(
               id=form.id.data,
               name=form.name.data,
               category=form.category.data
           )

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255))

    def __repr__(self):
        return F"id: {self.id}, name: {self.name}, category: {self.category}"
