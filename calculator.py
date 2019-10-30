    # python language calculator program
while 1:

    fir_no = float(input("Enter a first number"))
    operator = input("Enter a operator")
    sec_no = float(input("Enter a second number"))

    if operator == '+':
        result = fir_no + sec_no
    elif operator == '-':
        result = fir_no - sec_no
    elif operator == '*':
        result = fir_no * sec_no
    elif operator == '-':
        result = fir_no - sec_no
    elif operator == '/':
        result = fir_no / sec_no
    elif operator == '%':
        result = fir_no % sec_no
    else:
        print("operator worng")

    print("Result is : ", result)
    print("")


