import math, random

def h2(x):
    if x<=0.0 or x>=1.0: return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)

def jfun(q):
    if q<=0.0: return 0.0
    if q>=0.5: return 1.0
    return 1-h2(0.5+math.sqrt(q*(1-q)))

def jprime(q):
    if q<=1e-14: return 2/math.log(2)
    if q>=0.5-1e-14: return 0.0
    s=math.sqrt(q*(1-q)); y=0.5+s
    return -math.log2((1-y)/y)*(1-2*q)/(2*s)

def fwht(vals):
    a=[float(v) for v in vals]; N=len(a); h=1
    while h<N:
        for i in range(0,N,2*h):
            for k in range(i,i+h):
                x=a[k]; y=a[k+h]; a[k]=x+y; a[k+h]=x-y
        h*=2
    return [x/N for x in a]

def influences(vals,n):
    N=1<<n; out=[]
    for i in range(n):
        c=0; b=1<<i
        for x in range(N): c += vals[x]!=vals[x^b]
        out.append(c/N)
    return out

def center(vals,n):
    inf=influences(vals,n); mask=0
    for i,p in enumerate(inf):
        if p>0.5+1e-15: mask|=1<<i
    if mask==0: return tuple(vals)
    return tuple(-v if ((x&mask).bit_count()&1) else v for x,v in enumerate(vals))

def stats(vals,n):
    vals=center(vals,n); a=fwht(vals); p=[x*x for x in a]
    H=-sum(z*math.log2(z) for z in p if z>0)
    q=[min(x,1-x) for x in influences(vals,n)]
    J=sum(q); P=sum(jfun(x) for x in q); F=H-P
    return vals,H,J,P,F,q,p

def restrict_vals(vals,n,A,ass):
    A=sorted(A); rem=[i for i in range(n) if i not in A]
    out=[0]*(1<<len(rem))
    for y in range(1<<len(rem)):
        x=0
        for r,i in enumerate(A):
            if ass>>r&1: x|=1<<i
        for r,i in enumerate(rem):
            if y>>r&1: x|=1<<i
        out[y]=vals[x]
    return tuple(out),rem

def subset_entropy(p,n,coords):
    coords=list(coords); mass={}
    for s,z in enumerate(p):
        key=sum(((s>>i)&1)<<r for r,i in enumerate(coords))
        mass[key]=mass.get(key,0.0)+z
    return -sum(z*math.log2(z) for z in mass.values() if z>0)

def block_data(parent,n,A,st=None):
    if st is None: st=stats(parent,n)
    vals,H,J,P,F,q,p=st; A=set(A); Ac=[i for i in range(n) if i not in A]
    B=H-subset_entropy(p,n,Ac); avgF=avgJ=0.0; avgq={j:0.0 for j in Ac}; den=1<<len(A)
    for ass in range(den):
        ch,rem=restrict_vals(vals,n,A,ass); _,_,jc,_,fc,qc,_=stats(ch,len(rem))
        avgF+=fc/den; avgJ+=jc/den
        for r,j in enumerate(rem): avgq[j]+=qc[r]/den
    dF=F-avgF; D=J-avgJ; I=sum(q[i] for i in A)
    c={j:q[j]-avgq[j] for j in Ac}; C=sum(c.values()); W=sum(jprime(q[j])*c[j] for j in Ac)
    K=B-W-dF; rho=F/J if J>1e-15 else 0.0; R=dF-rho*D
    return dict(B=B,D=D,I=I,C=C,W=W,K=K,R=R,c=c)

def partitions(n):
    parts=[[]]
    for x in range(n):
        new=[]
        for p in parts:
            new.append(p+[(x,)])
            for k in range(len(p)):
                q=[tuple(b) for b in p]; q[k]=tuple(sorted(q[k]+(x,))); new.append(sorted(q))
        seen=set(); parts=[]
        for p in new:
            key=tuple(sorted(tuple(sorted(b)) for b in p))
            if key not in seen: seen.add(key); parts.append(list(key))
    return [[set(b) for b in p] for p in parts]

def masks_to_vals(n,mask):
    N=1<<n; vals=[1]*N
    for x in range(1,N):
        if mask>>(x-1)&1: vals[x]=-1
    return tuple(vals)

max_ledger=0.0; min_K=1e9; ledgers=0; curvature_checks=0
for n in range(2,4):
    ps=partitions(n)
    for mask in range(1<<((1<<n)-1)):
        vals=masks_to_vals(n,mask); st=stats(vals,n)
        if st[2]<=1e-15: continue
        rho=st[4]/st[2]; cache={}
        for A_mask in range(1,(1<<n)-1):
            A={i for i in range(n) if A_mask>>i&1}; d=block_data(vals,n,A,st); cache[A_mask]=d
            min_K=min(min_K,d['K']); curvature_checks+=1
        for pi in ps:
            if len(pi)==1: continue
            dtc=st[1]-sum(cache[sum(1<<i for i in A)]['B'] for A in pi)
            rhs=dtc+sum(rho*cache[sum(1<<i for i in A)]['C']+cache[sum(1<<i for i in A)]['W']+cache[sum(1<<i for i in A)]['K']+cache[sum(1<<i for i in A)]['R'] for A in pi)
            max_ledger=max(max_ledger,abs(st[3]-rhs)); ledgers+=1

n=4; ps=partitions(n); rng=random.Random(130956)
for _ in range(2048):
    vals=masks_to_vals(n,rng.getrandbits((1<<n)-1)); st=stats(vals,n)
    if st[2]<=1e-15: continue
    rho=st[4]/st[2]; cache={}
    for A_mask in range(1,(1<<n)-1):
        A={i for i in range(n) if A_mask>>i&1}; d=block_data(vals,n,A,st); cache[A_mask]=d
        min_K=min(min_K,d['K']); curvature_checks+=1
    for pi in ps:
        if len(pi)==1: continue
        dtc=st[1]-sum(cache[sum(1<<i for i in A)]['B'] for A in pi)
        rhs=dtc+sum(rho*cache[sum(1<<i for i in A)]['C']+cache[sum(1<<i for i in A)]['W']+cache[sum(1<<i for i in A)]['K']+cache[sum(1<<i for i in A)]['R'] for A in pi)
        max_ledger=max(max_ledger,abs(st[3]-rhs)); ledgers+=1

crit_min_R=1e9; max_ratios={}
for n in range(2,5):
    best=(-1,None,None)
    for mask in range(1<<((1<<n)-1)):
        vals=masks_to_vals(n,mask); st=stats(vals,n)
        if st[2]>1e-15 and st[4]/st[2]>best[0]+1e-13: best=(st[4]/st[2],vals,st)
    max_ratios[n]=best[0]; vals,st=best[1],best[2]
    for A_mask in range(1,(1<<n)-1):
        A={i for i in range(n) if A_mask>>i&1}; crit_min_R=min(crit_min_R,block_data(vals,n,A,st)['R'])

max_gauge=0.0; gauge_checks=0
for n in range(2,4):
    for mask in range(1<<((1<<n)-1)):
        vals=masks_to_vals(n,mask); st0=stats(vals,n)
        for T in range(1<<n):
            gv=tuple(-v if ((x&T).bit_count()&1) else v for x,v in enumerate(vals)); st1=stats(gv,n)
            max_gauge=max(max_gauge,abs(st0[1]-st1[1]),abs(st0[2]-st1[2]),abs(st0[3]-st1[3]))
            for A_mask in range(1,(1<<n)-1):
                A={i for i in range(n) if A_mask>>i&1}; d0=block_data(vals,n,A,st0); d1=block_data(gv,n,A,st1)
                max_gauge=max(max_gauge,abs(d0['B']-d1['B']),abs(d0['C']-d1['C']),abs(d0['W']-d1['W'])); gauge_checks+=1

def tensor(v1,n1,v2,n2): return tuple(v1[x&((1<<n1)-1)]*v2[x>>n1] for x in range(1<<(n1+n2)))
def comp_block(v,n,A,st):
    if not A: return {'B':0.0,'D':0.0,'C':0.0,'W':0.0,'K':0.0}
    if len(A)==n: return {'B':st[1],'D':st[2],'C':0.0,'W':0.0,'K':st[3]}
    return block_data(v,n,A,st)
max_tensor=0.0; tensor_checks=0; funcs2=[masks_to_vals(2,m) for m in range(1<<3)]
for v1 in funcs2:
    for v2 in funcs2:
        prod=tensor(v1,2,v2,2); stp=stats(prod,4); s1=stats(v1,2); s2=stats(v2,2)
        max_tensor=max(max_tensor,abs(stp[1]-(s1[1]+s2[1])),abs(stp[2]-(s1[2]+s2[2])),abs(stp[3]-(s1[3]+s2[3])),abs(stp[4]-(s1[4]+s2[4])))
        for A_mask in range(1,15):
            A={i for i in range(4) if A_mask>>i&1}; dp=block_data(prod,4,A,stp)
            d1=comp_block(v1,2,{i for i in A if i<2},s1); d2=comp_block(v2,2,{i-2 for i in A if i>=2},s2)
            for key in ('B','D','C','W','K'): max_tensor=max(max_tensor,abs(dp[key]-(d1[key]+d2[key])))
            tensor_checks+=1

min_terminal=float('inf')
for n in range(8,65):
    q=2.0**(2-n); jp=jprime(q)
    min_terminal=min(min_terminal,h2(q)-4*q,(n-1)*h2(q)-jp*q-4*n*q)

assert max_ledger<2e-9 and min_K>-2e-9 and crit_min_R>-2e-9 and max_gauge<2e-9 and max_tensor<2e-9 and min_terminal>0
print('PASS')
print('ledger_checks',ledgers,'max_ledger_error',format(max_ledger,'.3e'))
print('curvature_checks',curvature_checks,'min_K',format(min_K,'.3e'))
print('max_ratios_n2_n4',max_ratios,'critical_min_R',format(crit_min_R,'.3e'))
print('gauge_checks',gauge_checks,'max_gauge_error',format(max_gauge,'.3e'))
print('tensor_checks',tensor_checks,'max_tensor_error',format(max_tensor,'.3e'))
print('two_point_n8_64_min_K4_terminal_slack',format(min_terminal,'.12g'))
print('two_point_normalized_depth_defect',0.5)
print('two_point_U4_over_J_at_n64',format(2*(64-1)*(4+jprime(2.0**(2-64))),'.12g'))
