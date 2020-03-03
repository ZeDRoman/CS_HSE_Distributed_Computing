from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    id = IntegerField("id", validators=[DataRequired()])
    name = StringField("name", validators=[DataRequired()])
    category = StringField("category", validators=[DataRequired()])
    submit = SubmitField()

    def to_string(self):
        return F"id: {self.id.data}, name: {self.name.data}, category: {self.category.data}"
