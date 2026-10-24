"""A bounded exact-arithmetic measurement; the proofs are in the Markdown packet."""
from fractions import Fraction as F
from pathlib import Path
from time import perf_counter
import json

JOB=Path(__file__).resolve().parent
gate_path=JOB/'COMPUTE_GATE.json'
gate=json.loads(gate_path.read_text(encoding='utf-8'))
assert gate['status']=='ready', 'This compute gate is single-use.'
start=perf_counter()
evaluations=0
cases=[]
def evaluate():
    global evaluations
    evaluations+=1
    assert evaluations<=gate['max_evaluations']
    assert perf_counter()-start<gate['max_internal_runtime_seconds']

gammas=[F(n,10) for n in range(1,20)]
xi=F(1)
identity_cases=0
for gamma in gammas:
    q=2/gamma+gamma/2
    for alpha in [F(-2),F(-1),F(0),gamma,F(1),F(3,2),F(2)]:
        evaluate()
        value=(2-alpha*alpha/2)/(xi*(q-alpha))
        gap=(alpha-gamma)**2/(2*xi*(q-alpha))
        assert gamma/xi-value==gap
        assert gap>=0 and (gap==0)==(alpha==gamma)
        identity_cases+=1

for gamma in gammas:
    evaluate()
    q=2/gamma+gamma/2
    old_prediction=gamma*q-gamma*gamma/2
    actual=2-gamma*gamma/2
    error=old_prediction-actual
    assert old_prediction==2 and error==gamma*gamma/2 and error>0
    cases.append({'gamma':str(gamma),'false_universal_kpz_prediction':str(old_prediction),'source_backed_euclidean_dimension':str(actual),'error':str(error)})

boundary=[]
for n in [10,100,1000,10000]:
    epsilon=F(1,n)
    gamma=2-epsilon
    q=2/gamma+gamma/2
    for c in [F(0),F(1,4),F(1)]:
        evaluate()
        delta=c*epsilon**2
        alpha=2-delta
        value=(2-alpha*alpha/2)/(q-alpha)
        predicted_limit=2*c/(c+F(1,4))
        assert q-2==epsilon**2/(2*gamma)
        boundary.append({'n':n,'c':str(c),'normalized_ratio':str(value),'decimal':float(value),'limiting_value':str(predicted_limit)})

evaluate()
brownian={'gamma_squared':'8/3','metric_dimension':'4','false_universal_kpz_prediction':'2','source_backed_euclidean_dimension':str(2-F(8,3)/2),'error':str(F(8,3)/2)}
elapsed=perf_counter()-start
result={'command':'python -X utf8 measure.py','gate_id':gate['gate_id'],'evaluations':evaluations,'exact_deficit_checks':identity_cases,'dependent_set_bridge':{'before_inconsistent_cases':len(cases),'after_using_thick_point_result_inconsistent_cases':0,'cases':cases,'known_brownian_anchor':brownian},'boundary_checks':boundary,'runtime_seconds':elapsed,'proof_status':'Arithmetic measurements supplement source-backed written proofs. No formal checker or independent review is implied.'}
(JOB/'MEASUREMENTS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
gate['status']='consumed'
gate['evaluations']=evaluations
gate['runtime_seconds']=elapsed
gate_path.write_text(json.dumps(gate,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['dependent_set_bridge','boundary_checks']},indent=2))
print('Universal dependent-set KPZ false cases:',len(cases),'of',len(cases))
print('Brownian anchor:',json.dumps(brownian))
