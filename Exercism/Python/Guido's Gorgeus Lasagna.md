----

```python
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME_PER_LAYER = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calcula el tiempo de horneado restante.

    :param elapsed_bake_time: tiempo que la lasaña lleva en el horno.
    :return: minutos restantes de horneado.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calcula el tiempo de preparación según el número de capas.

    :param number_of_layers: número de capas de la lasaña.
    :return: minutos totales de preparación.
    """
    return number_of_layers * PREPARATION_TIME_PER_LAYER


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calcula el tiempo total transcurrido preparando y horneando la lasaña.

    :param number_of_layers: número de capas.
    :param elapsed_bake_time: tiempo ya horneado.
    :return: minutos totales transcurridos.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

```

