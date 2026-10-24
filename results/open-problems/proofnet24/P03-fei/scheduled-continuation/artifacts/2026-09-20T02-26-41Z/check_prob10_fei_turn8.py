import math, json, hashlib, random
from functools import lru_cache
from fractions import Fraction

LN2=math.log(2.0)
C=2.0/LN2

def walsh_int(vals):
    h=list(map(int,vals)); N=len(h); step=1
    while step<N:
        for i in range(0,N,2*step):
            for j in range(step):
                a=h[i+j]; b=h[i+j+step]
                h[i+j]=a+b; h[i+j+step]=a-b
        step*=2
    return h

def spectral_masses(vals):
    N=len(vals); h=walsh_int(vals); D=N*N
    return [Fraction(a*a,D) for a in h]

def restrict_vals(vals,n,i,bit):
    out=[]
    for y in range(1<<(n-1)):
        low=y & ((1<<i)-1); high=y>>i
        x=low | (bit<<i) | (high<<(i+1))
        out.append(vals[x])
    return tuple(out)

def inf_i(vals,n,i):
    mask=1<<i; N=1<<n; c=0
    for x in range(N):
        if not (x&mask) and vals[x]!=vals[x|mask]: c+=2
    return Fraction(c,N)

def total_inf(vals):
    n=(len(vals)).bit_length()-1
    return sum((inf_i(vals,n,i) for i in range(n)), Fraction(0))

def pair_stats(vals,n,i):
    p=spectral_masses(vals); mask=1<<i
    K=B=0.0; E=Fraction(0)
    for s in range(1<<n):
        if s&mask: continue
        a=p[s]; b=p[s|mask]
        E += min(a,b)
        af=float(a); bf=float(b); m=af+bf
        if af>0 and bf>0:
            K += float(min(a,b))*abs(math.log2(af/bf))
        if af>0: B += af*math.log2(m/af)
        if bf>0: B += bf*math.log2(m/bf)
    return K,B,E

def entropy(vals):
    p=spectral_masses(vals); H=0.0
    for x in p:
        y=float(x)
        if y>0: H += y*math.log2(1/y)
    return H

@lru_cache(None)
def Kstar(vals):
    vals=tuple(vals); n=(len(vals)).bit_length()-1
    if all(v==vals[0] for v in vals): return 0.0
    best=float('inf')
    for i in range(n):
        if inf_i(vals,n,i)==0: continue
        k,_,_=pair_stats(vals,n,i)
        v0=restrict_vals(vals,n,i,0); v1=restrict_vals(vals,n,i,1)
        best=min(best,k+0.5*(Kstar(v0)+Kstar(v1)))
    return best

@lru_cache(None)
def Rstar(vals):
    vals=tuple(vals); n=(len(vals)).bit_length()-1
    if all(v==vals[0] for v in vals): return 0.0
    best=float('inf')
    for i in range(n):
        if inf_i(vals,n,i)==0: continue
        _,b,_=pair_stats(vals,n,i)
        v0=restrict_vals(vals,n,i,0); v1=restrict_vals(vals,n,i,1)
        best=min(best,b+0.5*(Rstar(v0)+Rstar(v1)))
    return best

def tensor(f,g):
    # bits of f first, then g; pointwise product
    nf=(len(f)).bit_length()-1; ng=(len(g)).bit_length()-1
    out=[]
    for y in range(1<<ng):
        for x in range(1<<nf): out.append(f[x]*g[y])
    return tuple(out)

def one_defect(n):
    return tuple([-1]+[1]*((1<<n)-1))

def one_defect_Kstar_formula(n):
    s=0.0
    for m in range(2,n+1):
        if m==2: term=0.0
        else: term=(2.0**(-m))*math.log2(2**(m-1)-1)
        s += term
    return 8.0*(2.0**(-n))*s

def canalyzing(g,c=1):
    # old y low bits, selector z high bit: z=0 -> c, z=1 -> g
    N=len(g); out=[]
    out.extend([c]*N); out.extend(g)
    return tuple(out)

res={"status":"PASS","scope":"Self-checks only; universal claims rely on written proofs. No independent audit or Lean verification."}

# 1. exhaustive local/tree inequalities through n=4
counts=0; max_gap=0.0; max_kstar_ratio={}
for n in range(1,5):
    N=1<<n; maxr=0.0
    # fix first truth value +1 to quotient global sign
    for bits in range(1<<(N-1)):
        vals=tuple([1]+[1 if ((bits>>(j-1))&1) else -1 for j in range(1,N)])
        I=float(total_inf(vals)); H=entropy(vals); ks=Kstar(vals); rs=Rstar(vals)
        if I>0: maxr=max(maxr,ks/I)
        if not (ks <= rs+1e-11): raise AssertionError(("Kstar<=Rstar",n,bits,ks,rs))
        if not (rs <= ks+C*I+1e-10): raise AssertionError(("Rstar upper",n,bits,rs,ks,I))
        if not (H <= ks+2*C*I+2e-10): raise AssertionError(("H upper",n,bits,H,ks,I))
        for i in range(n):
            k,b,e=pair_stats(vals,n,i); ji=min(inf_i(vals,n,i),1-inf_i(vals,n,i))
            if k>b+1e-11: raise AssertionError(("k<=B",n,bits,i,k,b))
            if b>k+C*float(ji)+1e-10: raise AssertionError(("B upper",n,bits,i,k,b,ji))
            if e>ji: raise AssertionError(("Bayes<=j",n,bits,i,e,ji))
            counts += 1
    max_kstar_ratio[str(n)]=maxr
res["exhaustive_tree_dimensions"]="1..4"
res["local_coordinate_checks"]=counts
res["max_Kstar_over_I_by_dimension"]=max_kstar_ratio

# 2. tensorization checks for all canonical functions through n<=2 pairs
funcs=[]
for n in (1,2):
    N=1<<n
    for bits in range(1<<(N-1)):
        funcs.append(tuple([1]+[1 if ((bits>>(j-1))&1) else -1 for j in range(1,N)]))
tc=0; maxerr=0.0
for f in funcs:
    for g in funcs:
        lhs=Kstar(tensor(f,g)); rhs=Kstar(f)+Kstar(g)
        maxerr=max(maxerr,abs(lhs-rhs)); tc+=1
        if abs(lhs-rhs)>1e-10: raise AssertionError(("tensor",lhs,rhs))
res["tensorization_checks"]=tc; res["tensorization_max_abs_error"]=maxerr

# 3. one-defect formula and explicit normalized bound
rows=[]
for n in range(2,21):
    ks=one_defect_Kstar_formula(n); I=2*n/(2**n); ratio=ks/I
    if ratio>=4/n+1e-12: raise AssertionError(("one-defect bound",n,ratio,4/n))
    row={"n":n,"Kstar_formula":ks,"I":I,"ratio":ratio,"upper_4_over_n":4/n}
    if n<=6:
        kd=Kstar(one_defect(n)); row["direct_Kstar"]=kd; row["formula_error"]=abs(kd-ks)
        if abs(kd-ks)>1e-11: raise AssertionError(("one-defect formula",n,kd,ks))
    rows.append(row)
res["one_defect_rows"]=rows

# 4. butterfly posterior-error obstruction analytic certificates
brows=[]
for m in range(2,13):
    eps=Fraction(1,2**(2*m))
    # Bayes error exactly eps; K/eps >= 2 log2(2^m-1)
    lower=2*math.log2(2**m-1)
    if lower < 2*m-2-1e-12: raise AssertionError(("butterfly lower",m,lower))
    brows.append({"m":m,"epsilon":str(eps),"Bayes_error":str(eps),"K_over_error_lower":lower,"simple_lower":2*m-2})
res["butterfly_posterior_obstruction"]=brows

# 5. canalyzing local K formula direct checks for all old children through n<=3
cc=0; maxerr=0.0; maxratio=0.0
for n in range(0,4):
    N=1<<n
    total=1<<N
    # all functions; quotient unnecessary small
    for bits in range(total):
        g=tuple(1 if (bits>>j)&1 else -1 for j in range(N))
        for c in (-1,1):
            F=canalyzing(g,c); nn=n+1; z=n
            k,_,_=pair_stats(F,nn,z)
            delta=sum(1 for v in g if v!=c)/N
            j=min(delta,1-delta)
            formula=0.0 if j in (0,0.5) else 2*j*j*math.log2((1-j)/j)
            # at j=1/2 ratio masses equal => log=0
            maxerr=max(maxerr,abs(k-formula)); cc+=1
            if abs(k-formula)>1e-10: raise AssertionError(("canalyzing formula",n,bits,c,k,formula,delta))
            if delta>0: maxratio=max(maxratio,k/delta)
res["canalyzing_selector_checks"]=cc; res["canalyzing_formula_max_abs_error"]=maxerr; res["max_observed_Kz_over_selector_influence"]=maxratio

# script hash filled externally by launcher
print(json.dumps(res,indent=2,sort_keys=True))
