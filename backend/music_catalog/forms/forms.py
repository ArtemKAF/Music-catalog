from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class LoginForm(FlaskForm):
    email = StringField("Email: ", validators=[Email()])
    password = PasswordField(
        "Пароль: ",
        validators=[DataRequired(), Length(min=4, max=30)]
    )
    remember_me = BooleanField("Запомнить", default=False)
    submit = SubmitField("Войти")


class RegisterForm(FlaskForm):
    name = StringField("Имя: ")
    email = StringField("Email: ", validators=[Email()])
    password = PasswordField(
        "Пароль: ",
        validators=[
            DataRequired(),
            Length(min=4, max=30),
            EqualTo("password_confirm", message="Пароли должны совпадать!"),
        ]
    )
    password_confirm = PasswordField(
        "Еще раз пароль: ",
        validators=[
            DataRequired(),
            Length(min=4, max=30),
        ],
    )
    submit = SubmitField("Зарегистрироваться")
