# 🧮 Problem: Read and Print Floating Point Numbers
#
# 📌 Description:
#    Read a line of space-separated floating-point numbers and print each number on a separate line.
#
# 🧾 Extended Description:
#    This problem helps you understand how to:
#      - Read multiple floating-point values from a single line
#      - Convert input strings to `float` using `map()`
#      - Iterate through the mapped values and print each one individually
#
#    Unlike integers, floats can contain decimal points and require more careful handling,
#    especially when working with scientific or financial data.
#
#    The `map(float, input().split())` reads multiple numbers like `12.5 3.14 0.001` and converts each to a `float`.
#
# 🧠 Hint:
#    - Use `map(float, input().split())` to read multiple floats in one line.
#    - Use a `for` loop to print each number on a new line.
#
# ✅ Sample Input:
#    1.1 2.2 3.3
#
# ✅ Sample Output:
#    1.1
#    2.2
#    3.3

floats = map(float, input().split())
for num in floats:
    print(num)
