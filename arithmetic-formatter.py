def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return 'Error: Too many problems.'

    problems = [problem.split() for problem in problems]
    print(problems)
    first_line, second_line, third_line, ans_line = [], [], [], []

    #Declare spacing variables
    SPACING = 4 * ' '
    OPERATOR_SPACING = 2

    for problem in problems:
        first_operand = problem[0]
        operator = problem[1]
        second_operand = problem[2]

        max_w = max(len(first_operand), len(second_operand)) + OPERATOR_SPACING

        #Check for Errors
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        elif not all([first_operand.isnumeric(), second_operand.isnumeric()]):
            return 'Error: Numbers must only contain digits.'
        elif len(first_operand) > 4 or len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        first_line.append(first_operand.rjust(max_w, " "))
        second_line.append(operator.ljust(max_w - len(second_operand)) + second_operand)
        third_line.append("-" * max_w)

        if show_answers:
            ans = str(int(first_operand) + int(second_operand)) if operator == '+' else str(int(first_operand) - int(second_operand))
            ans = ans.rjust(max_w) if len(ans) < max_w else ans.rjust(max_w + 1)
            ans_line.append(ans)
        

    str_to_return = SPACING.join(first_line) + '\n' + SPACING.join(second_line) + '\n' + SPACING.join(third_line)
    if show_answers:
        str_to_return += '\n' + SPACING.join(ans_line)

    return str_to_return
    


def main():
    print(arithmetic_arranger(["3801 - 2", "123 + 49"], True))

if __name__ == "__main__":
    main()