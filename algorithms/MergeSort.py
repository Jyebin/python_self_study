#병합 구현
def merge(arr1, arr2):                  #두 배열이 정렬돼 있다는 가정
    n1 = len(arr1)
    n2 = len(arr2)
    p1 = 0                              #인덱스
    p2 = 0                              #인덱스
    
    arr_merged = []                     #새로운 배열을 나타내는 리스트
    while p1 < n1 and p2 < n2:          #짧은 배열에 맞춤, 오름차순 정렬
        if arr1[p1] <= arr2[p2]:        
            arr_merged.append(arr1[p1])
            p1 += 1
        else:
            arr_merged.append(arr2[p2])
            p2 += 1
    while p1 < n1:                      # 남은 원소들
        arr_merged.append(arr1[p1])
        p1 += 1
        
    while p2 < n2:                      #남은 원소들
        arr_merged.append(arr2[p2])
        p2 += 1
        
    return arr_merged

#병합 코드가 잘 실행되는지 실험
arr1 = [2,4,6,8,11,13]
arr2 = [1,2,3,4,9,16,21]
arr3 = merge(arr1, arr2)
print(arr3)

#병합 정렬 구현
def merge_sort(arr):
    if len(arr) == 1:                       #원소가 1개일 때 탈출
        print("Single element:", arr)
        print()
        return arr
    
    mid = len(arr) // 2                     #분할
    left = arr[:mid]
    right = arr[mid:]
    left_sorted = merge_sort(left)          #배열 정렬
    right_sorted = merge_sort(right)        #배열 정렬
    print("mid:", mid)
    print("left:", left_sorted)
    print("right:", right_sorted)
    print()
    return merge(left_sorted, right_sorted) #병합
