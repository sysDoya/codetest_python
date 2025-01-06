# 숫자 카드 게임
# 여러개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
# 룰
# 1. 숫자가 쓰인 카드들이 N X M 형태로 놓여 있다 이때 N은 행의 개수, M은 열의 개수
# 2. 먼저 뽑고자 하는 카드가 포함된 행을 선택
# 3. 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 함
# 4. 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 함

n, m = map(int, input().split())

result = 0

for i in range(n):
  data = list(map(int, input().split()))
  # 현재 행에서 가장 작은수 찾기
  min_value = min(data)
  # 가장 작은 수중 가장 큰수 찾기
  result = max(result, min_value)

print(result)






