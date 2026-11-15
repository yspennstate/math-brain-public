"""Independent exact radius-curve certificate from our own prefix ledger."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from datetime import datetime
import contextlib,json,math,itertools
from audit_t067_uniform_own import polynomial,C,V,add,sub,sc,mul,pw,ev,deg,bern_axis,direct_G,memcheck
root=Path(__file__).resolve().parent
proof=Path('~/brain_workers/w682/proofs/T067-LOCAL-CURVE-001_v1.md')
initial=sha256(proof.read_bytes()).hexdigest()
def divide_l(p,d):
    q={};rem=dict(p);lead=max(i for i,j in d);assert all(j==0 for i,j in d)
    leading=d[lead,0]
    while rem:
        i,j=max(rem)
        assert i>=lead,('nonzero division remainder',rem)
        coef=rem[i,j]/leading;term={(i-lead,j):coef}
        q=add(q,term);rem=sub(rem,mul(term,d))
    return q
with (root/'checks/t067_local_curve_own.log').open('w',encoding='utf-8') as log,contextlib.redirect_stdout(log):
    memcheck();delta=F(1,1000)
    q0=polynomial(F(0),delta,1);qp=polynomial(F(1),delta,1);qm=polynomial(F(-1),delta,1)
    linear=sc(sub(qp,qm),F(1,2));quadratic=sc(sub(add(qp,qm),sc(q0,2)),F(1,2))
    assert add(q0,sc(linear,2),sc(quadratic,4))==polynomial(F(2),delta,1)
    l=V(0);m=sc(pw(sub(C(1),l),2),F(5,4))
    qcurve=add(q0,mul(linear,m),mul(quadratic,pw(m,2)))
    denominator=pw(sub(C(1),l),3)
    p=divide_l(sc(qcurve,1728000),denominator)
    assert mul(p,denominator)==sc(qcurve,1728000)
    assert deg(p)==(18,6)
    zpoly={(i,j):c/F(2)**i for (i,j),c in p.items()}
    sources=Path('~/brain_workers/w682/checks')
    raw=json.loads((sources/'local_curve_c5over4_Lhalf_raw.json').read_text(encoding='utf-8'))
    stored={tuple(e):F(int(v)) for e,v in raw['poly']}
    assert sc(zpoly,32768)==stored
    phases=[];phase0=bern_axis(zpoly,0,18);phase1=bern_axis(zpoly,1,6)
    final=bern_axis(phase0,1,6)
    assert final==bern_axis(phase1,0,18)
    for name,possibilities in [('bern1',[('lambda-first',phase0),('prefix-first',phase1)]),('bern2',[('both',final)])]:
        data=json.loads((sources/f'local_curve_c5over4_Lhalf_{name}.json').read_text(encoding='utf-8'))
        supplied={tuple(e):F(int(v)) for e,v in data['poly']}
        matches=[]
        for label,ours in possibilities:
            if set(ours)!=set(supplied):continue
            key=next(iter(ours));ratio=supplied[key]/ours[key]
            if ratio>0 and sc(ours,ratio)==supplied:matches.append({'phase':label,'positive_scale':str(ratio)})
        assert len(matches)==1,(name,matches)
        phases.append({'name':name,**matches[0]})
    signs={'positive':0,'zero':0,'negative':0};positive=[];zeros=[]
    for e in itertools.product(range(19),range(7)):
        value=final.get(e,F(0));signs['positive' if value>0 else 'negative' if value<0 else 'zero']+=1
        if value>0:positive.append(value)
        if not value:zeros.append(e)
    assert signs=={'positive':127,'zero':6,'negative':0}
    controls=0
    for d in [4,9,16,25,49,100,225,400]:
        strength=F(1,math.isqrt(d));threshold=F(5,4)*(1-strength)**2
        for k in sorted({2,3,min(7,d),d//2,d}):
            if not 2<=k<=d:continue
            r=F(k-2,d-2)
            assert ev(p,strength,r)==1728000*(1+strength)**3*direct_G(d,k,threshold,delta)
            controls+=1
assert sha256(proof.read_bytes()).hexdigest()==initial
result={'at':datetime.now().astimezone().isoformat(),'status':'independent exact local-curve certificate PASS','proof_sha256':initial,'degrees':[18,6],'power_terms':len(zpoly),'full_exact_division_and_identity':True,'full_author_raw_coefficients_match':True,'author_basis_phases_match':phases,'bernstein_signs':signs,'zero_indices':zeros,'minimum_positive_bernstein':str(min(positive)),'unsummed_recurrence_controls':controls,'method':'Own rational prefix ledger at M0,+1,-1, coefficientwise polynomial substitution and exact division; no author executable code imported','power_coefficients':[[list(e),str(c)] for e,c in sorted(zpoly.items())],'bernstein_coefficients':[[list(e),str(c)] for e,c in sorted(final.items())],'evaluator_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
(root/'checks/t067_local_curve_own.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','proof_sha256','degrees','bernstein_signs','unsummed_recurrence_controls']}))
