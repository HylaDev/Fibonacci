"""Importation de wraps"""
from functools import wraps


def my_decorator(f):
    """Décorateur pour vérifier si les arguments de la
        fonction sont bien passés.

    Args:
        f (function): La fonction à décorer

    Returns:
        f (function): La fonction décorée

    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'nb_iterations' not in kwargs and 'nb_maximum' not in kwargs:
            print("Veuillez renseigner au moins l'un des deux arguments.")
        return f(*args, **kwargs)
    return wrapper
