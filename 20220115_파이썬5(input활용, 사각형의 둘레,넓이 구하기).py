#input활용, 사각형의 둘레,넓이 구하기
n = int(input("한변의 길이를 입력하세요!"))
print("정사각형의 둘레의 길이는=",n * 4)
print("정사각형의 넓이는의 길이는=",n * n)

a = int(input("가로의 길이를 입력하세요!"))
b = int(input("세로의 길이를 입력하세요!"))
print("\n직사각형의 둘레의 길이는=",a + a + b + b)
print("직사각형의 넓이의 길이는=",a * b)
