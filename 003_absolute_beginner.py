# 🧮 Problem: Convert Celsius to Fahrenheit
#
# 📌 Description:
#    Read a temperature in Celsius and convert it to Fahrenheit using the formula:
#      Fahrenheit = (Celsius × 9/5) + 32
#    Print the result rounded to two decimal places.
#
# 🧾 Extended Description:
#    This problem reinforces working with:
#      - Floating-point input
#      - Arithmetic operations with decimals
#      - Output formatting using f-strings
#
#    Converting temperature units is a real-world task often required in applications
#    involving weather apps, data science, and IoT sensors.
#
# 🧠 Hint:
#    - Use `float(input())` to allow decimal input
#    - Apply the formula directly
#    - Use `f"{value:.2f}"` to print with 2 decimal precision
#
# ✅ Sample Input:
#    37
#
# ✅ Sample Output:
#    98.60

celsius = float(input())
fahrenheit = (celsius * 9/5) + 32
print(f"{fahrenheit:.2f}")
