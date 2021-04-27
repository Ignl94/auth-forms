from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from grocery_app.models import GroceryStore


class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    # TODO: Add the following fields to the form class:
    # - title - StringField
    # - address - StringField
    # - submit button
    title = StringField('Store Title', validators=[
                        DataRequired(), Length(min=5, max=50)])
    address = StringField('Address', validators=[
                          DataRequired(), Length(min=5, max=50)])
    submit = SubmitField('Submit')


class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    # TODO: Add the following fields to the form class:
    # - name - StringField
    # - price - FloatField
    # - category - SelectField (specify the 'choices' param)
    # - photo_url - StringField (use a URL validator)
    # - store - QuerySelectField (specify the `query_factory` param)
    # - submit button
    name = StringField('Name', validators=[
                       DataRequired(), Length(min=3, max=50)])
    price = FloatField('Price', validators=[
                       DataRequired(), Length(min=5, max=50)])
    category = SelectField('Category', choices=[
                           'produce'], validators=[DataRequired()])
    photo_url = StringField('Photo', validators=[URL(require_tld=False)])
    store = QuerySelectField(
        'Store', query_factory=lambda: GroceryStore.query, allow_blank=True)
    submit = SubmitField('Submit')
