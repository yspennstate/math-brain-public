import argparse, hashlib, json, math, time
from collections import Counter,defaultdict
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PREC=96; SCALE=1<<PREC; NAT_SCALE=1<<128; TERMS=48

def ln_unit(a,b):
    u,v=a-b,a+b
    low=sum(2*NAT_SCALE*pow(u,2*j+1)//((2*j+1)*pow(v,2*j+1)) for j in range(TERMS))
    num=2*NAT_SCALE*pow(u,2*TERMS+1)*v*v
    den=(2*TERMS+1)*pow(v,2*TERMS+1)*(v*v-u*u)
    return low,low+TERMS+(num+den-1)//den

LN2=ln_unit(2,1)

@lru_cache(None)
def log_int(n):
    if n<=1:return (0,0)
    k=n.bit_length()-1
    if n==1<<k:return(k*SCALE,k*SCALE)
    lo,hi=ln_unit(n,1<<k)
    lo+=k*LN2[0];hi+=k*LN2[1]
    return lo*SCALE//LN2[1],(hi*SCALE+LN2[0]-1)//LN2[0]

@lru_cache(None)
def g(a,b):
    if not a or not b:return (0,0)
    t=a+b;l,h=log_int(t);al,ah=log_int(a);bl,bh=log_int(b)
    return(t*l-a*ah-b*bh,t*h-a*al-b*bl)

@lru_cache(None)
def factor(n):
    ans=[];p=2
    while p*p<=n:
        k=0
        while n%p==0:n//=p;k+=1
        if k:ans.append((p,k))
        p+=1
    if n>1:ans.append((n,1))
    return tuple(ans)

def vector(packets,L):
    terms=defaultdict(int)
    for a,b in packets:
        if not a or not b:continue
        for n,c in ((a+b,a+b),(a,-a),(b,-b)):
            for p,k in factor(n):terms[p]+=c*k
    return tuple((p,Fraction(c,L)) for p,c in sorted(terms.items()) if c)

def same(v,w):return v==w

PAIRS=[[(s,s|(1<<i)) for s in range(32) if not(s>>i&1)] for i in range(5)]
SIGNS=[tuple(1 if (s&x).bit_count()%2==0 else -1 for s in range(32)) for x in range(32)]

def ratios(cs,proof=False):
    squares=[c*c for c in cs]; assert sum(squares)==256
    r=[]
    for i,pairs in enumerate(PAIRS):
        lo=hi=L=0;packets=[]
        for a,b in pairs:
            aa,bb=squares[a],squares[b];l,h=g(aa,bb);lo+=l;hi+=h;L+=bb
            if proof:packets.append((aa,bb))
        if L:r.append({'i':i,'lo':lo,'hi':hi,'L':L,'packets':packets})
    return r

def cmp_fraction(a,b,c,d):return (a*d>c*b)-(a*d<c*b)

def exact_min(cs):
    r=ratios(cs,True)
    r.sort(key=lambda x:Fraction(x['hi'],x['L']))
    best=r[0];best['vector']=vector(best['packets'],best['L'])
    for other in r[1:]:
        if other['lo']*best['L']>=best['hi']*other['L']:continue
        ov=vector(other['packets'],other['L'])
        if same(ov,best['vector']):continue
        if other['hi']*best['L']<best['lo']*other['L']:
            best=other;best['vector']=ov;continue
        raise ArithmeticError('Distinct per-coordinate expressions overlap fixed rigorous intervals')
    return best

def encode(best):
    if best is None:return None
    ans={k:v for k,v in best.items() if k not in ('vector','packets','cs')}
    ans['interval_bits']=[float(Fraction(best['lo'],best['L']*SCALE)),float(Fraction(best['hi'],best['L']*SCALE))]
    ans['prime_log_ratio']={str(p):str(c) for p,c in best['vector']}
    return ans

def run(pilot):
    start=time.perf_counter();cap=55 if pilot else 600;max_k=3 if pilot else 6
    counts=Counter();best_by_k={};ties_by_k=defaultdict(list);strict=0;hash_state=hashlib.sha256()
    def visit(A,ss,nextpoint):
        nonlocal strict
        k=len(A);cs=[-v for v in ss];cs[0]+=16
        rs=ratios(cs);assert rs
        # A coordinate furnishing the minimum upper interval certifies E(f) upper.
        upper=min(rs,key=lambda x:Fraction(x['hi'],x['L']))
        old=best_by_k.get(k);counts[k]+=1
        hash_state.update(bytes(A))
        if old is None or upper['hi']*old['L']>=old['lo']*upper['L']:
            candidate=exact_min(cs);candidate.update({'A':list(A),'negative_mask':sum(1<<x for x in A),'cs':cs})
            if old is None or candidate['lo']*old['L']>old['hi']*candidate['L']:
                best_by_k[k]=candidate;ties_by_k[k]=[list(A)]
                # Save every changed best immediately.
                (ROOT/'out'/('pilot_incumbents.json' if pilot else 'incumbents.json')).write_text(json.dumps({str(j):encode(v) for j,v in best_by_k.items()},indent=2),encoding='utf-8')
            elif candidate['hi']*old['L']<old['lo']*candidate['L']:strict+=1
            elif same(candidate['vector'],old['vector']):ties_by_k[k].append(list(A))
            else:raise ArithmeticError('Distinct incumbent expressions overlap rigorous intervals')
        else:strict+=1
        if sum(counts.values())%10000==0:
            checkpoint={'cases':sum(counts.values()),'counts':dict(counts),'runtime_seconds':time.perf_counter()-start,'best_by_k':{str(j):encode(v) for j,v in best_by_k.items()}}
            (ROOT/'out'/('pilot_checkpoint.json' if pilot else 'checkpoint.json')).write_text(json.dumps(checkpoint,indent=2),encoding='utf-8')
        if time.perf_counter()-start>cap:raise RuntimeError('Frozen elapsed-time cap reached; last checkpoint retained')
        if k<max_k:
            for x in range(nextpoint,32):visit(A+(x,),tuple(v+w for v,w in zip(ss,SIGNS[x])),x+1)
    visit((0,),SIGNS[0],1)
    expected={k:math.comb(31,k-1) for k in range(1,max_k+1)};assert dict(counts)==expected
    globalbest=None
    for b in best_by_k.values():
        if globalbest is None or b['lo']*globalbest['L']>globalbest['hi']*b['L']:globalbest=b
        elif b['hi']*globalbest['L']<globalbest['lo']*b['L']:pass
        elif not same(b['vector'],globalbest['vector']):raise ArithmeticError('Distinct per-size maxima overlap')
    result={'mode':'pilot' if pilot else 'full','dimension':5,'minority_support_cap':max_k,'counts':dict(counts),'cases':sum(counts.values()),'expected_cases':sum(expected.values()),'best_by_k':{str(j):encode(v) for j,v in best_by_k.items()},'ties_by_k':dict(ties_by_k),'global_best':encode(globalbest),'runtime_seconds':time.perf_counter()-start,'enumeration_sha256':hash_state.hexdigest(),'scale':str(SCALE),'all_cases_certified_against_incumbents':True,'comparison_unresolved':0,'no_claim_for_support_sizes_7_to_16':True}
    (ROOT/'out'/('pilot.json' if pilot else 'search.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('ties_by_k','best_by_k')},indent=2))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');run(ap.parse_args().pilot)
