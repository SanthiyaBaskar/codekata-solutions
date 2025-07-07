# 🧮 Problem: Read Array with Size and Key
#
# 📌 Description:
#    You are given two integers `n` and `k` in a single line.
#    The next line contains `n` space-separated integers representing the elements of an array.
#    Your task is to read and print `n`, `k`, and the array.
#
# 🧾 Extended Description:
#    This problem practices the typical pattern used in competitive programming and coding interviews:
#    reading two numbers from the first line, and then reading an array of numbers in the next line.
#    It's useful when solving problems related to searching, indexing, or working with array elements
#    based on some key value `k`.
#
#    Here:
#     - `n` is the size of the array.
#     - `k` can represent a target value, index, or operation count depending on the use case.
#
# 🧠 Hint:
#    - Use `map(int, input().split())` to read integers.
#    - Read the array with `list(map(int, input().split()))`.
#    - Use `print(*arr)` to print the array elements with space.
#
# ✅ Sample Input:
#    5 3
#    1 2 3 4 5
# ✅ Sample Output:
#    5 3
#    1 2 3 4 5

n, k = map(int, input().split())
print(n, k)
arr = list(map(int, input().split()))
print(*arr)
