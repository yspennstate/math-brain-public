"""Read-only artifact checks and local packet metadata refresh."""
import hashlib
import json
from pathlib import Path

root=Path(__file__).resolve().parent
def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def save(path,obj):
    Path(path).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

source=read(root/'SOURCE_STATUS.json')
source['canonical_store_check']=read(root/'CANONICAL_STORE_CHECK.json')
source['current_openness']='UNKNOWN'
save(root/'SOURCE_STATUS.json',source)
report_path=root/'REPORT.md'
report=report_path.read_text(encoding='utf-8')
note='The separate active canonical database locator remains unresolved; only audit databases were found in the canonical code checkout, and those were not opened. Exact live population C0052 cards were checked read-only and remain unverified. No exhaustive solved/retired-work or openness certificate is claimed.\n\n'
if note not in report:
    report_path.write_text(report.replace('Risks:',note+'Risks:'),encoding='utf-8')
packet=read(root/'REVIEW_PACKET.json')
existing={Path(item['path']) for item in packet['artifacts']}
existing.add(root/'CANONICAL_STORE_CHECK.json')
packet['artifacts']=[{'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()} for path in sorted(existing,key=str)]
packet['canonical_store_limit']='Separate canonical database unresolved; exact live population target cards checked read-only; current openness UNKNOWN.'
save(root/'REVIEW_PACKET.json',packet)
bundle=read(root/'bundle_001.json')
submitted=read('~/math-brain-inbox/w469/bundle_001.json')
assert bundle==submitted
assert all(item['kind']=='concept' and item['proof_text'] is None and item['statement'].startswith('DRAFT;') for item in bundle['entries'])
claims=[json.loads(line) for line in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
assert len({row['claim_id'] for row in claims})==len(claims)
for row in claims:
    assert all(key in row for key in ['statement','assumptions','source','proof_or_counterexample','independent_reviewer','remaining_gap','status'])
assert read(root/'VERIFICATION.json')['passed'] and read(root/'TREE_VERIFICATION.json')['passed']
assert read(root/'PATCH_CHECK.json')['before_unsupported_equivalence_count']==1
assert read(root/'PATCH_CHECK.json')['after_unsupported_equivalence_count']==0
for item in packet['artifacts']:
    assert hashlib.sha256(Path(item['path']).read_bytes()).hexdigest()==item['sha256']
result={'packet_sha256':hashlib.sha256((root/'REVIEW_PACKET.json').read_bytes()).hexdigest(),
        'claim_rows':len(claims),'submitted_concept_entries':len(bundle['entries']),
        'relation_rows':len(bundle['relations']),'artifact_hashes_checked':len(packet['artifacts']),
        'source_correction_before':1,'source_correction_after':0,'checks':'PASS',
        'proof_or_model_attestation':False,'parent_problem_solved':False,'state_to_set':'NEEDS_REVIEW'}
save(root/'FINAL_CHECK.json',result)
print(json.dumps(result))
