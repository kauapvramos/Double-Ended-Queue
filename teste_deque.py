


from Deque import Deque




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

print("Primeiro:", pilhalista.first())     
print("ultimo:", pilhalista.last())        
print("Tamanho:", pilhalista.size())       

print("Removido:", pilhalista.remove_first())   
print("Removido:", pilhalista.remove_last())    

pilhalista.insert_last(11)       
pilhalista.remove_any(5)     
pilhalista.printListaPilha()

print("Está vazia?", pilhalista.is_empty())    

