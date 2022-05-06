# VIRUS GOAT FILE
print("Goat file. Originally 27 lines long.")

s_init = 0 # m
v_init = 8 # m s-1
t_init = 0 # s
t_end = 0 # s
fineness = 1000

t = t_init
v = v_init
s = s_init
#dt = (t_end - t_init)/fineness
dt = 0.0001

#while t < t_end:
while v >= 0:
    a = -1.042 # accel function, m s-2
    v += a * dt
    s += v * dt
    t += dt

print("s:", s)
print("v:", v)
print("a_final", a)
print("t:", t)
