import requests
from behave import *
import json
empty = b'[]'

body = """{"version": "1.0","customizacion": "Tenarisv1","nombre": "Tenaris","fecha_inicio": "21/06/2023", "fecha_fin_estimada": "21/06/2021","estado": 1,"horas_consumidas": 60,"costo_estimado": 1000, "ultima_tarea":1}"""

    
@given('soy usuario del modulo proyectos y no hay proyectos existentes')
def no_projects(context):
    global apiUrl
    apiUrl = 'https://tribu-c-proyectos-backend.onrender.com/'
    
@when('consulto los proyectos')
def get_all_projects(context):
    global data
    completeApi = apiUrl+"projects/"
    data = requests.get(completeApi)
    
@then('el sistema no muestra ningún proyecto y se visualiza el mensaje "Aún no hay proyectos creados. Seleccione agregar para crear uno nuevo"')
def not_found_projects(context):
    if data.status_code==200:
        assert data.content == empty
        
@given('soy usuario del modulo proyectos y hay proyectos existentes')
def no_projects(context):
    global apiUrl
    apiUrl = 'https://tribu-c-proyectos-backend.onrender.com/'
    
@then('el sistema carga un listado de todos los proyectos de PSA con los campos: Nombre del proyecto, Cliente, producto,version,customizacion, fecha de inicio, fecha de cierre,Estado, Horas consumidas, Costo del proyecto, y listado de Tareas')
def not_found_projects(context):
    if data.status_code==200:
        assert data.content != empty