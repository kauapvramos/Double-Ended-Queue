


from Deque import Deque




if __name__ == "__main__":
     
  pilhalista = Deque()
  pilhalista.insert_last(1)
  pilhalista.insert_last(2)
  pilhalista.insert_last(4)




  print("",pilhalista)
  pilhalista.remove_last()
  print("",pilhalista)
  print(pilhalista.fist())
  print(pilhalista.last())

