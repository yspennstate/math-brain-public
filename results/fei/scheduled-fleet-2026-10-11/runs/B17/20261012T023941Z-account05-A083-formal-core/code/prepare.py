from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1]
(R/'out').mkdir(exist_ok=True)
old=R.parent/'20261011T222842Z-account05-A083-formal-core/code/check_lean.py'
s=old.read_text(encoding='utf-8')
s=s.replace("spec['helper_version']='check_lean.py v2'", "spec['helper_version']='check_lean.py JS v1'")
s=s.replace("spec['family']='all rational signed numerator intervals'", "spec['family']='central-binomial even power-series coefficient products, all indices n>=1'")
s=s.replace("spec['domain']='rational a,b,c,d,x,y; c>0, a<=x<=b, c<=y<=d'", "spec['domain']='all natural n>=1; no finite cutoff'\nspec['case_count']='six universal coefficient, factorial and finite partial-sum theorems'\nspec['arithmetic']='Lean core Nat and Rat proofs'")
s=s.replace('code/RationalDivision.lean','code/JSCoefficients.lean')
(R/'code/check_lean.py').write_text(s,encoding='utf-8')
paths=[Path(r'~\brain_workers\FEI100_20261011\BOARD.md'),Path(r'~\brain_workers\FEI100_20261011\claude\B17\STREAM_NOTES.md'),R.parents[1]/'STATUS.md',Path(r'~\brain_workers\FEI100_20261011\claude\B17\runs\20261011T224300Z-claude-B17-erasure-census-affine-bridge\CLAIMS.json'),Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')]
rows=[]
for p in paths:
    b=p.read_bytes(); rows.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(R/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
print('Prepared bounded compiler runner and source receipts.')
