import pytest

from tareas.gestor import GestorTareas


def test_agregar_asigna_id_y_prioridad_media_por_defecto():
    gestor = GestorTareas()
    tarea = gestor.agregar("Estudiar para el examen")
    assert tarea.id == 1
    assert tarea.titulo == "Estudiar para el examen"
    assert tarea.prioridad == "media"
    assert tarea.completada is False


def test_agregar_incrementa_el_id():
    gestor = GestorTareas()
    gestor.agregar("Primera")
    segunda = gestor.agregar("Segunda")
    assert segunda.id == 2


def test_agregar_quita_espacios_del_titulo():
    gestor = GestorTareas()
    tarea = gestor.agregar("   Lavar los trastes   ")
    assert tarea.titulo == "Lavar los trastes"


def test_agregar_rechaza_titulo_vacio():
    gestor = GestorTareas()
    with pytest.raises(ValueError):
        gestor.agregar("   ")


def test_agregar_rechaza_titulo_de_mas_de_100_caracteres():
    gestor = GestorTareas()
    with pytest.raises(ValueError):
        gestor.agregar("a" * 101)


def test_agregar_rechaza_prioridad_invalida():
    gestor = GestorTareas()
    with pytest.raises(ValueError):
        gestor.agregar("Hacer la tarea", prioridad="urgente")
