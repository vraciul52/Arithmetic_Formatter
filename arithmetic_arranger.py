def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    # Variables for lines
    topline = ""
    bottomline = ""
    dashline = ""
    resultline = ""

    for problem in problems:
        num1, op, num2 = problem.split()

        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if op not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        linelen = max(len(num1), len(num2)) + 2
        top = num1.rjust(linelen)
        bottom = op + num2.rjust(linelen - 1)

        sum_result = str(int(num1) + int(num2)) if op == '+' else str(int(num1) - int(num2))
        result = sum_result.rjust(linelen)

        dash = "-" * linelen

        if problem != problems[-1]:
            topline += top + "    "
            bottomline += bottom + "    "
            dashline += dash + "    "
            resultline += result + "    "
        else:
            topline += top
            bottomline += bottom
            dashline += dash
            resultline += result

    if show_answers:
        arranged_problems = topline + "\n" + bottomline + "\n" + dashline + "\n" + resultline
    else:
        arranged_problems = topline + "\n" + bottomline + "\n" + dashline

    return arranged_problems
