Feature: Project
 Scenario: 1- Consulto y hay proyectos existentes - get_all_projects
    Given soy usuario del modulo proyectos y hay proyectos existentes
    When consulto los proyectos
    Then el sistema carga un listado de todos los proyectos de PSA con los campos: Nombre del proyecto, Cliente, producto,version,customizacion, fecha de inicio, fecha de cierre,Estado, Horas consumidas, Costo del proyecto, y listado de Tareas

Scenario: 2- Consulto y no hay proyectos existentes - get_all_projects
    Given soy usuario del modulo proyectos y no hay proyectos existentes
    When consulto los proyectos
    Then el sistema no muestra ningún proyecto y se visualiza el mensaje "Aún no hay proyectos creados. Seleccione agregar para crear uno nuevo" 
 
















