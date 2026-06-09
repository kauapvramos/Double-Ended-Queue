from typing import Any, List


class Deque:

    def __init__(self) -> None:
        self.__data: List[Any] = []


    def __repr__(self) -> str:
            return str(self.__data)
   
    def insert_first(self,elemento:Any) -> None:
         self.__data.insert(0,elemento)
         
         
    def insert_last(self,elemento:Any) -> None:
          self.__data.append(elemento)


    def size(self) -> int:
        return print("Tamanho da Lista: ",len(self.__data))

    def remove_first(self) -> Any:
        return print("Primeiro Item Removido:",self.__data.pop(0))

    def remove_last(self) -> Any:
         return print("Ultimo Item Removido:",self.__data.pop(-1))
    
    def remove_any(self,elemento: Any) -> Any:
         return print("Item Removido:",self.__data.pop(elemento -1))
         
         
    def fist(self) -> Any:
         return print("Primeiro Item: ",self.__data[0])
   
    def last(self) -> Any:
         return  print(self.__data[-1])
    
    def is_empty(self) -> Any:
       if len(self.__data) == 0:
            return True
       else:
            return False
    
    def printListaPilha(self) -> Any:
         return print("Lista: ", self.__data)
    



   


if __name__ == "__main__":
     
  pilhalista = Deque()
  pilhalista.insert_last(1)
  pilhalista.insert_last(2)
  pilhalista.insert_last(3)
  pilhalista.insert_last(4)
  pilhalista.insert_last(5)
  pilhalista.insert_last(6)
  pilhalista.insert_last(7)
  pilhalista.insert_last(8)
  pilhalista.insert_last(9)
  pilhalista.insert_last(10)
  

  pilhalista.printListaPilha()
  pilhalista.remove_last()
  pilhalista.printListaPilha()
  pilhalista.remove_any()
  pilhalista.printListaPilha()
  pilhalista.size()
  pilhalista.printListaPilha()
  





 









