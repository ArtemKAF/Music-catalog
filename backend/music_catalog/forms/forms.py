from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField("Email: ", validators=[Email()])
    psw = PasswordField(
        "Пароль: ",
        validators=[DataRequired(), Length(min=4, max=30)]
    )
    remember = BooleanField("Запомнить", default=False)
    submit = SubmitField("Войти")
