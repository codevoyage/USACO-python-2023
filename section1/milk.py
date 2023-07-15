"""
ID: shikha11
LANG: PYTHON3
TASK: milk
"""

fin = open('milk.in', 'r')
fout = open('milk.out', 'w')

N, M = map(int, fin.readline().strip().split())

milk_prices = []
for i in range(M):
    milk_prices.append(list(map(int, fin.readline().strip().split())))

milk_prices.sort(key=lambda x: int(x[0]))

min_price = 0
milk_req = int(N)

for farmer in milk_prices:
    if milk_req >= farmer[1]:
        min_price = min_price + farmer[0] * farmer[1]
        milk_req = milk_req - farmer[1]
    else:
        min_price = min_price + farmer[0] * milk_req
        milk_req=0

    if milk_req == 0:
        break

fout.write(str(min_price) + '\n')


