from tareas.gestor import GestorTareas


def test_listar_ordena_por_prioridad_y_luego_por_id():
    gestor = GestorTareas()
    gestor.agregar("Baja", prioridad="baja")
    gestor.agregar("Alta", prioridad="alta")
    gestor.agregar("Media", prioridad="media")
    gestor.agregar("Otra alta", prioridad="alta")
    titulos = [t.titulo for t in gestor.listar()]
    assert titulos == ["Alta", "Otra alta", "Media", "Baja"]


def test_listar_filtra_por_prioridad():
    gestor = GestorTareas()
    gestor.agregar("Alta", prioridad="alta")
    gestor.agregar("Baja", prioridad="baja")
    titulos = [t.titulo for t in gestor.listar(prioridad="alta")]
    assert titulos == ["Alta"]


def test_listar_sin_tareas_devuelve_lista_vacia():
    gestor = GestorTareas()
    assert gestor.listar() == []
