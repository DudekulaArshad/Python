x=int(input())
y=int(input())
point=(x,y)
match point:
  case (0, 0):
    print("Origin")
  case (0, y):
    print(f"Y-axis at {y}")
  case (x, 0):
    print(f"X-axis at {x}")
  case (x, y):
    print(f"Point at ({x}, {y})")
