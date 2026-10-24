"""A052 v2: integer marginal spectra, optimal recentering, rational signs."""
import argparse,ast,hashlib,json,time
from collections import Counter,defaultdict
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE=Path(r'~\brain_workers\FEI100_20261011\agents\A051\runs\20261011T233123Z-account05-A051-near-extremizer-definition')
ASSERTIONS=0; PREC=96
def ck(v):
    global ASSERTIONS
    ASSERTIONS+=1
    if not v: raise AssertionError(ASSERTIONS)
def dump(path,v):
    s=json.dumps(v,indent=2)+'\n'; ck(len(s.encode())<20*1024*1024)
    path.write_text(s,encoding='utf-8')
def fwht(v):
    v=list(v); h=1
    while h<len(v):
        for a in range(0,len(v),2*h):
            for j in range(a,a+h):
                u,w=v[j],v[j+h]; v[j],v[j+h]=u+w,u-w
        h*=2
    return v
def direct(v):
    return [sum(x*(-1 if (j&s).bit_count()%2 else 1) for j,x in enumerate(v)) for s in range(len(v))]
@lru_cache(None)
def factors(x):
    ans={}; p=2
    while p*p<=x:
        while x%p==0: ans[p]=ans.get(p,0)+1; x//=p
        p+=1
    if x>1: ans[x]=ans.get(x,0)+1
    return ans
def combine(a,b,m=1,k=1):
    ans={p:c*m for p,c in a.items()}
    for p,c in b.items(): ans[p]=ans.get(p,0)+k*c
    return {p:c for p,c in ans.items() if c}
def entnum(weights):
    N=sum(weights); ans=defaultdict(int)
    for p,k in factors(N).items(): ans[p]+=N*k
    for x,count in Counter(weights).items():
        if x:
            for p,k in factors(x).items(): ans[p]-=count*x*k
    return {p:c for p,c in ans.items() if c}
def ln_series(z):
    power=z; s=F(0)
    for j in range(40): s+=2*power/(2*j+1); power*=z*z
    return s,s+2*power/(81*(1-z*z))
@lru_cache(None)
def lnprime(p):
    k=p.bit_length()-1; unit=1<<k
    l2,h2=ln_series(F(1,3)); l,h=ln_series(F(p-unit,p+unit))
    l+=k*l2; h+=k*h2; scale=1<<PREC
    return l.numerator*scale//l.denominator,-(-h.numerator*scale//h.denominator)
def enclosure(a,constant=0):
    lo=hi=constant*(1<<PREC)
    for p,c in a.items():
        l,h=lnprime(p)
        lo+=c*(l if c>=0 else h); hi+=c*(h if c>=0 else l)
    return lo,hi
def sign(a,c=0):
    if not a: return (c>0)-(c<0)
    l,h=enclosure(a,c)
    if l>0:return 1
    if h<0:return -1
    raise RuntimeError('Frozen precision insufficient for sign')
def enc(a): return {str(p):str(c) for p,c in sorted(a.items())}
def bits_interval(a,c,den):
    l,h=enclosure(a,c); l2,h2=lnprime(2)
    # All use sites here are nonnegative entropy/cost intervals.
    ck(l>=0)
    return [str(F(l,den*h2)),str(F(h,den*l2))]
def signed_bits_interval(a,c,den):
    l,h=enclosure(a,c); l2,h2=lnprime(2)
    corners=[F(x,den*y) for x in (l,h) for y in (l2,h2)]
    return [str(min(corners)),str(max(corners))]

@lru_cache(None)
def size(t): return 1 if t==() else sum(size(x) for x in t)
def table(t):
    if t==():return [0,1]
    children=[table(x) for x in t]; dims=[size(x) for x in t]; out=[]
    for x in range(1<<sum(dims)):
        offset=0; b=1
        for v,n in zip(children,dims): b*=v[(x>>offset)&((1<<n)-1)]; offset+=n
        out.append(1-b)
    return out
def hod(n,prime=False):
    clauses={6:[(0,1),(2,3),(0,2,4),(1,3,5) if prime else (2,4,5)],
             8:[(0,1),(2,3),(2,4,5),(0,2,4,6),(1,2,5,7) if prime else (2,4,6,7)]}[n]
    return [int(all(any(x>>i&1 for i in clause) for clause in clauses)) for x in range(1<<n)]
def hybrid(r):
    g=hod(6)
    z=[0,1] if r==1 else [int(x!=(1<<r)-1) for x in range(1<<r)]
    return [1-g[x&63]*z[x>>6] for x in range(1<<(6+r))]
def seeds():
    return [(f'Hod_g{n//2}'+('_prime' if prime else ''),hod(n,prime)) for n in (6,8) for prime in (False,True)]+[(f'NAND_Hod_g3_PD_{r}',hybrid(r)) for r in (1,2,3)]
def pack(x,loc):return sum(((x>>i)&1)<<j for j,i in enumerate(loc))
def unpack(x,loc):return sum(((x>>j)&1)<<i for j,i in enumerate(loc))
def block_stats(weights,A):
    n=len(weights).bit_length()-1; C=((1<<n)-1)^A
    ai=[i for i in range(n) if A>>i&1]; ci=[i for i in range(n) if C>>i&1]
    marginal=[0]*(1<<len(ci)); ones={i:[0]*len(marginal) for i in ai}
    for s,w in enumerate(weights):
        t=pack(s,ci); marginal[t]+=w
        for i in ai:
            if s>>i&1:ones[i][t]+=w
    beta=sum(min(z,m-z) for i in ai for m,z in zip(marginal,ones[i]))
    B=combine(entnum(weights),entnum(marginal),1,-1)
    IA=sum(w*(s&A).bit_count() for s,w in enumerate(weights))
    return B,beta,IA
def decrement(t,A,H):
    n=len(t).bit_length()-1; ai=[i for i in range(n) if A>>i&1]; ci=[i for i in range(n) if not A>>i&1]
    summed={}
    for x in range(1<<len(ai)):
        child=[2*t[unpack(x,ai)|unpack(y,ci)]-1 for y in range(1<<len(ci))]
        w=fwht(child); h=entnum([a*a for a in w]); summed=combine(summed,h)
    return combine(H,summed,1,-(1<<len(ai)))

def evaluate(t,name,source,direct_check=False,check_blocks=False):
    n=len(t).bit_length()-1; N=1<<n; den=N*N
    v=[2*x-1 for x in t]; w=fwht(v); weights=[x*x for x in w]
    ck(sum(weights)==den); ck(hashlib.sha256(bytes(t)).hexdigest()==source['truth_sha256'])
    if direct_check: ck(w==direct(v))
    H=entnum(weights); Itotal=sum(s.bit_count()*x for s,x in enumerate(weights))
    ck({str(p):str(F(c,den)) for p,c in H.items()}==source['H']); ck(F(Itotal,den)==F(source['I']))
    rows=[]
    for i in range(n):
        B,beta,Ii=block_stats(weights,1<<i)
        ck(Ii==sum(weights[s] for s in range(N) if s>>i&1))
        ck(F(Ii,den)==F(sum(t[x]!=t[x^(1<<i)] for x in range(N)),N))
        ck(beta<=min(Ii,den-Ii)); ck(Ii>0)
        gap=combine(H,B,Ii,-Itotal); constant=-2*beta*Itotal; sg=sign(gap,constant)
        L=decrement(t,1<<i,H); J=combine(L,B,1,-1)
        # Optimal recentring upper bound, checked directly against actual children.
        ck(sign({p:-c for p,c in J.items()},2*beta)>=0)
        rows.append({'i':i,'I_numerator':Ii,'B_nat_numerator':enc(B),'beta_numerator':beta,
                     'U_over_I_bits':bits_interval(B,2*beta,Ii),
                     'R_I_minus_U_nat_numerator':enc(gap),'gap_constant':constant,
                     'gap_sign':sg,'gap_per_coordinate_bits':signed_bits_interval(gap,constant,den*Itotal)})
    best=0; ties=[0]
    for i in range(1,n):
        a,b=rows[i],rows[best]
        # Compare U_i/I_i with the current minimum.
        expr=combine({int(p):int(c) for p,c in a['B_nat_numerator'].items()},
                     {int(p):int(c) for p,c in b['B_nat_numerator'].items()},b['I_numerator'],-a['I_numerator'])
        const=2*(a['beta_numerator']*b['I_numerator']-b['beta_numerator']*a['I_numerator'])
        s=sign(expr,const)
        if s<0:best=i;ties=[i]
        elif s==0:ties.append(i)
    passes=any(r['gap_sign']>=0 for r in rows)
    refmask=source['minimizing_masks'][0]; L=decrement(t,refmask,H)
    IA=sum(weights[s]*(s&refmask).bit_count() for s in range(N))
    exactgap=combine(H,L,IA,-Itotal); exactsign=sign(exactgap)
    # This physically verifies the named source minimizer as a witness; no source-minimum theorem needed.
    block_record={'mask':refmask,'actual_decrement_nat_numerator':enc(L),'I_A_numerator':IA,
                  'R_I_A_minus_L_A_sign':exactsign,'actual_gap_per_influence_bits':signed_bits_interval(exactgap,0,IA*Itotal)}
    if check_blocks:
        for A in range(1,N-1):
            B,beta,IA=block_stats(weights,A)
            singles={}; sb=0
            for i in range(n):
                if A>>i&1:
                    singles=combine(singles,{int(p):int(c) for p,c in rows[i]['B_nat_numerator'].items()});sb+=rows[i]['beta_numerator']
            ck(sign(combine(B,singles,1,-1))>=0); ck(beta>=sb)
            # Direct block channel validation and separate beta bounds.
            LB=decrement(t,A,H); J=combine(LB,B,1,-1); ck(sign({p:-c for p,c in J.items()},2*beta)>=0)
    return {'name':name,'n':n,'truth_sha256':hashlib.sha256(bytes(t)).hexdigest(),
            'H_nat_numerator':enc(H),'I_numerator':Itotal,'spectrum_denominator':den,
            'R_bits':bits_interval(H,0,Itotal),'U_min_over_I_bits':rows[best]['U_over_I_bits'],
            'best_singletons':ties,'certificate_exists':passes,'singleton_rows':rows,
            'source_minimizer_physically_rechecked':block_record}

def freeze():
    for mode in ('pilot','full'):
        spec={'helper_version':'A052-recentred-census-v2','family':'A051 saved read-once NAND formula shapes plus seven fixed Hod-named seed/hybrid controls',
              'domain':'n=6,7,8,9, all 1150 saved NAND trees and seven seed definitions in this helper; no recursion to larger dimension',
              'case_count':4 if mode=='pilot' else 1157,
              'pilot_indices':[0,32],'pilot_seeds':['Hod_g3','Hod_g3_prime'],
              'source_summary_sha256':hashlib.sha256((SOURCE/'out/full_SUMMARY.json').read_bytes()).hexdigest(),
              'source_seed_summary_sha256':hashlib.sha256((SOURCE/'out/SEEDED_FULL_SUMMARY.json').read_bytes()).hexdigest(),
              'symmetry':'No reduction for singleton costs. Analytic singleton-collapse theorem is exact over all proper blocks. Pilot/direct controls additionally enumerate all proper blocks; no all-function census.',
              'arithmetic':'Integer Walsh, exact marginal packet weights, natural prime-log vectors with integer coefficients and rational constants; 40-term positive atanh series; outward 96-bit dyadic ln enclosures',
              'memory_estimate_MB':70,'max_runtime_seconds':55 if mode=='pilot' else 600,
              'direct_checks':'Pilot cases, seven seeds, saved extrema 279,287,946,962. All-block checks only pilot cases and seeds Hod_g3/g3_prime.'}
        dump(ROOT/'out'/('FROZEN_'+mode.upper()+'.json'),spec)
    print('Specs frozen; no search performed.')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['freeze','pilot','full']);args=ap.parse_args()
    if args.mode=='freeze':freeze();return
    start=time.monotonic();spec=json.loads((ROOT/'out'/('FROZEN_'+args.mode.upper()+'.json')).read_text())
    source=json.loads((SOURCE/'out/full_SUMMARY.json').read_text())
    ck(hashlib.sha256((SOURCE/'out/full_SUMMARY.json').read_bytes()).hexdigest()==spec['source_summary_sha256'])
    seedrefs={x['name']:x for x in json.loads((SOURCE/'out/SEEDED_FULL_SUMMARY.json').read_text())['seed_cases']}
    ck(hashlib.sha256((SOURCE/'out/SEEDED_FULL_SUMMARY.json').read_bytes()).hexdigest()==spec['source_seed_summary_sha256'])
    indices=[0,32] if args.mode=='pilot' else range(len(source['cases']))
    results=[];(ROOT/'out/cases').mkdir(exist_ok=True)
    for ix in indices:
        ref=source['cases'][ix]; t=table(ast.literal_eval(ref['tree']));ck(len(t)==1<<ref['n'])
        result=evaluate(t,f'NAND_case_{ix:04d}',ref,direct_check=(args.mode=='pilot' or ix in (279,287,946,962)),check_blocks=args.mode=='pilot')
        dump(ROOT/'out/cases'/(result['name']+'.json'),result)
        results.append({k:v for k,v in result.items() if k!='singleton_rows'})
        ck(time.monotonic()-start<spec['max_runtime_seconds'])
    for name,t in seeds():
        if args.mode=='pilot' and name not in spec['pilot_seeds']:continue
        result=evaluate(t,name,seedrefs[name],direct_check=True,check_blocks=name in ('Hod_g3','Hod_g3_prime'))
        dump(ROOT/'out/cases'/(name+'.json'),result);results.append({k:v for k,v in result.items() if k!='singleton_rows'})
        ck(time.monotonic()-start<spec['max_runtime_seconds'])
    groups=[]
    for n in range(6,10):
        group=[r for r in results if r['name'].startswith('NAND_case') and r['n']==n]
        if group: groups.append({'n':n,'cases':len(group),'U_certificate_pass':sum(r['certificate_exists'] for r in group),
             'U_certificate_fail':sum(not r['certificate_exists'] for r in group),
             'failure_despite_verified_actual_descent':sum(not r['certificate_exists'] and r['source_minimizer_physically_rechecked']['R_I_A_minus_L_A_sign']>0 for r in group)})
    summary={'status':'PASS','helper_version':'A052-recentred-census-v2','mode':args.mode,'completed':len(results),'groups':groups,
             'assertions':ASSERTIONS,'runtime_seconds':time.monotonic()-start,'cases':results}
    ck(len(results)==spec['case_count']);dump(ROOT/'out'/(args.mode.upper()+'_SUMMARY.json'),summary)
    print(json.dumps({k:v for k,v in summary.items() if k!='cases'}))
if __name__=='__main__':main()
