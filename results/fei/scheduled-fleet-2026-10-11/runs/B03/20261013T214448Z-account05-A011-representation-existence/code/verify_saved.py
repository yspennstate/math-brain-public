import pathlib,json,hashlib,datetime
R=pathlib.Path(__file__).resolve().parents[1]; A=R.parents[1]
protocol=json.loads(pathlib.Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
def digest(p):
 b=p.read_bytes(); return {'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
claims=json.loads((R/'CLAIMS.json').read_text())
for claim in claims:
 assert set(claim)==set(protocol['required_per_run']['claim_fields'])
 expected=hashlib.sha256(json.dumps({'statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
 assert claim['statement_sha256']==expected
progress=json.loads((R/'PROGRESS.json').read_text())
assert set(progress)==set([x for x in protocol['required_per_run']['progress_fields'] if not x.startswith('packet_ids')]+['packet_ids'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
report=(R/'REPORT.md').read_text(encoding='utf-8')
for heading in protocol['required_per_run']['report_fields']: assert '## '+heading in report
assert '\n\n' not in report.rsplit('## Universal bridge',1)[1].strip()
assert 'c_j-JS' not in report and 'c_j-JS' not in (R/'PHASE_COMB.md').read_text()
out=json.loads((R/'out/EXACT_RESULTS.json').read_text())
assert out['status']=='PASS' and out['exact_assertions']==863307
assert out['helper']['sha256']==digest(R/'code/check_phase_comb.py')['sha256']
assert str(out['exact_assertions']) in progress['mathematical_delta']
assert '863,307' in report and '863,307' in (A/'STATUS.md').read_text()
assert len((A/'STATUS.md').read_text().splitlines())==2
for mode in ['general','equal-a3']:
 result=json.loads((R/f'out/EXACT_{mode}.json').read_text())
 assert result['status']=='PASS' and result['helper_version']=='A011-phase-comb-v1.2' and result['seconds']<55
receipts=json.loads((R/'out/PERSISTENCE_RECEIPTS.json').read_text())
receipts['at_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
receipts['final_checked_total']=863307
receipts['artifacts']=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
  assert p.stat().st_size<20_000_000
  if p.suffix=='.json': json.loads(p.read_text(encoding='utf-8-sig'))
  receipts['artifacts'].append(digest(p))
receipts['rolling']=[digest(A/n) for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]
(R/'out/PERSISTENCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'verification':'PASS','artifacts':len(receipts['artifacts']),'exact_assertions':863307,'review':'PENDING','full_FEI':'OPEN'}))
