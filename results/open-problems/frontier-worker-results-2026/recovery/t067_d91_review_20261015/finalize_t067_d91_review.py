"""Pin the independently checked complete composition without admitting a frontier."""
from pathlib import Path
from datetime import datetime
import hashlib,json
HERE=Path(__file__).resolve().parent;W=Path('~/brain_workers/w682')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
original=json.loads((HERE/'T067_LEAD_REVIEW_RECEIPT.json').read_text(encoding='utf-8'))
scopes={'T067-SOFTMAX-DERIVATIVES-001':'Global F derivatives',
        'T067-CUBIC-FUSION-001':'Full signed CF and arbitrary-fixed-point sign corollary',
        'T067-TERNARY-MOMENTS-001':'F2 and C; right support domain eta_ref=2887/5000',
        'T067-UNIFORM-LOCAL-001':'Exact prefix recurrences and criterion only; new rectangle rebuilt',
        'T067-FIXEDPOINT-001':'Canonical limiting argument, also rederived in main review',
        'T067-GAUSSIAN-QUAD-001':'Conditional-bin mean, Hessian error and whole-tail method',
        'T067-SHARP-LINDEBERG-001':'Orbit/tensor identities only; no old small-L constants'}
old=[]
for entry in original['dependencies']:
    if entry['claim'] not in scopes:continue
    p=W/'proofs'/(entry['claim']+'_v1.md');assert sha(p)==entry['proof_sha256']
    old.append(dict(entry,scope=scopes[entry['claim']]))
assert len(old)==7
new={
'T067-COMPENSATED-D91-001_v1.md':'3f41f2986e611f38d248077ab2da3352d70634fec300ae91cb40e83655ceb9bd',
'T067-COMPENSATED-REPLACEMENT-EXT-001_v1.md':'7f3239238dd9f7df70c55bde9697d77f62a6ab26e39820e6c22d3abbcb914ddf',
'T067-COMPENSATED-CUBIC-001_v1.md':'fde2080aa7178b05e755b90d758738608cddf5532dac51edb768bb5dfb37bbfe',
'T067-FOURTH-DERIVATIVES-001_v1.md':'c0f285f87e817086133cd22e9b1f6e3c690308124c7cd6aaa0f1f8867c2415da',
'T067-UNIFORM-LOCAL-EXT-001_v1.md':'1163cfb98bd9adb486df2c79dce11a4844a000d86ecee897749c73874fe78c94',
'T067-GAUSSIAN-FOURTH-GATE-001_v1.md':'b1e094fac2ee638d88414611f9c3abdadd99a4d673799f71ecda263072d30637'}
for name,digest in new.items():assert sha(W/'proofs'/name)==digest
receipts=['T067_LOCAL42_LEAD_RECEIPT.json','T067_LOCAL42_POLYNOMIAL_BINDING.json',
          'T067_COMPENSATED_CUBIC_LEAD_RECEIPT.json','T067_FOURTH_DERIVATIVES_LEAD_RECEIPT.json',
          'T067_GAUSSIAN_FOURTH_OWN_SUMMARY.json','T067_D91_OWN_GATE_RECEIPT.json']
for name in receipts:assert json.loads((HERE/name).read_text(encoding='utf-8'))['status'].startswith('PASS')
mapping=json.loads((HERE/'T067_OWN_ENDPOINT_MAP.json').read_text(encoding='utf-8'))
for name,digest in mapping['source_files'].items():assert sha(HERE/'t067_own_endpoints'/name)==digest
fourth=json.loads((HERE/'T067_FOURTH_DERIVATIVES_LEAD_RECEIPT.json').read_text(encoding='utf-8'))
for row in fourth['files']:assert sha(HERE/'t067_fourth_own'/row['file'])==row['sha256']
for name in ['audit_t067_local42.py','audit_t067_compensated_cubic.py','audit_t067_fourth_derivatives.py']:
    receipt=next(json.loads((HERE/r).read_text(encoding='utf-8')) for r in receipts
                 if json.loads((HERE/r).read_text(encoding='utf-8')).get('script_sha256')==sha(HERE/name))
    assert receipt['status'].startswith('PASS')
q=json.loads((HERE/'T067_GAUSSIAN_FOURTH_OWN_SUMMARY.json').read_text(encoding='utf-8'))
assert q['completed']==86 and q['source_sha256']==sha(HERE/'audit_t067_gaussian_fourth.py')
gate=json.loads((HERE/'T067_D91_OWN_GATE_RECEIPT.json').read_text(encoding='utf-8'))
assert gate['script_sha256']==sha(HERE/'audit_t067_d91_gate.py')
assert gate['own_Q_summary_sha256']==sha(HERE/'T067_GAUSSIAN_FOURTH_OWN_SUMMARY.json')
files=receipts+['T067_D91_LEAD_ANALYTIC_AUDIT.md','T067_OWN_ENDPOINT_MAP.json',
               'audit_t067_local42.py','audit_t067_compensated_cubic.py',
               'audit_t067_fourth_derivatives.py','audit_t067_gaussian_fourth.py',
               'audit_t067_d91_gate.py','finalize_t067_d91_review.py','run_polite.py']
out={'at':datetime.now().astimezone().isoformat(),'reviewer':'codex-term-362ebe34',
     'status':'PASS lead full analytic and independent finite review',
     'subject':'T067-COMPENSATED-D91-001 v1','proof_sha256':new['T067-COMPENSATED-D91-001_v1.md'],
     'admission':'PENDING required exact-content distinct-account reviews; checked cutoff256 unchanged',
     'new_subjects':new,'older_exact_scoped_dependencies':old,
     'files':{name:sha(HERE/name) for name in files},
     'minimum_continuous_margin':gate['minimum_margin'],
     'scope':'q3 uniform-root regular d-ary trees, integer d>=91, positive lambda<=1/sqrt(d), including equality. No full T067, q4, random offspring, or priority claim.',
     'excluded':'RESCALE v1 unrestricted F1 corollary; no author saved PASS field used as independent proof'}
(HERE/'T067_D91_LEAD_REVIEW_RECEIPT.json').write_bytes((json.dumps(out,indent=2)+'\n').encode('utf-8'))
print(json.dumps({'status':out['status'],'subject':out['subject'],'admission':out['admission']}))
