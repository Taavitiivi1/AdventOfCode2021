def depth_and_forward(commands: list) -> int:
    forward_total = 0
    depth_total = 0
    
    for line in commands:
        number = line[len(line) - 1]
        number = int(number)

        if "forward" in line:
            forward_total += number
        if "up" in line:
            depth_total -= number
        if "down" in line:
            depth_total += number

    return forward_total * depth_total
     

def main():
    commands = []

    with open("D:\Koodi\Python\AdventOfCode2021\Day2_input.txt") as file:
        for line in file:
            line = line.strip()
            commands.append(line)

    result = depth_and_forward(commands)
    print(result)

if __name__ == "__main__":
    main()