import numpy as np, math
def a_of_n(n):
    h=np.zeros(n+1); h[1:]=np.cumsum(1.0/np.arange(1,n+1))
    a=np.zeros(n+1); a[n]=1.0
    for m in range(n-1,0,-1):
        idx=np.arange(m+1,n+1)
        a[m]=np.dot(a[idx],1.0/(h[idx-1]*(idx-m)))
    return a
NS=list(range(6,1400))
print("Source's conjecture (its 'technical obstacle' section): n -> a(n,i) is DECREASING for each i>=2.")
A={n:a_of_n(n) for n in [6,8,12,16,24,32,48,64,96,128,192,256,384,512,768,1024,1350]}
ns=sorted(A)
bad=0; checked=0
for i in [2,3,5,8,13,21,34,55,89]:
    seq=[(n,A[n][i]) for n in ns if n>i]
    viol=[(seq[k][0],seq[k+1][0]) for k in range(len(seq)-1) if seq[k+1][1]>seq[k][1]+1e-12]
    checked+=len(seq)-1; bad+=len(viol)
    print(f"  i={i:<3} a(n,i) over n={seq[0][0]}..{seq[-1][0]}: {seq[0][1]:.6f} -> {seq[-1][1]:.6f}  limit {6*sum(1.0/k for k in range(1,i))/(math.pi**2*(i-1)):.6f}  violations of monotonicity: {len(viol)}")
print(f"\n  total consecutive pairs checked: {checked}, decreasing failures: {bad}")
print("\nAnd the diagonal, which is why dominated convergence cannot work unmodified:")
for i in [2,5,13,55]:
    print(f"  i={i:<3}  a(i,i)=1 exactly, but a(i) = {6*sum(1.0/k for k in range(1,i))/(math.pi**2*(i-1)):.6f}   ratio sup_n a(n,i)/a(i) = {1/(6*sum(1.0/k for k in range(1,i))/(math.pi**2*(i-1))):.2f}")
