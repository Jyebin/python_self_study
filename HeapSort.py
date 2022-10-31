def HeapSort(a):
    def swap(a,i,j): #임시 저장공간 temp를 사용하여 a[i]와 a[j]를 swap하는 함수
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

    def downheap(a, i, size): #
        l = 2*i + 1
        r = 2*i + 2
        largest = i
        if l <= size-1 and a[l] > a[i]:
            largest = l
        if r <= size-1 and a[r] > a[largest]:
            largest = r
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
arr = [1,3,2,4,9,7]
print(arr)
HeapSort(arr)
print(arr)