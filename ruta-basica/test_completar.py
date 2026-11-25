import pytest

from tareas.gestor import GestorTareas, TareaNoEncontrada


def test_completar_marca_la_tarea():
    gestor = GestorTareas()
    tarea = gestor.agregar("Entregar la práctica")
    gestor.completar(tarea.id)
    assert tarea.completada is True


def test_listar_separa_pendientes_y_completadas():
    gestor = GestorTareas()
    hecha = gestor.agregar("Hecha")
    gestor.agregar("Pendiente")
    gestor.completar(hecha.id)
    assert [t.titulo for t in gestor.listar(estado="completadas")] == ["Hecha"]
    assert [t.titulo for t in gestor.listar(estado="pendientes")] == ["Pendiente"]


def test_completar_id_inexistente_lanza_error():
    gestor = GestorTareas()
    with pytest.raises(TareaNoEncontrada):
        gestor.completar(99)
