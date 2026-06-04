file = open("../../sample.txt", "r") # this file path should be written in a relative way from where you are running
# basically, if I am running "python3 file_handling.py", then this path is correct
# if I am running "python3 parent_directoryfile_handling.py", then this path will become "../sample.txt"


file_read_type = input("Choose between read, readline, readlines: ")
match file_read_type:
    case "read":
        content = file.read()
        print(content)
    case "readline":
        while True:
            content = file.readline()
            
            if content == "":
                break
            
            print(content)
    case "readlines":
        content = file.readlines()
        print(content)
    case _:
        "Invalid Option"
    
file.close()