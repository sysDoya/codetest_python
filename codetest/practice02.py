# 큰수의 법칙 
# 1. N개의 숫자로 이루어진 배열이 주어짐
# 2. 배열에서 숫자를 선택해 총 M번 더해야 함
# 3. 단, 특정 숫자는 최대 K번 연속해서 더할 수 있음
# 4. 가능한 한 큰 수를 많이 더하도록 배열에서 숫자를 선택

n, m, k = map(int, input().split()) 
data = list(map(int, input().split()))
result = 0

data.sort()

first = data[n-1]
second = data[n-2]

count = int(m / (k+1)) * k
count += m % (k+1)

result += (count) * first
result += (m - count) * second

print(result)

# 시간 복잡도 
# 정렬: O(n log n)
# 계산: O(1)