"""Proposed exact interval root/index certificate, not a global entry proof.

Refuses to run before the arithmetic and independent closed-form checks pass.
"""
from resource_limits import apply_limits
RESOURCE_LIMITS=apply_limits()
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from iv_exact import I,S,pi
from iv_scm import variables,full_driver,symmetric_driver,determinant

ROOT=Path(__file__).resolve().parents[1]

def invert_rational(a):
    n=len(a)
    a=[list(row)+[Fraction(int(i==j)) for j in range(n)]
       for i,row in enumerate(a)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if a[i][j])
        a[j],a[pivot]=a[pivot],a[j]
        d=a[j][j]
        a[j]=[v/d for v in a[j]]
        for i in range(n):
            if i!=j:
                d=a[i][j]
                a[i]=[v-d*w for v,w in zip(a[i],a[j])]
    return [row[n:] for row in a]

def main():
    for filename in ['iv_hardening_test.json','symmetric_closed_check.json','iv_scm_check.json']:
        check=json.loads((ROOT/'logs'/filename).read_text(encoding='utf-8-sig'))
        assert check.get('passed',check.get('engine_self_test_completed')) is True
    engine_check=json.loads((ROOT/'logs/iv_hardening_test.json').read_text(encoding='utf-8-sig'))
    assert engine_check['sha256']==hashlib.sha256(
        (ROOT/'scripts/iv_exact.py').read_bytes()).hexdigest()
    closed_check=json.loads((ROOT/'logs/symmetric_closed_check.json').read_text(encoding='utf-8-sig'))
    assert closed_check['sha256']==hashlib.sha256(
        (ROOT/'scripts/check_symmetric_closed.py').read_bytes()).hexdigest()
    driver_check=json.loads((ROOT/'logs/iv_scm_check.json').read_text(encoding='utf-8-sig'))
    for name,digest in driver_check['source_sha256'].items():
        assert digest==hashlib.sha256((ROOT/'scripts'/name).read_bytes()).hexdigest()
    center=[I.of(v) for v in ['0.36771969907760643','0.32538554792403124',
                              '0.4143941508524791']]
    radius=I.of('0.0000001').hi
    box=[I(v.lo-radius,v.hi+radius) for v in center]
    eta=I(I.of('0.4999999999').lo,I.of('0.5000000001').hi)
    f0=symmetric_driver(center,eta)
    fb=symmetric_driver(box,eta)
    jac=[list(row.d) for row in fb]
    midpoint=[[Fraction(v.lo+v.hi,2*S) for v in row] for row in jac]
    a_rational=invert_rational(midpoint)
    assert determinant(a_rational)!=0
    A=[[I.of(v) for v in row] for row in a_rational]
    M=[[I.of(int(i==j))-sum(A[i][l]*jac[l][j] for l in range(3))
        for j in range(3)] for i in range(3)]
    image=[center[i]-sum(A[i][l]*f0[l].v for l in range(3))
           +sum(M[i][j]*(box[j]-center[j]) for j in range(3))
           for i in range(3)]
    strict=all(b.lo<x.lo and x.hi<b.hi for b,x in zip(box,image))
    contraction=max(sum(v.maxabs() for v in row) for row in M)
    assert strict and contraction<S, 'Krawczyk inclusion or contraction failed'
    q,c,r=box
    physical=[q-c,q+c-4*r.square()]
    assert all(v.positive() for v in physical)
    j3=jac
    a1=-sum(j3[i][i] for i in range(3))
    a2=sum(j3[i][i]*j3[j][j]-j3[i][j]*j3[j][i]
           for i in range(3) for j in range(i+1,3))
    a3=-determinant(j3)
    hurwitz=[a1,a2,a3,a1*a2-a3]
    assert all(v.positive() for v in hurwitz), 'Symmetric block not certified Hurwitz'
    lifted=[q,c,q,r,r,r,r]
    j7=[list(row.d) for row in full_driver(variables(lifted),eta)]
    V=[[1,0],[0,0],[-1,0],[0,1],[0,1],[0,-1],[0,-1]]
    W=[[Fraction(1,2),0,Fraction(-1,2),0,0,0,0],
       [0,0,0,Fraction(1,4),Fraction(1,4),Fraction(-1,4),Fraction(-1,4)]]
    j2=[[sum(I.of(W[a][i])*j7[i][j]*V[j][b]
              for i in range(7) for j in range(7)) for b in range(2)]
         for a in range(2)]
    tr2=j2[0][0]+j2[1][1]
    det2=determinant(j2)
    assert tr2.negative() and det2.positive(), 'Student-odd even-teacher block failed'
    mu=2/pi()
    As=mu/(1+2*q).sqrt()
    Ac=mu/((1+q).square()-c.square()).sqrt()
    T=mu/(2*(1+q)-r.square()).sqrt()
    beta=(q*As+c*Ac-2*r*T)/(1+q)
    Tp=mu*r/((2*(1+q)-r.square())*(2*(1+q)-r.square()).sqrt())
    common=eta*(Tp+beta-As-Ac)
    unstable=eta*(Tp+beta-As+Ac)
    assert common.negative() and unstable.positive(), 'Teacher-odd sector signs failed'
    record={
        'passed':True,'scope':'Local plateau existence, uniqueness in box, physical PD, index one only; global entry remains open',
        'eta':eta.record(),'root_box':[v.record() for v in box],
        'krawczyk_image':[v.record() for v in image],
        'strict_inclusion':strict,'contraction_numerator':str(contraction),
        'contraction_denominator':str(S),
        'rational_preconditioner':[[str(v) for v in row] for row in a_rational],
        'physical_margins':[v.record() for v in physical],
        'symmetric_jacobian':[[v.record() for v in row] for row in j3],
        'cubic_hurwitz':[v.record() for v in hurwitz],
        'student_odd_block':[[v.record() for v in row] for row in j2],
        'student_odd_trace':tr2.record(),'student_odd_determinant':det2.record(),
        'teacher_odd_common':common.record(),'unstable_lambda':unstable.record(),
        'source_sha256':{name:hashlib.sha256((ROOT/'scripts'/name).read_bytes()).hexdigest()
                         for name in ['iv_exact.py','iv_scm.py','certify_plateau.py',
                                      'check_symmetric_closed.py']},
    }
    (ROOT/'logs/plateau_interval_certificate.json').write_text(
        json.dumps(record,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'eta':eta.record(),'lambda':unstable.record(),
                      'scope':record['scope']}),flush=True)

if __name__=='__main__': main()
