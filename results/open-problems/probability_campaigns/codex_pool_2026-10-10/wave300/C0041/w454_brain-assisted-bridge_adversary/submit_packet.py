"""Finish local validation and submit labeled concepts to w454's authorized inbox."""
from pathlib import Path
from datetime import datetime, timezone
import json
import sqlite3

ROOT=Path(__file__).resolve().parent
bundle_path=ROOT/'drafts/bundle_001.json'
bundle=json.loads(bundle_path.read_text(encoding='utf-8'))
required={'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
for entry in bundle['entries']:
    assert required<=entry.keys()
    assert entry['kind']=='concept' and entry['proof_text'] is None
    assert len(entry['statement'])>=20 and entry['statement'].startswith('DRAFT')
    assert all(isinstance(entry['source'][key],str) and entry['source'][key] for key in ('source_id','url','revision','license'))
    assert entry['source']['license']=='owner-own-work'
assert len(bundle['entries'])==3 and len(bundle['relations'])==3
measurement=json.loads((ROOT/'alias_measurement.json').read_text(encoding='utf-8'))
assert measurement['before_title_body_matches']==0 and measurement['after_exact_metadata_alias_matches']==1
assert measurement['invalid_queries_rejected']==5 and measurement['case_equivalence']
database=Path('~/math-brain-build/local/population/brain.sqlite3')
target=measurement['retrieved_logical_id']
with sqlite3.connect(database.as_uri()+'?mode=ro',uri=True,timeout=3) as connection:
    row=connection.execute("SELECT body FROM nodes WHERE json_extract(metadata_json,'$.logical_id')=? LIMIT 1",(target,)).fetchone()
    assert row, 'Cross-bundle endpoint no longer exists'
existing_statement=row[0]
by_key={entry['key']:entry for entry in bundle['entries']}
edge_evidence=[]
for relation in bundle['relations']:
    edge_evidence.append({'kind':relation['kind'],'from_key':relation['from_key'],'from_statement_quote':by_key[relation['from_key']]['statement'],'to_key_or_logical':relation.get('to_key') or relation['to_existing_logical'],'to_statement_quote':by_key[relation['to_key']]['statement'] if relation.get('to_key') else existing_statement,'rationale':relation['rationale'],'location':'Own-folder evidence report only; existing private card prose is not copied into the submitted bundle.'})
(ROOT/'EDGE_EVIDENCE_REPORT.jsonl').write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in edge_evidence),encoding='utf-8')
inbox=Path('~/math-brain-inbox/w454')
expected='~/math-brain-inbox/w454'
if inbox.exists():
    assert str(inbox.resolve()).replace('\\','/').casefold()==expected
inbox.mkdir(exist_ok=True)
assert str(inbox.resolve()).replace('\\','/').casefold()==expected
payload=bundle_path.read_bytes()
submitted=None
for index in range(1,1000):
    candidate=inbox/f'bundle_{index:03d}.json'
    partial=inbox/f'bundle_{index:03d}.part'
    if candidate.exists():
        if candidate.read_bytes()==payload:
            submitted=candidate
            break
        continue
    if partial.exists():
        continue
    partial.write_bytes(payload)
    assert not candidate.exists()
    partial.rename(candidate)
    submitted=candidate
    break
assert submitted is not None
now=datetime.now(timezone.utc).isoformat()
state={'checked_at_utc':now,'prepared':{'value':True,'path':str(bundle_path)},'submitted':{'value':True,'path':str(submitted)},'reviewed':{'value':False,'scope':'Own new mathematical claims await w455; concept schema checked locally'},'ingested':{'value':'UNKNOWN','integrator_run_by_w454':False},'retrievable':{'value':'UNKNOWN','reason':'No claim of retrieval of submitted concepts; exact-ID measurement concerns an existing card'},'theorem_entries':0,'concept_entries':3,'relations':3}
(ROOT/'BUNDLE_STATE.json').write_text(json.dumps(state,ensure_ascii=False,indent=2),encoding='utf-8')
timings={'command':measurement['command'],'observed_runs_seconds':[1.4700259000528604,53.31741820008028],'coverage_each_run':{'title_body_matches':0,'metadata_exact_matches':1},'claim':'Coverage change only; elapsed-time variation does not certify a speed improvement.'}
(ROOT/'alias_timing_runs.json').write_text(json.dumps(timings,indent=2),encoding='utf-8')
report_path=ROOT/'REPORT.md'
report=report_path.read_text(encoding='utf-8')
start=report.index('Elapsed time in the first measurement:')
end=report.index(' Main-brain recall separately',start)
report=report[:start]+'Two observed timings were 1.470 and 53.317 seconds; both returned the same target. Lookup coverage is the measured effect.'+report[end:]
old='Apply: reviewer may apply patches/01_candidate_alias_ro.diff to add ~/.claude/brain_graph/bin/candidate_alias_ro.py, then invoke it with the read-only population database and C0041; policy wiring remains proposed.'
new="Apply: reviewer can copy candidate_alias_ro.py to ~/.claude/brain_graph/bin/candidate_alias_ro.py after reviewing patches/01_candidate_alias_ro.diff, then run it with python -B -X utf8, the read-only population database and C0041; policy wiring remains proposed."
assert old in report
report=report.replace(old,new)
report_path.write_text(report,encoding='utf-8')
validation=json.loads((ROOT/'packet_validation.json').read_text(encoding='utf-8'))
validation.update({'source_required_fields_checked':True,'cross_bundle_target_resolved':True,'bundle_submitted_path':str(submitted),'all_claim_ids_unique':True,'all_audit_ids_unique':True,'exact_edge_quotes_saved':True})
for name in ('CLAIMS.jsonl','AUDIT.jsonl'):
    rows=[json.loads(line) for line in (ROOT/name).read_text(encoding='utf-8').splitlines() if line.strip()]
    assert len({row['id'] for row in rows})==len(rows)
(ROOT/'packet_validation.json').write_text(json.dumps(validation,indent=2),encoding='utf-8')
votes=Path('~/primary_directive/democracy/OPEN_VOTES.json')
open_votes=json.loads(votes.read_text(encoding='utf-8-sig')) if votes.exists() else []
print(json.dumps({'validation':validation,'bundle_state':state,'open_votes':open_votes},ensure_ascii=False,indent=2))
