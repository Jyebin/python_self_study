import time
import pandas as pd
cnt = 0
def check_time(df,mesege):
    L = []
    for i in df.values:
        L.append(i[0])
    start = time.time()  # 시작 시간 저장
    result = merge_sort(L)
    comcount = cnt #이 부분만 바꾸면 시간 출력함
    ing_time = time.time() - start
    print(mesege + "time :", ing_time)  # 현재시각 - 시작시간 = 실행 시간
    print("comcount",comcount)
    return ing_time

def merge(arr1, arr2): #두 배열이 정렬돼 있다는 가정
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

#병합 정렬 구현
def merge_sort(arr):
    global cnt
    cnt += 1
    if len(arr) == 1:                       #원소가 1개일 때 탈출
        return arr
    mid = len(arr) // 2                     #분할
    left = arr[:mid]
    right = arr[mid:]
    left_sorted = merge_sort(left)          #배열 정렬
    right_sorted = merge_sort(right)        #배열 정렬
    return merge(left_sorted, right_sorted) #병합

sort_list = []
df = pd.read_csv(f'./Data/SortedArr32.csv')  # csv파일형식은 간단하게 불러와짐
sort_list.append(check_time(df,'merge_sort'))

