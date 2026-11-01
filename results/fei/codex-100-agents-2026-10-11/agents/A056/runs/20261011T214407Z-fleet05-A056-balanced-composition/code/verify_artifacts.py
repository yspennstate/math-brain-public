from pathlib import Path
import json,hashlib
run=Path(__file__).resolve().parents[1]
proto=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
claims=json.loads((run/'CLAIMS.json').read_text(encoding='utf-8'))
progress=json.loads((run/'PROGRESS.json').read_text(encoding='utf-8'))
assert set(progress)=={x.split(' ')[0] for x in proto['required_per_run']['progress_fields']}
assert progress==json.loads((run/'PACKET_DELTA.json').read_text(encoding='utf-8'))
for c in claims:
    assert set(c)==set(proto['required_per_run']['claim_fields'])
    assert hashlib.sha256(c['exact_statement'].encode()).hexdigest()==c['statement_sha256']
checks=json.loads((run/'out/checks.json').read_text(encoding='utf-8'))
assert checks['restricted_majority_AND_witness']['influence']=='5/4'
assert checks['restricted_majority_AND_witness']['mean']=='-1/4'
receipts=json.loads((run/'out/receipts.json').read_text(encoding='utf-8'))
for item in receipts['files']:
    assert hashlib.sha256((run/item['path']).read_bytes()).hexdigest()==item['sha256']
t=(run/'REPORT.md').read_text(encoding='utf-8')
assert 'I(F)=9/8' not in t and 'inconsistent provisional' not in t
print('Schema, delta equality, witness, claim digests and persistence hashes PASS')
print(t[t.index('For comparison with Proposition'):t.index('### Physical restrictions')])
e=(run/'out/source_excerpts.txt').read_text(encoding='utf-8')
for name in ['OVERLAPPING_PRODUCT_NOTE.md','BLOCK_RESTRICTION_IDENTITY_2026-09-18.md','threshold_paper_29pp_earlier_version.txt','percolation_spectral_pivotal_entropy_31pp_other_version.txt']:
    pos=e.find(name)
    print('\nSOURCE EXCERPT',e[pos:pos+1000])
result={'protocol_schema_check':'PASS','packet_delta_equality':'PASS','witness_values':'PASS','claim_statement_digests':'PASS','persistence_hashes':'PASS','independent_review':'PENDING'}
(run/'out/artifact_validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
