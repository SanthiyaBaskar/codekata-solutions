# 🧮 Problem: Read Three Integers from Separate Lines
#
# 📌 Description:
#    Read three integer values from the user, each given on a separate line.
#    Then print all three integers on the same line, space-separated.
#
# 🧾 Extended Description:
#    This problem helps you get familiar with reading multiple lines of input individually.
#    Each call to `input()` will wait for a new line from the user.
#    This style of input is often used when the number of inputs is small and clearly defined.
#
#    This also gives practice for:
#      - Using `int(input())` for individual inputs
#      - Storing values in separate variables (`a`, `b`, `c`)
#      - Printing multiple variables in a single line using a single `print()` function
#
#    Output must be in the same order as input, with values space-separated.
#
# 🧠 Hint:
#    Use `int(input())` three times to read the values one by one.
#    Use `print(a, b, c)` to print all values in one line with space in between.
#
# ✅ Sample Input:
#    10
#    20
#    30
#
# ✅ Sample Output:
#    10 20 30

a = int(input())
b = int(input())
c = int(input())
print(a, b, c)
