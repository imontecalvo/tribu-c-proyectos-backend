
import requests
from behave import *
import json
empty = b'[]'

body_view = """{"id_tarea : 1,"id_proyecto": 16,"titulo":"Proyecto OSDE","descripcion": "Proyecto de salud destinado a la prepaga OSDE","tiempo_estimado_finalizacion :1250,"horas_acumuladas": 900,"estado": 1, "legajo_responsable":12}"""

body_create = """{"id_tarea : 1,"id_proyecto": 21,"titulo":"Proyecto OSDE","descripcion": "Proyecto de salud destinado a la prepaga OSDE","tiempo_estimado_finalizacion :1250,"horas_acumuladas": 900,"estado": 1, "legajo_responsable":12}"""

        
@given('el usuario del módulo del proyecto quiere visualizar la lista de tareas')
def no_projects(context):
    global url
    url = 'https://tribu-c-proyectos-backend.onrender.com/'
    
@when('ingresa a un proyecto')
def get_all_tasks(context):
    global data
    completeApi = url+"projects/"+"1/"+"tasks/"
    data = requests.get(completeApi)
    
@then('el sistema muestra las tareas contenidas en el proyecto')
def get_all_tasks(context):
    if data.status_code==200:
        assert data.content != empty
        
        
@given('el usuario del módulo del proyecto quiere visualizar los detalles de una tarea')
def view_task(context):
    global id, completeApi
    completeApi = url+"projects/"+"16/"+"tasks/"+"1/"
    bodyJson = json.loads(body_view)
    id = requests.post(completeApi, json=bodyJson).content.decode()
    
@when('selecciona una tarea')
def task_by_id(context):
    global data
    api = completeApi + id
    data = requests.get(api)

    
@then('el sistema muestra la siguiente información de la tarea seleccionada: id, titulo, descripción, tiempoEstimadoDeFinalizacion, HorasAcumulados, responsable y Estado')
def all_information(context):
    assert (data.content==body_view)
    
@given('el usuario del módulo del proyecto desea agregar una tarea nueva')
def add_task(context):
    global completeApi
    completeApi = url+"projects/"+"21/"+"tasks/"
    
    
@when('completa todos los campos requeridos de la tarea: id, titulo, descripción, tiempoEstimadoDeFinalizacion, HorasAcumulados, responsable y Estado y guarda los cambios')
def add_task(context):
  global data, bodyJson
  bodyJson = json.loads(body_create)
  requests.post(completeApi, json = bodyJson)

    
@then('se crea la tarea correctamente con estado No iniciada')
def all_information(context):
    data = requests.get(completeApi)
    assert (data.content==body_create)