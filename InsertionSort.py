def insert_sort(A): #삽입 정렬
	for j in range(1,len(A)): #1부터 배열의 길이까지
		key = A[j] 
		i = j-1
		while i>=0 and A[i]>key:
			A[i+1]=A[i]
			i-=1
		A[i+1]=key

arr = [32,1,2]
print (arr)
insert_sort(arr)
print (arr)