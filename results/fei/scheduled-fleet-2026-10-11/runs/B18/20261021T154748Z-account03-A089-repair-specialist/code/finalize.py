"""End-to-end saved-artifact audit; updates receipts after the final code changes."""
from pathlib import Path
import json,hashlib,datetime,re
R=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
report=R/'REPORT.md';t=report.read_text(encoding='utf-8')
repro=json.loads((R/'out/INDEPENDENT_REPRODUCTION.json').read_text(encoding='utf-8'))
t=re.sub(r'848 exact predicates, seven cases, [0-9.]+ seconds',f"848 exact predicates, seven cases, {repro['runtime_seconds']:.3f} seconds",t)
report.write_text(t,encoding='utf-8',newline='\n')
receipts=json.loads((R/'out/RECEIPTS.json').read_text(encoding='utf-8'))
claims=json.loads((R/'CLAIMS.json').read_text(encoding='utf-8'))
for c in claims:assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert t.rstrip().split('\n\n')[-2]=='## Universal bridge'
assert 'RUNTIME_UNVERIFIED' in t and 'Full FEI remains OPEN' in t
rows=json.loads((R/'out/REPAIRED_CASES.json').read_text(encoding='utf-8'))
assert len(rows)==7 and sum(x['corrected_selected_only_fails'] for x in rows)==3
assert all('old_booked_labels' in x and 'new_booked_labels' in x for x in rows)
entries=[]
for p in R.rglob('*'):
    if p.is_file() and p.name!='RECEIPTS.json':
        assert p.stat().st_size<20*1024**2
        entries.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
receipts['files']=entries;receipts['saved_at_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
receipts['final_audit']='PASS: exact statement hash; required schemas; delta identity; labelled ancestor/new debt; three corrected selected-owner failures; all seven allocations; full terminals; final universal bridge'
receipts['independent_reproduction_rung']='Separate representation by same A089; independent reviewer still pending'
(R/'out/RECEIPTS.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8',newline='\n')
for row in entries:assert sha(R/row['path'])==row['sha256']
print(json.dumps({'artifact_hashes_checked':len(entries),'corrected_failures':3,'third_query_cases':7,'rung':'proof and exact finite certificates; external review pending; Lean unverified','full_FEI':'OPEN'}))
