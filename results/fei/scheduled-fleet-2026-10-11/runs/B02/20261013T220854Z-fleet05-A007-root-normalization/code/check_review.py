"""Own checker module only, never A006 source code."""
import itertools as it, json, math, time
from pathlib import Path
from fractions import Fraction as Q
import check_lift as ck

totals={'assignments':0,'root_minors':0,'actual_events':0,'nontrivial_moments':0,'sunflower_sharp_cases':0}

def verify(tab,owned):
    rs,edges=ck.roots_and_graph(owned,tab)
    pi={l:Q(1,2**len(tab[l])) for l in owned}
    full_moment=Q(0); full_can=Q(0); full_up=Q(0)
    for roots in rs:
        ev,canonical=ck.base_events(owned,tab,roots,edges)
        poly,coords=ck.minor(owned,tab,roots)
        direct={}
        for groups in canonical:
            exp=tuple(len(groups.get(k,())) for k in coords)
            direct[exp]=direct.get(exp,0)+1
        ck.check(poly==direct)
        moment=sum(c*math.prod(math.factorial(h) for h in exp) for exp,c in poly.items())
        can=sum(poly.values())
        Ds=[sum(v!=u and j in tab[v] for v in owned) for u,j in coords]
        up=sum(c*math.prod((Q(d+1,2) if d else Q(1))**h for d,h in zip(Ds,exp)) for exp,c in poly.items())
        ck.check(moment==len(ev))
        ck.check(can<=moment<=min(math.factorial(len(owned)-len(roots))*can,up))
        rarity=math.prod(pi[l] for l in roots)
        full_moment+=rarity*moment; full_can+=rarity*can; full_up+=rarity*up
        totals['root_minors']+=1; totals['actual_events']+=len(ev)
        totals['nontrivial_moments']+=moment>can
    ck.check(full_can<=full_moment<=full_up)
    totals['assignments']+=1
    return full_moment,full_can

start=time.perf_counter()
for e in range(1,6):
    tab=tuple((0,i) for i in range(1,e+2))
    owned={0:(0,)}|{i:(i+1,) for i in range(1,e+1)}
    moment,can=verify(tab,owned)
    ck.check(moment==Q(math.factorial(e),4) and can==Q(1,4))
    values=ck.truth(tab,e+2); spectrum=ck.fwht(values)
    selected=1+sum(1<<j for j in range(2,e+2))
    ck.check(abs(Q(spectrum[selected],1<<(e+2)))==Q(1,2**(e+1)))
    if e==2:
        ck.check(moment==2*can) # SCC polynomial factors share x; expectations do not.
    totals['sunflower_sharp_cases']+=1

K4=tuple(it.combinations(range(4),2))
hetero=((0,1),(1,2),(0,2,3))
for tab in [K4,hetero]:
    ck.check(all(not(set(a)<=set(b)) for a,b in it.permutations(tab,2)))
    for owners in it.product(*(tuple(l for l,R in enumerate(tab) if j in R) for j in range(4))):
        owned={}
        for j,l in enumerate(owners): owned.setdefault(l,[]).append(j)
        verify(tab,{l:tuple(js) for l,js in owned.items()})

result={'status':'PASS','helper_version':'A007-root-lift-independent-v1-review-extension',
        'counts':totals,'assertions':ck.COUNTS['assertions'],'elapsed_seconds':time.perf_counter()-start,
        'arithmetic':'integer determinant polynomials, rational rare-root weights, explicit queue event permutations'}
result['precount_correction']='Frozen heterogeneous assignment count 4 was an arithmetic pre-count error: actual fixed domain has 2*2*2*1=8. No parameter or family was changed.'
Path(__file__).resolve().parents[1].joinpath('out','REVIEW_CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
