import matplotlib.pyplot as plt
r = 3
x , y = 0 , r
p = 1 - r

xcd = [x]
ycd = [y]
i = 0
while x < y:
  i += 1
  if p < 0:
    x += 1
    p = p + 2*x + 1
  else:
    x += 1
    y -= 1
    p = p + 2*x - 2*y + 1
  print("X0: ", format(x, ".1f"), "Y0", y)
  xcd.append(x)
  ycd.append(y)
plt.scatter(xcd, ycd, s=40)
plt.axis('equal')  # Ensure aspect ratio is maintained
plt.title("Mid point of a Circle")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()