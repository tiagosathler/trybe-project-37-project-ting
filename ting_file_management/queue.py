from collections import deque
from copy import deepcopy


class Queue:
    """
    Classe que representa a Estrutura de Dados de uma Fila.

    Utiliza a lista bidirecional 'deque' da biblioteca 'collections'
    do Python para implementar a Fila de forma performática. "Deque"
    é a abreviação para "double-ended-queue", ou seja, "fila duplamente
    terminada". É usada de forma segura e eficiente para implementar
    tanto "Pilhas" quanto "Filas".
    (https://docs.python.org/pt-br/3/library/collections.html#collections.deque)

    A Fila é uma estrutura de dados que o utiliza o princípio
    do "First In, First Out" (FIFO).
    """
    def __init__(self) -> None:
        self._data = deque()

    def __len__(self) -> int:
        """
        Representação do tamanho da Fila.
        """
        return len(self._data)

    def is_empty(self) -> bool:
        """
        Método que retorna o booleano se a Fila está vazia.
        """
        return not bool(self._data)

    def enqueue(self, value: dict) -> None:
        """
        Método que enfileira um dicionário à Fila (primeira posição do deque).
        """
        self._data.append(value)

    def dequeue(self) -> dict:
        """
        Método que desenfileira o primeiro dicionário da Fila.
        Retorna o dicionário
        """
        return self._data.popleft()

    def search(self, index: int) -> dict:
        """
        Método que busca o dicionário na posição 'index' da Fila.
        Retorna o dicionário
        """
        if (0 <= index < len(self)):
            return self._data[index]
        else:
            raise IndexError("Index out of bounds")

    def copy(self):
        """
        Método que faz uma cópia profunda e independente da instância.
        Retorna a cópia desta instância de Queue.
        """
        return deepcopy(self)
