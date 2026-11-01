"""Bounded exact-algebra checks. Not a formal proof or a proof of the Gibbs phase."""
import collections, datetime, itertools, json, math, pathlib, time, tracemalloc
from fractions import Fraction as F

ROOT=pathlib.Path(__file__).resolve().parent
started=time.perf_counter()
cpu_started=time.process_time()
tracemalloc.start()
gate=json.loads((ROOT/'COMPUTE_GATE.json').read_text(encoding='utf-8'))
assert gate['status']=='armed','A consumed gate cannot authorize a new run.'
assert gate['gpu'] is False and gate['training'] is False and gate['child_agents'] is False
gate_age=(datetime.datetime.now(datetime.timezone.utc)-datetime.datetime.fromisoformat(gate['created_utc'])).total_seconds()
assert 0<=gate_age<=60,'Compute gate is not fresh.'
gate['status']='running'
(ROOT/'COMPUTE_GATE.json').write_text(json.dumps(gate,indent=2)+'\n',encoding='utf-8')
counts=collections.Counter()

def checkpoint():
    assert sum(counts.values())<=gate['max_evaluations'],'Check-count gate exceeded.'
    assert time.process_time()-cpu_started<=gate['max_cpu_seconds'],'CPU gate exceeded.'
    assert time.perf_counter()-started<=gate['max_wall_seconds'],'Wall-time gate exceeded.'
    assert tracemalloc.get_traced_memory()[1]<=gate['max_python_allocation_bytes'],'Allocation gate exceeded.'

def poly_add(a,b):
    n=max(len(a),len(b)); c=[F(0)]*n
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    while len(c)>1 and c[-1]==0: c.pop()
    return tuple(c)

def poly_mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    while len(c)>1 and c[-1]==0: c.pop()
    return tuple(c)

def poly_scale(a,c): return tuple(c*x for x in a)

def add_term(expr,alpha,q,coeff):
    key=(tuple(alpha),q)
    value=poly_add(expr.get(key,(F(0),)),coeff)
    if all(x==0 for x in value): expr.pop(key,None)
    else: expr[key]=value

def derivative(expr,i):
    out={}
    for (alpha,q),coeff in expr.items():
        if alpha[i]:
            lowered=list(alpha); lowered[i]-=1
            add_term(out,lowered,q,poly_scale(coeff,alpha[i]))
        raised=list(alpha); raised[i]+=1
        add_term(out,raised,q+1,poly_scale(poly_mul(coeff,(F(2*q),F(1))),-1))
    return out

def powers(indices):
    return tuple(indices.count(i) for i in range(3))

ps=(F(0),F(1))
p2=poly_mul(ps,(F(2),F(1)))
p3=poly_mul(p2,(F(4),F(1)))
p4=poly_mul(p3,(F(6),F(1)))

for indices in itertools.product(range(3),repeat=2):
    expr={((0,0,0),0):(F(1),)}
    for i in indices: expr=derivative(expr,i)
    expected={}; add_term(expected,powers(indices),2,p2)
    if indices[0]==indices[1]: add_term(expected,(0,0,0),1,poly_scale(ps,-1))
    assert expr==expected,('Hessian identity',indices,expr,expected)
    counts['exact_hessian_component_identities']+=1

for indices in itertools.product(range(3),repeat=4):
    checkpoint()
    expr={((0,0,0),0):(F(1),)}
    for i in indices: expr=derivative(expr,i)
    expected={}; add_term(expected,powers(indices),4,p4)
    for a,b in itertools.combinations(range(4),2):
        if indices[a]==indices[b]:
            remaining=tuple(indices[k] for k in range(4) if k not in (a,b))
            add_term(expected,powers(remaining),3,poly_scale(p3,-1))
    for a,b,c,d in [(0,1,2,3),(0,2,1,3),(0,3,1,2)]:
        if indices[a]==indices[b] and indices[c]==indices[d]:
            add_term(expected,(0,0,0),2,p2)
    assert expr==expected,('Fourth derivative identity',indices,expr,expected)
    counts['exact_fourth_derivative_component_identities']+=1

assert poly_add(poly_add(p4,poly_scale(p3,6)),poly_scale(p2,3))==poly_mul(p2,(F(51),F(16),F(1)))
counts['exact_contraction_constant_identity']+=1

for R in range(3,65):
    checkpoint()
    dipole=2*F(1,R)-F(1,R+1)-F(1,R-1)
    assert dipole==-F(2,R*(R*R-1))
    assert abs(dipole)<=F(2,(R-2)**3)
    quadrupole=F(1,R+2)-4*F(1,R+1)+6*F(1,R)-4*F(1,R-1)+F(1,R-2)
    assert quadrupole==F(24,R*(R*R-1)*(R*R-4))
    assert quadrupole<=F(204,(R-2)**5)
    counts['exact_atomic_interaction_controls']+=2

for n in range(4,129):
    checkpoint()
    k=n//4
    assert (2*k+1)**2>=F(n*n,16)
    counts['exact_cone_cardinality_controls']+=1
    transverse=2*(4*k)**2
    for t in (-1,0,1):
        x1=4*n+t
        assert F(x1*x1,x1*x1+transverse)>=F(9,11)
        assert x1*x1+transverse<=36*n*n
        counts['exact_cone_geometry_controls']+=1
for s in (F(1,8),F(1,4),F(1,2),F(1),F(2)):
    assert (s+2)*F(9,11)-1>=F(7,11)
    counts['exact_cone_curvature_constant_controls']+=1

for n in range(1,6):
    checkpoint()
    shell=sum(max(abs(x),abs(y),abs(z))==n for x in range(-n,n+1) for y in range(-n,n+1) for z in range(-n,n+1))
    assert shell==24*n*n+2
    counts['independently_enumerated_lattice_shells']+=1

weights=[1,2,3,4,5,6]; energies=[0,1,3,4,6,9]; event=[3,4,5]; repair={3:0,4:1,5:2}
tau=min(energies[x]-energies[repair[x]] for x in event)
ratio=max(F(weights[x],weights[repair[x]]) for x in event)
assert tau==4 and ratio==4
for beta in (0.125,0.25,0.5,1,2,4):
    terms=[weights[i]*math.exp(-beta*energies[i]) for i in range(6)]
    probability=sum(terms[i] for i in event)/sum(terms)
    bound=float(ratio)*math.exp(-beta*tau)
    assert probability<=bound*(1+1e-12)
    counts['finite_weighted_repair_probability_controls']+=1

bundle=json.loads((ROOT/'bundle_001.json').read_text(encoding='utf-8'))
claims=[json.loads(x) for x in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
assert len({c['claim_id'] for c in claims})==len(claims)
allowed_status={'conjecture','numerical evidence','sketch','proved special case','independently checked proof'}
for c in claims:
    assert c['status'] in allowed_status
    for field in ['statement','assumptions','source','proof_or_counterexample','independent_reviewer','remaining_gap']: assert field in c
    counts['claim_schema_checks']+=1
keys={e['key'] for e in bundle['entries']}
assert len(keys)==len(bundle['entries'])==9
assert bundle['spec']=='mathbrain-draft-v1' and bundle['author_agent']=='w528'
for entry in bundle['entries']:
    for field in ['key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source']: assert field in entry
    assert entry['kind'] in {'concept','definition','lemma','theorem'}
    if entry['kind'] in {'lemma','theorem'}: assert isinstance(entry['proof_text'],str) and len(entry['proof_text'])>80
    else: assert entry['proof_text'] is None
    assert entry['source']['license'].startswith('owner-own-work')
    counts['draft_entry_schema_checks']+=1
assert next(e for e in bundle['entries'] if e['key']=='g')['kind']=='concept'
graph={k:[] for k in keys}
allowed_relations={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
for r in bundle['relations']:
    assert r['from_key'] in keys and r['kind'] in allowed_relations
    if 'to_key' in r: assert r['to_key'] in keys
    else: assert r['to_existing_logical']=='math:probability.core:open-problem-p0309-positive-temperature-crystalline-gibbs-phases-for-three-dimensional-ri'
    if r['kind']=='depends_on': graph[r['from_key']].append(r['to_key'])
    counts['draft_relation_schema_checks']+=1
seen=set(); visiting=set()
def visit(node):
    assert node not in visiting,'cyclic depends_on relation'
    if node in seen: return
    visiting.add(node)
    for child in graph[node]: visit(child)
    visiting.remove(node); seen.add(node)
for node in keys: visit(node)
counts['dependency_graph_acyclicity_checks']+=1

def dipole(R): return abs(-F(2,R*(R*R-1)))
def quadrupole(R): return F(24,R*(R*R-1)*(R*R-4))
measurement={
    'comparison':'Different explicitly stated charge hypotheses, not an improvement claim for the full Gibbs gas.',
    'dipole_interaction_at_R16':str(dipole(16)),
    'quadrupole_interaction_at_R16':str(quadrupole(16)),
    'dipole_observed_decay_exponent_R16_to_R32':math.log(float(dipole(16)/dipole(32)),2),
    'quadrupole_observed_decay_exponent_R16_to_R32':math.log(float(quadrupole(16)/quadrupole(32)),2),
    'analytic_asymptotic_exponents':{'neutral_dipole_at_s1':3,'dipole_free_quadrupole_at_s1':5}
}
result={
    'result':'PASS','command':'python -X utf8 verify_packet.py','date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'checks':dict(counts),'total_checks':sum(counts.values()),'measurements':measurement,'elapsed_seconds':time.perf_counter()-started,
    'formal_check':False,'trusted_axioms_receipt':None,'full_target_proved':False,'gap_G_proved':False,'independent_review':False,
    'scope':'Exact generalized-symbolic derivative identities; rational atomic controls; finite cone/shell controls; finite repair toy; draft structure. Analytic proofs and hypotheses remain in ATTEMPT.md.'
}
checkpoint()
gate.update({'status':'consumed','evaluations':sum(counts.values()),'runtime_cpu_seconds':time.process_time()-cpu_started,'runtime_wall_seconds':time.perf_counter()-started,'peak_python_allocation_bytes':tracemalloc.get_traced_memory()[1]})
(ROOT/'COMPUTE_GATE.json').write_text(json.dumps(gate,indent=2)+'\n',encoding='utf-8')
result['compute_gate']=gate
(ROOT/'VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
