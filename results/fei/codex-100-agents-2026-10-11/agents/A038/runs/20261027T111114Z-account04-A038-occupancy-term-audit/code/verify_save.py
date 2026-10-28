import json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def read(p):return p.read_text(encoding='utf-8')
def put(p,s):p.write_text(s,encoding='utf-8',newline='')
def dump(p,v):put(p,json.dumps(v,ensure_ascii=False,indent=2)+'\n')
# Correct provenance wording after the explicit archived-source decoding repair.
for p in [R/'REPORT.md',R/'code/finalize.py']:
 s=read(p).replace('were UTF8 scanned','were scanned with explicitly recorded source encodings')
 put(p,s)
p=json.loads(read(R/'PROGRESS.json'))
admission='Fresh memok exited1: physical3.1GB<4GB and commit3.3GB<8GB; no Lean/compiler launched.'
if admission not in p['blockers']:p['blockers'].append(admission)
for extra in ['out/BRAIN_AND_ADMISSION.json','out/SOURCE_SCAN_FAILURE.json','out/SCHEMA_SAVE_FAILURE.json','code/verify_save.py']:
 if extra not in p['source_artifacts']:p['source_artifacts'].append(extra)
dump(R/'PROGRESS.json',p);dump(R/'PACKET_DELTA.json',p)
protocol=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
expected={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(p)==expected
claims=json.loads(read(R/'CLAIMS.json'))
assert len(claims)==1 and set(claims[0])==set(protocol['required_per_run']['claim_fields'])
assert hashlib.sha256(claims[0]['exact_statement'].encode('utf-8')).hexdigest()==claims[0]['statement_sha256']
assert read(R/'PROGRESS.json')==read(R/'PACKET_DELTA.json')
report=read(R/'REPORT.md')
for field in protocol['required_per_run']['report_fields']:assert '\n## '+field+'\n' in report
assert report.strip().split('\n\n')[-1].startswith('Universal bridge:')
assert len(read(A/'STATUS.md').splitlines())==2
check=json.loads(read(R/'out/CHECK.json'))
assert check['status']=='PASS' and check['tables']==278 and check['assertions']==9270
receipt=json.loads(read(R/'out/RECEIPTS.json'))
receipt['schemas']='PASS; sole protocol display annotation packet_ids (...) normalized to packet_ids, as existing artifacts require'
receipt['artifact_hashes']={str(f.relative_to(R)):hashlib.sha256(f.read_bytes()).hexdigest() for f in R.rglob('*') if f.is_file() and f.name!='RECEIPTS.json'}
receipt['independent_persistence_readback']='PASS exact claim/progress/report schemas, statement hash, progress/delta equality, rolling two-line status, report final paragraph, actual finite certificate'
assert all(f.stat().st_size<20_000_000 for f in R.rglob('*') if f.is_file())
dump(R/'out/RECEIPTS.json',receipt)
nonutf=[{'path':s['path'],'encoding':s['encoding']} for s in json.loads(read(R/'out/SOURCE_RECEIPTS.json')) if s['encoding']!='utf-8-sig']
print(json.dumps({'status':'PASS_READBACK','tables':278,'assertions':9270,'nonUTF8_sources':nonutf,'full_FEI':'OPEN','external_review':'PENDING'}))
