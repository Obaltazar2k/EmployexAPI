import connexion
import json
import requests
import random
import string

from flask import Response
from swagger_server.models.independient_user import IndependientUser  # noqa: E501
from swagger_server.models.user import User
from swagger_server.models.media import Media as MediaModels
from swagger_server.models.laboral_experience import LaboralExperience
from swagger_server.models.education import Education
from swagger_server.models.section import Section
from swagger_server.models.certification import Certification
from swagger_server.data.DBConnection import DBConnection
from http import HTTPStatus
from flask_jwt_extended import jwt_required
from swagger_server.data.db import Media, Independiente, Usuario, Experiencialaboral, Educacion, Seccion, Certificacion,database
from peewee import DoesNotExist
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

@jwt_required()
def get_independint_user_by_id(user_id):  # noqa: E501
    """Get user by user id

     # noqa: E501

    :param user_id: Unique identifier of the user
    :type user_id: int

    :rtype: IndependientUser
    """
    response = Response(status=HTTPStatus.NOT_FOUND.value)
    database.connect()
    try:
        retrieveIndependientUser = Independiente.get(Independiente.usuariocorreo == user_id)
        independientUser = IndependientUser()
        independientUser.surnames = retrieveIndependientUser.apellidos
        independientUser.persoanl_description = retrieveIndependientUser.descripcionpersonal
        independientUser.name = retrieveIndependientUser.nombre
        independientUser.ocupation = retrieveIndependientUser.ocupacion

        retrieveGeneralUser = Usuario.get_by_id(retrieveIndependientUser.Usuariocorreo)
        generalUser = User()
        generalUser.city = retrieveGeneralUser.ciudad
        generalUser.email = retrieveGeneralUser.correo
        generalUser.country = retrieveGeneralUser.pais
        generalUser.user_id = retrieveGeneralUser.usuariocorreo

        retrievedPerfilPhoto = Media.get_by_id(retrieveGeneralUser.fotoperfil)
        profilePhoto = MediaModels()
        profilePhoto.file = retrievedPerfilPhoto.file
        generalUser.profile_photo = profilePhoto
        independientUser.user = generalUser
        
        #Recuperacion de experiencias laborales del usuario
        retrieveLaboralExperienice_list = Experiencialaboral.select().where(Experiencialaboral.independiente == retrieveIndependientUser.independiente_id)
        if retrieveLaboralExperienice_list.exists():
            laboralExperiencie_list = []
            for laboralExperience in retrieveLaboralExperienice_list:
                laboralExperience_aux = LaboralExperience()
                laboralExperience_aux.current_job = laboralExperience.cargoactual
                laboralExperience_aux.end_date = laboralExperience.fechafin.strftime("%Y-%m-%d")
                laboralExperience_aux.start_date = laboralExperience.fechainicio.strftime("%Y-%m-%d")
                laboralExperience_aux.company_name = laboralExperience.nombreempresa
                laboralExperience_aux.sector = laboralExperience.sector
                laboralExperience_aux.job_category = laboralExperience.tipoempleo
                laboralExperience_aux.job_title = laboralExperience.titulo
                laboralExperience_aux.location = laboralExperience.ubicacion
                laboralExperience_aux.laboral_experience_id = laboralExperience.experiencialaboral_id
                laboralExperiencie_list.append(laboralExperience_aux)
            independientUser.laboral_experience = laboralExperiencie_list

        #Recuperacion de educacion del ususario
        retrieveEducation_list = Educacion.select().where(Educacion.independiente == retrieveIndependientUser.independiente_id)
        if retrieveEducation_list.exists():
            education_list = []
            for education in retrieveEducation_list:
                education_aux = Education()
                education_aux.description = education.descripcion
                education_aux.discipline = education.disciplina
                education_aux.end_date = education.fechafin.strftime("%Y-%m-%d")
                education_aux.start_date = education.fechainicio.strftime("%Y-%m-%d")
                education_aux.average = education.promedio
                education_aux.title = education.titulo
                education_aux.university = education.universidad
                education_aux.education_id = education.educacion_id
                education_list.append(education_aux)
            independientUser.education = education_list
        
        #Recuperacion de certificacion del ususario
        retrieveCertification_list = Certificacion.select().where(Certificacion.independiente == retrieveIndependientUser.independiente_id)
        if retrieveCertification_list.exists():
            certification_list = []
            for certification in retrieveCertification_list:
                certification_aux = Certification()
                certification_aux.credential_url = certification.credencialurl
                certification_aux.issuing_company = certification.empresaemisora
                certification_aux.expiration_date = certification.fechacaducidad.strftime("%Y-%m-%d")
                certification_aux.expedition_date = certification.fechaexpedicion.strftime("%Y-%m-%d")
                certification_aux.title = certification.titulo
                certification_aux.credential_id = certification.certificacion_id
                certification_list.append(certification_aux)
            independientUser.certification = certification_list

        #Recuperacion de seccion del ususario
        retrieveSection_list = Seccion.select().where(Seccion.independiente == retrieveIndependientUser.independiente_id)
        if retrieveSection_list.exists():
            section_list = []
            for section in retrieveSection_list:
                section_aux = Section()
                section_aux.title = section.titulo
                section_aux.description = section.descripcion
                section_aux.section_id = section.seccion_id

                retrieveSectionMedia_list = Media.select().where(Media.seccion == section.seccion_id)
                if retrieveSectionMedia_list.exists():
                    media_list = []
                    for media in retrieveSectionMedia_list:
                        media_aux = MediaModels()
                        media_aux.file = media.file
                        media_list.append(media_aux)
                    section_aux.media = media_list
                section_list.append(section_aux)
            independientUser.section = section_list

        independientUser_json = IndependientUser.to_dict(independientUser)
        response = Response(json.dumps(independientUser_json),status=HTTPStatus.OK.value,mimetype="application/json")
    except DoesNotExist:
        response = Response(status=HTTPStatus.NOT_FOUND.value)
    finally:
        database.close()      
    return response

def register_indpendient_user(body):  # noqa: E501
    """Register independient user

     # noqa: E501

    :param body: Independient user object to register
    :type body: dict | bytes

    :rtype: None
    """
    response = Response(status=HTTPStatus.UNAUTHORIZED.value)
    if connexion.request.is_json:
        body = IndependientUser.from_dict(connexion.request.get_json())  # noqa: E501
        query = "SELECT Usuariocorreo FROM Usuario WHERE Usuariocorreo = %s"
        param = [body.user.email]
        connection = DBConnection()
        list_accounts = connection.select(query, param)
        if list_accounts:
            return response
        else:
            token = tokenGenerator()
            postedUser = Usuario.create(ciudad = body.user.city, contrasenia = body.user.password, correo = body.user.email,
            pais = body.user.country, usuariocorreo = body.user.email, validationtoken = token, validated = 0)

            postedMedia = Media()
            postedMedia.file = body.user.profile_photo.file
            postedMedia.usuariocorreo = body.user.email
            postedMedia.save()

            postedUser.fotoperfil = postedMedia.media_id
            postedUser.save()
        
            Independiente.create(apellidos = body.surnames, aptitud = 'Creatividad', descripcionpersonal = body.persoanl_description,
            nombre = body.name, ocupacion = body.ocupation, usuariocorreo = body.user.email)

            fullname = body.name + " " + body.surnames                      
            send_validationToken_email(body.user.email, fullname, token)

            response = Response(status=HTTPStatus.OK.value)
    return response

'''def send_validationToken_email(userEmail, userName):
	return requests.post(
		"https://api.mailgun.net/v3/sandboxe17ae3d14f484f0d8ed709818d484ebb.mailgun.org/messages",
		auth=("api", "b459a7a1da10092fb8a95fd81e4fa891-90ac0eb7-9d025828"),
		data={
            "from": "mailgun@sandboxe17ae3d14f484f0d8ed709818d484ebb.mailgun.org",
			"to": userEmail,
			"subject": "Prueba de email",
			"text": "Bienvenido a Employex " + userName})'''

def send_validationToken_email(userEmail, userName, token):
    employexEmail = "employexapp@gmail.com"
    message = MIMEMultipart("plain")
    message["From"] = "employexapp@gmail.com"
    message["To"] = userEmail
    message["Subject"] = "Codigo de verificación Employex"
    body = "Bienvenido a Employex " + userName + ", su código de verificacion es: " + token
    body = MIMEText(body)
    message.attach(body)

    smtp = SMTP("smtp.gmail.com")
    smtp.starttls()
    smtp.login(employexEmail, "Jinchuriki2k")
    smtp.sendmail(employexEmail, userEmail, message.as_string())
    smtp.quit()

def tokenGenerator():
    token = ''
    for x in range (0,3):
        token = token + random.choice(string.digits)
        token = token + random.choice(string.ascii_lowercase)
    return token