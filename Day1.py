# Read all the lines in the file and add them to a list
def measurements_list(file: str) -> list:
    measurements = []

    while True:
        line = file.readline()
        # Strip the newline from the end of each line
        line = line.rstrip("\n")
        if line == "":
            break
        measurements.append(line)

    return measurements

def str_to_int(str_list: list) -> list:
    int_list = []

    for string in str_list:
        number = int(string)
        int_list.append(number)

    return int_list

# Calculate the amount of times the current number is higher than the number before
def calculate_increase(measurements: list) -> list:
    count = 0
    earlier_number = 0

    for number in measurements:
        # First number does not have a number before it, so we just skip it
        if measurements.index(number) == 0:
            earlier_number = number
            continue
        elif number > earlier_number:
            print(f"{earlier_number}, {number}")
            count += 1
        earlier_number = number

    return count

def main():

    file = open("D:\Koodi\Python\AdventOfCode2021\Day1Input.txt", "r")
    
    measurements = measurements_list(file)
    int_measurements = str_to_int(measurements)
    increase_count = calculate_increase(int_measurements)
    print(increase_count)

if __name__ == "__main__":
    main()