def main():

    print("Task to return alternate char from string")
    string_alternative()

# function to return alternate char from string
def string_alternative():

    strInput = input("Enter string: ")
    strOutput = strInput[::2]
    print(strOutput)

if __name__ == "__main__":
    main()