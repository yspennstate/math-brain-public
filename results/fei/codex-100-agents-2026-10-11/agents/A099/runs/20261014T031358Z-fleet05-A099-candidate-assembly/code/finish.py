from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parent.parent
BASE=Path(r'~\mop_fei100\reports\fei-2026-10-11')
def read(p):return p.read_text(encoding='utf-8-sig')
def obj(p):return json.loads(read(p))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,v):(RUN/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=obj(BASE/'EXECUTION_PROTOCOL.json');report=read(RUN/'REPORT.md')
for h in protocol['required_per_run']['report_fields']:assert '## '+h in report
assert report.rstrip().splitlines()[-1].startswith('Universal bridge:')
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert set(obj(RUN/'PROGRESS.json'))=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
for c in obj(RUN/'CLAIMS.json'):assert set(c)==set(protocol['required_per_run']['claim_fields'])
val=obj(RUN/'out/VALIDATION.json');ok=len(val['build'])==2 and all(b.get('returncode')==0 for b in val['build'])
val['PDF_complete_two_passes']=ok;save('out/VALIDATION.json',val)
p=obj(RUN/'PROGRESS.json')
if ok:
    p['source_artifacts'].append('out/CANDIDATE_MANUSCRIPT.pdf')
    report=report.replace('Complete PDF availability is reported by out/VALIDATION.json after the bounded compiler passes.','The complete PDF compiled in two bounded passes; out/VALIDATION.json records the result. No local save blocker remains.')
else:
    p['blockers'].append('Verified complete PDF unavailable; bounded compiler result recorded; complete source saved')
    report=report.replace('Complete PDF availability is reported by out/VALIDATION.json after the bounded compiler passes.','A verified complete PDF is unavailable after the bounded compiler result recorded in out/VALIDATION.json. Source and protocol persistence are complete; PDF generation is the precise remaining artifact blocker.')
save('PROGRESS.json',p);save('PACKET_DELTA.json',p)
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
(ROOT/'STATUS.md').write_text('STATE: A099 v4 saved: linear shared-selector tax t+2+3/ln2 independently reviewed at application scope; complete refund/shared-data audits consumed; binary remainder and compression no-go assembled; full FEI OPEN.\nNEXT: A001/A096/A073 pay quotient remainder plus retained terminal row from one certified child slack; A094/A085 audit reserve and integrated chain; A095/A097 name exclusive collision core bank.\n',encoding='utf-8')
stamp=datetime.now(timezone.utc).isoformat()
with (ROOT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{stamp}: {RUN.name}: source-complete v4 assembled; independently reconstructed only A095 v3 shared-selector slice (linear tax and sharp leading coefficient), 466 pairs/932 references/8664 exact assertions PASS. Consumed A073/A001 refund reviews, A094 shared-bit review, A098 positive-erasure remainder acceptance; complete compression and partner no-go proofs retained. Three digest conventions identified from actual source generators. PDF complete={ok}; full FEI and both integrated audits remain open.\n')
with (ROOT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nFor t>=2 arbitrary shared data bits and disjoint private cubes, Delta<=(t+2+3/ln2)min(d,1-d); calibrated complete references retain average full terminal KL. The cap delta_C<=min(d*,2^t d*^2) makes the tax linear, with sharp leading coefficient one. It cannot yield an absolute selector-only tax. A095 bundled v3 is accepted here only at this new application slice.\n\nComplete KL marginalization may discard unbounded conditional divergence even with unit reference normalizer and full Fourier support at I->0. Keeping individually all low-degree atoms and one tail is refuted; canceling an actually common spectator factor is exact. One partner bit can contain the whole rarity refund, while deleting it loses the original terminal row cost.\n\nA073 positive-erasure binary quotient loses <63/256 of its query influence and its two losses fit a dedicated tenth of one core influence, but retained row cost/influence grows above d/2+3/4. This is a remainder-only reserve, not a free terminal entropy bank. A098 independently accepts the exact original family statement.\n\nSource digests have three verified conventions: raw UTF8 statement, canonical statement/hypotheses JSON, and exact_statement/hypotheses JSON with ensure_ascii=False. Verify the actual generator rather than silently rewriting identifiers. A094 one-node reference review does not accept the adaptive full tree.\n')
assert len(read(ROOT/'STATUS.md').splitlines())==2
assert all(q.stat().st_size<20_000_000 for q in RUN.rglob('*') if q.is_file())
save('out/SCHEMA_CHECK.json',{'report_fields':True,'claim_fields':True,'progress_fields':True,'compatibility_identical':True,'all_files_below_20MB':True,'rolling_status_two_lines':True,'PDF_complete':ok,'integrated_audits':'PENDING','mirror':'NOT_VERIFIED'})
receipts=[{'path':str(q.relative_to(RUN)),'bytes':q.stat().st_size,'sha256':sha(q)} for q in sorted(RUN.rglob('*')) if q.is_file() and q.name!='PERSISTENCE_RECEIPTS.json']
save('out/PERSISTENCE_RECEIPTS.json',{'run_id':RUN.name,'files':receipts,'self_excluded':True,'rolling_files':[{'path':str(q),'sha256':sha(q)} for q in [ROOT/'STATUS.md',ROOT/'WORKLOG.md',ROOT/'LEARNED.md']],'mirror':'NOT_VERIFIED'})
assert all(sha(RUN/r['path'])==r['sha256'] for r in receipts)
print(json.dumps({'status':'SAVED','receipt_files':len(receipts),'PDF_complete':ok,'full_FEI':'OPEN','integrated_audits':'PENDING'}))
