from pathlib import Path
import hashlib,json,sys,runpy
R=Path(__file__).resolve().parents[1];(R/'out').mkdir(exist_ok=True)
A=R.parents[1];old=A/'runs/20261023T041335Z-account03-A035-signed-cancellation-countersearch'
for name in ['dependency.py','reconstruct.py']:
 (R/'code'/('math_kernel.py' if name=='dependency.py' else 'truth_kernel.py')).write_bytes((old/'code'/name).read_bytes())
src=Path('agents/A031/runs/20261023T045953Z-account03-A031-convolution-identity')
paths=[src/x for x in ['REPORT.md','DERIVATION.md','CLAIMS.json','code/check_marker.py']]+[old/'DERIVATION.md',old/'code/dependency.py',old/'code/reconstruct.py']
manifest={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
(R/'out/SOURCES.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
spec=dict(helper_version='A035-terminal-KL-envelope-v1',helper_sha256=hashlib.sha256((R/'code/check_exit.py').read_bytes()).hexdigest(),family='Actual equal-width Boolean triangle; canonical x,b,private,a,c exposure; fresh Fair_j on retained private j',domain=list(range(1,21))+[32,64],case_count=22,pilot=[1,2,3],symmetry='Only unqueried private coordinates within each block compressed by empty/nonempty hit; queried and retained coordinates explicit; every physical outcome retained',arithmetic='Exact signed Fraction amplitudes, weighted 28-term rational atanh log bounds; 256-bit outward rounding AFTER multiplicity',memory_estimate_MB=120,max_runtime_seconds=180,pilot_max_seconds=55,independent='Separate truth-table integer FWHT L1,2,3; ALL adaptive query/stop policies holding private j at L1,2 via exact Bellman interval envelope; distinct24-term logs',independent_max_seconds=55)
(R/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
print('Source manifest and search spec saved before pilot.')
sys.path.insert(0,str(R/'code'));sys.argv=['check_exit.py','--pilot'];runpy.run_path(str(R/'code/check_exit.py'),run_name='__main__')
