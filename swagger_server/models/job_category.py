# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class JobCategory(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    CARPINTERO = "CARPINTERO"
    CERRAJERO = "CERRAJERO"
    MECANICO = "MECANICO"
    OBRERO = "OBRERO"
    FONTANERO = "FONTANERO"
    SOLDADOR = "SOLDADOR"
    ARTISTA = "ARTISTA"
    SASTRE = "SASTRE"
    AGRIGULTOR = "AGRIGULTOR"
    COCINERO = "COCINERO"
    REPARTIDOR = "REPARTIDOR"
    SEGURIDAD = "SEGURIDAD"
    ESTILISTA = "ESTILISTA"
    EXTERMINADOR = "EXTERMINADOR"
    CAMARERO = "CAMARERO"
    CONDUCTOR = "CONDUCTOR"
    ELECTRICISTA = "ELECTRICISTA"
    FOTOGRAFO = "FOTOGRAFO"
    CASERO = "CASERO"
    JARDINERO = "JARDINERO"
    VENDEDOR = "VENDEDOR"
    DENTISTA = "DENTISTA"
    ENFERMERO = "ENFERMERO"
    DOCTOR = "DOCTOR"
    EMPRESARIO = "EMPRESARIO"
    DEPORTISTA = "DEPORTISTA"
    ADMINISTRADOR = "ADMINISTRADOR"
    SECRETARIO = "SECRETARIO"
    SOLDADO = "SOLDADO"
    CIENTIFICO = "CIENTIFICO"
    PROFESOR = "PROFESOR"
    POLICIA = "POLICIA"
    GERENTE = "GERENTE"
    BOMBERO = "BOMBERO"
    INGENIERO = "INGENIERO"
    ARQUITECTO = "ARQUITECTO"
    PERIODISTA = "PERIODISTA"
    BIBLIOTECARIO = "BIBLIOTECARIO"
    ABOGADO = "ABOGADO"
    OTRO = "OTRO"
    def __init__(self):  # noqa: E501
        """JobCategory - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'JobCategory':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The JobCategory of this JobCategory.  # noqa: E501
        :rtype: JobCategory
        """
        return util.deserialize_model(dikt, cls)