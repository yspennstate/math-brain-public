"""Check report statements and independent shortcut-obstruction witnesses."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[k]='1'
import json,re,time,resource
from pathlib import Path
from fractions import Fraction as Q
from q1_core import exact,lump
from q2_search import log

start=time.monotonic();report=Path('REPORT.md').read_text()
assert report.splitlines()[0]=='Result: partial'
assert report.count('$$')%2==0
for name in set(re.findall(r'\b[A-Za-z0-9_]+\.(?:py|json|txt|md)\b',report)):
    assert Path(name).exists(),name
assert 'Gap:' in report and '$3\\le K(7)\\le4$' in report
with open('k7_final_results.json') as f:z=json.load(f)
assert z['independent_witness_audits']==36
assert sum(v['evaluations'] for v in z['adversarial_runs'])==389193
for v in z['adversarial_runs']+[z['prequotient_metadata']]:
    assert v['seconds']<300 and v['peak_rss']<10**9
for key,v in z['best'].items():
    assert v['value'] in report,(key,'exact value missing')
    assert Q(v['ratio'])<=3
for v in z['minimum_obstructions']:
    assert min(map(Q,v['orientation_values']))>1
    assert Q(v['ratio'])<3
    assert v['seconds']<300 and v['peak_rss']<10**9
assert Q(z['minimum_obstructions'][1]['ratio'])>=2
with open('k7_leads_results.json') as f:lead=json.load(f)
for v in lead['diagonal_family']:
    t=Q(v['t']);w=[[Q(a) for a in row] for row in v['w']];bs=v['partition']
    x=exact(w);y=exact(lump(w,bs));aa=y['F'][0][0]-x['F'][0][0]
    W=t**6+2*t*t+2*t+2;S=t*t+2*t+2
    N=t**7+t**6+2*t**5+2*t**4+2*t**3+t*t+4*t+2
    assert aa==(W-S)**2/(t*t*W)==t*t*(t**4+1)**2/W
    assert x['t']==N/W==Q(v['T'])
    assert aa/x['t']==Q(v['a_over_T'])
v=lead['cauchy_schwarz_bound_exceeds_3T']
T=Q(v['T']);F=Q(v['Fij']);a=Q(v['ai']);b=Q(v['aj'])
assert 3*T-F>0 and a*b>(3*T-F)**2 and Q(v['cross'])>0
assert Q(v['Fhat'])<3*T
v=lead['intermediate_row_sum_exceeds_proposed_budget']
w=[[Q(a) for a in row] for row in v['w']];x=exact(w)
y=exact(lump(w,[[0],[1],[2,3],[4],[5]]))
assert max(y['F'][0])+max(y['F'][1])==Q(10002120000039,250055500001)==Q(v['row_sum_after_first'])
assert max(x['F'][0])+max(x['F'][1])+x['t']==Q(229169325000879,6251387500025)==Q(v['budget'])
assert Q(v['row_sum_after_first'])>Q(v['budget'])
for name,marker in (
    ('k7_finalize_output.txt','INDEPENDENT EXACT AUDIT PASSED'),
    ('k7_minimum_output.txt','Orthogonal minimum refinement audit passed'),
    ('k7_leads_output.txt','ALL LEAD CHECKS PASSED')):
    assert marker in Path(name).read_text()
print('REPORT CHECK PASSED')
print('Exact singleton witnesses audited:',z['independent_witness_audits'])
print('Diagonal family checks:',len(lead['diagonal_family']))
print('Main exact objectives:',sum(v['evaluations'] for v in z['adversarial_runs']))
print('Fork prequotient partitions:',z['prequotient_metadata']['partitions'])
print('K(7) unresolved: 3 <= K(7) <= 4')
log(f'REPORT CHECK PASSED: exact fractions, all referenced artifacts, 36 independent winner audits, {len(lead["diagonal_family"])} diagonal family checks, shortcut obstructions, resource metadata, and explicit unresolved K(7) statement. {time.monotonic()-start:.3f}s; peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss} bytes.')
