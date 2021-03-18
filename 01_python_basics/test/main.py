import os

class Owner:
  # Constructor
  def __init__(self):
    self.money = 0
  # Destructor
  def __del__(self):
    print("Jangsa is over")
  # Method
  def sell_recycle(self):
    running = True
    while running: 
      os.system("clear")
      print(f"====   Money: {self.money}   ====")
      print("==== Recycle man is back ====")
      print("1. Can            $ 12       ")
      print("2. Aluminiun      $ 11       ")
      print("3. Plastic        $ 09       ")
      print("4. Bottle         $ 15       ")
      print("=============================")
      choice = input("Choose Trash: ")
      if choice == '1':
        self.money = self.money+12
      elif choice == '2':
        self.money = self.money+11
      elif choice == '3':
        self.money = self.money+9
      elif choice == '4':
        self.money = self.money+15
      elif choice == 'q':
        running = False
      else:
        pass

owner = Owner()
owner.sell_recycle()
      

