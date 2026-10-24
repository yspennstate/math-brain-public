import pathlib,json
p=pathlib.Path(__file__).resolve().parent
claims=[
 dict(claim='Moment-separation criterion: for a truncated alpha-stable base plus any driftless perturbing Levy measure, uniform prefix-mass and tail-first-moment bounds on wide bands with summable reciprocal log endpoints imply (H).',status='proved_special_case',proof_location='SECOND_ATTEMPT.md, Theorem A',remaining_gap='Arbitrary measures need not have the required moment-separated cutoffs or a stable base.',checks='Entire B-window inclusion, finite-energy quantifier, stable-base regularity; invokes survey Theorem 2.11(i).'),
 dict(claim='For all 0<alpha<beta<1, arbitrary pulse measures of mass at most C r_n^(-beta) supported on [r_n,2r_n], with r_(n+1)<=r_n^K and K>beta(1-alpha)/(alpha(1-beta)), satisfy (H) when added to a truncated alpha-stable base.',status='proved_special_case',proof_location='SECOND_ATTEMPT.md, Theorem B',remaining_gap='Does not cover dense scales, absence of a stable base, or arbitrary type-(alpha,beta) densities.',checks='Prefix/tail geometric bounds, arbitrary singular pulse profiles, finite early-overlap correction; derived from Theorem A.'),
 dict(claim='At the critical K for full pulses, the fixed-power between-pulse implementation of the moment criterion has no nontrivial exponent interval.',status='proved',proof_location='SECOND_ATTEMPT.md, Boundary K=K_crit',remaining_gap='An obstruction to the stated method only, not a counterexample to (H).',checks='Necessary exponent inequalities p*alpha>=beta and q*(1-alpha)<=K*(1-beta).'),
 dict(claim='The atomic brain witness admits no cutoffs satisfying Theorem A for any fixed base index alpha in (0,1), even after adding that stable base.',status='proved',proof_location="SECOND_ATTEMPT.md, The brain's atomic example defeats Theorem A",remaining_gap='Does not decide (H) for the atomic witness or its stable regularization.',checks='Exact tail first moment 2^(-m), prefix mass at least 2^(-m)4^(m^2), incompatible quadratic and linear logarithmic endpoint bounds.'),
 dict(claim='The original positive example has mutually singular path laws on [0,1] to every truncated stable reference of fixed index gamma in (0,1) and amplitude c>0.',status='proved',proof_location='SECOND_ATTEMPT.md, Checking approach 2',remaining_gap='Singularity precludes this direct path-equivalence transfer but does not imply failure of (H).',checks='Independent Poisson jump-bin counts; exact affinity formula; full Borel-Cantelli separation argument; pulse bins for gamma<=alpha, gap bins for gamma>alpha.')
]
existing={json.loads(x)['claim'] for x in (p/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines()}
with (p/'CLAIMS.jsonl').open('a',encoding='utf8') as f:
 for c in claims:
  if c['claim'] not in existing: f.write(json.dumps({'problem_id':'E0025',**c},ensure_ascii=False)+'\n')
with (p/'ATTEMPT.md').open('a',encoding='utf8') as f:
 if '## Second attempt (12 October 2026)' not in (p/'ATTEMPT.md').read_text(encoding='utf8'):
  f.write('\n## Second attempt (12 October 2026)\n\nThe complete continuation is in SECOND_ATTEMPT.md. It records two new approaches, proves a moment-separation theorem and an arbitrary-pulse special case for every 0<alpha<beta<1, and proves obstructions to both this criterion and direct stable-reference path equivalence. The general question remains unresolved. The remaining gap and referee checklist appear at the end of that file.\n')
lit=(p/'LITERATURE.md').read_text(encoding='utf8')
if '## Second-attempt sources and brain query' not in lit:
 with (p/'LITERATURE.md').open('a',encoding='utf8') as f:
  f.write('\n## Second-attempt sources and brain query — 2026-10-12\n\nNo new claim of a solution in literature is made. Reused the verified Hu–Sun survey Theorem 2.11(i), Proposition 2.27, Theorem 2.30, and the Hawkes equivalence on p. 4. Lévy jump-bin Poisson counts are the standard Lévy–Itô construction (Bertoin, Lévy Processes, Cambridge University Press, 1996, survey reference [1]); the affinity and singularity argument is proved directly in SECOND_ATTEMPT.md rather than assumed from an unverified Kakutani/Sato reference.\n\nRead-only brain query: math_recall.py "Hunt hypothesis Hu Sun finite energy Clog subordinators good frequency bands arbitrary Levy density". It returned the old atomic witness and general energy cards; none supplies the missing cutoff theorem. No external web searches were run in this continuation.\n')
status=(p/'STATUS.md').read_text(encoding='utf8')
nextline=next(x for x in status.splitlines() if x.startswith('NEXT:'))
status=status.replace(nextline,'NEXT: Complete second-attempt checks, then close with the stronger partial result and precise general gap.')
status+='\n2026-10-12: Second attempt proved a moment-separation criterion and arbitrary pulse family for all alpha<beta, plus method obstructions for the atomic witness and all direct stable-reference path-law comparisons. See SECOND_ATTEMPT.md.\n'
(p/'STATUS.md').write_text(status,encoding='utf8')
print('Second-attempt proofs and claims saved; STATE remains WORKING.')
