from checkvalues.checker import check_solution



filepath = "https://raw.githubusercontent.com/rcabanasdepaz/checkvalues/main/examples/solution_example.csv"

# Run the checker without having defined the variables and functions
check_solution(filepath)



# Correct code
def func1(a,b):
    return 10*a+b
x = 2
y = 3.0
z = 4
lista = ["1", 2, 3.0]

check_solution(filepath)


# Wrong code
def func1(a,b):
    return 100*a+b
x = 2.0
y = 3
z = 5
lista = ["1", 2, 3.0, 3]

check_solution(filepath)
