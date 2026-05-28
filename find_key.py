def countdown(i,key):
    print(i)
    if i == key:
        return print(f"La llave es: {i}")
    else:
        countdown(i-1, key)

countdown(100,32)