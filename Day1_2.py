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
            count += 1
        earlier_number = number

    return count

# Calculate sliding window from a list and return the amount of times second sum is greater than the first one
def calculate_sliding_window(measurements: list) -> int:
    increase_count = 0
    # Start at index 2, because we are comparing sliding window at index with index - 1
    index = 2
    
    while index < len(measurements) - 1:
        sum1 = measurements[index-1] + measurements[index] + measurements[index+1]
        sum2 = measurements[index-2] + measurements[index-1] + measurements[index]
        print(f"sum1: {sum1}, sum2: {sum2}")
        if sum2 < sum1:
            increase_count += 1
        sum1 = 0
        sum2 = 0
        index += 1

    return increase_count


def main():

    file = open("D:\Koodi\Python\AdventOfCode2021\Day1Input.txt", "r")
    
    measurements = measurements_list(file)
    int_measurements = str_to_int(measurements)
    increase_count = calculate_increase(int_measurements)
    print(f"Day1 answer: {increase_count}")
    sliding_window_count = calculate_sliding_window(int_measurements)
    print(sliding_window_count)

if __name__ == "__main__":
    main()