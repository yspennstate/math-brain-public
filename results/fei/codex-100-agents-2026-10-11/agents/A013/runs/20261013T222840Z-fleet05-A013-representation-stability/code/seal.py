from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj):(R/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
extra=json.loads((R/'out/CONSTANT_BOUNDARY_RESULTS.json').read_text());base=json.loads((R/'out/EXACT_RESULTS.json').read_text())
assert extra['status']==base['status']=='PASS';assert extra['partial_assignment_cases']==20736
total=extra['exact_assertions']+base['exact_assertions']
claims=json.loads((R/'CLAIMS.json').read_text())
own=claims[0]
own['exact_statement']=own['exact_statement'].replace('as specified in the proof; six coherent-reference','as specified in the proof, with constant children handled by the point-mass vacuum reference and density/rarity distinguished at zero-literal boundaries; six coherent-reference')
own['statement_sha256']=hashlib.sha256(own['exact_statement'].encode()).hexdigest()
own['proof_source']['sha256']=sha(R/'DERIVATION.md')
own['proof_source']['constant_boundary_validation']=str(R/'out/CONSTANT_BOUNDARY_RESULTS.json')
save('CLAIMS.json',claims)
text=(R/'REPORT.md').read_text()
needle='No failed search or mathematical assertion occurred in this stage.'
extra_text=f'''No failed search or mathematical assertion occurred in this stage.

A final analytic audit identified the zero-literal clipping boundary: a fully satisfied clause makes the child constant +1 and uses the vacuum reference, rather than giving a density-one gate the nonconstant root formula. Saved out/CONSTANT_BOUNDARY_SPEC.json before running `python -X utf8 runs\\{R.name}\\code\\check_constant_boundary.py`. All 20,736 partial assignments on the 256 shared-bit branch pairs passed {extra['exact_assertions']:,} exact assertions in {extra['elapsed_seconds']:.7f} seconds (30 MB estimate). These include {extra['constant_children']:,} constant children and {extra['zero_literal_histories']:,} zero-literal histories. Surviving nonconstant density equals clipped rarity and has the stated root probability. This new boundary concern justified the additional check; the passed mux enumeration was not repeated. Total completed assertions: {total:,}.
'''
assert needle in text;text=text.replace(needle,extra_text)
(R/'REPORT.md').write_text(text,encoding='utf-8')
progress=json.loads((R/'PROGRESS.json').read_text())
progress['mathematical_delta']+=' All 20,736 partial physical assignments verify constant-child clipping and original cover/root metadata; total 348,136 exact assertions.'
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
status=(A/'STATUS.md').read_text().replace('181327 exact assertions','348136 exact assertions')
(A/'STATUS.md').write_text(status,encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{stamp} Stage 3 final boundary audit: distinguished surviving gate density from clipped rarity when a clause loses its last literal. Constants use vacuum. Froze all20736 partial assignments;166809 assertions PASS in0.3824929s; total348136. Sealed refreshed proof hashes and receipts without repeating prior checks or altering the initial status snapshot.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage 3 constant boundary: removing a last satisfied literal yields a constant-true gate and hence a constant child; use the vacuum reference. Density doubles per removed literal, but density-one is not the nonconstant clipped rarity. A constant child may also arise by a union covering the whole cube without a zero-literal clause. Only nonconstant children use independent root pi/(N+pi); all20736 partial assignments checked.\n')
protocol=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
fields=json.loads(protocol.read_text(encoding='utf-8-sig'))['required_per_run']
assert set(progress)=={x.split(' (')[0] for x in fields['progress_fields']}
for c in claims:
 assert set(c)==set(fields['claim_fields'])
 assert hashlib.sha256(c['exact_statement'].encode()).hexdigest()==c['statement_sha256']
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text().splitlines())==2
receipts=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
  assert p.stat().st_size<20_000_000;receipts.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size})
for p in [A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']:receipts.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size})
save('out/PERSISTENCE_RECEIPTS.json',receipts)
for rec in receipts:assert sha(Path(rec['path']))==rec['sha256']
print(json.dumps({'status':'SEALED_AND_REREAD_VERIFIED','exact_assertions':total,'receipts':len(receipts),'claims':len(claims)}))
