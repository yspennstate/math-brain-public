"""Exact finite-graph checks; these are corroboration, not a parent proof."""
from decimal import Decimal, localcontext
from fractions import Fraction as Q
import itertools
import json
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent
GATE = json.loads((ROOT / "compute_gate.json").read_text(encoding="utf-8"))
START = time.perf_counter()

def check_time():
    if time.perf_counter()-START > GATE["max_elapsed_seconds"]:
        raise RuntimeError("fresh compute gate elapsed-time limit")

def roots(n, edges, mask, identified=()):
    parent = list(range(n))
    def find(x):
        while x != parent[x]:
            x = parent[x]
        return x
    def merge(x, y):
        parent[find(x)] = find(y)
    for block in identified:
        for vertex in block[1:]:
            merge(block[0], vertex)
    for index, (u, v) in enumerate(edges):
        if mask & (1 << index):
            merge(u, v)
    return tuple(find(v) for v in range(n))

def law(n, edges, p, q, boundary):
    assert len(edges) <= GATE["max_edges_per_enumerated_graph"]
    assert 2**len(edges) <= GATE["max_configurations_per_graph"]
    result = {}
    for mask in range(2**len(edges)):
        count = mask.bit_count()
        clusters = len(set(roots(n, edges, mask, boundary)))
        result[mask] = p**count * (1-p)**(len(edges)-count) * q**clusters
    normalizer = sum(result.values())
    return {mask:weight/normalizer for mask,weight in result.items()}

def marginal(distribution, index):
    return sum(probability for mask,probability in distribution.items() if mask & (1<<index))

def path_gap(length, p, q):
    a = p/(p+q*(1-p))
    return (q-1)*(1-a)*a**length/(1+(q-1)*a**length)

graphs = [
    ("path2", 3, [(0,1),(1,2)], (0,2)),
    ("path4", 5, [(0,1),(1,2),(2,3),(3,4)], (0,4)),
    ("triangle", 3, [(0,1),(1,2),(2,0)], (0,2)),
    ("square", 4, [(0,1),(1,2),(2,3),(3,0)], (0,2)),
    ("square_diagonal", 4, [(0,1),(1,2),(2,3),(3,0),(0,2)], (0,2)),
]
identity_checks = witness_checks = tv_checks = path_checks = spin_checks = 0
for name,n,edges,endpoints in graphs:
    for q,p in itertools.product((1,2,3,5), (Q(1,3),Q(1,2),Q(2,3))):
        check_time()
        free = law(n,edges,p,q,())
        wired = law(n,edges,p,q,(endpoints,))
        a = p/(p+q*(1-p))
        for boundary,distribution in (((),free),((endpoints,),wired)):
            for index,(u,v) in enumerate(edges):
                connection = sum(probability for mask,probability in distribution.items() if (lambda r:r[u]==r[v])(roots(n,edges,mask & ~(1<<index),boundary)))
                assert marginal(distribution,index) == a+(p-a)*connection
                identity_checks += 1
        differences = [marginal(wired,index)-marginal(free,index) for index in range(len(edges))]
        assert min(differences) >= 0
        events = [lambda mask:bool(mask), lambda mask:mask==(1<<len(edges))-1, lambda mask:mask.bit_count()>=2, lambda mask:mask.bit_count()%2==1]
        for event in events:
            gap = abs(sum(probability for mask,probability in wired.items() if event(mask))-sum(probability for mask,probability in free.items() if event(mask)))
            assert gap <= sum(differences)
            witness_checks += 1
        for selected in (tuple(range(len(edges))), tuple(range(0,len(edges),2))):
            def projected(distribution):
                projected_law = {}
                for mask,probability in distribution.items():
                    key = tuple(bool(mask & (1<<index)) for index in selected)
                    projected_law[key] = projected_law.get(key,Q(0))+probability
                return projected_law
            wf,ff = projected(wired),projected(free)
            total_variation = sum(abs(wf[key]-ff[key]) for key in wf)/2
            assert total_variation <= sum(differences[index] for index in selected)
            tv_checks += 1
        if name.startswith("path"):
            for difference in differences:
                assert difference == path_gap(len(edges),p,q)
                path_checks += 1
        # Independently check the FK-to-spin energy normalization by enumerating spins.
        # exp(beta)=1/(1-p), so all weights remain rational.
        if q in (2,3):
            for boundary,distribution in ((False,free),(True,wired)):
                partition = Q(0)
                equal = [Q(0)]*len(edges)
                for spin in itertools.product(range(q),repeat=n):
                    if boundary and any(spin[vertex]!=0 for vertex in endpoints):
                        continue
                    indicators = [spin[u]==spin[v] for u,v in edges]
                    weight = (1/(1-p))**sum(indicators)
                    partition += weight
                    for index,indicator in enumerate(indicators):
                        if indicator:
                            equal[index] += weight
                for index in range(len(edges)):
                    assert marginal(distribution,index) == p*equal[index]/partition
                    spin_checks += 1

path_measurements=[]
for length in (2,4,8,16,32):
    gap=path_gap(length,Q(1,2),3)
    path_measurements.append({"length":length,"q":3,"p":"1/2","gap_exact":str(gap),"gap_decimal":float(gap),"naive_positive_gap_claim":gap>0,"corrected_infinite_transition_claim":False,"reason":"exact geometric gap tends to zero; fixed finite-temperature 1D limit is iid Bernoulli(a)"})

with localcontext() as context:
    context.prec=60
    beta_mf=4*Decimal(2).ln()
    barrier=Decimal(3).ln()-Decimal(19)/12*Decimal(2).ln()
    assert 3**12>2**19 and barrier>0
    barrier_result={"normalized_beta_mf":str(beta_mf),"barrier_exact":"log(3)-(19/12)log(2)","barrier_decimal":str(barrier),"arithmetic_positivity_witness":[3**12,2**19],"minimum_generic_BC_error_d3":"beta_mf/9", "minimum_generic_BC_error_d3_decimal":str(beta_mf/9),"error_to_barrier_ratio_lower_bound":str(beta_mf/(9*barrier)),"warning":"This is a lower bound on the published error allowance, not on the actual physical covariance."}

result={"command":"python -X utf8 ~/brain_workers/w465/verify_bridges.py","elapsed_seconds":time.perf_counter()-START,"status":"PASS","identity_checks_exact":identity_checks,"event_gap_checks_exact":witness_checks,"total_variation_checks_exact":tv_checks,"path_formula_checks_exact":path_checks,"FK_spin_energy_normalization_checks_exact":spin_checks,"path_measurements":path_measurements,"narrow_reasoning_regression":{"family":"five endpoint-wired path lengths at q=3,p=1/2","before_false_transition_claims":sum(row["naive_positive_gap_claim"] for row in path_measurements),"after_false_transition_claims":sum(row["corrected_infinite_transition_claim"] for row in path_measurements),"improvement_scope":"This exact path family only; no broad recall or proof-solving improvement claimed."},"mean_field":barrier_result,"independent_review":False,"formal_proof":False,"parent_problem_proved":False}
output=ROOT/"evidence"
output.mkdir(exist_ok=True)
(output/"bridge_checks.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
