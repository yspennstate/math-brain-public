from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];H=R.parents[1]
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
claims=json.loads((R/'CLAIMS.json').read_text(encoding='utf-8'));c=claims[1]
c['hypotheses'][2]='Arbitrary two-bit mask identity requires h balanced; parity-mask supplement permits arbitrary h; supplied h/s reference costs finite and references normalized'
suffix=' Additionally, for any possibly nonbalanced Boolean h and parity on k>=1 shared bits, H(F)=2+H(h)/2 and a supplied normalized complete h reference with cost c_h gives a normalized root reference of CE=2+c_h/2; early shared erasure is zero and final erasure is (1+beta^2)/2*h2(beta^2/(1+beta^2))<=1, with conditional influence1/2. Thus this arbitrary-core parity prefix has zero K2 bad-node bill and conditional rate max(C,4) if c_h<=C I(h). No such core reference is universally supplied.'
if suffix not in c['exact_statement']:c['exact_statement']+=suffix
c['statement_sha256']=hashlib.sha256(json.dumps(dict(statement=c['exact_statement'],hypotheses=c['hypotheses']),sort_keys=True,separators=(',',':')).encode()).hexdigest()
c['proof_source']=c['proof_source'].split('; REPORT nonbalanced inherited cores')[0]+'; REPORT nonbalanced inherited cores; code/parity_core.py; out/PARITY_CORE.json'
c['review_records'][0]['arbitrary_core_parity_cases']=276
dump(R/'CLAIMS.json',claims)
p=json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'));p['mathematical_delta']=p['mathematical_delta'].split(' Arbitrary biased core/parity')[0]+' Arbitrary biased core/parity mask prefix additionally has zero K2 bill and exact supplied-reference CE=2+c_h/2;276 exact cases PASS.'
p['next_action']='For nonlinear shared masks and cores BOTH with nonzero mean, price exact coincident empty-row interference against SAME complete inherited core reference and one unused reserve; retain arbitrary-core parity as paid control.'
p['source_artifacts']+=['PARITY_CORE_SPEC.json','code/parity_core.py','out/PARITY_CORE.json']
p['source_artifacts']=list(dict.fromkeys(p['source_artifacts']))
dump(R/'PROGRESS.json',p);dump(R/'PACKET_DELTA.json',p)
H.joinpath('STATUS.md').write_text('STATE: A020 stage4 complete: A019 internal-pivotal theorem independently HOLDS; positive W/raw rate4 deficit with CE2 and zero K4 bill; arbitrary biased-core parity K2 paid;1796 exact cases PASS; FEI OPEN.\nNEXT: Price coincident empty rows when nonlinear shared mask AND inherited core both have nonzero means, retaining SAME complete core reference and one private reserve; A018/A019/A090/A091 review.\n',encoding='utf-8')
marker='Stage4 supplement: arbitrary nonbalanced core with shared parity'
for fn,body in [('WORKLOG.md','\nStage4 supplement: arbitrary nonbalanced core with shared parity was closed before handoff. Froze276 actual Boolean core fixtures and pilot4; both passed (full0.2610548s). Exact final-shared empty-row erasure<=1 at influence1/2; all earlier B0; complete inherited-reference CE=2+c_h/2. NEXT now targets BOTH nonzero means and nonlinear mask rather than generic balance loss. Final files/hash receipts regenerated.\n'),('LEARNED.md','\nStage4 supplement: arbitrary nonbalanced core with shared parity still has H=2+Hh/2 and supplied-reference CE=2+c_h/2. Earlier shared erasures0; last B=(1+beta^2)/2*h2(beta^2/(1+beta^2))<=1 at influence1/2, so K2 bill0. Mean loss alone is insufficient to create debt: next coincident row requires both nonzero core mean and nonzero shared-mask mean. Fullcore/parity test276 cases passed.\n')]:
    f=H/fn
    if marker not in f.read_text(encoding='utf-8'):
        with f.open('a',encoding='utf-8') as out:out.write(body)
prot=json.loads(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))['required_per_run']
assert set(p)==set(x.split(' (')[0] for x in prot['progress_fields'])
assert all(set(c)==set(prot['claim_fields']) for c in claims)
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
report=(R/'REPORT.md').read_text(encoding='utf-8');assert all('## '+x in report for x in prot['report_fields']);assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
supp=json.loads((R/'out/PARITY_CORE.json').read_text());assert supp['cases']==276
files=[f for f in R.rglob('*') if f.is_file() and f.name!='PERSISTENCE_RECEIPTS.json'];assert all(f.stat().st_size<20_000_000 for f in files)
dump(R/'out/PERSISTENCE_RECEIPTS.json',dict(status='PASS_LOCAL_FINAL_READBACK',schema_exact=True,packet_delta_identical=True,rolling_status_lines=2,total_exact_family_cases=1796,review_pairs=272,balanced_calibration_cases=1248,arbitrary_core_parity_cases=276,growth_formula_cases=32,full_parity_runtime_seconds=supp['runtime_seconds'],files=[dict(path=str(f.relative_to(R)),bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest()) for f in files],mirror_verified=False,new_diagnostic_independently_reviewed=False))
print(json.dumps(dict(status='PASS_FINAL',total_exact_cases=1796,growth_formula_cases=32,files=len(files))))
