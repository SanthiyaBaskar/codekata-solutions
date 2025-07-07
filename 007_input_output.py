# 🧮 Problem: Print Characters with Space
#
# 📌 Description:
#    Read a single string from the user and print each character separated by a space.
#
# 🧾 Extended Description:
#    This problem is designed to test your understanding of string manipulation and formatting.
#    When working with strings, it’s common to:
#      - Access individual characters
#      - Modify how the output looks (like inserting spaces, commas, etc.)
#
#    Here, you take a single string input and print each character separated by a space.
#    This can be done easily by using Python’s `join()` function:
#      - `join()` combines elements of a sequence (like a list or string) using a separator.
#      - In this case, we use `' '.join(s)` to put a space between each character.
#
# 🧠 Hint:
#    - Strings in Python are iterable, so `' '.join(s)` will insert a space between each character.
#
# ✅ Sample Input:
#    hello
#
# ✅ Sample Output:
#    h e l l o

s = input()
print(' '.join(s))
