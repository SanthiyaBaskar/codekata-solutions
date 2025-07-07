# 🧮 Problem: Print Characters Separated by Commas (with Error Handling)
#
# 📌 Description:
#    Read a string from the user and print each character separated by a comma.
#    If there's any error during input, print "Input error".
#
# 🧾 Extended Description:
#    This problem combines basic string formatting with exception handling.
#    The goal is to:
#      - Read input as a string
#      - Format the output so that each character is separated by a comma
#      - Gracefully handle any unexpected input issues using `try` and `except`
#
#    Python's `",".join(s)` takes a string and inserts commas between every character.
#    Using `try-except` ensures that the program doesn't crash if something unexpected happens (like invalid input).
#
# 🧠 Hint:
#    - Use `",".join(s)` to insert commas between characters.
#    - Use `try-except` to safely wrap the logic and catch errors.
#
# ✅ Sample Input:
#    guvi
#
# ✅ Sample Output:
#    g,u,v,i
#
# ✅ Sample Input (Error Case):
#    (force input error, e.g. EOF)
#
# ✅ Sample Output:
#    Input error

try:
    s = input()
    print(",".join(s))
except:
    print("Input error")
