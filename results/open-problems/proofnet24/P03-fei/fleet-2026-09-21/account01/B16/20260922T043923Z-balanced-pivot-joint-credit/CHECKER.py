import math, itertools, numpy as np

LN2 = math.log(2.0)

def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p*math.log2(p)-(1-p)*math.log2(1-p)

def walsh(vals):
    a=np.array(vals,dtype=float)
    out=a.copy()
    h=1
    while h<len(out):
        for i in range(0,len(out),2*h):
            x=out[i:i+h].copy()
            y=out[i+h:i+2*h].copy()
            out[i:i+h]=x+y
            out[i+h:i+2*h]=x-y
        h*=2
    return out/len(out)

def phi(x):
    x=max(0.0,min(1.0,x))
    y=math.sqrt(max(0.0,1-x*x))
    return h2((1-y)/2)-h2((1-x)/2)

def phi_prime(x):
    if x<=1e-12:
        return 0.0
    if x>=1:
        return float("inf")
    y=math.sqrt(max(0.0,1-x*x))
    if y>=1:
        return 0.0
    return (math.atanh(x)+(x/y)*math.atanh(y))/LN2

def credit_from_pair(a,b):
    T=(a*a+b*b)/2
    keep=T>1e-30
    Tk=T[keep]
    aa=a[keep]; bb=b[keep]
    c=2*aa*bb/(aa*aa+bb*bb)
    X=np.abs(c)
    rho=float(np.dot(Tk,c))
    delta=(1-rho)/2
    branch=0.0
    layer=0.0
    for ti,ai,bi,ci in zip(Tk,aa,bb,c):
        branch += float(ti)*h2(float(ai*ai/(ai*ai+bi*bi)))
        layer += float(ti)*h2(float((1-ci)/2))
    C = branch + h2(delta) - layer
    Ephi=float(sum(float(ti)*phi(float(xi)) for ti,xi in zip(Tk,X)))
    EX=float(np.dot(Tk,X))
    var=float(np.dot(Tk,(X-EX)**2))
    r=max(0.0,min(1.0,abs(rho)))
    strong=phi(r)
    if r < 1-1e-10:
        strong += phi_prime(r)*(EX-r)+var/(2*LN2)
    return C,h2(delta)+Ephi,r,EX,var,strong,Ephi,delta

max_id=0.0
min_strong=1e9
pairs=0
for n in range(1,4):
    N=1<<n
    funcs=[]
    for mask in range(1<<N):
        vals=[1.0 if ((mask>>x)&1)==0 else -1.0 for x in range(N)]
        funcs.append(walsh(vals))
    for a in funcs:
        for b in funcs:
            C,C2,r,EX,var,strong,Ephi,delta=credit_from_pair(a,b)
            max_id=max(max_id,abs(C-C2))
            min_strong=min(min_strong,Ephi-strong)
            pairs+=1

def vals_from_mask(n,mask):
    N=1<<n
    return np.array([1.0 if ((mask>>x)&1)==0 else -1.0 for x in range(N)])

balanced=[]
for m in range(16):
    v=vals_from_mask(2,m)
    if abs(v.mean())<1e-12:
        balanced.append(v)
allh=[vals_from_mask(2,m) for m in range(16)]
max_tube=0.0
tube_count=0
for g in balanced:
    for hv in allh:
        f0=np.array([g[x] for y in range(4) for x in range(4)])
        f1=np.array([g[x]*hv[y] for y in range(4) for x in range(4)])
        a=walsh(f0); b=walsh(f1)
        C,_,_,_,_,_,_,delta=credit_from_pair(a,b)
        bb=1-2*delta
        D=(1+bb*bb)/2
        expected = D*h2((0.5*bb*bb)/D) + h2(delta) - D*h2((delta*delta)/D) - 2*delta*(1-delta)
        max_tube=max(max_tube,abs(C-expected))
        tube_count+=1

print("PASS")
print("ordered_boolean_pairs_checked",pairs)
print("max_exact_credit_identity_error",format(max_id,".3e"))
print("min_strong_convexity_slack",format(min_strong,".3e"))
print("balanced_tensor_tubes_checked",tube_count)
print("max_tensor_tube_credit_error",format(max_tube,".3e"))
