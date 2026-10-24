from pathlib import Path
import json,hashlib,shutil
R=Path(__file__).resolve().parents[1];HOME=R.parents[1];TEAM=HOME.parent.parent
(R/'out'/'sources').mkdir(parents=True,exist_ok=True)
files=[TEAM/'BOARD.md',TEAM/'claude/B01/STREAM_NOTES.md',HOME/'STATUS.md',Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')]
for agent,run,names in [('A096','20261014T013836Z-account05-A096-live-gap-ledger',['REPORT.md','DERIVATION.md','CLAIMS.json']),('A003','20261014T021415Z-account05-A003-minimal-target-formulation',['REPORT.md','DERIVATION.md','CLAIMS.json']),('A026','20261014T011337Z-account05-A026-good-coordinate-erasure',['REPORT.md'])]:
 for name in names:files.append(TEAM/'agents'/agent/'runs'/run/name)
manifest=[]
for j,p in enumerate(files):
 b=p.read_bytes();dst=R/'out/sources'/f'{j:02d}-{p.name}';dst.write_bytes(b)
 manifest.append({'source':str(p),'snapshot':str(dst.relative_to(R)),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
(R/'out/SOURCE_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
shutil.copyfile(HOME/'runs/20261013T235034Z-account05-A004-constant-and-unit-ledger/code/arithmetic.py',R/'code/arithmetic.py')
spec={'helper_version':'A004-KL-shadow-owner-v1','family':'all uniform Boolean seeds up to three bits, disjoint parity pairs, Maj3/partner unlocking trees, quadratic bent/flip controls',
 'domain':{'all_truth_tables_n':[0,1,2,3],'parity_subsets':'every J','unlocking_outer_n':[1,2],'unlocking_n3_masks':[0,1,7,15,105,150,232,255],'unlocking_coordinate':'every seed coordinate including irrelevant','encoder':'Maj3','orders':['forward','adaptive_reverse'],'bent_d':[2,4,6,8]},
 'case_count':{'seeds':278,'partial_parity_substitutions':2122,'unlocking_compositions':60,'unlocking_trees':120,'bent_controls':4},
 'symmetry':'none on seeds, J or distinguished coordinate; two explicitly prescribed physical encoder policies; no dimension escalation',
 'arithmetic':'integer Walsh, direct flips, Fraction, canonical prime-log identities; rational atanh sign certificates; analytic all-dimensional proof separate',
 'memory_estimate_MB':100,'max_runtime_seconds':60}
(R/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
(HOME/'STATUS.md').write_text('STATE: A004 stage 4 IN PROGRESS: reviewing A096 partner KL ownership and cross-route signed terminal reserve; full FEI OPEN.\nNEXT: Exact parity/encoder certificates, then source-bound review and one-owner surplus criterion.\n',encoding='utf-8')
print('Frozen spec and source snapshots saved.')
