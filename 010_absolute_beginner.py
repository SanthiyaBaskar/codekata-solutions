# 🧮 Problem: Check Leap Year
#
# 📌 Description:
#    Read a year as input.
#    Print "Y" if it is a leap year, otherwise print "N".
#
# 🧾 Extended Description:
#    This problem reinforces the concept of conditional logic with multiple conditions.
#    A year is a leap year if:
#      - It is divisible by 4 and not divisible by 100
#      - Or it is divisible by 400
#
#    Leap year logic is a classic question and widely used in calendar systems,
#    date calculations, and logic-based coding problems.
#
# 🧠 Hint:
#    - Use `year % 4 == 0 and year % 100 != 0` for regular leap years
#    - Use `year % 400 == 0` for century leap years (like 2000)
#
# ✅ Sample Input:
#    2024
#
# ✅ Sample Output:
#    Y
#
# ✅ Sample Input:
#    1900
#
# ✅ Sample Output:
#    N

year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Y")
else:
    print("N")
