from typing import Any, List


class Deque:

    def __init__(self) -> None:
        self.__data: List[Any] = []

    def __repr__(self) -> str:
        return str(self.__data)

    def insert_first(self, elemento: Any) -> None:
        self.__data.insert(0, elemento)

    def insert_last(self, elemento: Any) -> None:
        self.__data.append(elemento)

    def size(self) -> int:
        return len(self.__data)

    def remove_first(self) -> Any:
        if self.is_empty():
            raise IndexError("não é possível remover: a fila está vazia.")
        return self.__data.pop(0)

    def remove_last(self) -> Any:
        if self.is_empty():
            raise IndexError("não é possível remover: a fila está vazia.")
        return self.__data.pop(-1)

    def remove_any(self, elemento: Any) -> Any:
        if self.is_empty():
            raise IndexError("não é possível remover: a fila está vazia.")

        if elemento not in self.__data:
            print("Elemento:", elemento, "não está na lista")
            return

        self.__data.remove(elemento)
        print("Item removido:", elemento)

    def first(self) -> Any:  
        if self.is_empty():
            raise IndexError("Esta vazia")
        return self.__data[0]

    def last(self) -> Any:
        if self.is_empty():
            raise IndexError("Esta vazia")
        return self.__data[-1]

    def is_empty(self) -> bool:
        return len(self.__data) == 0

    def clear(self) -> None:
        self.__data.clear()

    def printListaPilha(self) -> None:
        print("Deque:", self.__data)
    






 









