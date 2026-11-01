import itertools,json,time
from fractions import Fraction as F
from pathlib import Path
start=time.perf_counter()
def rule(v): return int(all(v) if len(v)==2 else any(v))
checks=0
for d in [F(k,100) for k in range(101)]:
    weights={(0,0):(1-d)/2,(1,1):(1-d)/2,(0,1):d/2,(1,0):d/2}
    out=F(0)
    for degree,prior in [(2,F(3,5)),(3,F(2,5))]:
        val=F(0)
        for pairs in itertools.product(weights,repeat=degree):
            prob=F(1)
            for pair in pairs: prob*=weights[pair]
            if rule([p[0] for p in pairs])!=rule([p[1] for p in pairs]): val+=prob
        out+=prior*val
    assert out==F(9,10)*d-F(3,5)*d*d+F(1,10)*d*d*d
    assert 0<=out<=F(9,10)*d
    checks+=1
atoms={(2,0):F(9,20),(2,1):F(3,20),(3,0):F(1,20),(3,1):F(7,20)}
selected={a:F(0) for a in atoms}; configurations=0
for degree,prior in [(2,F(3,5)),(3,F(2,5))]:
    for children in itertools.product(atoms,repeat=degree):
        configurations+=1
        prob=prior
        for a in children: prob*=atoms[a]
        colour=rule([a[1] for a in children]); eligible=[a for a in children if a[1]==colour]
        assert eligible
        for a in eligible: selected[a]+=prob/len(eligible)
assert selected==atoms
d=.5
for _ in range(20): d=.9*d-.6*d*d+.1*d*d*d
receipt={'problem_id':'P0033','label':'exact finite checks; numerical depth-20 recursion','disagreement_parameters_checked':checks,'selected_child_configurations_checked':configurations,'selected_child_total_variation_error':0,'depth20_disagreement':d,'depth20_proved_upper_bound':.5*.9**20,'elapsed_seconds':time.perf_counter()-start,'command':'python -B -X utf8 checks/p0033_exact.py','audit_status':'PENDING w347'}
root=Path(__file__).resolve().parents[1]
(root/'checks/P0033_receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
with (root/'results.jsonl').open('a',encoding='utf-8') as f: f.write(json.dumps({'row':'S1.O.w331.003','problem_id':'P0033','label':'proof, pending independent audit','statement':'The recorded AND/OR candidate has disagreement contraction d_(n+1)<=0.9 d_n; the measurable same-colour flow preserves GW and is nonergodic.','source_quote':'GW is stationary, the root colour is invariant along the chain','source_path':'~/<private-repo>/06_math_research/prob1000_lean_20260908/REPORT_thirteen_settled_2026-09-08.md','proof_path':str(root/'proofs/P0033.md'),'measurement':receipt,'audit_status':'PENDING w347'})+'\n')
print(json.dumps(receipt))
