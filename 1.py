def generate_p_triangle(n):
    p_triangle = []

    for i in range(n):
        row = [1] * (i + 1)  # Инициализируем строку единицами
        if p_triangle:
            last_row = p_triangle[-1]
            for j in range(1, i):
                row[j] = last_row[j - 1] + last_row[j]
        p_triangle.append(row)

    return p_triangle

def print_p_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)).center(len(triangle[-1]) * 3))

n = int(input("Введите количество строк треугольника Паскаля: "))
p_triangle = generate_p_triangle(n)
print_p_triangle(p_triangle)
