import pathlib,json,hashlib
R=pathlib.Path(__file__).resolve().parent
p=R/'ATTEMPT.md';s=p.read_text(encoding='utf8')
s=s.replace('# D0051 attempt — checkpoint 2026-10-12','# D0051 attempt — completed partial investigation, 2026-10-12')
s=s.replace('A complete proof and kernel-checked algebra will be added below.','The complete connectedness proof is in §A1 and the passed kernel-checked algebra is in SpectrumAlgebra.lean / lean_check.txt.')
s=s.replace('The final Lean receipt will be recorded when available.','Final Lean run: exit code 0, 174.29 seconds; all four lemmas passed the kernel using only propext, Classical.choice, and Quot.sound. Receipt: lean_check.txt. No sorry, native_decide, or omnibus Mathlib import is present. The runner uses a 3600-second timeout, runs from ~/lean_verify, and keeps the .lean source in D0051. Formal coverage is strictly the four algebra lemmas, not the analytic proof.')
s+='\n## Final verdict\n\nPARTIAL. Subcritical upper bounds, Brownian-parameter collective negative-thickness concentration, endpoint dimensions zero in both metrics, and the negative-level determinism reduction are established as specified above. D0051 as posed for all xi and all alpha is not solved. No exact literature solution was located in the bounded search. All unresolved statements are explicit in §E; no uniqueness or fixed-level lower-bound conjecture is claimed as a theorem.\n'
p.write_text(s,encoding='utf8')
p=R/'CLAIMS.jsonl';rows=[json.loads(l) for l in p.read_text(encoding='utf8').splitlines()]
for x in rows:
 x['checks']=[c.replace('Brownian algebra independently checked with fractions; Lean verification pending','Brownian algebra checked with fractions and kernel-checked in SpectrumAlgebra.lean; lean_check.txt exit_code=0').replace('Lean algebra verification pending','Kernel-checked algebra in SpectrumAlgebra.lean, lean_check.txt exit_code=0') for c in x['checks']]
p.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows),encoding='utf8')
(R/'STATUS.md').write_text('STATE: DONE\nNEXT: Obtain a matching fixed-alpha geodesic occupation lower bound / Frostman construction; no such estimate is presently proved.\nVERDICT: PARTIAL\n2026-10-12: Verified source Problem 5.3, PDF p.24: limsup thick points, all xi>0.\n2026-10-12: Queried arXiv, OpenAlex and source citations, Crossref, Semantic Scholar, and GitHub; saved all 23 HTTP attempts. OpenAlex and Semantic Scholar rate-limited; no exact solution located.\n2026-10-12: Read-only brain, intake attempt, and neighbouring repository attempt consulted. Rejected unsupported KPZ independence and hitting-exponent heuristics.\n2026-10-12: Proved source-compatible subcritical threshold bound dim_E(P intersect {beta>=a})<=xi(Q-a), using GP Lemma 2.6 and a full parameter-interval covering proof.\n2026-10-12: At gamma=sqrt(8/3), points with beta<a carry full Euclidean geodesic dimension for every a>-1/sqrt(6), a<Q; this is collective, not a fixed-level result.\n2026-10-12: Proved subcritical alpha=+-2 intersections have zero dimension in both metrics; recorded combined upper bounds and negative-alpha uniformity deduction from arXiv:2608.22693.\n2026-10-12: Hostile referee audit completed; 10000 exact rational interval checks passed. Four Brownian algebra lemmas passed Lean (exit_code=0), no sorry/native_decide, 3600-second timeout, minimal imports.\n2026-10-12: Closed partial investigation. Full spectrum, maximizing thickness, critical/supercritical cases, and fixed-alpha lower bounds remain unresolved. Novelty not claimed.\n',encoding='utf8')
checks={}
checks['required_files_exist']=all((R/n).exists() for n in ['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl'])
checks['status_first_line']=(R/'STATUS.md').read_text(encoding='utf8').splitlines()[0]
checks['claim_count']=len(rows)
checks['claims_valid']=all(set(['problem_id','claim','status','proof_location','remaining_gap','checks'])<=set(x) and x['problem_id']=='D0051' for x in rows)
checks['lean_passed']=(R/'lean_check.txt').read_text(encoding='utf8').startswith('exit_code=0')
lean=(R/'SpectrumAlgebra.lean').read_text(encoding='utf8')
checks['lean_no_sorry_native_decide']=('sorry' not in lean and 'native_decide' not in lean)
checks['lean_no_omnibus_import']=('import Mathlib\n' not in lean)
checks['search_count']=len((R/'search_log.jsonl').read_text(encoding='utf8').splitlines())
checks['file_sha256']={n:hashlib.sha256((R/n).read_bytes()).hexdigest() for n in ['ATTEMPT.md','LITERATURE.md','CLAIMS.jsonl','SpectrumAlgebra.lean','lean_check.txt']}
assert checks['required_files_exist'] and checks['claims_valid'] and checks['lean_passed'] and checks['lean_no_sorry_native_decide']
(R/'validation.json').write_text(json.dumps(checks,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in checks.items() if k!='file_sha256'},indent=2))
