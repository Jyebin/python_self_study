def quick_sort(a) :
    if len(a) <= 1 : # 리스트의 길이가 1이면 정렬할 필요가 없기 때문에 바로 반환한다.
        return a
    pivot = a[0] # 리스트에서 원하는 기준점(피벗)을 선택한다.
    left = [] # 피벗보다 작은 수들의 리스트
    right = [] # 피벗보다 큰 수들의 리스트
    piv = [] #피벗을 빼놓고 큰수 작은수로 나누어야 하기때문에 피벗 부분을 넣을 리스트를 생성한다.
    for i in a :
        if i < pivot :
            left.append(i)
        elif i > pivot :
            right.append(i)
        else :
            piv.append(i)
    return quick_sort(left) + piv + quick_sort(right)
arr = [10,30,20,40,90,60]
print(quick_sort(arr))
#[10,20,30,40,60,90]