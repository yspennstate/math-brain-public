from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]; (R/'out').mkdir(exist_ok=True)
old=R.parent/'20261012T023941Z-fleet05-A083-formal-core/code/check_lean.py'
s=old.read_text(encoding='utf-8').replace('code/JSCoefficients.lean','code/CoherentTransport.lean')
s=s.replace("spec['helper_version']='check_lean.py JS v1'", "spec['helper_version']='coherent row check v1'")
s=s.replace("spec['family']='central-binomial even power-series coefficient products, all indices n>=1'", "spec['family']='actual coherent branch row; arbitrary rational mass variables with stated normalization and zero-row hypotheses'")
s=s.replace("spec['domain']='all natural n>=1; no finite cutoff'", "spec['domain']='all rational p0,p1,a,b with p0+p1=(a+b)/2; zero-row child mass zero'")
s=s.replace("spec['case_count']='six universal coefficient, factorial and finite partial-sum theorems'", "spec['case_count']='two universal mass-transport interfaces, including zero fallback'")
(R/'code/check_lean.py').write_text(s,encoding='utf-8')
paths=[Path(r'~\brain_workers\FEI100_20261011\BOARD.md'),Path(r'~\brain_workers\FEI100_20261011\claude\B17\STREAM_NOTES.md'),R.parents[1]/'STATUS.md',Path(r'~\brain_workers\FEI100_20261011\agents\A092\runs\20261013T222550Z-fleet05-A092-counterexample-referee\REPORT.md'),Path(r'~\brain_workers\FEI100_20261011\agents\A092\runs\20261013T222550Z-fleet05-A092-counterexample-referee\CLAIMS.json'),Path(r'~\brain_workers\FEI100_20261011\agents\A037\runs\20261011T220010Z-fleet05-A037-conditional-credit-ledger\NO_REUSE_CERTIFICATE.md'),Path(r'~\brain_workers\FEI100_20261011\agents\A037\runs\20261011T220010Z-fleet05-A037-conditional-credit-ledger\CLAIMS.json'),Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')]
rows=[]
for p in paths:
    b=p.read_bytes(); rows.append({'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
(R/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
print('Prepared formal runner and source receipts.')
