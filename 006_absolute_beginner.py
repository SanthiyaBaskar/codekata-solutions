# 🧮 Problem: Round and Check Number Type
#
# 📌 Description:
#    Read a floating-point number from the user.
#    Round it to the nearest integer.
#    Then:
#      - If it is 0, print "Zero"
#      - If it is an even number, print "Even"
#      - Otherwise, print "Odd"
#
# 🧾 Extended Description:
#    This problem helps you practice:
#      - Rounding float values using `round()`
#      - Conditional logic with `if-elif-else`
#      - Checking for even/odd using the modulo operator
#
#    Real-world cases like sensor readings or user inputs often give decimal values,
#    but you may want to work with rounded integers for classification, decision-making, or counting.
#
# 🧠 Hint:
#    - Use `round(num)` to round the input
#    - Use `num % 2 == 0` to check if a number is even
#    - Always check for zero first to avoid confusion
#
# ✅ Sample Input:
#    3.6
#
# ✅ Sample Output:
#    Even
#
# ✅ Sample Input:
#    -2.4
#
# ✅ Sample Output:
#    Even
#
# ✅ Sample Input:
#    0.3
#
# ✅ Sample Output:
#    Zero

num = float(input())
rounded = round(num)
if rounded == 0:
    print("Zero")
elif rounded % 2 == 0:
    print("Even")
else:
    print("Odd")
