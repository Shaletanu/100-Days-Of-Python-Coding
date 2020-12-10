arr = []
size = int(input("Enter size: "))
for i in range(0, size) :
    b = int(input("Enter list item: "))
    arr.append(b)
print(arr)

def FindPair(arr, k):
    for i in range(0, len(arr)) :
        for j in range(0, len(arr)):
            if k == arr[i] + arr[j]:
                return True
    return False

k = int(input("Enter Number: "))
print(FindPair(arr, k))
