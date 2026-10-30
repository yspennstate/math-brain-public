from pathlib import Path
import json,hashlib,shutil
R=Path(__file__).resolve().parents[1];HOME=R.parents[1];TEAM=HOME.parent.parent
(R/'out/sources').mkdir(parents=True,exist_ok=True)
sources=[TEAM/'BOARD.md',TEAM/'claude/B01/STREAM_NOTES.md',HOME/'STATUS.md',Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')]
for agent,run,names in [('A003','20261014T050612Z-fleet05-A003-minimal-target-formulation',['REPORT.md','DERIVATION.md','CLAIMS.json','REVIEW.md']),('A027','20261014T043519Z-fleet05-A027-block-selection',['REPORT.md']),('A096','20261014T042803Z-fleet05-A096-live-gap-ledger',['REPORT.md'])]:
 for name in names:sources.append(TEAM/'agents'/agent/'runs'/run/name)
receipts=[]
for j,p in enumerate(sources):
 b=p.read_bytes();dst=R/'out/sources'/f'{j:02d}-{p.name}';dst.write_bytes(b)
 receipts.append({'path':str(p),'snapshot':str(dst.relative_to(R)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(R/'out/SOURCE_MANIFEST.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8')
shutil.copyfile(HOME/'runs/20261014T024610Z-fleet05-A004-constant-and-unit-ledger/code/arithmetic.py',R/'code/arithmetic.py')
spec={'helper_version':'A004-point-edit-ledger-v1','family':'all positive-endpoint single-vertex edits through three dimensions; A003 point-constant pair; padded AND3 edits with destroyed or neutral origin edges',
 'domain':{'exhaustive_n':[1,2,3],'masks':'all truth tables','vertex':'every vertex at which b=+1','point_dimensions':list(range(1,11)),'padded_AND3_dummy_bits':[1,2,3],'tensor_test':'independent dictator on point pairs'},
 'case_count':{'exhaustive_positive_endpoint_pairs':1060,'point_pairs':10,'padded_AND3_pairs':3,'tensor_checks':10},
 'symmetry':'global sign symmetry covers negative endpoints; all labelled positive-endpoint pairs retained; no permutation quotient',
 'arithmetic':'integer FWHT, independent physical edge counts, Fraction, exact prime-log identities, proved rational atanh enclosures; all-dimensional source review analytic',
 'memory_estimate_MB':80,'max_runtime_seconds':60,'automatic_dimension_escalation':False}
(R/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
(HOME/'STATUS.md').write_text('STATE: A004 stage 5 IN PROGRESS: review sharp retained point allowance; exact destroyed-edge terminal-owner ledger; FEI OPEN.\nNEXT: Validate arbitrary small point edits and neutral padded AND3, then record scoped acceptance and honest universal gap.\n',encoding='utf-8')
print('Saved source snapshots and frozen specification.')
