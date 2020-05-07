def sp(V, m, h):
    if h == "":
        h = V / m
        print(h)
    elif m == "":
        m = h * V
        print(m)
    elif V == "":
        V = m / h
        print(V)
