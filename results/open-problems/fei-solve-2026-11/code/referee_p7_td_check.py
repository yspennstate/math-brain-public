# TD(w,Q), Q prime, built as lines {(g, a+b*g mod Q) : g<w}; terms = the Q^2 blocks. Exact WHT, H/I and min E/Inf.
import sys, numpy as np
def wht(a):
    h=1; n=a.size
    while h<n:
        a=a.reshape(-1,2,h); a=np.stack([a[:,0]+a[:,1],a[:,0]-a[:,1]],1).reshape(-1); h*=2
    return a
def eta(x):
    o=np.zeros_like(x); m=x>0; o[m]=-x[m]*np.log2(x[m]); return o
w,Q=int(sys.argv[1]),int(sys.argv[2]); n=w*Q; N=1<<n
blocks=[sum(1<<(g*Q+(a+b*g)%Q) for g in range(w)) for a in range(Q) for b in range(Q)]
# linearity check
for i in range(len(blocks)):
    for j in range(i):
        assert bin(blocks[i]&blocks[j]).count('1')<=1
x=np.arange(N,dtype=np.int64); F=np.zeros(N,bool)
for t in blocks: F|=(x&t)==t
f=(1.0-2.0*F); fh=wht(f)/N; wt=fh*fh
size=np.zeros(N,np.int8)
for i in range(n): size+=((x>>i)&1).astype(np.int8)
H=eta(wt).sum(); I=(wt*size).sum()
mins=[]
for i in range(0,n,Q):   # one coordinate per group suffices by symmetry; check a second too
    for j in (i,i+1):
        lo=x[((x>>j)&1)==0]; p=wt[lo]; q=wt[lo|(1<<j)]
        mins.append(((eta(p)+eta(q)-eta(p+q)).sum())/q.sum())
print(f"TD({w},{Q}) n={n} terms={len(blocks)} P[F=0]={1-F.mean():.6f} H/I={H/I:.6f} minE/Inf(sampled)={min(mins):.6f} maxE/Inf={max(mins):.6f}")
