command_list = list(input("Enter commands for Chandrayaan 3 in one line, with a single space in between : \nf/b : Move spacecraft forward/backward\n \
                          l/r : Rotate spacecraft in left or right direction\nu/d : Turn the spacecraft up/down").split())
coordinates = [0, 0, 0]

for i in command_list:
    if i == "f":
        coordinates[1] += 1
    if i == "b":
        coordinates[1] -= 1
    
    