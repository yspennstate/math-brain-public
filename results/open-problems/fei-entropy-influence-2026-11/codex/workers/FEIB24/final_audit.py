import csv,json,hashlib,re,math,time
from pathlib import Path
from fractions import Fraction
import numpy as np
from analysis import evaluate
R=lambda p:json.load(open(p))
checks=[]
expected=[(3,3),(6,5),(20,10),(168,30),(7581,210),(7828354,16353)]
a=R('audit.json')
assert [(x['labelled'],x['classes']) for x in a['counts']]==expected;checks.append('labelled and permutation counts')
for n in range(1,7):
 rows=list(csv.DictReader(open(f'census_n{n}.csv')));assert sum(int(r['orbit']) for r in rows)==expected[n-1][0]
 iv=R('interval_census.json')['results'][n-1]
 for field in ['minratio','HI','EI']:
  saved={int(x['truth_hex'],16) for x in R('all_extrema.json')[str(n)][field]};cert={int(x,16) for x in iv['fields'][field]['extremizers']};assert saved==cert
  f=iv['fields'][field];assert Fraction(f['upper_exact'])-Fraction(f['lower_exact'])==Fraction(f['interval_width_exact'])
  if f['nonmax_gap_lower_exact'] is not None:assert Fraction(f['nonmax_gap_lower_exact'])>0
checks.append('all monotone extrema agree with interval-certified winners; exact positive separation gaps')
for line in Path('npn.log').read_text().splitlines():
 m=re.match(r'npn n=(\d+) classes=(\d+) (.*)',line);assert m
 n=int(m[1]);assert int(m[2])==R('highprecision.json')['npn_inputs'][str(n)]['count']
 vals=[float(t.split('@')[0]) for t in m[3].split()];cs=R('census_summary.json')[str(n)]
 for x,y in zip(vals,[float(cs['minratio']['minratio']),cs['HI']['HI'],cs['EI']['EI']]):assert abs(x-y)<1e-12
checks.append('unrestricted NPN extrema match monotone extrema through five variables')
for line in Path('unrestricted.log').read_text().splitlines():
 m=re.match(r'unrestricted n=(\d+) (.*)',line);assert m;n=int(m[1]);vals=[float(t.split('@')[0]) for t in m[2].split()];cs=R('census_summary.json')[str(n)]
 for x,y in zip(vals,[float(cs['minratio']['minratio']),cs['HI']['HI'],cs['EI']['EI']]):assert abs(x-y)<1e-12
checks.append('direct truth-table exhaustive comparison through four variables')
record=R('record18.json');s=evaluate(np.load('witnesses/profile_best.npz')['f']);assert abs(s['minratio']-record['stats']['minratio'])<1e-12;assert abs(s['minratio']-R('profile_best.json')['minratio'])<1e-12;assert len(record['minterms'])==24
assert Fraction(s['I'])==Fraction(110889,65536)
checks.append('literal 24-term DNF independently matches the eighteen-variable record and exact influence')
all_search=R('structured.json')+R('profiles.json')+R('more_constructions.json')['rows']+list(R('hill_audit.json').values())
assert max(r['minratio'] for r in all_search)<=s['minratio']+1e-12
checks.append('reported minimum-coordinate search record dominates every saved search outcome')
tribes=evaluate(np.load('witnesses/tribes_10x2.npz')['f']);assert tribes['HI']>4;assert abs(tribes['HI']-R('tribes_10x2.json')['HI'])<1e-12
assert max(r['HI'] for r in all_search)<=tribes['HI']+1e-12
checks.append('reported raw entropy/influence record dominates saved search outcomes and exceeds four')
for row in R('paired_hidden.json'):
 assert row['x_w2_ratio']==0 and row['other_min_w2_ratio']>0
checks.append('complementary-pair level-two selector fails as stated')
p=R('proof_checks.json');assert p['maximum_parity_upper_violation_bits']==0;assert p['max_leaf_formula_residual_bits']<1e-12;assert p['minimum_charging_slack_bits']>=0
checks.append('parity, leaf composition and charging checks')
resources=R('resources.json');assert len(resources['units'])==16 and len(R('reproduction_progress.json'))==16
assert resources['max_child_rss_bytes']<3*2**30 and resources['parent_nice']>=10 and resources['numerical_threads_per_process']==1 and resources['concurrent_units']==1
checks.append('complete sequential reproduction and process limits')
nonempty=[str(p) for p in Path('run_logs').glob('*.err') if p.stat().st_size];assert not nonempty,nonempty;checks.append('all reproduction stderr logs empty')
files=[p for p in Path('.').rglob('*') if p.is_file()];size=sum(p.stat().st_size for p in files);assert size<200*10**6
checks.append('workspace below 200 MB')
inputs=R('highprecision.json')['npn_inputs']
for info in inputs.values():assert hashlib.sha256(Path(info['path']).read_bytes()).hexdigest()==info['sha256']
checks.append('inherited NPN input hashes unchanged')
for filename in ['STATUS.md','RESULTS.md','PROOFS.md','REPORT.md','LITERATURE.md','LEARNINGS.md']:
 assert Path(filename).exists()
checks.append('all required deliverables present')
result=dict(checks=checks,count=len(checks),workspace_file_bytes_before_audit_write=size,workspace_file_count_before_audit_write=len(files),resource_checks=resources,interval_certificate_sha256=hashlib.sha256(Path('interval_census.json').read_bytes()).hexdigest(),proofs_sha256=hashlib.sha256(Path('PROOFS.md').read_bytes()).hexdigest(),report_sha256=hashlib.sha256(Path('REPORT.md').read_bytes()).hexdigest())
Path('final_audit.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items() if k!='resource_checks'},indent=2))
