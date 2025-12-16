v = 0
u = 10
g = -9.8
t = 0.0001

for step in range(100):
    v += g * t 
    u += v * t
    print(f"x: {v}, y: {u}")