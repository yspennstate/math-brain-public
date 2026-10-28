"""Post-save audit of certificates, handwritten bounds, and persistence receipts."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib

ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
receipt=read(ROOT/'out/PERSISTENCE.json')
for record in receipt['files']:
    path=ROOT/record['path']
    assert sha(path)==record['sha256'] and path.stat().st_size==record['bytes']
a=read(ROOT/'out/DIAGONAL_ANALYTIC.json')
def inside(cert,lo,hi):assert Q(lo)<Q(cert['lower'])<=Q(cert['upper'])<Q(hi)
inside(a['A'],'4.2893126964','4.2893126965')
inside(a['dimensions']['4']['K'],'-2.5960773854','-2.5960773853')
inside(a['dimensions']['5']['K'],'0.8466176555','0.8466176556')
inside(a['dimensions']['4']['sibling_after_subsidy_over_p'],'1.6932353110','1.6932353111')
inside(a['dimensions']['4']['S_over_p'],'0.5333441997','0.5333441999')
inside(a['dimensions']['5']['S_over_p'],'1.9025286543','1.9025286545')
inside(a['dimensions']['4']['D_over_p'],'3.1294215850','3.1294215853')
inside(a['dimensions']['5']['D_over_p'],'1.0559109987','1.0559109990')
inside(a['dimensions']['4']['root_subsidy_over_p2'],'13.8457460552','13.8457460553')
for n in [8,12,16,24,32,48]:
    row=read(ROOT/'out'/f'DIAGONAL_n{n}.json')['states'][-1]
    assert row['zero_flow_if_new_descendant_labels_reassigned']
    assert Q(row['rebooking_slack']['lower'])>0
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert 'not a lower bound over all admissible payment policies' in (ROOT/'PROOF.md').read_text(encoding='utf-8')
# Keep the qualification in the durable entry itself, not in an adjacent correction.
learned=ROOT.parent.parent/'LEARNED.md'
old='This is not a proof that all ancestor net debits are nonnegative for all n. A089 signed-capacity minimum'
new='If new descendant bookings may be reassigned with their conditional means retained, both positive full children allow zero transfer through the capacity kernel; Gamma4 is not a lower bound over all payment policies. This is not a proof that all ancestor net debits are nonnegative for all n. A089 signed-capacity minimum'
text=learned.read_text(encoding='utf-8')
assert text.count(old)==1
learned.write_text(text.replace(old,new),encoding='utf-8')
audit={'saved_file_hashes':'PASS','nine_handwritten_rational_bounds':'PASS','zero_transfer_after_rebooking':'ALL_SIX_DECLARED_ENDPOINTS_PASS','scope':'fixed routing obstruction only; no full-history all-n legality or universal FEI asserted','independent_review':'new endpoint theorem pending; A089 generic theorem and18 signs only independently reviewed','own_jobs_remaining':'NONE'}
(ROOT/'out/AUDIT.json').write_text(json.dumps(audit,indent=2)+'\n',encoding='utf-8')
receipt['files']=[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(ROOT.rglob('*')) if p.is_file() and p.name!='PERSISTENCE.json']
receipt['rolling_files']=[{'path':str(p),'sha256':sha(p)} for p in [ROOT.parent.parent/x for x in ['STATUS.md','WORKLOG.md','LEARNED.md']]]
receipt['post_save_audit']='PASS; see out/AUDIT.json'
(ROOT/'out/PERSISTENCE.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'audit':'PASS','files':len(receipt['files']),'rolling_files':len(receipt['rolling_files']),'full_fei':'OPEN','own_jobs_remaining':'NONE'}))
