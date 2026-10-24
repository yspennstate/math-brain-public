"""Exact finite checks of the independent obstruction, not an asymptotic proof."""
from fractions import Fraction as F
from itertools import product
import json
import pathlib
import time

root=pathlib.Path(__file__).resolve().parent
start=time.perf_counter()
gate={"created_at":"2026-10-10","task":"C0047 exact overlap/coupling controls","maximum_configurations_per_case":32,"maximum_seconds":5,"network":False,"gpu":False,"processes":1}
(root/"compute_gate.json").write_text(json.dumps(gate,indent=2),encoding="utf-8")
def joint(probabilities,route1,route2):
    answer=[F(0)]*4
    assert 2**len(probabilities)<=gate["maximum_configurations_per_case"]
    for bits in product((0,1),repeat=len(probabilities)):
        weight=F(1)
        for value,p in zip(bits,probabilities):weight*=p if value else 1-p
        a=all(bits[i] for i in route1)
        b=all(bits[i] for i in route2)
        answer[2*int(a)+int(b)]+=weight
    assert sum(answer)==1
    return answer

cases=[]
for p in (F(1,4),F(1,2),F(3,4)):
    row=joint([p]*3,(0,1),(0,2))
    a,b,ab=row[2]+row[3],row[1]+row[3],row[3]
    assert a==b==p*p and ab==p**3 and ab>a*b
    union=a+b-ab
    iid_union=2*p*p-p**4
    assert union<iid_union
    assert ab/b==p and (a-ab)/(1-b)==p*p/(1+p)
    independent=joint([p]*4,(0,1),(2,3))
    assert independent[3]==p**4
    cases.append({"p":str(p),"P_A":str(a),"P_B":str(b),"P_AB":str(ab),"iid_P_AB":str(a*b),"P_union":str(union),"iid_P_union":str(iid_union),"control_disjoint_P_AB":str(independent[3])})

coupling=[]
for t in (F(1,4),F(1,2),F(3,4)):
    # Two routes share a base edge but receive different slots there.
    for bits in product((0,1),repeat=4):
        base_shared=bits[0] or bits[1]
        a=bits[0] and bits[2]
        b=bits[1] and bits[3]
        assert not a or (base_shared and bits[2])
        assert not b or (base_shared and bits[3])
    row=joint([t]*4,(0,2),(1,3))
    assert row[3]==t**4
    coupling.append({"slot_probability":str(t),"shared_base_probability":str(1-(1-t)**2),"independent_route_probability":str(t*t),"joint_route_probability":str(row[3])})

result={"command":"python -X utf8 ~/brain_workers/w562/check_overlap.py","elapsed_seconds":time.perf_counter()-start,"overlap_cases":cases,"disjoint_controls":3,"slot_coupling_cases":coupling,"deterministic_inclusion_assignments_checked":48,"exact_arithmetic":True,"all_checks_passed":True,"scope":"Finite control only; infinite coupling needs the separate written product-space proof and independent referee."}
assert result["elapsed_seconds"]<gate["maximum_seconds"]
(root/"overlap_measurement.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
print(json.dumps(result,indent=2))
