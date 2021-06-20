import connexion
import json

from flask import Response
from swagger_server.models.independient_user import IndependientUser  # noqa: E501
from swagger_server.models.user import User
from swagger_server.models.media import Media as MediaModels
from swagger_server.models.laboral_experience import LaboralExperience
from swagger_server.models.education import Education
from swagger_server.models.section import Section
from swagger_server.models.certification import Certification
from http import HTTPStatus
from flask_jwt_extended import jwt_required
from swagger_server.data.db import Media, Independiente, Usuario, Experiencialaboral, Educacion, Seccion, Certificacion,database
from peewee import DoesNotExist
from swagger_server.controllers.general_user_controller import send_validationToken_email, tokenGenerator

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

        try:
            retrievedPerfilPhoto = Media.get_by_id(retrieveGeneralUser.fotoperfil)
            profilePhoto = MediaModels()
            profilePhoto.file = retrievedPerfilPhoto.file
            generalUser.profile_photo = profilePhoto
        except DoesNotExist:
            generalUser.profile_photo = None
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
        try:
            list_accounts = Independiente.get_by_id(body.user.email)
            return Response(status=HTTPStatus.CONFLICT.value)
        except DoesNotExist:
            token = tokenGenerator()
            postedUser = Usuario.create(ciudad = body.user.city, contrasenia = body.user.password, correo = body.user.email,
            pais = body.user.country, usuariocorreo = body.user.email, validationtoken = token, validated = 0)

            postedMedia = Media()
            if body.user.profile_photo.file:
                postedMedia.file = body.user.profile_photo.file
            postedMedia.usuariocorreo = body.user.email
            postedMedia.save()

            postedUser.fotoperfil = postedMedia.media_id
            postedUser.save()
        
            Independiente.create(apellidos = body.surnames, aptitud = 'Creatividad', descripcionpersonal = body.persoanl_description,
            nombre = body.name, ocupacion = body.ocupation, usuariocorreo = body.user.email)

            fullname = body.name + " " + body.surnames                      
            send_validationToken_email(body.user.email, fullname, token)

            response = Response(status=HTTPStatus.CREATED.value)
    return response


@jwt_required()
def patch_independint_user_by_id(body, user_id):  # noqa: E501
    """Patch user by id

     # noqa: E501

    :param body: Independient user object to patch
    :type body: dict | bytes
    :param user_id: Unique identifier of the user
    :type user_id: str

    :rtype: None
    """
    response = Response(status=HTTPStatus.UNAUTHORIZED.value)
    database.connect()
    if connexion.request.is_json:
        body = IndependientUser.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            retrieveIndependientUser = Independiente.get(Independiente.usuariocorreo == user_id)
            retrieveGeneralUser = Usuario.get_by_id(user_id)
            retrieveMedia = Media.get((Media.usuariocorreo == user_id) & (Media.seccion.is_null(True)) & (Media.ofertadetrabajo.is_null(True)))
            retrieveGeneralUser.ciudad = body.user.city
            retrieveGeneralUser.pais = body.user.country
            retrieveIndependientUser.nombre = body.name
            retrieveIndependientUser.apellidos = body.surnames
            retrieveIndependientUser.ocupacion = body.ocupation
            retrieveIndependientUser.descripcionpersonal = body.persoanl_description
            retrieveMedia.file = body.user.profile_photo.file
            retrieveIndependientUser.save()
            retrieveGeneralUser.save()
            retrieveMedia.save()
            response = Response(status=HTTPStatus.OK.value)
        except DoesNotExist:
            response = Response(status=HTTPStatus.NOT_FOUND.value)
        finally:
            database.close()
    return response