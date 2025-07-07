# 🧮 Problem: Print Characters Line by Line
#
# 📌 Description:
#    Read a string from the user and print each character on a new line.
#
# 🧾 Extended Description:
#    This problem helps you get familiar with:
#      - Iterating through strings in Python
#      - Printing characters one at a time
#
#    Strings are iterable in Python, which means you can loop over each character directly.
#    This is especially useful when dealing with problems involving character-by-character processing,
#    such as encryption, parsing, or pattern checking.
#
# 🧠 Hint:
#    - Use a `for` loop: `for ch in s` where `s` is the input string.
#    - Use `print(ch)` inside the loop to print one character per line.
#
# ✅ Sample Input:
#    code
#
# ✅ Sample Output:
#    c
#    o
#    d
#    e

s = input()
for ch in s:
    print(ch)
