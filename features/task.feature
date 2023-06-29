Feature: Task

    Scenario: 1- Visualización del listado de tareas de un proyecto - get_all_task
        Given el usuario del módulo del proyecto quiere visualizar la lista de tareas
        When ingresa a un proyecto
        Then el sistema muestra las tareas contenidas en el proyecto

    Scenario: 2- Visualización correcta de una tarea - get_task
        Given el usuario del módulo del proyecto quiere visualizar los detalles de una tarea 
        When selecciona una tarea
        Then el sistema muestra la siguiente información de la tarea seleccionada: id, titulo, descripción, tiempoEstimadoDeFinalizacion, HorasAcumulados, responsable y Estado

    Scenario: 3- Creación exitosa de la tarea - add_task
	    Given el usuario del módulo del proyecto desea agregar una tarea nueva
        When completa todos los campos requeridos de la tarea: id, titulo, descripción, tiempoEstimadoDeFinalizacion, HorasAcumulados, responsable y Estado y guarda los cambios
        Then se crea la tarea correctamente con estado No iniciada