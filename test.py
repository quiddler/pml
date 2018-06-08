import matplotlib.pyplot as plt 
import numpy as np

########################################################################## FIB SEQUENCE
def fibSqn(n):
    a = [0, 1]
    for i in range(2, n + 1):
        a.append(a[i - 1] + a[i - 2])
    return a

########################################################################## FIB VALUE AT X
def fibAt(n):
    if n == 0: return 0
    if n == 1: return 1
    a = [0, 1]
    for i in range(2, n +  1):
        a.append(a[i - 1] + a[i - 2])
    return a[-1]

########################################################################## TEST
ans = []
for i in range(50):
    ans.append( [fibAt(i), i] )

ans = np.array(ans, dtype=np.float).reshape((len(ans), 2))

print(ans)

plt.plot(np.sin(ans))
plt.show()

ans = fibSqn(50)
print(ans)

x = np.linspace(0, 2 * np.pi, 50)
print(x)
plt.plot(np.sin(x), label="sin")
plt.plot(np.cos(x), label="cos")
plt.ylabel('amplitude')
plt.xlabel('radians')
plt.title('Sin and Cos')
plt.legend(loc='best')
plt.show()

