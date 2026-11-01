from pathlib import Path
import json,hashlib
from fractions import Fraction as F
RUN=Path(__file__).resolve().parents[1]
P=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
protocol=json.loads(P.read_text())
claims=json.loads((RUN/'CLAIMS.json').read_text())
for c in claims:
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
    actual=hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert actual==c['statement_sha256']
    assert all((RUN/f).is_file() for f in c['proof_source']['files'])
progress=json.loads((RUN/'PROGRESS.json').read_text())
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert progress==json.loads((RUN/'PACKET_DELTA.json').read_text())
for k,lo,hi in [(2,'1.836014211380','1.836014211381'),(4,'1.956704604624','1.956704604625')]:
    out=json.loads((RUN/'out'/f'OPTIMUM_K{k}.json').read_text())
    iv=out['optimal_cost_over_total_influence']
    assert F(lo)==F(iv['lower']) and F(hi)==F(iv['upper'])
    assert out['policies']['control']['exact_gap_from_optimum']=={}
    assert json.loads((RUN/'out'/f'INDEPENDENT_K{k}.json').read_text())['status']=='PASS'
manifest=RUN/'out/PERSISTENCE_RECEIPTS.json'
receipt=json.loads(manifest.read_text())
for f in receipt['files']:
    data=(RUN/f['path']).read_bytes()
    assert hashlib.sha256(data).hexdigest()==f['sha256'] and len(data)==f['bytes']
for f in receipt['rolling_files']:
    assert hashlib.sha256(Path(f['path']).read_bytes()).hexdigest()==f['sha256']
output={'status':'SAVED_CONTENT_VERIFIED','claim_hashes_recomputed':True,'protocol_key_sets_exact':True,'all_recorded_file_hashes_match':True,'displayed_optimum_intervals_match_exact_outputs':True,'external_review_completed':False}
out=RUN/'out/SAVED_CONTENT_CHECK.json';out.write_text(json.dumps(output,indent=2),encoding='utf-8')
for path in [Path(__file__).resolve(),out]:
    data=path.read_bytes(); assert len(data)<20_000_000
    receipt['files'].append({'path':str(path.relative_to(RUN)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
receipt['saved_content_check']='out/SAVED_CONTENT_CHECK.json'
manifest.write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(output))
