# PWM modulation 

Ra = 6800
Rb = 3900
Ca = 0.000000001
f = 1.44 / ((Ra + 2*Rb) * Ca)
t = 1/f
print(f)
print(t)

Cb=0.00000001
Rc = (10/4 * t)/Cb
print(Rc)

Rc = 2200
print(Rc*Cb)

#Rc = 10000
#Cb = (1/4 * t) / Rc
#print(Cb)