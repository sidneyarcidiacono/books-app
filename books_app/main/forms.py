from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    DateField,
    SelectField,
    SubmitField,
    TextAreaField,
)
from wtforms.ext.sqlalchemy.fields import (
    QuerySelectField,
    QuerySelectMultipleField,
)
from wtforms.validators import DataRequired, Length, ValidationError
from books_app.models import Audience, Book, Author, Genre, User

# Define our custom validator
def validate_name(form, field):
    if "banana" in field.data.lower():
        raise ValidationError("Title cannot contain the word banana")


class BookForm(FlaskForm):
    """Form to create a book."""

    title = StringField(
        "Book Title",
        validators=[DataRequired(), Length(min=3, max=80), validate_name],
    )
    publish_date = DateField("Date Published")
    author = QuerySelectField(
        "Author", query_factory=lambda: Author.query, allow_blank=False
    )
    audience = SelectField("Audience", choices=Audience.choices())
    genres = QuerySelectMultipleField(
        "Genres", query_factory=lambda: Genre.query
    )
    submit = SubmitField("Submit")


class AuthorForm(FlaskForm):
    """Form to create an author."""

    name = StringField(
        "Author Name", validators=[DataRequired(), Length(min=4, max=80)]
    )
    biography = TextAreaField(
        "Author Biography",
        validators=[DataRequired(), Length(min=5, max=200)],
    )
    submit = SubmitField("Submit")


class GenreForm(FlaskForm):
    """Form to create a genre."""

    # - the genre's name (e.g. fiction, non-fiction, etc)
    name = StringField(
        "Genre Name", validators=[DataRequired(), Length(min=3, max=80)]
    )
    submit = SubmitField("Submit")
