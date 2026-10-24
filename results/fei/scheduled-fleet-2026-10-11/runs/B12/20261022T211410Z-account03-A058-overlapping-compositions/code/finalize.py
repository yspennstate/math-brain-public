from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]
A=R.parents[1]
protocol=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def readj(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def writej(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
P=readj(protocol)
claims=readj(R/'CLAIMS.json')
progress=readj(R/'PROGRESS.json')
assert readj(R/'PACKET_DELTA.json')==progress
formal_path=R/'out'/'FORMAL_STATUS.json'
if formal_path.exists():
    progress['blockers']=[b for b in progress['blockers'] if not b.startswith('Lean verification')]
    if 'Lean did not start: fresh admission WAIT at 2.0GB physical free; formal core and full theorem remain unverified.' not in progress['blockers']:
        progress['blockers'].append('Lean did not start: fresh admission WAIT at 2.0GB physical free; formal core and full theorem remain unverified.')
for c in claims:
    assert set(c)==set(P['required_per_run']['claim_fields'])
    assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
assert set(progress)=={s.split(' (')[0] for s in P['required_per_run']['progress_fields']}
assert readj(R/'PACKET_DELTA.json')['run_id']==progress['run_id']
report=(R/'REPORT.md').read_text(encoding='utf-8')
for field in P['required_per_run']['report_fields']: assert '# '+field in report
assert report.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
for spec in ['FROZEN_SPEC','PRIVATE_SPEC','ALL_HISTORY_SPEC']: assert readj(R/'out'/f'{spec}.json')
v1=readj(R/'out'/'exact_matching_means.json');v2=readj(R/'out'/'exact_common_phase.json')
assert v1['cases']==6238 and v1['exact_assertions']==18714
assert v2['states']==4448 and v2['data_checks']==17312 and v2['exact_mean_only_representation_assertions']==1734
assert v1['status']==v2['status']=='PASS'
sources=[protocol,Path(r'~\AGENTS.md'),Path(r'~\brain_workers\FEI100_20261011\BOARD.md'),Path(r'~\brain_workers\FEI100_20261011\claude\B12\STREAM_NOTES.md')]
base=protocol.parent
sources += [base/x for x in ['README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json']]
sources += list(base.glob('*.tex'))
push=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
sources += [push/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
sources += list((push/'sources').glob('*.md'))
sources += list(Path(r'~\brain_workers\FEI100_20261011\context').glob('*.txt'))
old=A/'runs'/'20261014T052501Z-account05-A058-overlapping-compositions'
sources += [old/x for x in ['REPORT.md','CLAIMS.json','ALL_ORDER_REPAIR.md']]
receipts=[]
for p in sources:
    if p.is_file():
        b=p.read_bytes();receipts.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'use':'orientation/context only unless named in REPORT'})
writej(R/'out'/'SOURCE_RECEIPTS.json',receipts)
status=A/'STATUS.md'
if not (R/'out'/'PRIOR_STATUS.txt').exists() and status.exists(): (R/'out'/'PRIOR_STATUS.txt').write_text(status.read_text(encoding='utf-8-sig'),encoding='utf-8')
status.write_text('STATE: A058 substantive stage6 saved: arbitrary common-phase scalar R; all-history coherent rates54/162, closure166; 42786 exact assertions plus controls PASS; independent review pending, FEI OPEN.\nNEXT: A091/A090 review v6; perturb one phase off the common ray and pay only noncollinear remainder from SAME unused inherited source, preserving old debits and both full terminals.\n',encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
marker=R.name
entries={
'WORKLOG.md':f'\n{stamp} | {marker} | Common-phase collision transport: exact matching-mean identity, mean-only R, rates54 data/162 residual selector/166 full selector; first private12. 6238 equal-mean cases and4448 history states,578 full Walsh fixtures PASS. Both terminals retained; unrelated phases/core payment remain open. Wake integrity warning disclosed; local shell transport slow; no other work stopped. Independent review and remote persistence pending.\n',
'LEARNED.md':f'\n[{marker}] For disjoint private blocks, mux entropy equals half both core entropies plus4 selector influence plus sum rho(shared mean amplitudes). Matching full conditional means cancel rho; equal overall bias alone does not. For independently point-activated SAME arbitrary phase, homogeneity eliminates all nonempty spectral-scale logarithms: R=rho(1-2pt,1-2qt)+4t(1-t)rho(p,q). Separate9-Lipschitz scalar rho yields54 per actual data influence,162 selector residual and166 full selector cost through all adaptive histories. Both core entropy bills and signed decrements remain; arbitrary u is not a certified FEI terminal. First equal-probability private query improves to12. Distinct phases break collinearity; do not export the mean-only formula or renew physical ownership across nested mux levels. Proof author-checked, independent review pending, no full Lean certification.\n'}
for name,entry in entries.items():
    p=A/name
    oldtext=p.read_text(encoding='utf-8-sig') if p.exists() else ''
    if marker not in oldtext: p.write_text(oldtext+entry,encoding='utf-8')
progress['deliverable_status']='COMPLETE_LOCAL'
writej(R/'PROGRESS.json',progress);writej(R/'PACKET_DELTA.json',progress)
files=list(R.rglob('*'))
assert all(p.stat().st_size<20*1024*1024 for p in files if p.is_file())
manifest=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name not in ['MANIFEST.json','FINALIZE.json']:
        manifest.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
for p in [A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']:
    manifest.append({'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
writej(R/'out'/'MANIFEST.json',manifest)
receipt={'status':'PASS','at_utc':stamp,'run_id':marker,'claim_statement_sha256':claims[0]['statement_sha256'],'manifest_entries':len(manifest),'source_receipts':len(receipts),'exact_check_assertions':42786,'hypothesis_controls':2,'full_fei':'OPEN','independent_review':'PENDING','remote_copy':'UNVERIFIED','lean_full_theorem':'NOT_CHECKED'}
writej(R/'out'/'FINALIZE.json',receipt)
print(json.dumps(receipt))
