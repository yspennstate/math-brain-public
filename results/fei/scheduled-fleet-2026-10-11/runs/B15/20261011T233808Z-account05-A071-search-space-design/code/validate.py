import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
protocol=json.loads(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text())['required_per_run']
p=json.loads((ROOT/'PROGRESS.json').read_text());c=json.loads((ROOT/'CLAIMS.json').read_text());report=(ROOT/'REPORT.md').read_text()
assert set(p)=={x.split(' (')[0] for x in protocol['progress_fields']}
assert p['packet_ids']==['A071']
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert all(x in report for x in protocol['report_fields']) and report.rstrip().split('\n\n')[-2]=='## Universal bridge'
for claim in c:
    assert set(claim)==set(protocol['claim_fields'])
    b=json.dumps({'statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':')).encode()
    assert hashlib.sha256(b).hexdigest()==claim['statement_sha256']
full=json.loads((ROOT/'out/full_census.json').read_text());last=json.loads((ROOT/'out/final_certificate.json').read_text())
assert full['counts']['raw']==2**31 and full['counts']['minority_le_16']==2**30
assert full['counts']['strict_upper_passes']+full['counts']['candidates']==full['counts']['entropy_evaluated']
assert last['full_E5_certificate_complete'] and last['extremizer_truth_tables_including_output_complement']==640
v={'protocol_fields':'PASS','packet_delta':'BYTE_IDENTICAL','statement_hash':'PASS','complete_full_domain':'PASS','universal_bridge_last_paragraph':'PASS','independent_review':'PENDING'}
(ROOT/'out/validation.json').write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
manifest=[]
for path in sorted(ROOT.rglob('*')):
    if path.is_file() and path.name!='manifest.json' and '__pycache__' not in str(path):
        b=path.read_bytes();assert len(b)<20_000_000
        manifest.append({'path':str(path.relative_to(ROOT)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(ROOT/'out/manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
assert all(hashlib.sha256((ROOT/m['path']).read_bytes()).hexdigest()==m['sha256'] for m in manifest)
print(json.dumps({**v,'files_hashed_and_read_back':len(manifest)},indent=2))
