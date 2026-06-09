from typing import Any, List




class Deque:




    def __init__(self) -> None:
        self.__data: List[Any] = []


    def __repr__(self) -> str:
            return str(self.__data)
   
    def insert_first(self,elemento:Any) -> None:
         self.__data.insert(0,elemento)
         
         
    def insert_last(self,elemento:Any) -> None:
          self.__data.insert(0,elemento)


    def size(self) -> int:
        return len(self.__data)


    def remove_last(self) -> None:
         self.__data.pop()
         
    def fist(self) -> Any:
         return self.__data[0]
   
    def last(self) -> Any:
         return self.__data[-1]


   


if __name__ == "__main__":
     
  pilhalista = Deque()
  pilhalista.insert_first(1)
  pilhalista.insert_first(2)
  pilhalista.insert_first(4)




  print("",pilhalista)
  pilhalista.remove_last()
  print("",pilhalista)
  print(pilhalista.fist())
  print(pilhalista.last())






 









