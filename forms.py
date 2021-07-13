from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SelectField, DateField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    name = StringField('Nazwa', validators=[DataRequired()])
    price = DecimalField('Kwota', validators=[DataRequired()], places=2)
    type = SelectField('Rodzaj', choices=[('Przyjemnosci', 'Przyjemności'), ('Jedzenie', 'Jedzenie'), ('Rachunki', 'Rachunki'), ('Dodatkowe Wydatki', 'Dodatkowe Wydatki')])
    data = DateField('Data', validators=[DataRequired()])
