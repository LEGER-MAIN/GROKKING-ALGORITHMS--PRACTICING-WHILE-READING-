def countdown(i,key):
    print(i)
    if i == key:
        return "La llave es: f{i}"
    else:
        countdown(i-1, key)

countdown(100,32)