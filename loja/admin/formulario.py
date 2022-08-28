from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    nomeCompleto = StringField('Digite seu nome completo', [validators.Length(min=4, max=25)])
    email = StringField('Digite seu e-mail', [validators.Length(min=6, max=35)])
    senha = PasswordField('Digite sua senha', [
        validators.DataRequired(),
        validators.EqualTo('confirmacao', message='Confirmação inválida')
    ])
    confirmacao = PasswordField('Digite sua senha novamente')


class LoginFormulario(Form):
    email = StringField('Digite seu e-mail', [validators.Length(min=6, max=35)])
    senha = PasswordField('Digite sua senha', [validators.DataRequired()])
    