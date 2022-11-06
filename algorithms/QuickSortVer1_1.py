import time
import pandas as pd
cnt = 0
def check_time(df,mesege):
    L = []
    for i in df.values:
        L.append(i[0])
    start = time.time()  # 시작 시간 저장
    result = quick_sort_ver1(L)
    comcount = cnt #이 부분만 바꾸면 시간 출력함
    ing_time = time.time() - start
    print(mesege + "time :", ing_time)  # 현재시각 - 시작시간 = 실행 시간
    print("comcount",comcount)
    return ing_time

def quick_sort_ver1(a) :
    global cnt
    cnt += 1
    if len(a) <= 1 : # 리스트의 길이가 1이면 정렬할 필요가 없기 때문에 바로 반환
        return a
    pivot = (a[int(len(a)/2)]) #피벗이 배열의 처음과 마지막 요소의 평균값
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
    return quick_sort_ver1(left) + piv + quick_sort_ver1(right)

sort_list = []
df = pd.read_csv(f'./Data/UnsortedArr32.csv') 
sort_list.append(check_time(df,'quick_sort_ver1'))