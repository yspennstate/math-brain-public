"""Exact reviewed-version reconciliation and independent integer zero-cover audit."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime
from math import factorial
import json,hashlib
HERE=Path(__file__).resolve().parent
W=Path('~/brain_workers/w674')
A=Path('~/brain_workers/w683')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
spec=[('C005_four_message_core.md','T186-W674-C005',1,'T186-C005','c300345293448cb73e7e5f32d2afc66b36c0d58d8f124cc12b217c5e76a5e5da'),
 ('C007v2_tree_certificates.md','T186-W674-C007v2',2,'T186-C007','8e8cbdb850b13175f88f2f599e9a7eba216a5ef8174e2d5a0ffb71057d9f14e3'),
 ('C013_finite_subcritical_emptiness.md','T186-W674-C013',1,'T186-W674-C013','9c127b0e5c3825d994b570eb636602f029b3c798838331cc7f02ad58c513562a')]
first=(W/'AUDITS_FROM_REVIEWER.tsv').read_text(encoding='utf-8').splitlines()
second=(A/'AUDITS.tsv').read_text(encoding='utf-8').splitlines()
reviews=[]
for filename,firstid,version,secondid,digest in spec:
    proof=W/'T186/proofs'/filename
    assert sha(proof)==digest,(proof,sha(proof))
    rows=[l for l in first if l.split('\t')[:3]==[firstid,str(version),'PASS']]
    assert rows and any(digest[:16] in l for l in rows),(firstid,'missing exact first review')
    audit=A/'audits'/f'w674_{secondid}_v{version}.md'
    assert digest in audit.read_text(encoding='utf-8'),(audit,'proof hash mismatch')
    verdicts=[l for l in second if l.split('\t')[1:5]==['w674',secondid,str(version),'PASS']]
    assert verdicts,(secondid,'missing second verdict')
    reviews.append({'proof':str(proof),'proof_sha256':digest,'first_review_rows':rows,
        'second_review':str(audit),'second_review_sha256':sha(audit),'second_verdict':verdicts[-1]})
covers=[]
for k,cutoff,nboxes in [(3,F('6.84256'),733),(4,F('9.23414'),686)]:
    source=W/'T186/logs'/f't3_zero_JS_k{k}.json'
    own=A/'checks'/f't186_c007_zero_k{k}_own.json'
    data=json.loads(source.read_text(encoding='utf-8'))
    audited=json.loads(own.read_text(encoding='utf-8'))
    assert audited['input_sha256']==sha(source)
    assert audited['script_sha256']==sha(A/'checks/t186_c007_zero_own.py')
    assert len(audited['checked'])==nboxes,'Incomplete independent Arb replay'
    scale=int(data['scale'])
    boxes=sorted(data['done'],key=lambda r:int(r['c_scaled'][0]))
    assert len(boxes)==nboxes and F(data['cutoff'])==cutoff
    right=0
    for row in boxes:
        a,b=map(int,row['c_scaled']); u=list(map(int,row['upper_scaled']))
        assert 0<=a<=right and a<=b and b>=right,'Gap or malformed ordered cover'
        assert len(u)==3 and 0<=u[0]<=u[1]<=u[2]<=scale
        assert b**(k-1)*u[1]**(k-2)<factorial(k-1)*scale**(2*k-3),'Stopping test failed'
        right=b
    assert F(right,scale)==cutoff
    covers.append({'k':k,'cutoff':str(cutoff),'boxes':nboxes,'raw_sha256':sha(source),
        'auditor_receipt_sha256':sha(own),'coverage':'exact closed cover from zero to cutoff',
        'stopping_tests':'all strict exact integer inequalities pass',
        'limit':'Interval domination is supplied by the independent full Arb replay, not proved by the integer stopping check alone.'})
out={'at':datetime.now().astimezone().isoformat(),'claim':'T186-W674-C013 v1 with C005 v1/C007 v2',
    'status':'PASS reviewed-version reconciliation, own exact coverage/stopping audit and lead union-bound derivation',
    'reviews':reviews,'covers':covers,
    'analytic_check':'For k>=3, a=k/2-1>0; count min-degree sets by t=ceil(ks/2) edge witnesses. With eps<=k/(2ec), base ecs/(kn)<=1/2, so rounding t down increases bound. Bound is [e(ec/k)^(k/2)(s/n)^a]^s. Split at sqrt(n): two geometric tails vanish. Zero density plus absence of small min-degree-k sets implies emptiness without independence among candidate sets.',
    'result':'For each fixed c<=9.23414 strong4-core empty whp; for each fixed c<=6.84256 strong3-core empty whp, including endpoints.',
    'scope':'Lower-side target3 move only; no positive finite transfer, exact finite onset, simultaneous/varying-c assertion or priority claim.'}
(HERE/'T186_LOWER_RECEIPT.json').write_bytes((json.dumps(out,indent=2)+'\n').encode('utf-8'))
print(json.dumps({'at':out['at'],'status':out['status'],'covers':[(r['k'],r['boxes']) for r in covers]}))
