phone_book=["119", "97674223", "1195524421"]
def solution(phone_book):
    # 짧은 길이 순으로 정렬
    phone_book=sorted(phone_book, key=len)
    for i,v in enumerate(phone_book):
        for j in range(i+1, len(phone_book)):
            if v == phone_book[j][:len(v)]:
                return False
        return True
print(solution(phone_book))

"""
다른 사람 풀이

def solution(phone_book): 
    for i in range(len(phone_book)): 
        pivot = phone_book[i] 
        for j in range(i+1, len(phone_book)): 
            strlen = min(len(pivot), len(phone_book[j])) 
            if pivot[:strlen] == phone_book[j][:strlen]: 
                return False 
    return True

"""