import time
import pandas as pd
def check_time(df,mesege):
    L = []
    for i in df.values:
        L.append(i[0])
    start = time.time()  # 시작 시간 저장
    comcount = insert_sort(L) #이 부분만 바꾸면 시간 출력함
    ing_time = time.time() - start
    print(mesege+"time :", ing_time)  # 현재시각 - 시작시간 = 실행 시간

    print("comcount",comcount)
    return ing_time

def insert_sort(A): #삽입 정렬
	cnt = 0
	for j in range(1,len(A)): #1부터 배열의 길이까지
		key = A[j] 
		i = j-1
		while i>=0 and A[i]>key:
			A[i+1]=A[i]
			i-=1
			cnt+=1
		A[i+1]=key
	return cnt

sort_list = []
df = pd.read_csv(f'./data/0_random.csv')  # csv파일형식은 간단하게 불러와짐
sort_list.append(check_time(df,'insert_sort'))

arr = [32,1,2]
print (arr)
insert_sort(arr)
print (arr)