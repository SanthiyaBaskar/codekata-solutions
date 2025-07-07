# 🧮 Problem: Read Multiple Lines of Input
#
# 📌 Description:
#    You are required to read 3 lines of input from the user, one after another.
#    After reading each line, print it immediately.
#
# 🧾 Extended Description:
#    In some programming problems, especially involving strings or logs, you're required to process multiple
#    lines of input — either line-by-line or all at once. This task helps you practice:
#
#     - Reading multiple inputs using a loop
#     - Handling input where the number of lines is known in advance
#     - Printing each input line as soon as it's read (useful in streaming or logging scenarios)
#
#    The use of the underscore `_` in `for _ in range(3)` is a Python convention for "we don't care about the loop variable".
#
# 🧠 Hint:
#    - Use a loop like `for _ in range(3)` to repeat 3 times
#    - Use `input()` to read each line
#    - Use `print(line)` immediately after reading it
#
# ✅ Sample Input:
#    Hello World
#    GUVI is awesome
#    CodeKata practice
#
# ✅ Sample Output:
#    Hello World
#    GUVI is awesome
#    CodeKata practice

for _ in range(3):
    line = input()
    print(line)
