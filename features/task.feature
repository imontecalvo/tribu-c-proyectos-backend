Scenario: 1- Visualización correcta de los campos requeridos para la tarea - get_task_by_id
	Given el usuario del módulo del proyecto 
    When accede a un proyecto y selecciona crear una tarea
    Then visualiza un modal con los campos requeridos para completar.

Scenario: 2- Creación exitosa de la tarea - create_task
	Given el usuario del módulo del proyecto 
    When completa todos los campos requeridos de la tarea: id, titulo, descripción, tiempoEstimadoDeFinalizacion, HorasAcumulados, nombreDelResponsable, tickets y Estado y guarda los cambios
    Then se crea la tarea correctamente con estado No iniciada y se visualiza dentro del proyecto.

Scenario: 3- Creación no exitosa de la tarea - create_task
	Given el usuario del módulo del proyecto 
    When completa todos los campos requeridos de la tarea: id, titulo, descripción, tiempoEstimadoDeFinalizacion, HorasAcumulados y Estado y no guarda los cambios
    Then no se crea la tarea y no se visualiza ningún cambio dentro del proyecto.

Scenario: 4- Edición exitosa de la descripcion de una tarea - edit_task
	Given el usuario del módulo del proyecto quiere editar el titulo de una tarea particular.
    When completa el titulo y guarda la información
    Then se actualiza el titulo de la tarea correctamente.

Scenario: 5- Edición exitosa del estado ‘No iniciada’ a ‘Iniciada’ de una tarea - edit_task
	Given el usuario del módulo del proyecto quiere editar el estado de una tarea particular.
    When selecciona la opción ‘Iniciada’ y guarda la información
    Then se actualiza el estado de la tarea correctamente.

Scenario: 6- Edición exitosa del estado ‘Iniciada’ a ‘Finalizada’ de una tarea.
	Given el usuario del módulo del proyecto quiere editar el estado de una tarea particular - edit_task
    When selecciona la opción ‘Finalizada’ y guarda la información
    Then se actualiza el estado de la tarea correctamente.

Scenario: 7- Edición exitosa del estado ‘Finalizada’ a ‘No iniciada’ de una tarea - edit_task
	Given el usuario del módulo del proyecto quiere editar el estado de una tarea particular.
    When selecciona la opción ‘No iniciada’ y guarda la información
    Then se actualiza el estado de la tarea correctamente.

Scenario: 8- Edición exitosa de la descripcion de una tarea - edit_task
	Given el usuario del módulo del proyecto quiere editar la descripcion de una tarea particular.
    When completa la descripcion y guarda la información
    Then se actualiza la descripcion de la tarea correctamente.


Scenario: 9- Visualización correcta del detalle de una tarea - get_task_by_id
	Given el usuario del módulo del proyecto quiere visualizar los detalles de una tarea particular 
    When selecciona dicha tarea
    Then visualiza la siguiente información de la tarea seleccionada: id, titulo, descripción, tiempoEstimadoDeFinalizacion, HorasAcumulados,  nombreDelResponsable, tickets y Estado.

Scenario: 10- Eliminación exitosa de una tarea - delete_task
    Given el usuario del módulo del proyecto quiere eliminar una tarea de un proyecto particular.
    When selecciona eliminar la tarea y acepta la confirmación de eliminación
    Then se elimina la tarea del proyecto correctamente y se deja de visualizar en el listado de tareas dentro del proyecto.

Scenario: 11- Eliminación no exitosa de una tarea - delete_task
    Given el usuario del módulo del proyecto quiere eliminar una tarea de un proyecto particular.
    When selecciona eliminar la tarea y no acepta la confirmación de eliminación
    Then no se elimina el tarea del proyecto visualizándose en el listado de tareas del proyectos
