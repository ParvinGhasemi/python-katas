def d():
    color = "green"
    def e():
        nonlocal color
        print(color)
        color = "yellow"
    e()
    print("Color: " + color)
    color = "red"
color = "blue"
d()