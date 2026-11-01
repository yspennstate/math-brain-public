import numpy as np, math
def a_of_n(n):
    h=np.zeros(n+1); h[1:]=np.cumsum(1.0/np.arange(1,n+1))
    a=np.zeros(n+1); a[n]=1.0
    for m in range(n-1,0,-1):
        idx=np.arange(m+1,n+1)
        a[m]=np.dot(a[idx], 1.0/(h[idx-1]*(idx-m)))
    return a
def a_lim(m):
    return 6*(np.cumsum(1.0/np.arange(1,m))[-1])/(math.pi**2*(m-1))
NS=[256,512,1024,2048]
A={n:a_of_n(n) for n in NS}
print("check a(n,m) -> a(m):")
for n in NS: print(f"  n={n:<5} a(n,2)={A[n][2]:.5f} (limit {a_lim(2):.5f})   a(n,5)={A[n][5]:.5f} (limit {a_lim(5):.5f})")
al=np.zeros(400001)
h=np.cumsum(1.0/np.arange(1,400001))
for m in range(2,400001): al[m]=6*h[m-2]/(math.pi**2*(m-1))
def series(f,N=400000): return sum(al[i]*f(i) for i in range(2,N))
tests={
 "1{j=2^r}   (my counterexample: bounded, f(n) does NOT ->0)": lambda j: 1.0 if (j>1 and (j&(j-1))==0) else 0.0,
 "j^-0.5     (f(n)->0)": lambda j: j**-0.5,
 "1/log(j)^3 (f(n)->0 slowly)": lambda j: 1.0/math.log(j)**3 if j>=3 else 0.0,
}
for name,f in tests.items():
    S=series(f)
    print(f"\n  f = {name}\n    limit series (to 4e5) = {S:.6f}")
    for n in NS:
        tot=float(np.dot(A[n][2:n+1], np.array([f(i) for i in range(2,n+1)])))
        print(f"      n={n:<5} sum a(n,i)f(i) = {tot:.6f}   gap = {tot-S:+.6f}   f(n)={f(n):.4f}")
