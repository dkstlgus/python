#리스트(변수 추가,변수 삭제)
bp = ["지수", "로제", "리사", "제니"]
list = [10, 20, 30, 40]

print(bp)
print(list)

print(bp[0])
print(bp[1])
print(bp[2])
print(bp[3])

list.append(999)
print(list)

list.append(1000)
print(list)

del(list[2])
print(list)
