row_size=int(input("Enter the row size:"))print_control_x=row_size//2+1for out in range(1,row_size+1):  for inn in range(1,row_size+1):    if inn==out or inn+out==row_size+1:      print("*",end="")    else:      print(" ", end="")  print("\r")