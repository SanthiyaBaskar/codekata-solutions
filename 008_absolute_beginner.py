# 🧮 Problem: Multiples of 9
#
# 📌 Description:
#    Read an integer `n` from the user.
#    If `n` is 0, print "NULL".
#    Otherwise, print the first `n` multiples of 9, space-separated.
#
# 🧾 Extended Description:
#    This problem helps you practice:
#      - Basic control flow using `if-else`
#      - List comprehension
#      - Working with loops and mathematical patterns (multiples)
#
#    Multiples are commonly used in math-based logic, sequence generation,
#    and in problems related to patterns or tables.
#
# 🧠 Hint:
#    - Use a list comprehension `[9 * i for i in range(1, n + 1)]`
#    - Convert each number to string using `str()`
#    - Use `' '.join(...)` to print with spaces
#    - Handle `n == 0` as a special case
#
# ✅ Sample Input:
#    5
#
# ✅ Sample Output:
#    9 18 27 36 45
#
# ✅ Sample Input:
#    0
#
# ✅ Sample Output:
#    NULL

n = int(input())
if n == 0:
    print("NULL")
else:
    result = [str(9 * i) for i in range(1, n + 1)]
    print(' '.join(result))
