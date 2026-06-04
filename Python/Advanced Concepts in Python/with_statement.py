file_name = "../../using_with.txt"

with open(file_name, "w") as file:
    file.write("This is created using the \"with\" statement.")

with open(file_name, "a") as file:
    file.write("\nI am appending using the \"with\" statement.")
    
with open(file_name, "r") as file:
    print(file.read())