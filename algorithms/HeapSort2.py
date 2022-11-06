import time
import pandas as pd
count = 0
def check_time(df, mesege):
    L = []
    for i in df.values:
        L.append(i[0])
    start = time.time()  # 시작 시간
    comcount = HeapSort(L) #배열
    ing_time = time.time() - start
    print(mesege + "time :", ing_time)  # 현재시각 - 시작시간 = 실행 시간
    print("comcount",comcount)
    return ing_time

def HeapSort(a):
    global count
    def swap(a,i,j): #임시 저장공간 temp를 사용하여 a[i]와 a[j]를 swap하는 함수
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
    def downheap(a, i, size): 
        global count 
        count += 1
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left <= size-1 and a[left] > a[i]:
            largest = left
        if right <= size-1 and a[right] > a[largest]:
            largest = right
        if largest != i:
            swap(a, i, largest)
            downheap(a, largest, size)
    def heapify(a, size): 
        p = (size//2) - 1 #탐색을 줄이기 위하여 가장 마지막 부모 노드를 p에 대입
        while p>=0:
            downheap(a, p, size)
            p -= 1
    size = len(a)
    heapify(a, size)
    end = size-1
    while(end > 0):
        swap(a, 0, end)
        downheap(a, 0, end)
        end -= 1
    return count
sort_list=[]
df = pd.read_csv(f'./Data/0_random.csv')   # csv파일형식은 간단하게 불러와짐
sort_list.append(check_time(df,'Heap_sort'))