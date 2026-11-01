from pathlib import Path
import json,hashlib,sys
root=Path(__file__).parent
log=(root/'lean_check.log').read_text(encoding='utf-8')
completed='exit_code=' in log or 'Timeout after 3600' in log
if not completed and '--allow-unfinished' not in sys.argv:
 print('Lean result still pending; STATUS remains WORKING.',flush=True)
 raise SystemExit(2)
success='exit_code=0' in log and 'error' not in log.lower()
if not completed:
 lean_result='At closure no completed result was available from the corrected finite Lean run. It is unverified; live output remains in lean_check.log. The complete written counting proof and Python exact enumeration are the independent checks. No Lean certification is claimed.'
elif success:
 lean_result='Lean 4 kernel checks passed for all four finite parity lemmas (n=3,5), with decide +kernel and no sorry/native_decide. The analytic probability theorems are not formalized.'
else:
 lean_result='The finite Lean run did not complete successfully; its output is retained in lean_check.log and no Lean verification is claimed. The written counting proof and Python exact enumeration remain the independent checks.'
rows=[]
for line in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines():
 r=json.loads(line)
 if r['proof_location']=='ATTEMPT.md, Section 1':
  r['checks']='All proper subset sign marginals enumerated exactly for n=2,...,9 in checks.py; complete counting and Gaussian-density proof. '+lean_result
 if r['proof_location']=='ATTEMPT.md, Section 3':
  r['checks']+=' Exact endpoint representation checked on 142 univariate polynomials of degree at most 6, including every root, using rational arithmetic.'
 rows.append(r)
(root/'CLAIMS.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf-8')
attempt=root/'ATTEMPT.md'
with attempt.open('a',encoding='utf-8') as f:
 f.write('\n## Final verification record — 2026-10-12\n\n'+lean_result+'\n\n')
 f.write('The first Lean run failed to infer DecidablePred for named definitions; the corrected source uses reducible abbreviations. The failed output is preserved in lean_check_first_attempt.log. Only one Lean command ran at a time, from ~/lean_verify, with a 3600-second timeout.\n\n')
 f.write('All exact parity checks (n=2 through 9), all 142 rational endpoint representations, all quadrature and Monte Carlo assertions, the scalar-perturbation phase and normalization checks, and the required-file/JSON audit passed. Floating-point checks are evidence only; the probability claims rely on the full written proofs. The search limitations are recorded in LITERATURE.md.\n\n')
 f.write('Final verdict: PARTIAL. The completed work does not determine the optimal k(d,epsilon) for arbitrary degree-d polynomials. No SOLVED or SOLVED_IN_LITERATURE claim is made.\n')
status='''STATE: DONE
NEXT: Future work must close the dimension-free gap for arbitrary degree-d PTFs; lean_check.log retains any later finite-check result.
VERDICT: PARTIAL

2026-10-12: Confirmed the exact source on PDF page 9 and searched arXiv, Crossref, OpenAlex, Semantic Scholar and GitHub. OpenAlex and some Semantic Scholar requests were rate-limited; successful raw responses and every request are retained. No theorem answering the exact optimal-independence question was identified in the bounded audit.
2026-10-12: Reproved the exact Gaussian parity lower construction; proved its positive-integral linear-threshold discrepancy formula. Proved error <=32d/sqrt(k), for even k, for p(x)=q(a dot x), and an explicit degree-3 scalar-moment obstruction that is not an admissible vector counterexample. Also proved error <=B sqrt(d) k^(-1/4) for arbitrary degree-d PTFs under the additional bound ||r-1||_2<=B on the law's density. Full proofs and failure-point audits are in ATTEMPT.md and DENSITY_BOUND.md.
2026-10-12: Exact parity marginals through n=9, 142 rational polynomial endpoint checks, numerical integral/kernel checks and simulations passed. '''+lean_result+'''
2026-10-12: For density r<=M, improved the general-PTF bound to (M+1)d sqrt(log(k)/(2k))+sqrt(M-1)/k, and exhibited exact k-wise Gaussian laws with arbitrarily large density norms and singular laws. The added density condition is essential to this partial argument and does not follow from the original hypothesis.
2026-10-12: Stopped after completing the literature audit, independent proof review, checks and documentation. Remaining gap: the least k(d,epsilon) for ALL multivariate degree-d PTFs is not established; the special-case argument and independent-sum PRGs do not settle it. No novelty claim.
'''
(root/'STATUS.md').write_text(status,encoding='utf-8')
required=['STATUS.md','LITERATURE.md','ATTEMPT.md','DENSITY_BOUND.md','CLAIMS.jsonl','checks.json','scalar_barrier_checks.json','ParityCheck.lean','lean_check_first_attempt.log']
if completed:required.append('lean_check.log')
manifest={name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in required}
(root/'final_manifest.json').write_text(json.dumps({'date':'2026-10-12','verdict':'PARTIAL','lean_passed':success,'lean_completed_at_closure':completed,'live_lean_log_excluded_from_hashes':not completed,'sha256':manifest},indent=2),encoding='utf-8')
print(status,flush=True)
