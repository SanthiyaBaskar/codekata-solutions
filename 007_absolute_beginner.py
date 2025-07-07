# 🧮 Problem: Find the Greatest of Three Numbers
#
# 📌 Description:
#    Read three integers from the user.
#    Print the largest (maximum) of the three numbers.
#
# 🧾 Extended Description:
#    This problem helps you learn how to:
#      - Read multiple integer inputs
#      - Compare more than two values
#      - Use Python’s built-in `max()` function
#
#    This is a common task in basic programming: identifying the largest among several inputs.
#    It applies to ranking systems, comparison engines, grading logic, and more.
#
# 🧠 Hint:
#    - Read each input using `int(input())`
#    - Use `max(a, b, c)` to get the largest value
#
# ✅ Sample Input:
#    3
#    17
#    9
#
# ✅ Sample Output:
#    17

a = int(input())
b = int(input())
c = int(input())
print(max(a, b, c))
