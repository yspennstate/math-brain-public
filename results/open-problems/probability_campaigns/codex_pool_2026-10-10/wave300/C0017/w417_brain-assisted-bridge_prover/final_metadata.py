"""Update local source receipts and validate complete delivery artifacts."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
path=ROOT/'SOURCE_STATUS.json'
source=json.loads(path.read_text(encoding='utf-8'))
source['parameter_source']['locator']='Conjecture1 Eq.(3.3), PDF page index9 (10th PDF page)'
source['recent_claim']['primary_map_url']='https://raw.githubusercontent.com/openai/math/main/CONTENTS.md'
source['recent_claim']['primary_manuscript_url']='https://raw.githubusercontent.com/openai/math/main/preprints/Conformal-Limits-of-Critical-Square-Lattice-Random-Cluster-Interfaces-October-5-2026/paper.pdf'
source['recent_claim']['notes']='The exact manuscript and q=1 claim were verified in the primary manuscript map, lines4545-4547. The index PDF link failed, and the raw PDF browser fetch rejected application/octet-stream. The mathematical proof has not been validated; current openness remains UNKNOWN.'
source['prior_work_search']['owner_directory_search']='Five matching local note snippets concerned tree Cartesian-product percolation or squared kernels, not square-lattice conformal invariance; no exact C0017 resolution was located. This bounded search is not an exhaustive solved-work certification.'
path.write_text(json.dumps(source,indent=2)+'\n',encoding='utf-8')
required=['STATUS.md','SOURCE_STATUS.json','ATTEMPT.md','CLAIMS.jsonl','REVIEW_PACKET.md','REPORT.md','MEASUREMENTS.json','REPAIR_MEASUREMENT.json','MATH_BRAIN_RETRIEVAL.json','HYPOTHESIS_COMPARISON.md','EDGE_EVIDENCE.jsonl','BUNDLE_STATE.json','HOOK_PROPOSALS.jsonl','PROGRESS_ROW.json','COMMUNICATION_RECEIPTS.json','patches/01_c0017_spin_source_correction.diff']
assert all((ROOT/p).is_file() for p in required)
claims=[json.loads(s) for s in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if s]
for c in claims:
    assert all(k in c for k in ['statement','assumptions','source','proof_or_counterexample','independent_reviewer','remaining_gap','status'])
assert len({c['id'] for c in claims})==len(claims)
local=(ROOT/'bundle_001.json').read_text(encoding='utf-8')
assert local==Path('~/math-brain-inbox/w417/bundle_001.json').read_text(encoding='utf-8')
bundle=json.loads(local)
assert all(e['kind'] in ['definition','concept'] and e['proof_text'] is None for e in bundle['entries'])
assert len((ROOT/'EDGE_EVIDENCE.jsonl').read_text(encoding='utf-8').splitlines())==len(bundle['relations'])
measure=json.loads((ROOT/'MEASUREMENTS.json').read_text(encoding='utf-8'))
assert measure['L1_violations']==measure['L2_violations']==0
assert measure['seconds']<=measure['gate']['max_wall_seconds']
patch=(ROOT/'patches/01_c0017_spin_source_correction.diff').read_text(encoding='utf-8')
assert '@@ -17 +17 @@' in patch and 'draft_pending_w419' in patch
receipt={'artifact_validation':'PASS','claim_rows':len(claims),'bundle_entries':len(bundle['entries']),'edge_rows':len(bundle['relations']),'unreviewed_theorem_promotions':0,'bundle_matches_named_inbox':True,'mathematical_proof_status':'Partial written proofs; C0017 and G1 unproved; formal-check receipt absent.'}
(ROOT/'FINAL_VALIDATION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
