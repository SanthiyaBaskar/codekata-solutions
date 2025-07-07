# 🧮 Problem: Find the Minimum of Two Numbers
#
# 📌 Description:
#    Read two integers from a single line of input.
#    Print the smaller of the two numbers.
#
# 🧾 Extended Description:
#    This problem is aimed at helping you:
#      - Read multiple values from a single line
#      - Compare two values
#      - Use Python's built-in `min()` function
#
#    Understanding how to compare values is essential in many algorithms such as
#    finding the smallest/largest element, conditional branching, etc.
#
# 🧠 Hint:
#    - Use `map(int, input().split())` to read both values at once
#    - Use `min(a, b)` to get the smaller number
#
# ✅ Sample Input:
#    9 4
#
# ✅ Sample Output:
#    4

a, b = map(int, input().split())
print(min(a, b))
