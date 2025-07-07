# 🧮 Problem: Read and Print Integers
# 📌 Description:
#    Given a line of space-separated integers, read them and print them in the same order.
#
# 🧠 Hint:
#    Use `input().split()` to split the input string and `map(int, ...)` to convert each element to an integer.
#    Use unpacking `*` in the `print()` function to print values with space.
#
# ✅ Sample Input:
#    5 10 15 20
# ✅ Sample Output:
#    5 10 15 20

nums = list(map(int, input().split()))
print(*nums) 

