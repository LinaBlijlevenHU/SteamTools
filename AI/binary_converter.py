# This function will be linked to the button in
# the application later
def binary_converter(txt):
    """ Convert a number to binary """
    return ' '.join(format(ord(c), 'b') for c in txt)

if __name__ == "__main__":
    print(binary_converter("green"))