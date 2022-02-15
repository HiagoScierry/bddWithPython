# language: pt

Funcionalidade: Mapear areas

Cenário: Mapear mapa de acordo com o planejado
    Dado que entrei no site do "globalforestwatch"
    Quando remover aviso de cookies
        E remover modal
        E clicar em "forest change"
        E clicar em "Alertas de desmatamento (GLAD)"
        E clicar em "Alertas de desmatamento (RADD)"
    Então o mapa sera renderizado corretamente