def read_file():
    while True:
        try:
            name_file = input("Enter a class file to grade (e.g., class1 for class1.txt): ")
            with open(f"./Data_Files/input/{name_file}.txt", 'r') as file:
                file_read = file.read().splitlines()
            print(f"Successfully opened {name_file}.txt")
            return file_read, name_file
        except FileNotFoundError:
            print("File cannot be found.")