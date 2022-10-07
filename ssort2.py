def sel_sort(a):
    n = len(a)
    for i in range(0, n-1):
        min_idx = i
        for j in range(i+1, n):
            min_idx = i
            if a[j] < a[min_idx]:
                min_idx = j
                a[i], a[min_idx] = a[min_idx], a[i] #쉼표를 이용하여 두 변수의 위치 바꾸기

d = [2, 4, 5, 1, 3]
sel_sort(d)
print(d)