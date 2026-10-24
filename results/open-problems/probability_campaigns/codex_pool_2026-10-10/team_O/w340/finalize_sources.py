"""Refresh two source-scope receipts and atomically replace only this worker's own draft."""
import difflib
import json
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
report_path=ROOT/'CACHED_SOURCE_REPORT.json'
report=json.loads(report_path.read_text(encoding='utf-8'))
for pid,pattern in [('C0123',r'\bbridges?\b|\bislands?\b'),('P0012',r'symmetric injective')]:
    text=Path(report[pid]['cached_text_path']).read_text(encoding='utf-8-sig',errors='replace')
    matches=list(re.finditer(pattern,text,re.I))
    selected=matches[-2:] if pid=='C0123' else matches[:1]
    contexts=[{'char_offset':x.start(),'line':text.count('\n',0,x.start())+1,'context':text[max(0,x.start()-350):x.end()+450]} for x in selected]
    if pid=='C0123': report[pid]['matches']=contexts
    else:
        report[pid]['norm_definition_matches']=contexts
        report[pid]['norm_convention']='Symmetric repeated-vector homogeneous polynomial norm; covered by the sign-support paragraph of p0012_proof.md.'
report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')

local=ROOT/'bundle_002.json'
bundle=json.loads(local.read_text(encoding='utf-8'))
for entry in bundle['entries']:
    if entry['key'].startswith('diagonal-'):
        entry['proof_text']=(ROOT/'p0012_proof.md').read_text(encoding='utf-8')
        entry['source']['revision']='2026-10-10-source-convention-confirmed-draft-awaiting-w346'
    if entry['key']=='paired-block-nk-exact-bridge-deficit-threshold':
        entry['statement']=entry['statement'].replace('Two peaks differing','Two distinct peaks differing')
        entry['source']['revision']='2026-10-10-distinct-peak-scope-draft-awaiting-w346'
        statement=entry['statement'].split('independent audit pending. ',1)[1]
        for relation in bundle['relations']:
            if relation['from_key']==entry['key']:
                relation['rationale']=re.sub(r'New end: "[^\"]+"',lambda _: 'New end: "'+statement[:230]+'"',relation['rationale'],count=1)
    model=('Consider one FCFS server with Poisson arrival rate lambda>0 and independent exponential service rate mu>lambda. After becoming empty it remains on for deterministic grace g in [0,infinity], then switches off. A cold arrival triggers deterministic setup tau>=0, which is never cancelled; arrivals during setup wait. ')
    if entry['key']=='mm1-deterministic-delayedoff-stationary-waiting-power-curve':
        entry['statement']=entry['statement'].replace('For the specified stable one-server DelayedOff queue, put',model+'Put')
    if entry['key']=='mm1-delayedoff-regenerative-state-fractions':
        entry['statement']=entry['statement'].replace('In the stable one-server deterministic DelayedOff model, set',model+'Set')
    if entry['key']=='diagonal-gaussian-tensor-type-two-all-p':
        entry['statement']=entry['statement'].replace('For diagonal real order-r multilinear tensors','For integer r>=2 and p in [2,infinity], diagonal real order-r multilinear tensors')

entry_by_key={e['key']:e for e in bundle['entries']}
def fragment(entry,length=230):
    text=entry['statement'].split('independent audit pending. ',1)[1]
    if entry['key']=='mm1-deterministic-delayedoff-stationary-waiting-power-curve':
        text=text[text.index('The stationary mean'):]
    if entry['key']=='mm1-delayedoff-regenerative-state-fractions':
        text=text[text.index('Busy, on-idle'):]
    return text[:length]
for relation in bundle['relations']:
    text=fragment(entry_by_key[relation['from_key']])
    relation['rationale']=re.sub(r'(New end|From end): "[^\"]+"',lambda match:match[1]+': "'+text+'"',relation['rationale'],count=1)
    if 'to_key' in relation:
        text_to=fragment(entry_by_key[relation['to_key']],200)
        relation['rationale']=re.sub(r'to end: "[^\"]+"',lambda _: 'to end: "'+text_to+'"',relation['rationale'],count=1)
rows_path=ROOT/'results.jsonl'
rows=[json.loads(x) for x in rows_path.read_text(encoding='utf-8').splitlines() if x.strip()]
for row in rows:
    if row.get('entry_key')=='paired-block-nk-exact-bridge-deficit-threshold':
        row['statement']=row['statement'].replace('Two peaks differing','Two distinct peaks differing')
    if row.get('entry_key') in entry_by_key:
        row['statement']=entry_by_key[row['entry_key']]['statement'].split('independent audit pending. ',1)[1]
rows_path.write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in rows),encoding='utf-8')
local.write_text(json.dumps(bundle,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
inbox=Path('~/math-brain-inbox/w340')
part=inbox/'bundle_002.part'
assert not part.exists()
part.write_bytes(local.read_bytes())
part.replace(inbox/'bundle_002.json')
live='~/math-brain-inbox/w340/bundle_002.json'
patch=''.join(difflib.unified_diff([],local.read_text(encoding='utf-8').splitlines(keepends=True),fromfile='a/'+live,tofile='b/'+live))
(ROOT/'patches/02_remaining_research_bundle.diff').write_text(patch,encoding='utf-8')
print(json.dumps({'refreshed_source_scopes':['C0123','P0012'],'draft':'bundle_002.json','audit_status':'PENDING_W346'},ensure_ascii=False))
