from checkvalues.solution import Solution

x = 2
y = 3.0
z = 4
L = ["1", 2, 3.0]


s = Solution()

s.add("Exercise 1", "var", "x", x)
s.add("Exercise 2", "var", "y", y)
s.add("Exercise 3", "var", "z", z)
s.add("Exercise 4", "var", "L", L)
s.add("Exercise 5", "func", "func1", 23.0, args="int:2;float:3", points=0.5)
s.add("Exercise 5", "func", "func1", 32, kwargs="b=int:2;a=int:3", points=0.5)


s.save("./examples/solution_example.csv")