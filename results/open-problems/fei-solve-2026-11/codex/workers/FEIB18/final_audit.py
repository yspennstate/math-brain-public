"""Read the finished artifacts and check their provenance and scope."""
import json,hashlib,platform,sys,os
from pathlib import Path
import numpy,scipy
required=['STATUS.md','RESULTS.md','REPORT.md','REFEREE.md','PROOFS.md','LEARNINGS.md','FLOW_SNAPSHOT.md','SOURCE_SHA256.txt','attack.py','attack.log','cube_rows.jsonl','attack_summary.json','verify.py','verification.json','verification.log','constants.py','constants.json','constants.log']
assert all(Path(p).is_file() and Path(p).stat().st_size for p in required)
sha=hashlib.sha256(Path('FLOW_SNAPSHOT.md').read_bytes()).hexdigest()
assert sha==Path('SOURCE_SHA256.txt').read_text().split()[0]
s=json.load(open('attack_summary.json'));v=json.load(open('verification.json'));c=json.load(open('constants.json'))
rows=0;maxima={k:-1 for k in ['M_all','M_positive','L_over_delta','E_over_delta','cross_stay','H_over_I']};dims=set()
for line in open('cube_rows.jsonl'):
    row=json.loads(line);rows+=1;dims.add(row['n'])
    for k in maxima:maxima[k]=max(maxima[k],row[k])
assert rows==s['counts']['cube_cases']-s['counts']['constants']
for k,value in maxima.items():assert value==s['best'][k]['value']
assert max(dims)==16 and {1,2}.issubset(dims)
assert len(s['rhos'])*rows==s['counts']['noise_rates']
assert s['actual_nice']>=10 and v['actual_nice']>=10
assert max(s['peak_rss_bytes'],v['peak_rss_bytes'])<3*2**30
assert not Path('VIOLATION.json').exists()
assert c['K0']==3 and c['Mcs_rounded']==80 and c['M_exact']=='101913/100'
assert v['direct_pair_max_residual']==0
assert 'NEXT:' in Path('STATUS.md').read_text()
assert all(label in Path('REFEREE.md').read_text() for label in ['11(a):','11(b):','11(c):','11(e):','11(i):','11(j):','11(k):','Final theorem:','Setting and small dimensions:'])
# Required output numbers are traced to the final machine-readable records.
report=Path('REPORT.md').read_text()
assert f"{s['counts']['cube_cases']:,}" in report
assert f"{s['counts']['cube_cases']-s['counts']['constants']:,}" in report
assert f"{s['counts']['noise_rates']:,}" in report
sizes={p:Path(p).stat().st_size for p in required}
folder_bytes=sum(p.stat().st_size for p in Path('.').rglob('*') if p.is_file())
assert folder_bytes<10**9
out={'status':'PASS','source_sha256':sha,'required_files':sizes,'rows':rows,'dimensions_in_nonconstant_rows':sorted(dims),'maxima_reconstructed_from_rows':maxima,'folder_bytes_at_audit':folder_bytes,'python':sys.version,'numpy':numpy.__version__,'scipy':scipy.__version__,'platform':platform.platform(),'actual_nice':os.getpriority(os.PRIO_PROCESS,0),'artifact_sha256':{p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in required}}
Path('final_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','rows','source_sha256','folder_bytes_at_audit','actual_nice']},indent=2))
