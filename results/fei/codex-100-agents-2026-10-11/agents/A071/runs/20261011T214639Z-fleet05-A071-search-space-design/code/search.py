import argparse, hashlib, itertools, json, math, time
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCALE = 1 << 80
OUTSCALE = 1 << 60
TERMS = 32

def ln_unit(a, b):
    # 1 <= a/b <= 2. Positive atanh series, each term rounded down.
    u, v = a-b, a+b
    lo = 0
    for j in range(TERMS):
        lo += (2*SCALE*pow(u, 2*j+1)) // ((2*j+1)*pow(v, 2*j+1))
    # R <= 2 y^(2N+1)/((2N+1)(1-y^2)).
    rn = 2*SCALE*pow(u,2*TERMS+1)*v*v
    rd = (2*TERMS+1)*pow(v,2*TERMS+1)*(v*v-u*u)
    return lo, lo+TERMS+(rn+rd-1)//rd

LN2 = ln_unit(2,1)

@lru_cache(None)
def log_interval(p):
    a,b = p.numerator,p.denominator
    if a & (a-1) == 0 and b & (b-1) == 0:
        z=(a.bit_length()-b.bit_length())*OUTSCALE
        return z,z
    k=a.bit_length()-b.bit_length()
    aa,bb=(a,b<<k) if k>=0 else (a<<(-k),b)
    if aa<bb:
        k-=1
        aa,bb=(a,b<<k) if k>=0 else (a<<(-k),b)
    l,h=ln_unit(aa,bb)
    if k>=0: l,h=l+k*LN2[0],h+k*LN2[1]
    else: l,h=l+k*LN2[1],h+k*LN2[0]
    corners=[F(x*OUTSCALE,y) for x in (l,h) for y in LN2]
    low,high=min(corners),max(corners)
    return low.numerator//low.denominator, -((-high.numerator)//high.denominator)

@lru_cache(None)
def entropy(q):
    lo=hi=F(0)
    for p in q:
        if p:
            a,b=log_interval(p)
            lo-=p*b
            hi-=p*a
    return lo,hi

def spectrum(table, ms):
    n=len(ms); size=1<<n
    weights=[math.prod(ms[i] if x>>i&1 else 8-ms[i] for i in range(n)) for x in range(size)]
    vals=[]
    for s in range(size):
        v=sum(table[x]*weights[x]*math.prod((8*((x>>i)&1)-ms[i]) for i in range(n) if s>>i&1) for x in range(size))
        vals.append(F(v*v,8**(2*n)*math.prod(ms[i]*(8-ms[i]) for i in range(n) if s>>i&1)))
    assert sum(vals)==1
    return tuple(vals)

def restrict(table,ms,A,z):
    B=[i for i in range(len(ms)) if i not in A]
    child=[]
    for y in range(1<<len(B)):
        x=sum(((z>>j)&1)<<i for j,i in enumerate(A))+sum(((y>>j)&1)<<i for j,i in enumerate(B))
        child.append(table[x])
    return spectrum(child,tuple(ms[i] for i in B))

def encode_interval(pair):
    return {'lower_scaled':str(pair[0]),'upper_scaled':str(pair[1]),'scale':str(OUTSCALE),'approx_bits':[float(x/OUTSCALE) for x in pair]}

def run(pilot):
    start=time.perf_counter(); count=0; unresolved=[]; violations=[]; exact_zero=0; minimum=None; minrow=None
    biases=[(4,4,4)] if pilot else itertools.product((1,2,4),repeat=3)
    for ms in biases:
        for code in range(128):
            # f(000)=+1, seven free output signs. Little-endian assignments.
            table=tuple(1 if x==0 or not (code>>(x-1)&1) else -1 for x in range(8))
            parent=spectrum(table,ms); hp=entropy(parent)
            for mask in range(1,7):
                A=[i for i in range(3) if mask>>i&1]; B=[i for i in range(3) if not mask>>i&1]
                q=tuple(sum(parent[s] for s in range(8) if sum(((s>>i)&1)<<j for j,i in enumerate(B))==t) for t in range(1<<len(B)))
                avg=[F(0),F(0)]; mixed=[F(0)]*len(q)
                for z in range(1<<len(A)):
                    w=F(math.prod(ms[i] if z>>j&1 else 8-ms[i] for j,i in enumerate(A)),8**len(A))
                    c=restrict(table,ms,A,z); hc=entropy(c)
                    for j in range(2): avg[j]+=w*hc[j]
                    for t in range(len(q)): mixed[t]+=w*c[t]
                assert tuple(mixed)==q
                hq=entropy(q); delta=[F(0),F(0)]
                for i in A:
                    p=F(ms[i],8); hb=entropy((p,1-p)); lm=log_interval(max(p,1-p))
                    for j in range(2): delta[j]+=hb[j]+lm[j]
                defect=(hp[0]-2*hq[1]+avg[0]+delta[0],hp[1]-2*hq[0]+avg[1]+delta[1])
                count+=1; row={'code':code,'bias_numerators_over_8':ms,'block_mask':mask,'defect':encode_interval(defect)}
                if defect[1]<0: violations.append(row)
                elif defect[0]<0: unresolved.append(row)
                elif defect==(0,0): exact_zero+=1
                if defect[0]>0 and (minimum is None or defect[0]<minimum): minimum=defect[0];minrow=row
        if time.perf_counter()-start>55:
            raise RuntimeError('Frozen 55-second runtime cap reached; no automatic escalation')
    # Existing tax-free AND is a control embedded with a dummy third input.
    control_table=tuple(-1 if (x&3)==3 else 1 for x in range(8))
    control=spectrum(control_table,(1,2,4))
    assert control[:4]==(F(225,256),F(7,256),F(3,256),F(21,256)) and control[4:]==(F(0),)*4
    result={'helper':'B09-BIASED-BLOCK-UNCERTAINTY@1','mode':'pilot' if pilot else 'full','cases':count,'certified_nonnegative':count-len(unresolved)-len(violations),'exact_zero':exact_zero,'unresolved':unresolved,'violations':violations,'minimum_positive_lower_bound_case':minrow,'runtime_seconds':time.perf_counter()-start,'cached_logarithms':log_interval.cache_info().currsize,'cached_entropies':entropy.cache_info().currsize,'control_spectrum':[str(x) for x in control]}
    (ROOT/'out'/('pilot.json' if pilot else 'search.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args();run(args.pilot)
