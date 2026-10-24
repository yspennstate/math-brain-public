"""Extract only named P0321 records and exact canonical node IDs."""
from pathlib import Path
import json
import sqlite3

root=Path(__file__).resolve().parent
base=Path('~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907')
entries=[]
for name,key in [('brain_bundle_C006p02.json','op-p0321'),('brain_bundle_C006a05.json','at-p0321')]:
    document=json.loads((base/name).read_text(encoding='utf-8-sig'))
    matched=[entry for entry in document['entries'] if entry.get('key')==key]
    assert len(matched)==1
    entries.append({'source_file':str(base/name),'entry':matched[0]})

canonical=[]
store=Path('~/math-brain-build/local/population/brain.sqlite3')
if store.exists():
    with sqlite3.connect(store.as_uri()+'?mode=ro',uri=True,timeout=5) as db:
        db.row_factory=sqlite3.Row
        has_nodes=db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='nodes'").fetchone()
        if has_nodes:
            for nodeid in ['claim_648b6149635f3ed755552a110f297d32ce8291ed63aa1fbfa8c148a36fcad248','claim_f0fcbb1d46ce0001a883659cae4db27b444d22c8c3d7f3b762bd0376496a0c54']:
                row=db.execute('SELECT * FROM nodes WHERE id=?',(nodeid,)).fetchone()
                if row:
                    parsed=dict(row)
                    metadata=json.loads(parsed.get('metadata_json') or '{}')
                    canonical.append({'id':nodeid,'title':parsed.get('title'),'body':parsed.get('body'),'logical_id':metadata.get('logical_id'),'truth_status':metadata.get('truth_status'),'source_id':metadata.get('source_id'),'read_mode':'ro'})

result={'records':entries,'canonical_population_store':str(store),'canonical_records':canonical,'prior_attempts_H_I_targeted_search':'No P0321 or hexatic match in named H/I attempt folders; this is not an exhaustive current solved/retired certificate.','lean_check':'Only historical ranking match found in prob1000_lean_20260908; no P0321 formal theorem receipt.','Team_O_check':'No P0321 or hexatic match on W0300_O/TEAM_BOARD.md.','percolation_material':'Not read; no relevance identified to this selected elastic/observable-transfer lemma.'}
(root/'TARGET_RECORDS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
status_path=root/'SOURCE_STATUS.json'
status=json.loads(status_path.read_text(encoding='utf-8'))
status['exact_intake_record']={'file':str(base/'brain_bundle_C006p02.json'),'key':'op-p0321','statement':entries[0]['entry']['statement'],'precision':'The exact archived record is qualitative, not a quantified theorem.'}
status['prior_attempt_record']={'file':str(base/'brain_bundle_C006a05.json'),'key':'at-p0321','scope':'Rotation-averaged one-point orientation diagnostic only; marked no independent review.'}
status['owner_solved_retired_check']=result['prior_attempts_H_I_targeted_search']
status['canonical_record_check']={'file':str(store),'mode':'ro','matched_records':len(canonical),'export_target_ids_also_recovered':True}
status['next']='Audit w540 transfer proof; retain UNKNOWN openness and unreviewed concept status.'
status_path.write_text(json.dumps(status,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'exact_intake':entries[0]['entry'],'prior_attempt':entries[1]['entry'],'canonical_records':canonical},ensure_ascii=False,indent=2))
