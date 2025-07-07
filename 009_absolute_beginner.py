# 🧮 Problem: Square of a Non-Negative Number
#
# 📌 Description:
#    Read an integer `n` from the user.
#    - If `n` is negative, print "Error"
#    - If `n` is zero, print 0
#    - If `n` is positive, print its square (n²)
#
# 🧾 Extended Description:
#    This problem helps you practice conditional statements and basic math operations.
#    It's a good example of input validation combined with mathematical logic.
#
#    Use cases like these appear in calculators, validations, simulations, etc.,
#    where negative inputs must be restricted or treated differently.
#
# 🧠 Hint:
#    - Use `n * n` or `n ** 2` to compute square
#    - Check for negative values first to prevent invalid output
#
# ✅ Sample Input:
#    5
#
# ✅ Sample Output:
#    25
#
# ✅ Sample Input:
#    -3
#
# ✅ Sample Output:
#    Error
#
# ✅ Sample Input:
#    0
#
# ✅ Sample Output:
#    0

n = int(input())
if n < 0:
    print("Error")
elif n == 0:
    print(0)
else:
    print(n * n)
