"""Meaningful exact-oracle checks for the rational residual certificate."""
import copy
from fractions import Fraction as F
import json
from pathlib import Path
from qso_certified_solver import validate_pairs,equiprobable_input,solve,certify
from qso_verify_certificate import verify_certificate

def check_case(name,data,true_fixed):
    result=solve(validate_pairs(data))
    verify_certificate(result,data)
    x=[F(v) for v in result['candidate']]
    actual=sum(abs(a-b) for a,b in zip(x,true_fixed))
    assert result['tolerance_met']
    assert actual<=F(result['certified_error_l1_upper'])
    for (lo,hi),v in zip(result['coordinate_intervals'],true_fixed):
        assert F(lo)<=v<=F(hi)
    return {'name':name,'known_fixed_point':[str(v) for v in true_fixed],
            'actual_error_l1':str(actual),'result':result}

results=[check_case('equiprobable interior',equiprobable_input(),[F(1,4)]*4)]
rows=[]
for i in range(4):
    for j in range(i,4):
        allowed=[k for k in range(3) if k not in (i,j)]
        rows.append({'i':i,'j':j,'p':[str(F(1,len(allowed))) if k in allowed else '0'
                                      for k in range(4)]})
results.append(check_case('invariant triple boundary',{'pairs':rows},[F(1,3)]*3+[F(0)]))

invalid=[]
for name,modify in [
    ('parent offspring leakage',lambda d:d['pairs'][0].update(p=['1','0','0','0'])),
    ('nonstochastic row',lambda d:d['pairs'][0].update(p=['0','1/4','1/4','1/4'])),
    ('JSON floating point',lambda d:d['pairs'][0].update(p=[0,.25,.25,.5])),
    ('missing pair',lambda d:d['pairs'].pop()),
]:
    data=copy.deepcopy(equiprobable_input());modify(data)
    try:
        validate_pairs(data)
    except ValueError:
        invalid.append(name)
    else:
        raise AssertionError('Invalid input was accepted: '+name)

tiny=copy.deepcopy(equiprobable_input())
delta=F(1,10**20)
tiny['pairs'][0]['p']=['0',str(F(1,3)+delta),str(F(1,3)-delta),'1/3']
P=validate_pairs(tiny)
exact=certify(P,[F(1,4)]*4)
assert verify_certificate(exact,tiny)['residual']==delta/8
rejected_api=[]
for name,call in [
    ('float candidate false-zero regression',lambda:certify(P,[.25]*4)),
    ('boolean tolerance',lambda:solve(P,True,max_steps=0)),
    ('NaN tolerance',lambda:solve(P,float('nan'),max_steps=0)),
    ('infinite tolerance',lambda:solve(P,float('inf'),max_steps=0)),
]:
    try:
        call()
    except ValueError:
        rejected_api.append(name)
    else:
        raise AssertionError('Invalid API input accepted: '+name)

report={'status':'all exact-oracle assertions passed','cases':results,
        'invalid_inputs_rejected':invalid,
        'api_regressions_rejected':rejected_api,
        'tiny_perturbation_exact_certificate':exact,
        'scope':'Checks the finite implementation and known examples; the universal theorem is analytic.'}
Path(__file__).with_name('qso_solver_verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':report['status'],'certified_cases':len(results),
                  'invalid_inputs_rejected':len(invalid),
                  'api_regressions_rejected':len(rejected_api),
                  'boundary_search_step':results[1]['result']['search_step']}))
