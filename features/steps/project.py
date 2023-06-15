import requests
from behave import *
import json


body = """{"nombre": "Tenaris","fecha_inicio": "21/06/2023", "fecha_estimada_fin": "21/06/2021"}"""



@given('Consulto y hay proyectos existentes')
def no_projects(context):
    global apiUrl
    apiUrl = 'hhttps://tribu-c-proyectos-backend.onrender.com/'