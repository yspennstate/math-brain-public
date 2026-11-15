"""Actual generator-row fault check supplement; no full replay is repeated."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime
import json
root=Path(__file__).resolve().parents[1]
r=json.loads((root/'checks/t170_d14_rolling_own.json').read_text(encoding='utf-8'))
w=r['actual_base_fault_witness'];a=w['a'];b=w['b'];S=r['scale'];A=r['alpha_units'];C=256
def sigma(n):return 26*n-2*sum(j.bit_count() for j in range(n))
ra=sigma(a) if a<C else 0
rb=sigma(b)+max(a-b,0) if b<C else 0
rc=sigma(1)+max(b-1,0)
assert (ra,rb,rc)==(w['ra'],w['rb'],w['rc'])
p=Path('~/crash_recovery_20261014/workers_1015/term_362ebe34/T170_THREE_COMPRESSED_d14_C256_BASE.json')
assert sha256(p.read_bytes()).hexdigest()=='884c5412e7d1418a02a952674cc12a415aa3e777e4fcdaf53cd1144e593c3079'
H=json.loads(p.read_text(encoding='utf-8'))['base_bias']
def h(a,b):return H[(a-1)*C+b-1]
assert w['h']==h(a,b) and w['front_h']==h(b,1)
if ra:assert w['a_child']==h(a+1,b)
if rb:assert w['b_child']==h(a,b+1)
def residual(coefficient):
    value=S-coefficient+(h(b,1)-h(a,b))+rc*(w['h_c2']-h(a,b))
    if ra:value+=ra*(h(a+1,b)-h(a,b))
    if rb:value+=rb*(h(a,b+1)-h(a,b))
    return value
assert residual(A)==-21817 and residual(r['max_required_units']-1)==1
receipt={'at':datetime.now().astimezone().isoformat(),'status':'actual reconstructed generator-row fault control PASS','state':[a,b,1],'rates':[ra,rb,rc,1],'valid_coefficient':A,'valid_residual':residual(A),'bad_coefficient':r['max_required_units']-1,'bad_residual':1,'note':'Fresh rates and frozen BASE children; c2 child is the recorded value from our full independent replay. Original one-line fault assertion was only a simplified subtraction; this recomputes the generator expression. Full all-state inequality proof unchanged.'}
(root/'checks/t170_d14_actual_fault_own.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
audit=root/'audits/term_362ebe34_T170-LEAD-ROLLING-D14-001_v1.md'
text=audit.read_text(encoding='utf-8')
marker='## Exact claim and accepted dependency'
insert='''## Fault-control supplement

The original full replay checked every actual inequality. Its standalone
bad-coefficient assertion simplified to requirement-minus-requirement;
checks/t170_d14_actual_fault_own.py now separately re-evaluates the actual
worst generator row using freshly derived rates, frozen BASE children,
and the c2 value recorded by our full independent replay. Its valid
residual is-21817 and the deliberately lowered coefficient gives+1.
See checks/t170_d14_actual_fault_own.json. This strengthens the diagnostic;
it changes no all-state inequality, proof hash, bound or PASS verdict.

'''
assert '## Fault-control supplement' not in text
audit.write_text(text.replace(marker,insert+marker),encoding='utf-8')
print(json.dumps(receipt))
