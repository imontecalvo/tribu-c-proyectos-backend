Feature: Task

    Scenario: 1- Visualización correcta del detalle de una tarea - get_task
        Given el usuario del módulo del proyecto quiere visualizar los detalles de una tarea
        When selecciona una tarea
        Then el sistema muestra la siguiente información de la tarea seleccionada: id, titulo, descripción, tiempoEstimadoDeFinalizacion, HorasAcumulados, responsable y Estado