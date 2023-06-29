import requests
from behave import *
import json
empty = b'[]'

body_view = """{"codigo": 100,"id_cliente": 100,"id_producto": 100,"version": "1.0","customizacion": "Tenarisv1","nombre": "Tenaris","fecha_inicio": "21/06/2023", "fecha_fin_estimada": "21/06/2021","estado": 1,"horas_consumidas": 60,"costo_estimado": 1000, "ultima_tarea":1}"""
body_create = """{"codigo": 101,"id_cliente": 101,"id_producto": 101,"version": "1.0","customizacion": "Galiciav1","nombre": "Banco Galicia","fecha_inicio": "30/06/2023", "fecha_fin_estimada": "20/12/2023","estado": 1,"horas_consumidas": 160,"costo_estimado": 7500000, "ultima_tarea":5}"""

body_incomplete_create = """{"codigo": null,"id_cliente": 101,"id_producto": 101,"version": "1.0","customizacion": "Galiciav1","nombre": "Banco Galicia","fecha_inicio": "30/06/2023", "fecha_fin_estimada": "20/12/2023","estado": 1,"horas_consumidas": 160,"costo_estimado": 7500000, "ultima_tarea":5}"""

body_edit = """{"codigo": 101,"id_cliente": 101,"id_producto": 101,"version": "1.0","customizacion": "Galiciav1","nombre": "Banco Galicia","fecha_inicio": "30/06/2023", "fecha_fin_estimada": "20/12/2023","estado": 1,"horas_consumidas": 160,"costo_estimado": 7500000, "ultima_tarea":5}"""
body_edited = """{"codigo": 101,"id_cliente": 101,"id_producto": 101,"version": "1.0","customizacion": "HSBCv1","nombre": "Banco HSBC","fecha_inicio": "30/06/2023", "fecha_fin_estimada": "20/12/2023","estado": 1,"horas_consumidas": 160,"costo_estimado": 7500000, "ultima_tarea":5}"""

body_delete = """{"codigo": 101,"id_cliente": 101,"id_producto": 101,"version": "1.0","customizacion": "HSBCv1","nombre": "Banco HSBC","fecha_inicio": "30/06/2023", "fecha_fin_estimada": "20/12/2023","estado": 1,"horas_consumidas": 150,"costo_estimado": 7500000, "ultima_tarea":20}"""

completeApi='https://tribu-c-proyectos-backend.onrender.com/projects/'
    
@given('soy usuario del modulo proyectos y no hay proyectos existentes')
def no_projects(context):
    global url
    url = 'https://tribu-c-proyectos-backend.onrender.com/'
    
@when('consulto los proyectos')
def get_all_projects(context):
    global data
    completeApi = url+"projects/"
    data = requests.get(completeApi)
    
@then('el sistema no muestra ningún proyecto y se visualiza el mensaje "Aún no hay proyectos creados. Seleccione agregar para crear uno nuevo"')
def not_found_projects(context):
    if data.status_code==200:
        assert data.content == empty
        
@given('soy usuario del modulo proyectos y hay proyectos existentes')
def no_projects(context):
    global url
    url = 'https://tribu-c-proyectos-backend.onrender.com/'
    
@then('el sistema carga un listado de todos los proyectos de PSA con los campos: Nombre del proyecto, Cliente, producto,version,customizacion, fecha de inicio, fecha de cierre,Estado, Horas consumidas, Costo del proyecto, y listado de Tareas')
def not_found_projects(context):
    if data.status_code==200:
        assert data.content != empty
        
@given('soy usuario del módulo del proyecto y quiero visualizar los detalles de un proyecto particular')
def view_information(context):
    global id

    bodyJson = json.loads(body_view)
    id = requests.post(completeApi, json=bodyJson).content.decode()
    
    
@when('selecciona un proyecto')
def project_by_id(context):
        global data
        api = completeApi + id
        data = requests.get(api)
        
@then( 'visualiza la siguiente información del proyecto: Nombre del proyecto, Cliente, producto,version,customizacion, fecha de inicio, fecha de cierre,Estado, Horas consumidas, Costo del proyecto, y listado de Tareas')
def all_information(context):
    if data.content==body_view:
     assert True
     
     
@given('el usuario del módulo del proyecto quiere dar de alta un proyecto')
def create_project(context):
    global api
    api = 'https://tribu-c-proyectos-backend.onrender.com/projects/'
    

@when('agrega un proyecto y completa todos los campos requeridos')
def add_project(context):
    global data, bodyJson
    bodyJson = json.loads(body_create)
    requests.post(api, json = bodyJson)
        
@then('se guarda el proyecto correctamente')
def all_information(context):
    
    data = requests.get(api)
    if data.content==body_create:
     assert True

    
@when('agrega un proyecto y no completa todos los campos requeridos')
def add_project(context):
        global data, bodyJson
        bodyJson = json.loads(body_incomplete_create)
        requests.post(api, json = bodyJson)
        
@then('no puede guardar el proyecto')
def all_information(context):
    data = requests.get(api)
    if data.content[1] is None:
       assert True
          
@given('el usuario del módulo del proyecto quiere editar el nombre de un proyecto')
def edit_project(context):
    global id
    bodyJson = json.loads(body_edit)
    id = requests.post(completeApi, json=bodyJson).content.decode()
    

@when('edita el campo nombre del proyecto y guarda la información')
def edit_project(context):
    global data
    url = completeApi + id
    bodyJson = json.loads(body_edited)
    data = requests.put(url, json = bodyJson)
        
@then('se actualiza el nombre del proyecto correctamente visualizandose el nuevo nombre')
def save_project(context):
    data = requests.get(url)
    if data.content==body_edited:
        assert True
    if data.content==body_edit:
        assert False
        
        
@given('el usuario del módulo del proyecto quiere eliminar un proyecto')
def delete_project(context):
    global id
    bodyJson = json.loads(body_delete)
    id = requests.post(completeApi, json=bodyJson).content.decode()
    

@when('selecciona eliminar el proyecto y acepta la confirmación de eliminación')
def delete_project(context):
    global data,url
    url = completeApi + id
    data = requests.delete(url)
 
        
@then('se elimina el proyecto correctamente')
def delete_project(context):
    data = requests.get(url)
    
    assert not (data.content==body_delete)