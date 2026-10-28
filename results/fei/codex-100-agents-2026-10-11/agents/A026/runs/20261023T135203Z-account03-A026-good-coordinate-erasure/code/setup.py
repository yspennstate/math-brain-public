from pathlib import Path
import json,shutil,hashlib
R=Path(__file__).resolve().parents[1];A=R.parents[1];(R/'out').mkdir(exist_ok=True)
old=A/'runs/20261023T113002Z-account03-A026-good-coordinate-erasure'
for n in ('prior.py','exact_helper.py'):shutil.copyfile(old/'code'/n,R/'code'/n)
P=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json');proto=json.loads(P.read_text(encoding='utf-8'))
(R/'out/PROTOCOL_PIN.json').write_text(json.dumps({'revision':proto['revision'],'sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'required_per_run':proto['required_per_run']},indent=2)+'\n',encoding='utf-8',newline='\n')
spec={'helper_version':'A026@5 copied prior and exact_helper; new canonical full-reference implementation', 'family':'A029 common-character point3/negative-majority3 source; outside-image guard a=y,G=z,H=z*b_n', 'domain':'pilot m1 policy0; full m1,2 policies0..5, both full children, old shape1/8 and literal controller/first odds; guard n3..8', 'case_count':'pilot one mixed tree; full12 policies with at most3060 nodes; six guard n; generic local bound all reached states', 'symmetry':'none; no dimension escalation', 'arithmetic':'Fraction Walsh, exact prime-log signed CE and outward rational enclosures; real parameter bridge proved analytically', 'memory_estimate_MB':180, 'maximum_runtime_seconds':{'pilot':55,'full':300,'independent':55},'targets':'empty DATA row relative lambda1/2,1,2; nonempty row epsilon0,1/32,1/16; literal first odds retained', 'negative_guard':'fixed-strength vacuum floors unpaid in rare-control family; already A029@4, not re-searched'}
(R/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8',newline='\n')
src=[P,old/'CLAIMS.json',A/'STATUS.md',Path(r'BOARD.md'),Path(r'claude\B06\STREAM_NOTES.md'),Path(r'agents\A029\runs\20261023T125429Z-account03-A029-child-deficit-transport\DERIVATION.md'),Path(r'agents\A028\runs\20261023T122923Z-account03-A028-stopping-tree-payment\REPORT.md')]
(R/'out/SOURCE_RECEIPT.json').write_text(json.dumps([{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in src],indent=2)+'\n',encoding='utf-8',newline='\n')
print('stage21 spec and source pins saved')
