"""What is the exact relation between the block mass B_n and the octave integral?

B_n   = int over [(3/2)^n, (3/2)^(n+1)) of Q(v)^2 dv,  Q(u) = prod_(j>=0) cos(pi (2/3)^j u)
J_n   = int over [1/3, 2/3] of prod_(m<=n) (1 + cos 2 pi theta (3/2)^m) d theta
I_n   = 3 J_n   (the same integral in x = 3 theta over [1,2])
The paper now asserts B_K = (3/4)^K I_K / 2. Test it, and if false find the true constant.
"""
import numpy as np

def Qsq_block(n, ppu=400):
    lo, hi = 1.5**n, 1.5**(n+1)
    N = max(20000, int((hi-lo)*ppu))
    v = lo + (np.arange(N)+0.5)*(hi-lo)/N
    q = np.ones(N); j = 0
    while True:
        a = (2.0/3.0)**j * v
        q *= np.cos(np.pi*a); j += 1
        if a.max() < 1e-9: break
    return (q*q).sum()*(hi-lo)/N

def J(n, N=4_000_000):
    th = 1/3 + (np.arange(N)+0.5)/N/3.0
    p = np.ones(N)
    for m in range(n+1):
        p *= 1.0 + np.cos(2*np.pi*np.mod(th*1.5**m, 1.0))
    return p.sum()/N/3.0

print(f"{'n':>3} {'B_n':>13} {'J_n':>11} {'B_n/((3/4)^n J_n)':>20} {'B_n/((3/4)^n I_n)':>20}")
for n in (8, 10, 12, 14):
    B = Qsq_block(n); Jn = J(n)
    r1 = B/((0.75**n)*Jn); r2 = B/((0.75**n)*3*Jn)
    print(f"{n:>3} {B:>13.6e} {Jn:>11.6f} {r1:>20.6f} {r2:>20.6f}")
print()
print("paper asserts B_K = (3/4)^K I_K / 2, i.e. the last column should be 0.5")
