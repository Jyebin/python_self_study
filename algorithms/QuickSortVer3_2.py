import time
import pandas as pd
cnt = 0
def check_time(df,mesege):
    L = []
    for i in df.values:
        L.append(i[0])
    start = time.time()  # 시작 시간 저장
    result = quick_sort_ver3(L)
    comcount = cnt #이 부분만 바꾸면 시간 출력함
    ing_time = time.time() - start
    print(mesege + "time :", ing_time)  # 현재시각 - 시작시간 = 실행 시간
    print("comcount",comcount)
    return ing_time
def quick_sort_ver3(a) :
    global cnt
    cnt += 1
    if len(a) <= 1 : # 리스트의 길이가 1이면 정렬할 필요가 없기 때문에 바로 반환한다.
        return a
    pivotList = []
    pivotList.append(a[int(len(a)/2)]) #배열의 중간값을 pivotList에 추가
    pivotList.append(a[-1]) #배열의 끝 값을 pivotList에 추가
    pivotList.append(a[0]) #배열의 처음 값을 pivotList에 추가
    pivotList.remove(max(pivotList)) #pivotList에서 가장 큰 값을 pop
    pivotList.remove(min(pivotList)) #pivotList에서 가장 작은 값을 pop
    pivot = pivotList[0] #pivotList에서 남은 값을 pivot으로 설정
    left = [] # 피벗보다 작은 수들의 리스트
    right = [] # 피벗보다 큰 수들의 리스트
    piv = [] #피벗을 빼놓고 큰수 작은수로 나누어야 하기때문에 피벗 부분을 넣을 리스트를 생성한다.
    for i in a :
       if i < pivot :
           left.append(i)
           cnt += 1
       elif i > pivot :
           right.append(i)
           cnt += 1
       else :
           piv.append(i)
           cnt += 1
    return quick_sort_ver3(left)+pivot+quick_sort_ver3(right)
sort_list = []
df = pd.read_csv(f'./Data/0_random.csv')  # csv파일형식은 간단하게 불러와짐
sort_list.append(check_time(df,'quick_sort_ver3'))