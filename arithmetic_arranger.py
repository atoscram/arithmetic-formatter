
def arithmetic_arranger(problems, display_answer=False):
    problem_limit = 5
    digit_limit = 4

    processed_problems = list()

    try:
        if len(problems) > problem_limit:
            return "Error: Too many problems."

        for problem in problems:
            ###
            # Example
            # "34 + 3"
            # the problem assumes the formatting is correct
            # this will catch inproper format anyway
            ###
            problem = problem.split()

            if problem[1] != "+" == problem[1] != "-":
                return "Error: Operator must be '+' or '-'"
            elif len(problem[0]) > digit_limit or len(problem[2]) > digit_limit:
                return "Error: Numbers cannot be more than four digits."

            # throws a valueerror if the variable cannot be casted as an int
            op1 = int(problem[0])
            op2 = int(problem[2])

            # creates a list of tuples with the operands and the operator consecutively
            processed_problems.append(((op1, op2), problem[1]))

    except ValueError as e:
        print(e)
        return "Error: Numbers must only contain digits."
    except Exception as e:
        print(e)
        return "Error: with input problems"

    top_line = ""
    mid_line = ""
    dvd_line = ""
    btm_line = ""

    for prb in processed_problems:
        # There should be a single space between the operator and the longest of the two operands.
        max_width = len(str(max(prb[0], key=abs))) + 2
        op1 = prb[0][0]
        op2 = prb[0][1]
        opr = prb[1]

        if prb[1] == "+":
            total_value = op1 + op2
        else:
            total_value = op1 - op2

        # There should be four spaces between each problem.
        top_line = top_line + "    "
        mid_line = mid_line + "    "
        dvd_line = dvd_line + "    "
        btm_line = btm_line + "    "


        top_line = top_line + str(op1).rjust(max_width, " ")
        mid_line = mid_line + opr + " " + str(op2).rjust(max_width - 2, " ")
        dvd_line = dvd_line + "".rjust(max_width, "-")

        if display_answer:
            btm_line = btm_line + str(total_value).rjust(max_width, " ")

    return top_line + '\n' + mid_line + '\n' + dvd_line + '\n' + btm_line

