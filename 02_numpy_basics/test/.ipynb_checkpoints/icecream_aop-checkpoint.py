import os
import numpy as np

class IceCreamShop:
    def __init__(self):
        self.row = row = np.array(["Chocolate", "Strawberry", "Vanila", 
                                   "Hazelnut", "Banana", "Orange"])
        self.col = np.array(["Price", "Stock"])
        self.money = 0
        self.menu = np.array([
            [3, 10],
            [5, 10],
            [2, 10],
            [7, 10],
            [5, 10],
            [6, 10],
        ])
    def buy_icecream(self, select):
        self.money += self.menu[select-1, 0]
        self.menu[select-1, 1] -= 1
    def print_menu(self):
        running = True
        while running:
            os.system("clear")
            print("Hello! Welcome to Hoon's Icecream :D ".center(40))
            print()
            print("Menu".center(40))
            print()
            for index, value in enumerate(self.menu):
                line_1 = f"{index+1}. {self.row[index]}".ljust(20)
                line_2 = f"${value[0]}".ljust(10)
                line_3 = f"Left: {value[1]}".ljust(10)
                print(line_1+line_2+line_3)
            print("(Press q to quit)".ljust(20) + f"Total income: ${self.money}".rjust(20))
            choice = input("Select number or quit: ")
            if choice == 'q':
                running = False
            elif int(choice) in range(1, 7):
                self.buy_icecream(int(choice))
            else:
                pass

if __name__ == "__main__":
    ics = IceCreamShop()
    ics.print_menu()
                
            
            
            
            
            
            
            
            
            
