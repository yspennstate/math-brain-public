from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1]
(R/'out').mkdir(exist_ok=True)
src=Path('agents/A031/runs/20261023T001357Z-fleet03-A031-convolution-identity')
data=(src/'code/check_nonfair.py').read_bytes()
(R/'code/dependency.py').write_bytes(data)
manifest={str(src/p):hashlib.sha256((src/p).read_bytes()).hexdigest() for p in ['REPORT.md','DERIVATION.md','CLAIMS.json','code/check_nonfair.py']}
(R/'out/SOURCES.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
spec=dict(helper_version='A035-closed-reset-cycle-v1',family='Actual equal-width three-clause Boolean triangle; physical x,b,y in X2,z in X3; final prescribed fair-a reference',domain=[1,2,3,4,8,16,32,64],pilot=[1,2,3],case_count=8,physical_terminals_per_width=16,symmetry='Only unexposed bits within each private block are exchangeable; all physical outcomes retained',arithmetic='Exact Fraction signed amplitudes; 28-term rational atanh log bounds with weighted masses before 256-bit outward rounding',memory_estimate_MB=90,max_runtime_seconds=180,independent_reproduction='Direct truth table and integer FWHT for L=1,2,3; separate 24-term log enclosure',reproduction_max_seconds=55)
spec['helper_sha256']=hashlib.sha256((R/'code/check_cycle.py').read_bytes()).hexdigest()
(R/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
print('Frozen source manifest and bounded domain saved.')
