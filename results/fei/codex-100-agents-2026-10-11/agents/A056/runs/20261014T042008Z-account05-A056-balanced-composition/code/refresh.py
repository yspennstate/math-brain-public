from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1];HOME=R.parents[1]
def sha(z):return hashlib.sha256(z).hexdigest()
def write(p,v):p.write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
claims=json.loads((R/'CLAIMS.json').read_text(encoding='utf-8'))
claims[0]['exact_statement']+=' At every controller query the compatible reference erasure, outcome and categorical KL releases are exactly zero; the fixed branch debt averages harmonically, so no controller-entropy payment is inferred.'
for c in claims:
 raw=json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()
 c['statement_sha256']=sha(raw)
write(R/'CLAIMS.json',claims)
p=json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'))
p['mathematical_delta']+=' Compatible controller-query KL releases are exactly zero, leaving entropy payment separate.'
p['source_artifacts']+=['out/CONTROLLER_SPEC.json','code/controller_zero.py','out/controller_zero.json']
write(R/'PROGRESS.json',p);write(R/'PACKET_DELTA.json',p)
with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n2026-10-14 stage5 supplement: Compatible-reference controller queries have E=O=C=0 by exact sector factorization;64 frozen checks PASS. Added this guard to the existing v3 statement/report. No release can be silently used to pay controller entropy.\n')
with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nCompatible mux reference controller query: erasureKL0 because Q/P is constant across controller subsets inside each exclusive data fiber; shared-only fibers Q=P. Projected reference outcome probabilities equal1/2, and normalized children already have the rebuilt form. Thus E=O=C=0 at every controller query; source-owned branch KL is harmonic, not a released controller-entropy bank.\n')
protocol=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
rules=json.loads(protocol.read_text(encoding='utf-8-sig'))['required_per_run']
assert set(p)=={s.split(' (')[0] for s in rules['progress_fields']}
assert all(set(c)==set(rules['claim_fields']) for c in claims)
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
report=(R/'REPORT.md').read_text(encoding='utf-8');assert all('# '+s in report for s in rules['report_fields']) and report.split('\n# ')[-1].startswith('Universal bridge\n')
assert len((HOME/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
checks={name:json.loads((R/f'out/{name}.json').read_text(encoding='utf-8')) for name in ['pilot','checks','trees','review_release','controller_zero']}
assert all(c['result']=='ALL PASS' for c in checks.values())
files=[]
for path in sorted(R.rglob('*')):
 if path.is_file() and path.name!='PERSISTENCE.json':
  raw=path.read_bytes();assert len(raw)<20_000_000;files.append({'path':str(path.relative_to(R)),'bytes':len(raw),'sha256':sha(raw)})
write(R/'out/PERSISTENCE.json',{'scope':'local only;mirror and downstream use unobserved','files':files,'checks':checks,'rolling_files':[{'path':str(HOME/name),'sha256':sha((HOME/name).read_bytes())} for name in ['STATUS.md','WORKLOG.md','LEARNED.md']]})
print(json.dumps({'schema':'ALL PASS','claims':len(claims),'packet_copy':'IDENTICAL','controller_KL':'EXACT ZERO','local_manifest_files':len(files)},indent=2))
