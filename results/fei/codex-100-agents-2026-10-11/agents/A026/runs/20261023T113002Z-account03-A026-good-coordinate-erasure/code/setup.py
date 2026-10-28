from pathlib import Path
import shutil,json,hashlib
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
old=A/'runs/20261023T045831Z-account03-A026-good-coordinate-erasure'
(R/'out').mkdir(parents=True,exist_ok=True)
for name in ('exact_helper.py','check.py'):
    shutil.copyfile(old/'code'/name,R/'code'/('prior.py' if name=='check.py' else name))
spec={'helper_version':'A026 stage19 exact_helper, prior API byte copy; structural completion stage20',
 'family':'A029 common-character point3/negative-majority3 mux; actual inherited selected DATA child',
 'domain':'pilot m=1, full m=1,2; theta=0,1/8,3/16; first controller j=0,1; phi=0,1/512,1/256; post-controller DATA coordinates individually and ordered-prefix recursion',
 'case_count':'pilot 3*2*2=12 controller children; full 24 controller children; each up to 633 ordered post-DATA prefixes at m2, transactions on each; six complete mixed policies',
 'symmetry':'no quotient in controller or post-DATA prefixes; m not escalated',
 'arithmetic':'Fraction/FWHT, exact prime-log vectors and outward rational log intervals; analytic all-m/continuum proof separate',
 'memory_estimate_MB':170,'maximum_runtime_seconds':{'pilot':55,'full':240,'independent':55},
 'negative_guard':'fair true-zero completion may fail rank-one nonempty shape; record actual witness',
 'no_heavy_job':True}
(R/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
p=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
d=json.loads(p.read_text(encoding='utf-8'))
(R/'out/PROTOCOL_PIN.json').write_text(json.dumps({'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'required_per_run':d['required_per_run']},indent=2)+'\n',encoding='utf-8')
sources=[p, A/'STATUS.md',Path(r'BOARD.md'),Path(r'claude\B06\STREAM_NOTES.md'),old/'DERIVATION.md',old/'CLAIMS.json',Path(r'agents\A029\runs\20261023T105559Z-account03-A029-child-deficit-transport\REPORT.md')]
(R/'out/SOURCE_RECEIPT.json').write_text(json.dumps([{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sources],indent=2)+'\n',encoding='utf-8')
print('stage20 setup and frozen spec saved')
