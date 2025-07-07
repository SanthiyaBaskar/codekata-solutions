# 🧮 Problem: Convert Kilometers to Meters and Centimeters
#
# 📌 Description:
#    Read a distance in kilometers and convert it to:
#      - Meters (1 km = 1000 m)
#      - Centimeters (1 km = 100000 cm)
#    Print both values as integers.
#
# 🧾 Extended Description:
#    This problem is useful for building understanding of unit conversions.
#    It tests your ability to:
#      - Work with floating-point input
#      - Perform basic multiplication
#      - Convert float results to integers using `int()` to remove decimal points
#
# 🧠 Hint:
#    - Multiply the kilometers by 1000 to get meters
#    - Multiply the kilometers by 100000 to get centimeters
#    - Use `int()` to remove decimal places before printing
#
# ✅ Sample Input:
#    1.2
#
# ✅ Sample Output:
#    1200
#    120000

km = float(input())
meters = km * 1000
centimeters = km * 100000
print(int(meters))
print(int(centimeters))
