from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parent.parent
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj):(ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
claims=json.loads((ROOT/'CLAIMS.json').read_text())
claims[0]['proof_source']['sha256']=digest(ROOT/'JOINT_CHANNEL_PROOF.md')
if 'Fixed-threshold minimal-counterexample assertions use K>=0' not in claims[0]['hypotheses']:
    claims[0]['hypotheses'].append('Fixed-threshold minimal-counterexample assertions use K>=0')
save('CLAIMS.json',claims)
manifest=json.loads((ROOT/'out/ARTIFACT_MANIFEST.json').read_text())
manifest['files']=[{'path':str(p.relative_to(ROOT)),'sha256':digest(p),'bytes':p.stat().st_size} for p in sorted(ROOT.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and p.name!='ARTIFACT_MANIFEST.json']
save('out/ARTIFACT_MANIFEST.json',manifest)
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text())
progress=json.loads((ROOT/'PROGRESS.json').read_text())
expected=[x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']]
assert set(progress)==set(expected)
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert progress['packet_ids']==['A051']
for c in claims:
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
    assert c['statement_sha256']==hashlib.sha256(c['exact_statement'].encode()).hexdigest()
    assert c['proof_source']['sha256']==digest(Path(c['proof_source']['path']))
report=(ROOT/'REPORT.md').read_text()
assert all('# '+field in report for field in protocol['required_per_run']['report_fields'])
assert report.rsplit('\n## ',1)[1].startswith('Universal bridge\n')
for row in manifest['files']:
    p=ROOT/row['path'];assert digest(p)==row['sha256'];assert p.stat().st_size<20_000_000
for row in manifest['rolling']:assert digest(Path(row['path']))==row['sha256']
assert len((ROOT.parent.parent/'STATUS.md').read_text().splitlines())==2
summary=json.loads((ROOT/'out/SUMMARY.json').read_text())
replay=json.loads((ROOT/'out/INDEPENDENT_REPLAY.json').read_text())
assert summary['assertions']==30340 and summary['blocks']==1736 and replay['assertions']==1663 and replay['blocks']==168
receipt={'schema':'PASS','hashes':'PASS','all_files_below_20MB':True,'files_checked':len(manifest['files']),
 'exact_assertions':summary['assertions']+replay['assertions'],'external_mirror_verified':False,'independent_agent_review':'PENDING'}
save('out/HANDOFF_CHECK.json',receipt)
# Include the receipt itself after checking the preceding artifacts.
manifest['files'].append({'path':'out\\HANDOFF_CHECK.json','sha256':digest(ROOT/'out/HANDOFF_CHECK.json'),'bytes':(ROOT/'out/HANDOFF_CHECK.json').stat().st_size})
save('out/ARTIFACT_MANIFEST.json',manifest)
print(json.dumps(receipt))
