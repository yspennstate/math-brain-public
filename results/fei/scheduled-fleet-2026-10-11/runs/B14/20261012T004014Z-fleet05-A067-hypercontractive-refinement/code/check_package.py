"""Correct coordinate attribution from the saved witness, then verify artifacts."""
from pathlib import Path
import hashlib, json
R=Path(__file__).resolve().parent.parent
A=R.parent.parent
w=json.loads((R/'out/TRIBES_NODE_WITNESS.json').read_text(encoding='utf-8'))
for row in w['rows']:
    assert row['worst_node']['query_original_coordinate']>=2*row['blocks']
# Both recorded worst nodes query the last remaining padding coordinate.
# Fix a draft attribution; no proof or numerical certificate changes.
replacements={
 'Their core nodes can exceed rate 5, so the point-defect rate cannot be transferred to arbitrary core restrictions.':
 'Their last-padding nodes can exceed rate 5, so even padding strips cannot inherit the point-defect rate for arbitrary seeds.',
 'certifies a core node rate >8':'certifies a last-padding node rate >8',
 'Finite edited-tribes core nodes exceed 5 (one exceeds 8), so universal core-access payment remains unpaid.':
 'Finite edited-tribes last-padding nodes exceed 5 (one exceeds 8); universal core-access payment remains a separate unpaid gap.',
 'Width-two edited-tribes finite tests expose core node rates >5 and >8; a padding-only rate must not be extrapolated to core queries.':
 'Width-two edited-tribes finite tests expose last-padding node rates >5 and >8; even padding queries cannot inherit a universal point-defect rate.',
}
for p in [R/'code/finalize.py',R/'REPORT.md',A/'WORKLOG.md',A/'LEARNED.md']:
    s=p.read_text(encoding='utf-8')
    for old,new in replacements.items(): s=s.replace(old,new)
    p.write_text(s,encoding='utf-8')
receipt_path=R/'out/SAVE_RECEIPT.json'
receipt=json.loads(receipt_path.read_text(encoding='utf-8'))
files=[p for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p!=receipt_path]
files += [A/n for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]
receipt['files']=[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in sorted(files)]
receipt['coordinate_attribution_checked']='Both finite tribes worst witnesses query the last padding coordinate, not a core coordinate; draft attribution corrected.'
receipt_path.write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=json.loads(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
progress=json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'))
assert set(progress)=={s.split(' (',1)[0] for s in protocol['required_per_run']['progress_fields']}
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
claims=json.loads((R/'CLAIMS.json').read_text(encoding='utf-8'))
originals=[]
for relative in ['A066/runs/20261011T233317Z-fleet05-A066-semigroup-dissipation/CLAIMS.json','A070/runs/20261011T230551Z-fleet05-A070-analytic-route-referee/CLAIMS.json']:
    originals+=json.loads((A.parent/relative).read_text(encoding='utf-8-sig'))
for c in claims:
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
    if c['claim_id'].startswith('A067-'):
        encoded=json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()
        assert hashlib.sha256(encoded).hexdigest()==c['statement_sha256'],c['claim_id']
    else:
        original=next(o for o in originals if o['claim_id']==c['claim_id'] and o['version']==c['version'])
        for field in ['exact_statement','hypotheses','statement_sha256','contributors','proof_source','proof_dependencies']:
            assert c[field]==original[field],(c['claim_id'],field)
report=(R/'REPORT.md').read_text(encoding='utf-8')
assert all('## '+h in report for h in protocol['required_per_run']['report_fields'])
assert report.rsplit('## ',1)[1].startswith('Universal bridge\n')
for f in receipt['files']:
    p=Path(f['path'])
    assert hashlib.sha256(p.read_bytes()).hexdigest()==f['sha256']
    assert p.stat().st_size==f['bytes']<20_000_000
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
print(json.dumps({'complete':True,'all_receipt_hashes_verified':len(receipt['files']),'schema_and_new_statement_hash_verified':True,'reviewed_source_versions_preserved':True,'packet_ids':progress['packet_ids'],'tribes_witness_attribution':'last-padding coordinate','full_fei_status':'OPEN'}))
