"""Small exact arithmetic verification, no stochastic experiment or live writes."""
from fractions import Fraction as Q
import json
import math
from pathlib import Path
import re
import time

ROOT = Path(__file__).resolve().parent
started = time.monotonic()

def add(a, b): return (a[0]+b[0], a[1]+b[1])
def sub(a, b): return (a[0]-b[0], a[1]-b[1])
def scale(a, r): return (a[0]*r, a[1]*r)
def itimes(a): return (-a[1], a[0])
def mul(a, b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def size(a): return abs(a[0])+abs(a[1])
def fmt(a): return [str(a[0]), str(a[1])]

def field(case, orientation, x, y):
    if case == "split_conjugate_z_z":
        return (x, -y if orientation == "H" else y)
    if case == "coherent_z": return (x, y)
    if case == "coherent_z_squared": return (x*x-y*y, 2*x*y)
    raise ValueError(case)

def stencil(case, d, x, y):
    e = field(case, "H", x+d/2, y)
    w = field(case, "H", x-d/2, y)
    n = field(case, "V", x, y+d/2)
    s = field(case, "V", x, y-d/2)
    weak = add(sub(e,w), itimes(sub(n,s)))
    h = scale(add(e,w),Q(1,2))
    v = scale(add(n,s),Q(1,2))
    return weak, sub(h,v), scale(add(h,v),Q(1,2))

def average(case,d,x,y): return stencil(case,d,x,y)[2]

rows=[]
cases = ["coherent_z","coherent_z_squared","split_conjugate_z_z"]
for case in cases:
    for mesh in (4,8,16):
        d=Q(1,mesh)
        residual=Q(0)
        defect=Q(0)
        checked=0
        for j in range(1,mesh):
            for k in range(1,mesh):
                weak, gap, _ = stencil(case,d,Q(j,mesh),Q(k,mesh))
                residual=max(residual,size(weak))
                defect=max(defect,size(gap))
                checked+=1
        x=y=Q(1,2)
        dx=scale(sub(average(case,d,x+d,y),average(case,d,x-d,y)),1/(2*d))
        dy=scale(sub(average(case,d,x,y+d),average(case,d,x,y-d)),1/(2*d))
        dbar=scale(add(dx,itimes(dy)),Q(1,2))
        contour=(Q(0),Q(0))
        for k in range(mesh):
            t=(Q(k)+Q(1,2))*d
            for px,py,dz in [(t,Q(0),(d,Q(0))),(Q(1),t,(Q(0),d)),(t,Q(1),(-d,Q(0))),(Q(0),t,(Q(0),-d))]:
                contour=add(contour,mul(average(case,d,px,py),dz))
        expected_dbar=(Q(1,2),Q(0)) if case.startswith("split") else (Q(0),Q(0))
        expected_contour=(Q(0),Q(1)) if case.startswith("split") else (Q(0),Q(0))
        assert residual == 0
        assert dbar == expected_dbar
        assert contour == expected_contour
        assert (defect <= 2*d) == (not case.startswith("split"))
        rows.append({"case":case,"mesh":mesh,"vertices_checked":checked,"weak_identity_max_residual":str(residual),"orientation_gap_max":str(defect),"orientation_gap_bound_2delta_satisfied":defect<=2*d,"dbar_of_vertex_average":fmt(dbar),"unit_square_contour_integral":fmt(contour)})

epsilon=Q(1,100)
tv=1-2*epsilon
endpoint_sensitive=2*epsilon*(1-epsilon)
endpoint_bound=3*tv*endpoint_sensitive
hybrid_sensitivities=[endpoint_sensitive,(1-epsilon)**2+epsilon**2,endpoint_sensitive]
hybrid_bound=tv*sum(hybrid_sensitivities)
def majority_probability(probabilities):
    total=Q(0)
    for mask in range(8):
        probability=Q(1)
        for i,p in enumerate(probabilities):
            probability*=p if mask & (1<<i) else 1-p
        if mask.bit_count() >= 2: total+=probability
    return total
actual_difference=majority_probability([1-epsilon]*3)-majority_probability([epsilon]*3)
assert actual_difference == 1-6*epsilon**2+4*epsilon**3
assert actual_difference == hybrid_bound == Q(249851,250000)
assert endpoint_bound == Q(14553,250000) < actual_difference
hybrid_example={"epsilon":str(epsilon),"configurations_enumerated_per_endpoint":8,"actual_expectation_difference":str(actual_difference),"false_endpoint_only_bound":str(endpoint_bound),"correct_hybrid_bound":str(hybrid_bound),"hybrid_sensitivity_probabilities":[str(x) for x in hybrid_sensitivities]}
def spin_consistency(filename):
    candidate=json.loads((ROOT/"extracts"/filename).read_text(encoding="utf-8"))
    matches=re.findall(r"has spin sigma = ([0-9]+/[0-9]+)",candidate["result"])
    assert len(matches)==1
    sigma=Q(matches[0])
    implied_q=4*math.sin(math.pi*float(sigma)/2)**2
    valid=0<=sigma<=1 and abs(implied_q-1)<1e-12
    return {"candidate_path":"extracts/"+filename,"sigma":str(sigma),"source_equation_implied_q_numeric":implied_q,"equation_consistent_with_q_1":valid}
before_spin=spin_consistency("attempt_C0017_before.json")
after_spin=spin_consistency("attempt_C0017_after.json")
assert not before_spin["equation_consistent_with_q_1"] and after_spin["equation_consistent_with_q_1"]
per_case={case:[r for r in rows if r["case"]==case] for case in cases}
holomorphic={case:all(r["dbar_of_vertex_average"]==["0","0"] and r["unit_square_contour_integral"]==["0","0"] for r in rs) for case,rs in per_case.items()}
baseline_accept={case:all(r["weak_identity_max_residual"]=="0" for r in rs) for case,rs in per_case.items()}
with_coherence={case:baseline_accept[case] and all(r["orientation_gap_bound_2delta_satisfied"] for r in rs) for case,rs in per_case.items()}
false_before=sum(baseline_accept[case] and not holomorphic[case] for case in cases)
false_after=sum(with_coherence[case] and not holomorphic[case] for case in cases)
controls_kept=sum(with_coherence[case] and holomorphic[case] for case in cases)
assert (false_before,false_after,controls_kept)==(1,0,2)
record={"command":"python -X utf8 ~/brain_workers/w418/measure_obstruction.py","verification_kind":"Exact rational stencils and majority enumeration; independent numeric source-equation consistency diagnostic for saved spin candidates, with exact trigonometric derivation in the packet. No proof certification by computation.","cases":rows,"total_stencils_checked":sum(r["vertices_checked"] for r in rows),"baseline_weak_identity_only_false_acceptances":false_before,"with_orientation_gap_bound_false_acceptances":false_after,"holomorphic_positive_controls_retained":controls_kept,"scope":"A three-case local audit fixture, not an improvement measured on the live recall engine. The analytic formulas in INDEPENDENT_OBSTRUCTION.md establish the all-mesh statements.","principal_spin_check":{"before":before_spin,"after_candidate":after_spin,"numeric_tolerance":1e-12,"exact_source_derivation":"Under the principal source equation, sin(pi/6)=1/2 gives q=1 for sigma=1/3; sin(pi/3)=sqrt(3)/2 gives q=3 for sigma=2/3.","inconsistent_legacy_statements_before":int(not before_spin["equation_consistent_with_q_1"]),"after":int(not after_spin["equation_consistent_with_q_1"])},"hybrid_counterexample":hybrid_example,"elapsed_seconds":time.monotonic()-started}
(ROOT/"obstruction_measurement.json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
print(json.dumps(record,indent=2))
