import argparse, itertools as it, json, math, time
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PREV=ROOT.parent/'20261013T220854Z-account05-A007-root-normalization'/'code'/'check_lift.py'
helpers={'__name__':'a007_own_helpers','__file__':str(PREV)}
exec(compile(PREV.read_text(encoding='utf-8'),str(PREV),'exec'),helpers)
START=time.perf_counter(); assertions=0
stats={'composition_records':0,'s_N_cases':0,'growth_identities':0,
       'trace_assignments':0,'root_minors':0,'actual_events':0,'parity_tables':0}

def check(v):
    global assertions
    assertions+=1
    assert v
    if time.perf_counter()-START>60: raise RuntimeError('frozen 60 second job limit')

def compositions(s,k):
    for cuts in it.combinations(range(1,s),k-1):
        seq=(0,)+cuts+(s,)
        yield tuple(seq[j+1]-seq[j] for j in range(k))

def rising(s,j): return math.prod(range(s,s+j))

def check_compositions(pilot):
    rows=[]
    for s in range(1,(5 if pilot else 12)+1):
        C=sum(Q(math.comb(s-1,k-1)*rising(s,k-1),math.factorial(k)) for k in range(1,s+1))
        check(C<=6**(s-1))
        for N in sorted({1,2,4,16,2**(s-1)}):
            zero=Q(0); record_count=0
            for k in range(1,min(s,N)+1):
                labels=Q(math.comb(N,k),N**k)
                factor=Q(rising(s,k-1),math.factorial(k))
                check(labels<=Q(1,math.factorial(k)))
                for sizes in compositions(s,k):
                    mult=Q(math.factorial(s),math.prod(math.factorial(v) for v in sizes))
                    B=math.prod(Q(v,s)**v for v in sizes)
                    A=labels*rising(s,k-1)*mult
                    # W=A B^(6/5); entropy damping W <= factor*B^(1/5)
                    # is certified by a rational fifth-power inequality.
                    check(mult*B<=1)
                    check(A**5*B**6<=factor**5*B)
                    if k==1: check(A==1 and B==1)
                    stats['composition_records']+=1; record_count+=1
            rows.append({'s':s,'N':N,'records':record_count,'C_s':str(C),'normalizer_lower_bound':'1'})
            stats['s_N_cases']+=1
    return rows

def check_growth(pilot):
    for n in range((8 if pilot else 40)+1):
        C=sum(Q(math.comb(n,j)*math.comb(n+j,j),j+1) for j in range(n+1))
        D=sum(math.comb(n,j)*math.comb(n+j,j) for j in range(n+1))
        alternative=sum(math.comb(n,j)**2*2**j for j in range(n+1))
        check(D==alternative)
        check(C<=D<=6**n)
        stats['growth_identities']+=1
    check(6**5<2**13)

def check_law(pilot):
    maxs=2 if pilot else 4; maxN=2 if pilot else 4
    for s in range(1,maxs+1):
        for N in range(1,maxN+1):
            tab=tuple(tuple(range(s)) for l in range(N))
            direct={}; predicted={}; assignments_by_k={}
            for assignment in it.product(range(N),repeat=s):
                owned={}
                for j,l in enumerate(assignment): owned.setdefault(l,[]).append(j)
                owned={l:tuple(js) for l,js in owned.items()}
                sizes=tuple(len(owned[l]) for l in sorted(owned)); k=len(owned)
                roots,edges=helpers['roots_and_graph'](owned,tab)
                moment=0
                for R in roots:
                    events,_=helpers['base_events'](owned,tab,R,edges)
                    poly,coords=helpers['minor'](owned,tab,R)
                    M=sum(coef*math.prod(math.factorial(h) for h in exp) for exp,coef in poly.items())
                    check(M==len(events)); moment+=M
                    stats['root_minors']+=1; stats['actual_events']+=len(events)
                # pi factors are common; sum all root minors/moments = (s)_(k-1).
                check(moment==rising(s,k-1))
                coefficient=Q(moment,N**k)
                direct[sizes]=direct.get(sizes,Q(0))+coefficient
                stats['trace_assignments']+=1
            for k in range(1,min(N,s)+1):
                for sizes in compositions(s,k):
                    predicted[sizes]=Q(math.comb(N,k)*rising(s,k-1)*math.factorial(s),N**k*math.prod(math.factorial(v) for v in sizes))
            check(direct==predicted)
            # Congestion B^(6/5) is identical per size vector, so coefficient
            # equality proves formal exact W law without evaluating irrational roots.

def check_boolean(pilot):
    for m in range(1,(3 if pilot else 5)+1):
        f=[(-1)**x.bit_count() for x in range(2**m)]
        spectrum=helpers['fwht'](f)
        check(sum(v!=0 for v in spectrum)==1)
        check(abs(spectrum[-1])==2**m)
        check(helpers['influence'](f,m)==m)
        # Every positive cell is prime: deleting any literal allows the opposite parity.
        positive=[x for x,v in enumerate(f) if v==1]
        check(len(positive)==2**(m-1))
        check(all(f[x^(1<<j)]==-1 for x in positive for j in range(m)))
        stats['parity_tables']+=1

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--pilot',action='store_true'); args=ap.parse_args()
    rows=check_compositions(args.pilot)
    check_growth(args.pilot); check_law(args.pilot); check_boolean(args.pilot)
    result={'status':'PASS','helper_version':'A007-original-posterior-tail-v1','assertions':assertions,
       'helper_assertions':helpers['COUNTS']['assertions'],'stats':stats,'elapsed_seconds':time.perf_counter()-START,
       'constant_certificate':{'bound':'E_W H <=5 log2(6)<13','integer_sign':'7776<8192'},
       'arithmetic':'exact integers/Fraction and rational fifth powers; formal gamma=6/5 factors; no floating logarithms',
       'case_receipts':rows,'first_unproved_line':'inherited R_g or arbitrary-support Psi_dist influence payment'}
    out=ROOT/'out'; out.mkdir(exist_ok=True)
    (out/('PILOT.json' if args.pilot else 'EXACT_CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='case_receipts'}))
