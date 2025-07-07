# 🧮 Problem: Print Each Line After Reading
#
# 📌 Description:
#    Read 3 lines of input from the user. After reading each line,
#    print it immediately on a new line.
#
# 🧾 Extended Description:
#    This problem focuses on reading **multiple lines of text** from the user.
#    It simulates scenarios where:
#      - Input is streamed line-by-line (like chat logs or file lines)
#      - Output is printed immediately for each line
#
#    The `for _ in range(3)` loop is used to repeat an action 3 times.
#    The underscore `_` is a convention used when the loop variable isn't needed.
#
#    This pattern is common in many coding problems where a fixed number of lines must be processed.
#
# 🧠 Hint:
#    - Use `input()` inside the loop to read each line
#    - Use `print(line)` to print each line after reading
#
# ✅ Sample Input:
#    Apple
#    Banana
#    Mango
#
# ✅ Sample Output:
#    Apple
#    Banana
#    Mango

for _ in range(3):
    line = input()
    print(line)
