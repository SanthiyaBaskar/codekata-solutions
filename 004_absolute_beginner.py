# 🧮 Problem: Number of Days in a Month
#
# 📌 Description:
#    Read an integer representing a month number (1 to 12).
#    Print the number of days in that month.
#    (Assume it's not a leap year — so February has 28 days.)
#
# 🧾 Extended Description:
#    This problem teaches how to:
#      - Work with dictionaries for lookup
#      - Validate input using conditional statements
#      - Apply real-world logic (calendar-based)
#
#    The program uses a dictionary `month_days` where the keys are month numbers (1–12)
#    and the values are the number of days in each respective month.
#
# 🧠 Hint:
#    - Use a dictionary to store days for each month
#    - Check if the month is between 1 and 12 before accessing
#
# ✅ Sample Input:
#    2
#
# ✅ Sample Output:
#    28
#
# ✅ Sample Input:
#    11
#
# ✅ Sample Output:
#    30

month = int(input())
month_days = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
if 1 <= month <= 12:
    print(month_days[month])
else:
    print("Invalid month")
