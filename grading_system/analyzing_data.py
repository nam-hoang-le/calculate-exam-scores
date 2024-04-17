import re

def analyzing_data(file_read):
    print("****ANALYZING****")
    count = len(file_read)
    error_count = 0
    correct_exams = []

    for line in file_read:
        res = re.findall(r"[N]\d{8}", line)
        if not res:
            error_count += 1
            print(f"Invalid line of data: N# is invalid \n {line}")
        else:
            element = line.split(",")
            if len(element) != 26:
                error_count += 1
                print(f"Invalid line of data: does not contain exactly 26 values:\n {line}")
            else:
                correct_exams.append(line)

    if error_count == 0:
        print("No error found!")

    print("****REPORT****")
    print(f"Total valid lines of data:", count - error_count)
    print(f"Total invalid lines of data:", error_count)
    
    return correct_exams