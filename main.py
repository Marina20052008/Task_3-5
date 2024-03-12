N = int(input("Ширина басейну (N): "))
M = int(input("Довжина басейну (M): "))
x = int(input("Відстань до довгого бортика (x): "))
y = int(input("Відстань до короткого бортика (y): "))

min_distance = min(x, y, N - x, M - y)

print(min_distance)
