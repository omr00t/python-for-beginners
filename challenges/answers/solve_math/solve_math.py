import sys

def calculate_result(n1, n2, op="+", /):
    """
    Calculates the result of operation "op" using "n1" and "n2"
    as arguments.

    returns the result of the operation.
    """

    n1 = int(n1)
    n2 = int(n2)

    if (op == '+'):
        return n1 + n2
    elif (op == '-'):
        return n1 - n2
    elif (op == '*'):
        return n1 * n2
    elif (op == '/'):
        try:
            return round(n1 / n2, 2)
        except ZeroDivisionError:
            return "Error - cannot divide by 0"
    else:
        # This should not happen.
        return None

def parse_math_problem(math_problem):
    """
    Parses a simple math problem to extract the operator
    and arguments.

    returns a tuple containing arguments and operator.
    """

    parts = tuple(math_problem.split(' '))
    
    match parts[1]:
        case '+':
            p_tuple = (parts[0], parts[2])
        case '-':
            p_tuple = (parts[0], parts[2], '-')
        case '*':
            p_tuple = (parts[0], parts[2], '*')
        case '/':
            p_tuple = (parts[0], parts[2], '/')
        case _:
            raise Exception("Unsupported operator:", _)
    return p_tuple

def write_file(*, file_name, problem_tuple, problem_result):
    """
    Writes a file containing the problems along with their result.
    """

    with open("solved_math_problems.txt", "at") as f:
        f.writelines(f"{problem_tuple[0]:2} "
                     f"{problem_tuple[2] if len(problem_tuple)==3 else '+'} "
                     f"{problem_tuple[1]:<2} = {problem_result}\n")

def read_file(file_name):
    """
    A generator that reads a file containing the problems.
    """

    with open(file_name, "rt") as f:
        for line in f:
            math_problem = line.strip()
            yield math_problem

def main(input_file, output_file):
    """
    The main function that drives calculation operations.
    """

    for problem in read_file(input_file):
        p_tuple = parse_math_problem(problem)
        result = calculate_result(*p_tuple)
        write_file(file_name = output_file,
                   problem_tuple = p_tuple,
                   problem_result = result)

if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print(f"python {sys.argv[0]} <input_file> <output_file>")
        print(f"python {sys.argv[0]} math_problems.txt solved_math_problems.txt")
        sys.exit(0)
    main(sys.argv[1], sys.argv[2])
