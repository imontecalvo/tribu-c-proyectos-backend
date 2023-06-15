Feature: Project

  Scenario: 1- Consulto y hay proyectos existentes - get_all_projects
    Given soy usuario del modulo proyectos y hay proyectos existentes
    When consulto el listado de los proyectos
    Then el sistema carga un listado de todos los proyectos de PSA con los campos: Nombre del proyecto, Cliente, producto,version,customizacion, fecha de inicio, fecha de cierre,Estado, Horas consumidas, Costo del proyecto, y listado de Tareas


 Scenario: 2- Consulto y no hay proyectos existentes - get_all_projects
    Given soy usuario del modulo proyectos y no hay proyectos existentes
    When consulto los proyectos
    Then el sistema no muestra ningún proyecto y se visualiza el mensaje "Aún no hay proyectos creados. Seleccione agregar para crear uno nuevo" 


Scenario: 3- Visualizacion correcta de campos requeridos al crear un proyecto - add_project
    Given el usuario del modulo del proyecto quiere dar de alta un proyecto
    When agrega un proyecto
    Then el sistema carga una pantalla del proyecto para completar los campos requeridos básicos: Nombre del proyecto, Cliente, producto,version,customizacion, fecha de inicio, fecha de cierre,Estado, Horas consumidas, Costo del proyecto

Scenario: 4- Creacion de proyecto exitosa - add_project
    Given el usuario del módulo del proyecto quiere dar de alta un proyecto
    When agrega un proyecto y completa todos los campos requeridos
    Then puede guardar el proyecto correctamente y se visualiza en el listado de proyectos en la última fila.

Scenario: 5- Creacion de proyecto no exitosa - add_project
    Given el usuario del módulo del proyecto quiere dar de alta un proyecto
    When agrega un proyecto y no completa todos los campos requeridos
    Then no puede guardar el proyecto

Scenario: 6- Visualización correcta del detalle de un proyecto - get_project
	Given el usuario del módulo del proyecto quiere visualizar los detalles de un proyecto particular.
    When selecciona un proyecto 
    Then visualiza la siguiente información del proyecto: Nombre del proyecto, Cliente, producto,version,customizacion, fecha de inicio, fecha de cierre,Estado, Horas consumidas, Costo del proyecto, y listado de Tareas
********************
Scenario: 7- Edición exitosa del nombre de un proyecto - update_project
	Given el usuario del módulo del proyecto quiere editar el nombre de un proyecto particular con caracteres válidos
    When edita el campo nombre del proyecto y guarda la información
    Then se actualiza el nombre del proyecto correctamente visualizandose el nuevo nombre.

Scenario: 8- Edición exitosa de la fecha de inicio del proyecto - update_project
	Given el usuario del módulo del proyecto quiere editar la fecha de inicio un proyecto particular con fecha válida.
    When edita el campo fecha de inicio del proyecto y guarda la información
    Then se actualiza la fecha de inicio del proyecto correctamente visualizandose la nueva fecha.

Scenario: 9- Edición exitosa de la fecha de cierre del proyecto - update_project
	Given el usuario del módulo del proyecto quiere editar la fecha de fin de un proyecto particular con fecha válida.
Cuando: edita el campo fecha de cierre del proyecto y guarda la información
Entonces: se actualiza la fecha de cierre del proyecto correctamente visualizandose la nueva fecha.

Scenario: 10- Edición exitosa del cliente de un proyecto - update_project
	Given el usuario del módulo del proyecto quiere editar el nombre del cliente de un proyecto particular con caracteres válidos.
    When edita el campo cliente del proyecto y guarda la información
    Then se actualiza el nombre del cliente del proyecto correctamente.


Scenario: 11- Eliminación exitosa de un proyecto - delete_project
    Given el usuario del módulo del proyecto quiere eliminar un proyecto particular.
    When selecciona eliminar el proyecto y acepta la confirmación de eliminación
    Then se elimina el proyecto correctamente y se deja de visualizar en el listado de proyectos.

Scenario: 12- Eliminación no exitosa de un proyecto - delete_project
    Given el usuario del módulo del proyecto quiere eliminar un proyecto particular.
    When selecciona eliminar el proyecto y no acepta la confirmación de eliminación
    Then no se elimina el proyecto visualizándose en el listado de proyectos.

























