import os
import time

class Client:
  # Input client information
  def enter_info(self):
    self.email = input("Enter email: ")
    self.password = input("Enter password: ")
  # Print client information
  def print_yourself(self):
    print(f'Email: {self.email}')
    print(f'Password: {self.password}')

class Admin:
  def print_cred(self, client_list):
    print("================= Client List =================")
    for client in client_list:
      client.print_yourself()
    print("===============================================")
  def login(self, client_list):
    email = input("Enter email: ")
    password = input("Enter password: ")
    for client in client_list:
      if client.email is email and client.password is password:
        print("Login Success")
        time.sleep(2)
      else:
        print("Login Failed")
        time.sleep(2)

client_list = []
mr_admin = Admin()
running = True
while running:
  os.system("clear")
  mr_admin.print_cred(client_list)
  print("==================== Select =====================")
  print("a. Create credentials")
  print("b. Log in")
  print("q. Exit")
  seletKey = input("Choose one: ")
  if seletKey == 'a':
    client = Client()
    client.enter_info()
    client_list.append(client) 
  elif seletKey == 'b':
    mr_admin.login(client_list)
  elif seletKey == 'q':
    running = False
  else:
    pass

