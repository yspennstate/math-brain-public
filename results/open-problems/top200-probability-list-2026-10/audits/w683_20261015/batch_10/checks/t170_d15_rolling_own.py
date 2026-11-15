"""Independent exact verifier from the frozen proof, importing no author code."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime
import json

ROOT=Path(__file__).resolve().parents[1]
AUTHOR=Path('~/crash_recovery_20261014/workers_1015/term_362ebe34')
def digest(p): return sha256(p.read_bytes()).hexdigest()
manifest=json.loads((AUTHOR/'T170_D15_SUBMISSION.json').read_text(encoding='utf-8'))
hashes={}
for name,expected in manifest['files'].items():
    actual=digest(AUTHOR/name); assert actual==expected,(name,actual)
    hashes[name]=actual
for name,expected in manifest['dependencies'].items():
    assert digest(Path(name))==expected,name

data=json.loads((AUTHOR/'T170_EMBEDDED_d15_C512_BIAS.json').read_text(encoding='utf-8'))
C=data['cap']; S=data['scale']; H=data['bias']
assert (data['dimension'],C,S,len(H))==(15,512,2**40,512**2)
assert all(type(v) is int for v in H)
alpha=Q(48279340039,549755813888)
assert Q(data['axis_upper_conditional'])==alpha and (alpha*S).denominator==1
scaled_alpha=int(alpha*S)

# Count actual edges of binary initial segments inside Q14. No author's
# popcount/rate routine is imported. Every coordinate contributes separately.
rates=[0]
pop_prefix=[0]
for n in range(1,C+1):
    internal=sum(1 for v in range(n) for k in range(14)
                 if v < (v^(1<<k)) < n)
    boundary=28*n-2*internal
    pop_prefix.append(pop_prefix[-1]+(n-1).bit_count())
    assert internal==pop_prefix[-1] and boundary>0
    rates.append(boundary)
splits=0; min_split=None
for n in range(2,C+1):
    for b in range(1,n//2+1):
        slack=pop_prefix[n]-pop_prefix[n-b]-pop_prefix[b]-b
        assert slack>=0,(n,b)
        min_split=slack if min_split is None else min(min_split,slack)
        splits+=1

def h(a,b): return H[(a-1)*C+b-1]
max_res=None; tight=None; min_res=None; max_rate=0
for a in range(1,C+1):
    for b in range(1,C+1):
        base=h(a,b)
        ra=rates[a] if a<C else 0
        rb=rates[b]+max(a-b,0) if b<C else 0
        assert 1<=ra+rb+b<=29696
        max_rate=max(max_rate,ra+rb+b)
        lhs=b*(h(b,1)-base)+S-scaled_alpha*b
        if ra: lhs+=ra*(h(a+1,b)-base)
        if rb: lhs+=rb*(h(a,b+1)-base)
        assert lhs<=0,(a,b,lhs)
        if max_res is None or lhs>max_res: max_res,tight=lhs,[a,b]
        min_res=lhs if min_res is None else min(min_res,lhs)

def solve(matrix,rhs):
    n=len(rhs); t=[[Q(x) for x in row]+[Q(y)] for row,y in zip(matrix,rhs)]
    for c in range(n):
        pivot=next(i for i in range(c,n) if t[i][c])
        t[c],t[pivot]=t[pivot],t[c]
        v=t[c][c]; t[c]=[x/v for x in t[c]]
        for i in range(n):
            if i!=c:
                v=t[i][c]; t[i]=[x-v*y for x,y in zip(t[i],t[c])]
    return [row[-1] for row in t]

# Independent cap2 stationary law and one complete regeneration cycle.
states=[(a,b) for a in (1,2) for b in (1,2)]
G=[[0]*4 for _ in states]; killed=[[0]*4 for _ in states]
for i,(a,b) in enumerate(states):
    events=[((b,1),b)]
    if a<2: events.append(((a+1,b),rates[a]))
    if b<2: events.append(((a,b+1),rates[b]+max(a-b,0)))
    for state,rate in events:
        j=states.index(state)
        G[i][i]-=rate; G[i][j]+=rate
        killed[i][i]+=rate
        if j!=0: killed[i][j]-=rate
stationary=solve([[G[j][i] for j in range(4)] for i in range(3)]+[[1]*4],[0,0,0,1])
assert all(p>0 for p in stationary)
assert all(sum(stationary[j]*G[j][i] for j in range(4))==0 for i in range(4))
stationary_alpha=1/sum(p*b for p,(a,b) in zip(stationary,states))
cycle_t=solve(killed,[1]*4)[0]
cycle_a=solve(killed,[b for a,b in states])[0]
assert stationary_alpha==cycle_t/cycle_a==Q(883,1709)
wrong_cycle_a=solve(killed,[0 if (a,b)==(1,1) else b for a,b in states])[0]
assert cycle_t/wrong_cycle_a!=stationary_alpha
assert max_res+ tight[1]>0  # lowering scaled alpha by one fails here

floor=Q(88164156999,10**12)
diag=json.loads(Path('~/brain_workers/w685/T170/logs/chord5_exact_certificates.json').read_text(encoding='utf-8'))
row=next(r for r in diag['rows'] if r['d']==15)
raw=row['lower']; lower=Q(int(raw['n']),int(raw['d']))
assert floor<=lower and floor>alpha
receipt={
 'at':datetime.now().astimezone().isoformat(),'proof_sha256':hashes['T170-LEAD-ROLLING-D15-001_v1.md'],
 'author_files_hash_verified':hashes,'dependency_hashes_verified':manifest['dependencies'],
 'independently_recomputed_all_states':C*C,'compared_inequalities_not_author_residuals':True,
 'precision':'unbounded Python integers; Fraction exact controls and gap',
 'scale':S,'boundary_rates_independently_counted':C,'finite_splits':splits,'minimum_split_slack':min_split,
 'max_cleared_bias_residual':max_res,'max_residual_state':tight,'min_cleared_bias_residual':min_res,
 'max_total_selected_rate':max_rate,'proof_rate_bound':29696,
 'negative_control_lower_alpha_one_scale_unit':'fails at tight state',
 'negative_control_omitted_self_reward_ratio':str(cycle_t/wrong_cycle_a),
 'bias_min':min(H),'bias_max':max(H),'cap2_stationary':[str(x) for x in stationary],
 'cap2_cycle_time':str(cycle_t),'cap2_cycle_advances':str(cycle_a),'cap2_ratio':str(stationary_alpha),
 'axis':str(alpha),'diagonal_floor':str(floor),'raw_diagonal_lower':str(lower),'gap':str(floor-alpha),
 'mathematical_physical_proof':'separate line-by-line audit required',
 'account_gate':'actual account4; does not add distinct account from lead',
 'evaluator_sha256':digest(Path(__file__)), 'status':'exact finite certificate PASS'}
(ROOT/'checks/t170_d15_rolling_own.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:receipt[k] for k in ['status','independently_recomputed_all_states','max_cleared_bias_residual','max_residual_state','cap2_ratio','gap']}))
