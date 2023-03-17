import numpy as np
import cmath
from scipy.integrate import solve_ivp

W=1
G=1
gam=G/2
delt=0
print(complex(1j))
# Определение функции
def system_of_equations(drdt, t, r):
       
    drdt[1] =1j*W/2*(r[2]-r[3])+G*r[4]
    drdt[4] =-1j*W/2*(r[2]-r[3])-G*r[4]
    drdt[2] =-(gam+1j*delt)*r[2]-1j*W/2*(r[4]-r[1])
    drdt[3]=np.conj(r[2])
    return drdt


r0 = [1+0j,0+0j,0+0j,0+0j] # Начальные значения переменных
t_span = [0, 10] # Интервал интегрирования
print(r0)

# Решение системы уравнений
sol = solve_ivp(system_of_equations, t_span, r0)

# Вывод результатов
print(sol.t) # Значения времени, 