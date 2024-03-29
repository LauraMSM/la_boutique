from wtforms import Form, StringField, PasswordField, SubmitField, validators, EmailField, FileField

class AddEmpForm(Form):

    email = EmailField([
                                        validators.InputRequired(),
                                        validators.Email()
                                    ])
    password = PasswordField([
                                        validators.Length(min=10, max=60),
                                        validators.EqualTo('password_confirm', message='Las contraseñas no coinciden'),
                                        validators.InputRequired()
                                    ])
    password_confirm = PasswordField([
                                        validators.InputRequired()
                                    ])
    e_name = StringField([
                                        validators.InputRequired()
                                    ])
    surname1 = StringField([
                                        validators.InputRequired()
                                    ])
    surname2 = StringField()
    user_image = FileField([            
                                        validators.InputRequired()
                                    ],
                                        render_kw={'id': 'file-reg', 'data-multiple-caption': '{count} files selected'})
    save = SubmitField('Añadir empleado')
