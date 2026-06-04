# open(file_path, mode) -> this fucntion is used to open a file
# modes:
# r : read only
# w : write only(created/truncates)
# a : append
# rb(read binary), wb(write binary), ab(append binary) : binary modes

# methods
# read() -> reads entire content
# readline() ->  reads one line at a time
# readlines() -> reads all lines into a list
# write() -> writes a string
# writelines() -> writes a list of strings
# append mode (a) -> to add content without truncating
# seek() -> moves pointer to a specific position
# tell() -> returns the pointer's current position

# we using "with" statement: Automatically closes file

# CSV files
# csv.reader
# csv.DictReader
# csv.writer
# csv.DictWriter

# JSON
# json.load() -> read
# json.dump() -> write

# XML
# xml.etree.ElementTree -> read