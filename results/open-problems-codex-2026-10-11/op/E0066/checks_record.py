import pathlib,json
p=pathlib.Path('.')
with p.joinpath('CLAIMS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps({'problem_id':'E0066','claim':'Two-type QBOs are exactly f(t)=1/2+a(t-1/2)+b(t-1/2)^2 with |a|+|b|/2<=1; except the identity and swap, every interior trajectory converges to the centre and boundary trajectories either do so or reach a fixed endpoint.','status':'proved_special_case','proof_location':'ATTEMPT.md Theorem 5','remaining_gap':'No gap for two types; does not classify higher dimensions.','checks':'Full polynomial/Bernstein proof; exact endpoint controls in experiments.py.'})+'\n')
rows=[json.loads(l) for l in p.joinpath('CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
for c in rows:
 if 'boundary' in c['claim'] or 'positive coordinates' in c['claim']:c['checks']='Complete nonnegative-coefficient/support proof; 60 LP controls for dimensions 2–6, worst face error 1.49e-14; numerical checks are not proofs.'
p.joinpath('CLAIMS.jsonl').write_text(''.join(json.dumps(c)+'\n' for c in rows),encoding='utf8')
with p.joinpath('ATTEMPT.md').open('a',encoding='utf8') as f:f.write('''

## Hostile-referee checks

1. Sorted-coordinate continuity and lower bounds: proved using finite maxima, not assumed differentiability of sorting.
2. A finite omega-set might conceivably have several cycles: ruled out by the unique-nearby-point argument and visits to every omega-point. Forward invariance alone would not suffice.
3. The first-order condition in Lemma 2 needs two-sided perturbations: used only in the relative interior of the appropriate invariant face, never directly at a boundary point of the original simplex.
4. Abel summation uses decreasing positive weights: its displayed identity and prefix bounds are explicit, including m=2. The final sign is (1-p)(y_1-y_2/2)<=0, with both factors nonnegative.
5. Majorisation cancellation with a common coordinate: proved through hinge sums and their top-k variational formula; it does not assume the common coordinate has a fixed rank.
6. Zero-output face invariance depends on nonnegative coefficients: all products x_i x_j in the support are strictly positive, so cancellation is impossible. This is where QSO positivity matters.
7. The phase permutations may disagree off the current support: the common vertex images define f on the union of supports. Surjectivity f(U)=U is proved using the full periodic cycle, not inferred from one phase.
8. Repeated positive coordinates invalidate distinct-coordinate rigidity: linear averaging within a repeated block gives nonidentity fixed points. The three-type bound handles these separately via at most three rearrangements; no analogous order bound is asserted in larger dimensions.
9. Boundary convergence: f(t)=2t(1-t) fixes t=0 and sends t=1 to 0, verified exactly with fractions. Identity and coordinate permutations also prevent any universal centre-attraction claim.

`experiments.py` builds the necessary coefficient inequalities sum_{i,j in I}p_{ij,k}<=|I| for all nonempty subsets, together with stochasticity, nonnegativity, and prescribed fixed points/cycles. It ran 60 random-objective LP checks of face rigidity, in m=2,...,6 and all support sizes, with distinct positive rational weights and zero remaining coordinates. All feasible optima agreed with the identity coefficients on the fixed face to 1.49e-14. These LP constraints are necessary for every QBO, so failure to find a contradiction supports the proof; floating-point LP is not used as a certificate.

A bounded exploratory search sampled 24 ordered cycles each of lengths five and six among the 12 rearrangements of (0.4,0.4,0.15,0.05) in four types. All 48 LPs were reported infeasible. This does not exhaust cycle orders, prove an order bound, or establish an open problem. Full results and statuses are in experiments.json. The job used small dense matrices (well below 1 GB) and took about 1.2 seconds once imports completed.

`PeriodBound.lean` formalises only the finite permutation-order step for Fin 2 and Fin 3. Compilation status is recorded separately in lean_check.log; no claim that the full analytic proof is formalised is made.
''')
print('Recorded theorem 5 and hostile checks')
