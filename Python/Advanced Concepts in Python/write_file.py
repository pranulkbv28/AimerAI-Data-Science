# the file relativity is the same as it is for read. PLease view the read_file.py for a better understanding

file = open("../../output.txt", "w")
file.write("Hello World!")
file.close()

file = open("../../output2.txt", "w")

lines = ["Hello.\n", "This is Pranaav.\n", "I am learnning Python."]

file.writelines(lines)
file.close()