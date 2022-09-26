from unittest import result


def find_ins_idx(r,v): #리스트 r에서 v가 들어가야 할 위치를 돌려주는 함수
    for i in range(0, len(r)): #이미 정렬된 리스트 r의 자료를 앞에서부터 차례로 확인하여
        if v < r[i]:
            return i
    return len(r)

def ins_sort(a):
        result = []
        while a:
            value = a.pop(0)
            ins_idx = find_ins_idx(result, value)
            result.insert(ins_idx,value)
        return result

d = [2,4,5,1,3]
print(ins_sort(d))