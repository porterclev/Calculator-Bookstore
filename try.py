def rot(arr):
    for i in range(len(arr)):
        a = sorted(arr)
        b = sorted(arr,reverse=True)
        x = arr.pop()
        arr.insert(0,x)
        print(arr)
        if a==arr or b==arr:
            return True
    return False

arr = [3,4,1,2]
# arr = [1,4,2,3]
print(rot(arr))