from peewee import *

database = MySQLDatabase('employex', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'user': 'root', 'password': 'Jinchuriki2k'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Usuario(BaseModel):
    ciudad = CharField(column_name='Ciudad', null=True)
    contrasenia = CharField(column_name='Contrasenia', null=True)
    correo = CharField(column_name='Correo', null=True)
    fotoperfil = IntegerField(column_name='Fotoperfil', null=True)
    pais = CharField(column_name='Pais', null=True)
    validationtoken = CharField(column_name='ValidationToken', null=True)
    validated = IntegerField(column_name='Validated', null=True)
    usuariocorreo = CharField(column_name='Usuariocorreo', primary_key=True)

    class Meta:
        table_name = 'usuario'

class Independiente(BaseModel):
    apellidos = CharField(column_name='Apellidos', null=True)
    aptitud = CharField(column_name='Aptitud', null=True)
    descripcionpersonal = CharField(column_name='Descripcionpersonal', null=True)
    independiente_id = AutoField(column_name='IndependienteID')
    nombre = CharField(column_name='Nombre', null=True)
    ocupacion = CharField(column_name='Ocupacion', null=True)
    usuariocorreo = ForeignKeyField(column_name='Usuariocorreo', field='usuariocorreo', model=Usuario)

    class Meta:
        table_name = 'independiente'

class Ofertadetrabajo(BaseModel):
    cargo = CharField(column_name='Cargo', null=True)
    descripcion = CharField(column_name='Descripcion', null=True)
    etiqueta = CharField(column_name='Etiqueta', null=True)
    ofertadetrabajo_id = AutoField(column_name='OfertadetrabajoID')
    tipoempleo = CharField(column_name='Tipoempleo', null=True)
    ubicacion = CharField(column_name='Ubicacion', null=True)
    usuariocorreo = ForeignKeyField(column_name='Usuariocorreo', field='usuariocorreo', model=Usuario)

    class Meta:
        table_name = 'ofertadetrabajo'

class Aplicacion(BaseModel):
    aplicacion_id = AutoField(column_name='AplicacionID')
    aprobado = IntegerField(column_name='Aprobado', null=True)
    fecha = DateField(column_name='Fecha', null=True)
    independiente = ForeignKeyField(column_name='IndependienteID', field='independiente_id', model=Independiente, null=True)
    ofertadetrabajo = ForeignKeyField(column_name='OfertadetrabajoID', field='ofertadetrabajo_id', model=Ofertadetrabajo, null=True)
    usuariocorreo = CharField(column_name='Usuariocorreo')

    class Meta:
        table_name = 'aplicacion'

class Certificacion(BaseModel):
    certificacion_id = AutoField(column_name='CertificacionID')
    credencialurl = CharField(column_name='Credencialurl', null=True)
    empresaemisora = CharField(column_name='Empresaemisora', null=True)
    fechacaducidad = DateField(column_name='Fechacaducidad', null=True)
    fechaexpedicion = DateField(column_name='Fechaexpedicion', null=True)
    independiente = ForeignKeyField(column_name='IndependienteID', field='independiente_id', model=Independiente)
    titulo = CharField(column_name='Titulo', null=True)

    class Meta:
        table_name = 'certificacion'

class Educacion(BaseModel):
    descripcion = CharField(column_name='Descripcion', null=True)
    disciplina = CharField(column_name='Disciplina', null=True)
    educacion_id = AutoField(column_name='EducacionID')
    fechafin = DateField(column_name='Fechafin', null=True)
    fechainicio = DateField(column_name='Fechainicio', null=True)
    independiente = ForeignKeyField(column_name='IndependienteID', field='independiente_id', model=Independiente)
    promedio = FloatField(column_name='Promedio', null=True)
    titulo = CharField(column_name='Titulo', null=True)
    universidad = CharField(column_name='Universidad', null=True)

    class Meta:
        table_name = 'educacion'

class Experiencialaboral(BaseModel):
    cargoactual = IntegerField(column_name='Cargoactual', null=True)
    experiencialaboral_id = AutoField(column_name='ExperiencialaboralID')
    fechafin = DateField(column_name='Fechafin', null=True)
    fechainicio = DateField(column_name='Fechainicio', null=True)
    independiente = ForeignKeyField(column_name='IndependienteID', field='independiente_id', model=Independiente)
    nombreempresa = CharField(column_name='Nombreempresa', null=True)
    sector = CharField(column_name='Sector', null=True)
    tipoempleo = CharField(column_name='Tipoempleo', null=True)
    titulo = CharField(column_name='Titulo', null=True)
    ubicacion = CharField(column_name='Ubicacion', null=True)

    class Meta:
        table_name = 'experiencialaboral'

class Seccion(BaseModel):
    descripcion = CharField(column_name='Descripcion', null=True)
    independiente = ForeignKeyField(column_name='IndependienteID', field='independiente_id', model=Independiente, null=True)
    seccion_id = AutoField(column_name='SeccionID')
    titulo = CharField(column_name='Titulo', null=True)

    class Meta:
        table_name = 'seccion'

class Media(BaseModel):
    file = TextField(column_name='File', null=True)
    media_id = AutoField(column_name='MediaID')
    ofertadetrabajo = ForeignKeyField(column_name='OfertadetrabajoID', field='ofertadetrabajo_id', model=Ofertadetrabajo, null=True)
    seccion = ForeignKeyField(column_name='SeccionID', field='seccion_id', model=Seccion, null=True)
    usuariocorreo = ForeignKeyField(column_name='Usuariocorreo', field='usuariocorreo', model=Usuario, null=True)

    class Meta:
        table_name = 'media'

class Organizacion(BaseModel):
    acercade = CharField(column_name='Acercade', null=True)
    codigopostal = IntegerField(column_name='Codigopostal', null=True)
    emailcontacto = CharField(column_name='Emailcontacto', null=True)
    nombre = CharField(column_name='Nombre', null=True)
    nombrecontact = CharField(column_name='Nombrecontact', null=True)
    organizacion_id = AutoField(column_name='OrganizacionID')
    sector = CharField(column_name='Sector', null=True)
    sitioweb = CharField(column_name='Sitioweb', null=True)
    telefonocontacto = CharField(column_name='Telefonocontacto', null=True)
    usuariocorreo = ForeignKeyField(column_name='Usuariocorreo', field='usuariocorreo', model=Usuario)

    class Meta:
        table_name = 'organizacion'

