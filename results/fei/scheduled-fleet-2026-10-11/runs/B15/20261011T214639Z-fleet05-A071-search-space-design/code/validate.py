import hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
protocol=json.loads(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text())
req=protocol['required_per_run']
# The protocol list embeds a parenthetical description in its last label;
# compatibility instructions elsewhere explicitly specify the actual key packet_ids.
fields=[f.split(' (')[0] for f in req['progress_fields']]
p=json.loads((root/'PROGRESS.json').read_text());claims=json.loads((root/'CLAIMS.json').read_text())
assert set(p)==set(fields)
assert p['packet_ids']==['A071']
assert (root/'PROGRESS.json').read_bytes()==(root/'PACKET_DELTA.json').read_bytes()
assert all(set(c)==set(req['claim_fields']) for c in claims)
assert all(f in (root/'REPORT.md').read_text() for f in req['report_fields'])
for c in claims:
    payload=json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()
    assert hashlib.sha256(payload).hexdigest()==c['statement_sha256']
old=json.loads((root/'out/manifest.json').read_text())
assert all(hashlib.sha256((root/x['path']).read_bytes()).hexdigest()==x['sha256'] for x in old)
result={'protocol_fields':'PASS','packet_ids_label_normalization':'Parenthetical explanation removed from protocol display label; canonical key packet_ids retained','compatibility_copy':'BYTE_IDENTICAL','statement_sha256':'PASS','previous_manifest_hashes':'PASS','full_fei':'OPEN','independent_review':'PENDING'}
(root/'out/validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
manifest=[]
for f in sorted(root.rglob('*')):
    if f.is_file() and f.name!='manifest.json' and '__pycache__' not in str(f):
        b=f.read_bytes();assert len(b)<20_000_000
        manifest.append({'path':str(f.relative_to(root)),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
(root/'out/manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
