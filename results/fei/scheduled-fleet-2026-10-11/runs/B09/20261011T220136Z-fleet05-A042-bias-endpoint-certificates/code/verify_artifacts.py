from pathlib import Path
import json,hashlib
root=Path(__file__).resolve().parents[1]
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
p=json.loads((root/'PROGRESS.json').read_text())
claims=json.loads((root/'CLAIMS.json').read_text())
expected={field.split(' (',1)[0] for field in protocol['required_per_run']['progress_fields']}
assert set(p)==expected
for c in claims:
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
    payload={'statement':c['exact_statement'],'hypotheses':c['hypotheses']}
    assert hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()==c['statement_sha256']
assert (root/'PACKET_DELTA.json').read_bytes()==(root/'PROGRESS.json').read_bytes()
checks=json.loads((root/'out/CHECK_OUTPUT.json').read_text())
assert checks['assertions_passed']==24095
receipt=root/'out/PERSISTENCE_RECEIPTS.json'
manifest=json.loads(receipt.read_text())
for item in manifest['local_files']:
    assert hashlib.sha256((root/item['path']).read_bytes()).hexdigest()==item['sha256']
validation={'protocol_fields':'PASS; parenthetical prose on packet_ids treated as annotation','statement_hash':'PASS','packet_delta_equality':'PASS','saved_assertions':24095,'original_file_hashes_verified':len(manifest['local_files']),'report_math_review':'AUTHOR_ONLY; INDEPENDENT_REVIEW_PENDING','earlier_shell_one_liner':'failed to parse due shell quoting; replaced by this script'}
(root/'out/ARTIFACT_VALIDATION.json').write_text(json.dumps(validation,indent=2)+'\n',encoding='utf-8')
manifest['local_files']=[]
for path in sorted(root.rglob('*')):
    if path.is_file() and path!=receipt:
        raw=path.read_bytes(); assert len(raw)<20_000_000
        manifest['local_files'].append({'path':str(path.relative_to(root)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
receipt.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps(validation,indent=2))
