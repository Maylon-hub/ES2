from entrega import classificar_entrega

def test_distancia_curta_sem_chuva():
    assert classificar_entrega(40, False) == "baixo"

def test_distancia_longa_sem_chuva():
    assert classificar_entrega(60, False) == "medio"

def test_distancia_curta_com_chuva():
    assert classificar_entrega(40, True) == "alto"

def test_distancia_longa_com_chuva():
    assert classificar_entrega(60, True) == "alto"
