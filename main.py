"""Importation des modules nécessaires"""
import matplotlib.pyplot as plt
from decorators import my_decorator


@my_decorator
def fibonacci_sequence(nb_iterations=None, nb_maximum=None):
    """
    Création de la suite de fibonacci

    Args:
        nb_iterations (int): Nombre d'itération
        nb_maximum (int): Nombre maximum pour la suite de fibonacci

    Returns:
        fibo_sequence (list): Suite de fibonacci
    """
    fibo_sequence = []
    a = 0
    b = 1
    if nb_iterations is not None:
        for _ in range(nb_iterations):
            a, b = b, a + b
            fibo_sequence.append(a)  # Ajoute le nombre à la suite de fibo
    elif nb_maximum is not None:
        while a <= nb_maximum:
            a, b = b, a + b
            fibo_sequence.append(a)

    return fibo_sequence


def create_file(fibo_sequence, filename):
    """
    Création d'un fichier texte avec la suite de fibonacci

    Args:
        fibo_sequence (list): La suite de fibonacci
        filename (str): Le nom du fichier dans lequel la suite sera
            sauvegardée
    """
    with open(filename, 'w', encoding="utf-8") as file:
        for i in fibo_sequence:
            file.write(f"{i} \n")


def fibonacci_spiral(fibo_sequence, fibo_img):
    """
    Création d'une image avec la suite de fibo

    Args:
        fibo_sequence (list): La suite de fibonacci
        fibo_img (str): Le nom du fichier image dans lequel
            la spirale sera sauvegardée
    """
    plt.figure(figsize=(12, 12))
    x, y = 0, 0  # Cordonnées de départ de la spirale

    for i, fibo_seq in enumerate(fibo_sequence):
        if i % 4 == 0:  # déplacement à droite
            x_new, y_new = x + fibo_seq, y
        elif i % 4 == 1:  # déplacement en haut
            x_new, y_new = x, y + fibo_seq
        elif i % 4 == 2:  # déplacement à gauche
            x_new, y_new = x - fibo_seq, y
        else:  # déplacement en bas
            x_new, y_new = x, y - fibo_seq

        plt.plot([x, x_new], [y, y_new], 'r')
        x, y = x_new, y_new

    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('Fibonacci')
    plt.savefig(fibo_img)
    plt.show()


if __name__ == "__main__":
    seq = fibonacci_sequence(nb_iterations=10)
    FIBO_FILE = "fibo_sequence.txt"
    create_file(seq, FIBO_FILE)
    FIBO_IMAGE = "fibo_img.png"
    fibonacci_spiral(seq, FIBO_IMAGE)
