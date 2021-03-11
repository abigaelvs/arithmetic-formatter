def exception_handling(number1, number2, operator):
    try:
        int(number1)
        int(number2)
    except:
        return 'Error: Numbers must only contain digits.'

    if len(number1) > 4 or len(number2) > 4:
        return "Error: Numbers cannot be more than four digits."

    if operator != '+' and operator != '-':
        return "Error: Operator must be '+' or '-'."

def arithmetic_arranger(problems, display=False):
    start = True
    line1 = line2 = line3 = line4 = ''
    side_space = '    '
    arranged_problems = []
    if len(problems) <= 5:
        for prob in problems:
            separated_problems = prob.split()
            number1 = separated_problems[0]
            operator = separated_problems[1]
            number2 = separated_problems[2]

            # exp = exception_handling(number1, number2, operator)
            # if exp != '':
            #     return exp

            try:
                int(number1)
                int(number2)
            except:
                return 'Error: Numbers must only contain digits.'

            if len(number1) > 4 or len(number2) > 4:
                return "Error: Numbers cannot be more than four digits."

            if operator != '+' and operator != '-':
                return "Error: Operator must be '+' or '-'."

            no1 = int(number1)
            no2 = int(number2)

            # if operator == '+':
            #     result = no1 + no2
            #     result_string = f'{no1} + {no2} = {result}'
            #     arranged_problems.append(result_string)
            # elif operator == '-':
            #     result = no1 - no2
            #     result_string = f'{no1} - {no2} = {result}'
            #     arranged_problems.append(result_string)

            space = max(len(number1), len(number2))
            if start == True:
                line1 += number1.rjust(space + 2)
                line2 += operator + ' ' + number2.rjust(space)
                line3 += '-' * (space + 2)
                if display == True:
                    if operator == '+':
                        line4 += str(no1 + no2).rjust(space + 2)
                    else:
                        line4 += str(no1 - no2).rjust(space + 2)
                start = False
            else:
                line1 += number1.rjust(space + 6)
                line2 += operator.rjust(5) + ' ' + number2.rjust(space)
                line3 += side_space + '-' * (space + 2)
                if display == True:
                    if operator == '+':
                        line4 += side_space + str(no1 + no2).rjust(space + 2)
                    else:
                        line4 += side_space + str(no1 - no2).rjust(space + 2)
                    

        if display == True:
            return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
            
        return line1 + '\n' + line2 + '\n' + line3
    else:
        return 'Error: Too many problems.'