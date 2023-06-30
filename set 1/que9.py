def fibonacci(num):
    arr = []
    if num <= 0:
        return arr
    arr.append(0)
    if num > 1:
        arr.append(1)
    for i in range(2, num):
        next_number = arr[i - 1] + arr[i - 2]
        arr.append(next_number)
    return arr

seq = fibonacci(5)
print(seq)
