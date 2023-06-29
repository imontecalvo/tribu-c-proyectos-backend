Feature: Project
 Scenario: 1- Consulto y hay proyectos existentes - get_all_projects
    Given soy usuario del modulo proyectos y hay proyectos existentes
    When consulto los proyectos
    Then el sistema carga un listado de todos los proyectos de PSA con los campos: Nombre del proyecto, Cliente, producto,version,customizacion, fecha de inicio, fecha de cierre,Estado, Horas consumidas, Costo del proyecto, y listado de Tareas

Scenario: 2- Consulto y no hay proyectos existentes - get_all_projects
    Given soy usuario del modulo proyectos y no hay proyectos existentes
    When consulto los proyectos
    Then el sistema no muestra ningún proyecto y se visualiza el mensaje "Aún no hay proyectos creados. Seleccione agregar para crear uno nuevo" 
 
Scenario: 3- Visualización correcta del detalle de un proyecto - get_project
    Given soy usuario del módulo del proyecto y quiero visualizar los detalles de un proyecto particular
    When selecciona un proyecto 
    Then visualiza la siguiente información del proyecto: Nombre del proyecto, Cliente, producto,version,customizacion, fecha de inicio, fecha de cierre,Estado, Horas consumidas, Costo del proyecto, y listado de Tareas

Scenario: 4- Creacion de proyecto exitosa - add_project
    Given el usuario del módulo del proyecto quiere dar de alta un proyecto
    When agrega un proyecto y completa todos los campos requeridos
    Then se guarda el proyecto correctamente

Scenario: 5- Creacion de proyecto no exitosa - add_project
    Given el usuario del módulo del proyecto quiere dar de alta un proyecto
    When agrega un proyecto y no completa todos los campos requeridos
    Then no puede guardar el proyecto


Scenario: 6- Edición exitosa del nombre de un proyecto - update_project
	Given el usuario del módulo del proyecto quiere editar el nombre de un proyecto
    When edita el campo nombre del proyecto y guarda la información
    Then se actualiza el nombre del proyecto correctamente visualizandose el nuevo nombre






