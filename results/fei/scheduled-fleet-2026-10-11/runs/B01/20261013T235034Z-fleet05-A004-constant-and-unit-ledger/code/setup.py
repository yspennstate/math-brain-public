from pathlib import Path
import json, hashlib, shutil
R=Path(__file__).resolve().parents[1]; HOME=R.parents[1]; BASE=HOME.parent.parent
(R/'out'/'sources').mkdir(parents=True,exist_ok=True)
sources=[BASE/'BOARD.md', BASE/'claude'/'B01'/'STREAM_NOTES.md', HOME/'STATUS.md',
 Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')]
for agent,run,files in [
 ('A003','20261013T222630Z-fleet05-A003-minimal-target-formulation',['REPORT.md','DERIVATION.md','CLAIMS.json']),
 ('A026','20261013T214810Z-fleet05-A026-good-coordinate-erasure',['REPORT.md','PROOF.md','CLAIMS.json']),
 ('A096','20261013T220343Z-fleet05-A096-live-gap-ledger',['REPORT.md'])]:
 for f in files: sources.append(BASE/'agents'/agent/'runs'/run/f)
sources += [HOME/'runs'/'20261012T030039Z-fleet05-A004-constant-and-unit-ledger'/f for f in ['REPORT.md','CLAIMS.json','CONVENTIONS.json','out/persistence_receipt.json']]
receipts=[]
for j,p in enumerate(sources):
 b=p.read_bytes(); dest=R/'out'/'sources'/f'{j:02d}-{p.name}';dest.write_bytes(b)
 receipts.append({'path':str(p),'snapshot':str(dest.relative_to(R)), 'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
(R/'out'/'SOURCE_MANIFEST.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8')
helper=HOME/'runs'/'20261012T030039Z-fleet05-A004-constant-and-unit-ledger'/'code'/'ledger_arithmetic.py'
shutil.copyfile(helper,R/'code'/'arithmetic.py')
spec={'helper_version':'A004-Krawtchouk-review-v1','family':'odd majority, actual once-sliced majority composed with every two-input Boolean outer; adaptive two-query-per-block trees on two Maj3 blocks',
 'domain':{'Krawtchouk_r':list(range(1,65)),'physical_slice_r':list(range(1,5)),'composition_M':[3,5,7],'outer_masks':list(range(16)),'tree_encoders':[3,3]},
 'case_count':{'Krawtchouk_rows':64,'physical_slices':8,'composed_slices':96,'adaptive_trees':16,'constant_calibrations':31},
 'symmetry':'majority permutation invariance only; all labelled outer masks and both slices retained; all physical inner coordinates checked',
 'arithmetic':'integer binomial/Krawtchouk sums, direct physical flips, integer FWHT, Fraction, exact prime-log identities, proved rational atanh intervals',
 'memory_estimate_MB':80,'max_runtime_seconds':60,'automatic_dimension_escalation':False}
(R/'out'/'FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
print('Saved source snapshots and frozen spec before computation.')
