"""Small exact checks supporting, but not replacing, ATTEMPT.md's proofs."""
import ctypes
import itertools
import json
import math
from pathlib import Path
import time

ROOT=Path(__file__).resolve().parent
started=time.monotonic()
class MemoryStatus(ctypes.Structure):
    _fields_=[('length',ctypes.c_ulong),('load',ctypes.c_ulong),('total_phys',ctypes.c_ulonglong),('avail_phys',ctypes.c_ulonglong),('total_page',ctypes.c_ulonglong),('avail_page',ctypes.c_ulonglong),('total_virtual',ctypes.c_ulonglong),('avail_virtual',ctypes.c_ulonglong),('avail_extended',ctypes.c_ulonglong)]
mem=MemoryStatus()
mem.length=ctypes.sizeof(mem)
if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(mem)):
    raise RuntimeError('fresh memory gate unavailable')
gate={'foreground_processes':1,'gpu':False,'max_wall_seconds':60,'max_vertices':5,'max_bond_state_visits':61000,'max_boolean_comparisons':17000,'available_memory_bytes':mem.avail_phys,'minimum_memory_bytes':128*1024**2,'observed_at_unix':time.time()}
gate['allowed']=mem.avail_phys>=gate['minimum_memory_bytes']
(ROOT/'COMPUTE_GATE.json').write_text(json.dumps(gate,indent=2)+'\n',encoding='utf-8')
if not gate['allowed']:
    raise SystemExit('gate refused: insufficient available memory')

def budget():
    if time.monotonic()-started>60:
        raise RuntimeError('bounded foreground compute gate expired')

def weights(nums):
    return [math.prod(nums[i] if (s>>i)&1 else 4-nums[i] for i in range(len(nums))) for s in range(1<<len(nums))]

checks=violations=0
for n in range(1,4):
    budget()
    states=1<<n
    for mu in itertools.product((1,3),repeat=n):
        wm=weights(mu)
        for nu in itertools.product((1,3),repeat=n):
            wn=weights(nu)
            for truth in range(1<<states):
                vals=[(truth>>s)&1 for s in range(states)]
                lhs=abs(sum(vals[s]*(wn[s]-wm[s]) for s in range(states)))
                rhs=0
                for i in range(n):
                    exterior=[nu[j] if j<i else mu[j] for j in range(n)]
                    for s in range(states):
                        if (s>>i)&1:
                            continue
                        if vals[s]==vals[s|(1<<i)]:
                            continue
                        exterior_weight=math.prod(exterior[j] if (s>>j)&1 else 4-exterior[j] for j in range(n) if j!=i)
                        rhs+=abs(nu[i]-mu[i])*exterior_weight
                checks+=1
                violations+=lhs>rhs
            budget()
assert checks<=17000
assert violations==0

def terminal_state(n,edges,mask):
    parents=list(range(n))
    def root(x):
        while parents[x]!=x:
            x=parents[x]
        return x
    for i,(a,b) in enumerate(edges):
        if (mask>>i)&1:
            parents[root(a)]=root(b)
    r=[root(i) for i in range(3)]
    if len(set(r))==1:
        return 'all'
    if len(set(r))==3:
        return 'none'
    return 'partial'

graphs=eligible=state_visits=no_partial=0
by_n=[]
for n in range(3,6):
    budget()
    all_edges=list(itertools.combinations(range(n),2))
    gn=en=vis=0
    for graph_mask in range(1<<len(all_edges)):
        edges=[e for i,e in enumerate(all_edges) if (graph_mask>>i)&1]
        gn+=1
        if terminal_state(n,edges,(1<<len(edges))-1)!='all':
            continue
        en+=1
        count_partial=0
        for mask in range(1<<len(edges)):
            count_partial+=terminal_state(n,edges,mask)=='partial'
            vis+=1
        no_partial+=count_partial==0
    graphs+=gn
    eligible+=en
    state_visits+=vis
    by_n.append({'vertices':n,'graphs':gn,'graphs_connecting_all_three':en,'bond_state_visits':vis})
    budget()
assert state_visits<=61000
assert no_partial==0

t=1/math.sqrt(2)
star={'pair_probability':t*t,'one_to_two_probability':2*t*t-t**3,'reference_probability':.5,'bias':2*t*t-t**3-.5,'fair_star_partial_probability':3/8,'fair_star_tv_from_fair_site':3/8}
sharp={'event':'AND of three cells','mu_success_each':.25,'nu_success_each':.5,'unweighted_bound':.75,'weighted_bound':7/64,'actual_difference':7/64,'bound_reduction_factor':48/7}
spin={'convention':'sin(pi*sigma/2)=sqrt(q)/2; 0<sigma<1','q':1,'prior_sigma':2/3,'correct_sigma':1/3,'prior_sigma_implied_q':4*math.sin(math.pi*(2/3)/2)**2,'correct_sigma_implied_q':4*math.sin(math.pi*(1/3)/2)**2}
result={'gate':gate,'L1_exact_checks':checks,'L1_violations':violations,'L2_graphs_considered':graphs,'L2_graphs_connecting_terminals':eligible,'L2_bond_state_visits':state_visits,'L2_violations':no_partial,'L2_by_n':by_n,'L3':star,'sharp_comparison':sharp,'independence_counterexample':{'marginal_tv_sum':0,'event_probability_difference':.5},'spin_check':spin,'seconds':time.monotonic()-started,'limitation':'Finite checks and numerical evaluations support the written proofs; they are not a proof of C0017 or of the unbounded graph lemma.'}
(ROOT/'MEASUREMENTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
