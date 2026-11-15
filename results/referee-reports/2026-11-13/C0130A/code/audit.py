"""Independent identities and data audits for the numerical certificates."""
import json
from pathlib import Path
import sympy as sp
from escape import kernel_row

counts=0
for stack in [[sp.Rational(4,5)]*3,
              [sp.Rational(9,10),sp.Rational(2,5),sp.Rational(9,10),sp.Rational(4,5)]]:
    M=len(stack)
    for i in range(6):
        row,mean=kernel_row(stack,i,13,sp.Rational)
        for j,actual in enumerate(row):
            # Independent coefficient extraction from all preterminal coins.
            probabilities=[stack[k] if k<M else sp.Rational(1,2)
                           for k in range(i+j+1)]
            coeff=[sp.Rational(1)]
            for p in probabilities[:-1]:
                new=[sp.Rational(0)]*(len(coeff)+1)
                for k,v in enumerate(coeff):
                    new[k]+=v*(1-p)
                    new[k+1]+=v*p
                coeff=new
            expected=probabilities[-1]*coeff[i]
            assert expected==actual
            counts+=1
        if i>=M-1:
            delta=sum(2*p-1 for p in stack)
            assert mean-i==1-delta

for path in Path('data').glob('cert_*.json'):
    value=json.loads(path.read_text())
    lo,hi=sp.Rational(value['rational_lower']),sp.Rational(value['rational_upper'])
    assert 0<lo<=hi<=sp.Rational(value['params'][0])
    if len(value['params'])==2:
        p,q=map(sp.Rational,value['params'])
        expected=(2*p+2*q-3)/(2*q-1)
        assert lo==hi==expected

refined=Path('data/cert_m3_p08_k128.json')
if refined.exists():
    fine=json.loads(refined.read_text())
    flo,fhi=map(sp.Rational,[fine['rational_lower'],fine['rational_upper']])
    for path in [Path('data/certificate_m3_p08_k64.json'),Path('data/cert_m3_p08.json')]:
        coarse=json.loads(path.read_text())
        clo,chi=map(sp.Rational,[coarse['rational_lower'],coarse['rational_upper']])
        assert clo<=flo<=fhi<=chi

result=dict(kernel_coefficients_checked=counts,
            signed_cookie_kernel_included=True,
            exact_drift_identity=True,
            two_cookie_closed_forms_match=True,
            refined_certificate_nested=refined.exists(),
            certificate_endpoint_ordering=True)
Path('data/audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
