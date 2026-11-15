"""Fresh matching implementation plus an independently built prefix automaton.
No imports or reads from claim_files/code. All numerical calls use one thread.
"""
import os
os.environ.update(OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', VECLIB_MAXIMUM_THREADS='1', MKL_NUM_THREADS='1', NUMEXPR_NUM_THREADS='1')
import math, csv, time, resource, sys
from fractions import Fraction
from collections import deque
import numpy as np
import scipy.linalg as la
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve
# Memory bounded structurally: k <= 4200; largest dense arrays below 150 MB each.

def family(n,a,fp):
    ans=[]
    for w in range(1<<n):
        if 2*w.bit_count()-n != a: continue
        if fp:
            h=0; ok=True
            for t in range(n):
                if h<=a: ok=False; break
                h+=2*((w>>(n-1-t))&1)-1
            if not ok: continue
        ans.append(w)
    return np.array(ans,dtype=np.int64)

def matrix(n,words):
    k=len(words); assert k <= 4200; c=np.zeros((k,k),dtype=np.int64)
    for shift in range(n):
        pre=words>>shift
        suf=words & ((1<<(n-shift))-1)
        c+=(pre[:,None]==suf[None,:])*(1<<(n-shift))
    return c

def rational_mean(c):
    # Bareiss elimination of [C|1], followed by exact back-substitution.
    k=len(c); a=[list(map(int,row))+[1] for row in c]
    prev=1
    for j in range(k-1):
        if a[j][j]==0:
            p=next(i for i in range(j+1,k) if a[i][j])
            a[j],a[p]=a[p],a[j]
        pivot=a[j][j]
        for i in range(j+1,k):
            factor=a[i][j]
            for h in range(j+1,k+1):
                val=pivot*a[i][h]-factor*a[j][h]
                assert val%prev==0
                a[i][h]=val//prev
            a[i][j]=0
        prev=pivot
    sol=[Fraction(0)]*k
    for i in range(k-1,-1,-1):
        sol[i]=(Fraction(a[i][k])-sum(a[i][h]*sol[h] for h in range(i+1,k)))/a[i][i]
    return 1/sum(sol)

def automaton_mean(n,words):
    # Aho-Corasick states are proper prefixes. Terminal transitions are killed.
    child=[{}]; terminal=[False]
    for w in words:
        s=0
        for t in range(n):
            b=int((w>>(n-1-t))&1)
            if b not in child[s]:
                child[s][b]=len(child); child.append({}); terminal.append(False)
            s=child[s][b]
        terminal[s]=True
    fail=[0]*len(child); trans=np.zeros((len(child),2),dtype=np.int32)
    q=deque()
    for b,s in child[0].items(): trans[0,b]=s; q.append(s)
    while q:
        s=q.popleft()
        for b in (0,1):
            if b in child[s]:
                u=child[s][b]; fail[u]=int(trans[fail[s],b]); trans[s,b]=u; q.append(u)
            else: trans[s,b]=trans[fail[s],b]
    live=[s for s in range(len(child)) if not terminal[s]]
    ids={s:i for i,s in enumerate(live)}
    row=list(range(len(live))); col=row.copy(); values=[1.]*len(live)
    for s in live:
        for u in trans[s]:
            if not terminal[u]: row.append(ids[s]); col.append(ids[int(u)]); values.append(-.5)
    a=coo_matrix((values,(row,col)),shape=(len(live),len(live))).tocsc()
    e=spsolve(a,np.ones(len(live)))
    return float(e[0]),len(live),float(np.max(np.abs(a@e-1)))

def main():
    print('nice',os.getpriority(os.PRIO_PROCESS,0),flush=True)
    cases=[]
    for n in (2,3,4,5,6,7,8,10,12,14):
        for alpha in (0.,.5,1.,-1.,-2.):
            cases.append((n,'BR' if alpha>=0 else 'FP',alpha))
    for n in (16,17): cases.append((n,'FP',-1.))
    cols=['n','family','alpha','endpoint','words','mean','mean_over_n','mean_over_n_log_n','rational','automaton_mean','automaton_states','automaton_residual','matrix_residual']
    extra='--extra' in sys.argv
    if extra: cases=[(17,'FP',-1.)]
    with open('data/independent_exact.csv','a' if extra else 'w') as f:
        writer=csv.DictWriter(f,fieldnames=cols)
        if not extra: writer.writeheader()
        for n,kind,alpha in cases:
            a=math.floor(alpha*math.sqrt(n)); a+=(n-a)%2
            if abs(a)>n or (kind=='FP' and a>=0): continue
            start=time.monotonic(); words=family(n,a,kind=='FP'); k=len(words)
            count=math.comb(n,(n+a)//2)
            if kind=='FP': count=count*(-a)//n
            assert count==k and k
            c=matrix(n,words)
            expected=[]
            for word in words:
                total=1.
                for l in range(1,n):
                    b=2*int(word>>(n-l)).bit_count()-l
                    if kind=='BR': total+=math.comb(l,(l+b)//2)/2**l
                    elif b<0: total+=(-b/l)*math.comb(l,(l-b)//2)/2**l
                expected.append(total)
            assert np.max(np.abs(c.sum(axis=0)/2**n-expected))<1e-11
            v=la.solve(c.astype(float),np.ones(k),check_finite=False)
            e=1/float(sum(v)); residual=float(np.max(np.abs(np.einsum('ij,j->i',c,v)-1)))
            assert v.min()>-1e-12
            rat=str(rational_mean(c)) if n<=8 and k<=70 else ''
            if rat: assert abs(float(Fraction(rat))-e)<1e-9
            ac,states,ar=automaton_mean(n,words) if n<=12 else ('','','')
            if ac: assert abs(ac-e)<1e-8
            out=dict(zip(cols,[n,kind,alpha,a,k,e,e/n,e/(n*math.log(n)),rat,ac,states,ar,residual]))
            writer.writerow(out); f.flush()
            print(n,kind,alpha,a,k,round(e,10),rat,'seconds',round(time.monotonic()-start,2),flush=True)
    print('peak_rss',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,flush=True)
if __name__=='__main__': main()
