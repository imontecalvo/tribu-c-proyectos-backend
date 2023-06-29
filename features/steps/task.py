
import requests
from behave import *
import json
empty = b'[]'

body_view = """{"id_tarea : 20,"id_proyecto": 1,"titulo":"Proyecto OSDE","descripcion": "Proyecto de salud destinado a la prepaga OSDE","tiempo_estimado_finalizacion :1250,"horas_acumuladas": 900,"estado": 1, "legajo_responsable":12}"""

        
@given('el usuario del módulo del proyecto quiere visualizar los detalles de una tarea')
def no_projects(context):
    global url
    url = 'https://tribu-c-proyectos-backend.onrender.com/'
    
@when('selecciona una tarea')
def get_all_tasks(context):
    global data
    completeApi = url+"projects/"+"1/"+"tasks/"
    data = requests.get(completeApi)
    
@then('el sistema muestra la siguiente información de la tarea seleccionada: id, titulo, descripción, tiempoEstimadoDeFinalizacion, HorasAcumulados, responsable y Estado')
def get_all_tasks(context):
    if data.status_code==200:
        assert data.content != empty