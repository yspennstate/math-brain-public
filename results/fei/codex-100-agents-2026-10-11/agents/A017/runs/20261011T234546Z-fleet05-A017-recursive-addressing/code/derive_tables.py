"""Verify newly derived spend formulas against existing exact tree receipts."""
from pathlib import Path
from fractions import Fraction as F
import json

R=Path(__file__).resolve().parents[1]
v=json.loads((R/'out'/'validation.json').read_text())
checks=[]
for n in [4,6]:
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    code=sum(1<<(n+pairs.index((i,i+1))) for i in range(0,n,2))
    for r in range(n+1):
        tree=next(t for t in v['trees'] if t['n']==n and t['qcode']==code and t['rows']==[1<<i for i in range(r)])
        k=n-r-r%2;s=k//2;delta=F(1,1<<n)
        expected=F(r,2)+F(1,1<<r)*(1-F(1,1<<s))+2*s*delta
        assert F(tree['spent_influence'])==expected
        terminal=tree['point_defect_terminal']
        assert len(terminal)==1
        leaf=terminal[0];d=n-r-s
        assert len(leaf['remaining_controls'])==d
        assert F(leaf['weight'])==F(1,1<<(r+s))
        assert F(leaf['weight'])*F(leaf['I_minus_1'])==2*d*delta
        checks.append(dict(n=n,r=r,k=k,s=s,d=d,spent_influence=str(expected),
                           point_terminal_weight=leaf['weight'],weighted_point_terminal_influence=str(2*d*delta)))

def rounded(interval,digits=9):
    a,b=map(F,interval);scale=10**digits
    lo=(a.numerator*scale)//a.denominator
    hi=-((-b.numerator*scale)//b.denominator)
    return [str(F(lo,scale)),str(F(hi,scale))]

samples=[]
for s in v['samples']:
    samples.append(dict(n=s['n'],r=s['r'],k=s['k'],H_exact=s['H']['log2_prime_form'],
                        H_rational_enclosure=rounded(s['H']['interval']),I=s['I'],
                        total_root_boundary=s['total_root_boundary'],
                        control_boundary=s['control_boundary'],data_boundary=s['data_boundary']))
result=dict(status='PASS',matching_spend_cases=len(checks),exact_spend_assertions=5*len(checks),
            matching_spend=checks,samples=samples,
            note='Derived from completed frozen outputs; no new Boolean search or dimension increase.')
(R/'out'/'tables.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status='PASS',matching_spend_cases=len(checks),exact_spend_assertions=5*len(checks)),indent=2))
