from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent

for name in ['first_passage_checks.json','first_hit_checks.json','logarithmic_lower_checks.json']:
    assert json.loads(ROOT.joinpath(name).read_text(encoding='utf-8'))['all_assertions_passed'],name
assert 'Exit code: 0' in ROOT.joinpath('first_passage_lean_check.txt').read_text(encoding='utf-8')
assert len(json.loads(ROOT.joinpath('first_passage_q_simulation.json').read_text())['rows'])==7

path=ROOT/'CLAIMS.jsonl'
old=[json.loads(x) for x in path.read_text(encoding='utf-8').splitlines()]
for x in old:
    if 'E T(FP(n,h)) <=' in x['claim']:
        x['remaining_gap']='This upper bound is strengthened by the new first-hit identity and matching n log n theorem; the unrestricted family problem remains open in this record.'
        x['checks']='1013 exact overlap cases, densities and second moments through n=9, 16 exact waiting means; Lean kernel checks passed.'
    if 'polynomial exponent is exactly 1' in x['claim']:
        x['remaining_gap']='The slowly varying order is now proved logarithmic in SECOND_ATTEMPT.md Section 7; an exact constant and the general collection question remain undetermined.'

new=[
 ('For first-passage words, p E T = E[C(W)] under the first-hit word law, with C(w)=1+sum_(1<=l<n) g(l,-S_l(w)).',
  'proved_special_case','SECOND_ATTEMPT.md Section 5','Identity does not replace first-hit weights by uniform weights.',
  '20 exact first-hit distributions from an independent absorbing prefix automaton; identity and density bounds passed.'),
 ('For any collection A, its first-hit word law is dominated by p E T times the uniform law. If U(C_A<L)<=r, then E T>=L/[p(1+Lr)].',
  'proved','SECOND_ATTEMPT.md Sections 7.1 and 8','Requires estimating the uniform lower tail of overlap for a specified family.',
  '20 exact first-hit domination checks; Lean kernel verification of the self-consistent lower-bound algebra.'),
 ('For an unconditioned fair walk and B_m=sum_(l<=m)g(l,-S_l), E B_m>=c log m and Var(B_m)<=K(1+log m) for absolute constants and all sufficiently large m.',
  'proved','SECOND_ATTEMPT.md Section 7.2','Exact asymptotic moment constants are not asserted.',
  '512 exact smoothing tests, 120 exact covariance tests, exact rational moments through m=64 and deterministic moment recursion through m=8192.'),
 ('For every fixed lambda<0, the first-passage family FP_(lambda,n) has E T=Theta_lambda(n log n).',
  'proved_special_case','SECOND_ATTEMPT.md Sections 1-7','An exact leading constant is not proved; arbitrary collections in Question 1.7 are not classified.',
  'Full ballot, first-hit identity, domination, covariance smoothing, Chebyshev and prefix-conditioning proofs. 146 exact prefix likelihood checks; all dependency checks passed; partial Lean algebra checks exit 0.'),
 ('Along n=h^2, the legal square-root first-passage word has C(w)~sqrt(2/pi) exp(-1/2) log n; hence maximum conditional overlap is Theta(log n).',
  'proved_special_case','SECOND_ATTEMPT.md Section 6','Worst-case growth alone does not determine first-hit mean growth.',
  'Legal path increments and endpoint checked through n=16384; Stirling argument gives the asymptotic proof.'),
 ('The downward-then-zigzag word is not a maximum of conditional-overlap/column sum for FP(64,8): the square-root word exceeds it by 464602032247/4398046511104.',
  'counterexample','SECOND_ATTEMPT.md Section 9 additional audit observation; exact_column_counterexample.json',
  'This concerns that explicit extremal-word comparison, not a counterexample to Question 1.7.',
  'Both literal words checked legal; comparison made in exact rational arithmetic.'),
 ('Seeded finite simulations estimate the enlarged-window first-passage occurrence probability at 0.2822 for n=64 and 0.2041 for n=4096, with intermediate values recorded.',
  'numerical_evidence','first_passage_q_simulation.json','Finite simulations do not identify an asymptotic leading constant.',
  '16384 independent blocks per n, 7 scales, direct small-word checks of filter alignment and strictness; large probabilities formed as exact ratios before float conversion.'),
]
with path.open('w',encoding='utf-8') as f:
    for x in old: f.write(json.dumps(x,ensure_ascii=False)+'\n')
    for claim,status,loc,gap,checks in new:
        f.write(json.dumps({'problem_id':'E0081','claim':claim,'status':status,'proof_location':loc,'remaining_gap':gap,'checks':checks},ensure_ascii=False)+'\n')

with ROOT.joinpath('LITERATURE.md').open('a',encoding='utf-8') as f:
    f.write('''

## Second attempt, 12 October 2026

The gap itself was queried in the read-only math store twice: “ballot theorem first passage probability Pitman Tang waiting time exponent gap” and “Bertrand ballot theorem simple symmetric random walk hitting time binomial”. The first returned first-passage percolation cards; the second returned optional-stopping/general random-walk cards. No directly applicable ballot or waiting-time solution was found. None of these unrelated cards is used as a theorem in the proof.

Re-read source.txt around (2.20)–(2.23) and the first-passage simulation discussion, then checked its intended extremal-word comparison independently. The new proof does not rely on that comparison. SECOND_ATTEMPT.md records a finite rational counterexample to the downward-then-zigzag word being a maximum.

Two additional network searches were run after obtaining the new first-passage order theorem. The arXiv author/passage search returned Pitman and Tang's *Tree formulas, mean first passage times and Kemeny's constant of a Markov chain*, arXiv:1603.09017v3, DOI 10.3150/16-bej916 (Bernoulli, 2018), whose abstract concerns finite-state Markov chain tree formulas rather than scale-indexed first-passage word scanning. Crossref returned that paper and unrelated physical/inventory first-passage papers. No theorem resolving the full Question 1.7 was verified. These two searches are additional bounded checks, not a claim of exhaustive literature coverage or novelty for the theorem proved here.

The new result is an author-proved special case: E T(FP_(lambda,n))=Theta_lambda(n log n), with full proof and checks in SECOND_ATTEMPT.md. It is not being marked SOLVED_IN_LITERATURE.

Additional exact queries:
''')
    for line in ROOT.joinpath('search_log.jsonl').read_text(encoding='utf-8').splitlines():
        x=json.loads(line)
        if x['service'].startswith('second_'):
            f.write(f"- **{x['service']}** — `{x['query_url']}` — {x.get('status',x.get('error'))}; date {x['date']}.\n")

path=ROOT/'STATUS.md'
text=path.read_text(encoding='utf-8'); lines=text.splitlines()
lines[0]='STATE: DONE'
lines[1]='NEXT: Determine the exact first-passage leading constant or apply the uniform-overlap lower-tail criterion to another specified natural family.'
lines[2]='VERDICT: PARTIAL'
path.write_text('\n'.join(lines)+'''

2026-10-12 second attempt completed: Recorded two new approaches (ballot/overlap concentration and descending-ladder renewal intersections), and pursued the former. Proved E T(FP_(lambda,n))=Theta_lambda(n log n) for every fixed lambda<0, closing the source's first-passage order gap. Exact leading constant remains unproved.
2026-10-12 second attempt audit: First-hit domination plus an exact overlap identity, unconditioned logarithmic mean/variance estimates, and bounded prefix likelihood ratios give the matching lower bound. 1013 overlap checks, 20 exact first-hit laws, 512 smoothing checks, 120 covariance checks, 146 prefix likelihood checks, exact and numeric moment recursions, and Lean kernel checks passed. Full proof: SECOND_ATTEMPT.md.
2026-10-12 final scope: General E0081 remains PARTIAL because arbitrary natural scale-indexed collections are not classified. The first-passage order gap previously listed in ATTEMPT.md is now closed. New general result: a uniform-overlap lower-tail criterion controlling the first-hit expected overlap without assuming uniform race probabilities. All results remain within E0081; no literature-solution or novelty claim made.
''',encoding='utf-8')
print('Finalized STATE: DONE, VERDICT: PARTIAL; proved first-passage order Theta_lambda(n log n).')
print('Claim records:',len(old)+len(new))
