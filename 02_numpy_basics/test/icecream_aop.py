import os
import numpy as np

class IceCreamShop:
    def __init__(self):
        self.money = 0
        self.name = np.array(["Chocolate", "Strawberry", "Vanila", 
                                   "Hazelnut", "Banana", "Orange"])
        self.feature = np.array(["Price", "Stock"])
        self.menu = np.array([
                        [3, 10],
                        [5, 10],
                        [2, 10],
                        [7, 10],
                        [5, 10],
                        [6, 10],
                    ])
        self.print_system()
    def __del__(self):
        print("Bye Bye, and thanks for using our shop!")
    def print_system(self):
        running = True
        while running:
            os.system("clear")
            print("Hello! Welcome to Hoon's Icecream :D ".center(40))
            self.print_menu()
            self.print_setting()
            print()
            print("(Press q to quit)".ljust(20) + f"Total income: ${self.money}".rjust(20))
            print()
            choice = input("Select icecream/setting: ")
            if choice == 'q':
                running = False
            elif choice in [str(a) for a in range(1, self.name.size+1)]:
                self.buy_icecream(int(choice))
            elif choice == 'a':
                self.add_menu()
            elif choice == 'b':
                self.remove_menu()
            elif choice == 'c':
                self.refill_icecream()
            else:
                pass
    def print_menu(self):
        print()
        print("[Menu]".center(40))
        print()
        for index, value in enumerate(self.menu):
            line_1 = f"{index+1}. {self.name[index]}".ljust(20)
            line_2 = f"${value[0]}".ljust(10)
            line_3 = f"Left: {value[1]}".ljust(10)
            print(line_1+line_2+line_3)
    def print_setting(self):
        print()
        print("[Settings]".center(40))
        print()
        print("a. Add Menu")
        print("b. Remove Menu")
        print("c. Refill Icecream")
    def buy_icecream(self, select):
        self.money += self.menu[select-1, 0]
        self.menu[select-1, 1] -= 1
    def add_menu(self):
        print()
        name = input("New icecream name: ")
        price = int(input("New icecream price: "))
        self.name = np.append(self.name, name)
        self.menu = np.append(self.menu, np.array([[price, 10]]), axis=0)
    def remove_menu(self):
        print()
        icecream = int(input("Icecream to remove: "))
        # Check if choice is in the range
        if icecream not in range(1, self.name.size+1):
            return
        truth = self.name != self.name[icecream-1]
        self.name = self.name[truth]
        self.menu = self.menu[truth]
    def refill_icecream(self):
        left = int(input("Set refill required amount: "))
        truth = self.menu[:, 1] < left
        self.menu[:, 1] = np.where(truth, 10, self.menu[:, 1])

if __name__ == "__main__":
    ics = IceCreamShop()
