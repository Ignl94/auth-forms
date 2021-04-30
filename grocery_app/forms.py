from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField, PasswordField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL, ValidationError
from grocery_app.models import GroceryStore, User,ItemCategory
from grocery_app import bcrypt


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
                       DataRequired()])
    category = SelectField('Category', choices=ItemCategory.choices(), validators=[DataRequired()])
    photo_url = StringField('Photo', validators=[URL(require_tld=False)])
    store = QuerySelectField(
        'Store', query_factory=lambda: GroceryStore.query, allow_blank=True)
    submit = SubmitField('Submit')


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'That username is taken. Please choose another one.')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

    def validate_username(self, username):
       user = User.query.filter_by(username=self.username.data).first()
       if not user:
           raise ValidationError('No such user. Please try again.')
    
    def validate_password(self, password):
       user = User.query.filter_by(username=self.username.data).first()
       if user and not bcrypt.check_password_hash(user.password, password.data):
           raise ValidationError('Passwords didn\'t match. Please try again.')
