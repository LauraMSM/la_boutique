from model.tablas import *

class Usuarios(Tablas):
    
    @classmethod
    def check_user(cls, email):
        user = cls.get_select(['Email'], {'Email':email})
        return True if user not in (None, [], ()) else False

    @classmethod
    def get_password(cls, email):
        return ''.join(cls.get_select(['Password'], {'Email':email}))

    @classmethod
    def check_credentials(cls, email, password):
        return True if cls.check_user(email) and password == cls.get_password(email) else False

    @classmethod
    def get_username(cls, email):
        return email.split('@')[0].replace('.', '_')

    @classmethod
    def user_log(cls, email):
        type = cls._get_name()
        query = (cls.get_select(['ID', 'Email'], {'Email':email}))[0]
        log = {'user_email' : query[1], 'user_id' : query[0], 'user_type' : type}
        Modules.write_session(log)

class Clientes(Usuarios):
    pass

class Empleados(Usuarios):
    pass
