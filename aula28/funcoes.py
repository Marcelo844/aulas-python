def divide(n1, n2)
    if n2 == 0:
        raise ValueError("O denominador não pode ser zero.")
    return n1 / n2

print divide(5,0)