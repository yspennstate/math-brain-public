from pathlib import Path
import json
root=Path.cwd()
t=Path('kalai.txt').read_text(encoding='utf8');i=t.index('3.3.4. A beautiful');j=t.index('3.4. Boolean',i)
with Path('LITERATURE.md').open('a',encoding='utf8') as f:f.write('\n## Source Section 3.3.4, PDF page 22 (exact extraction)\n\n```text\n'+t[i:j].strip()+'\n```\n\nSearch limitations: rate limits prevented OpenAlex verification, and only the returned Semantic Scholar citation page was searched. The source DOI used in the unsuccessful OpenAlex lookup was provisional, not verified; no source identity or citing coverage is inferred from that lookup. The targeted arXiv Grigorchuk/noise search returned zero entries (search words need not occur in metadata). The bounded search supports only "no exact solution found," not an exhaustive assertion of open status.\n')
rows=json.loads(Path('experiments.json').read_text());last=[x for x in rows if x['n']==80]
with Path('ATTEMPT.md').open('a',encoding='utf8') as f:
 f.write('''
## Computations and hostile-referee checks

`experiments.py` performs deterministic forward probability recursion, not Monte Carlo, with epsilon=1/4 and n up to 80. Groups use the semidirect-product rule (x,o)(t,s)=(x+o*t,o*s), o,s in {+1,-1}. Nonlazy dihedral generators are (0,-1),(1,-1); the four-generator aperiodic SRW adds (1,+1),(-1,+1). For the line, use (1,+1),(-1,+1). Finite cyclic tests reduce x modulo 5 or 6. Infinite-walk arrays use the full range [-80,80]; each step changes x by at most one, so no mass wraps before or at step 80 despite using array roll. Only orientation +1 is reached in the cyclic and line models. Pair-step weights are epsilon/d^2+(1-epsilon)1_{i=j}/d. State arrays are below 1 MB each and jobs finish in seconds once Python starts. Outputs are in `experiments.json`.

At n=80 the total variation distances were:
''')
 for x in last:f.write(f'- {x["model"]}: {x["tv"]:.12g}.\n')
 f.write('''
Normalization and joint symmetry were maintained within floating-point error; the endpoint matrices had minimum eigenvalues no smaller than about -3e-16. These are numerical consistency checks, not proofs of asymptotic results. The line and nonlazy dihedral outputs coincide, the four-generator dihedral distances decrease, and both cyclic models decay, including the periodic cycle of length 6. The four-generator example is covered by the 2025 virtually abelian theorem; it has a virtual real homomorphism and is outside the conjecture's sufficient-condition hypothesis.

`exact_checks.py` checks the conditional-mixture identity using Fraction arithmetic on S_3 at n=3, with the three transpositions (period two) and all five nonidentity elements (aperiodic). It verifies P=E(K tensor K), exact normalization, equality of marginals, and symmetry. The exact TV values are 9/32 and 1143/3125. These finite checks test the conditional-law construction and noncommutative product convention.

Potential failure points and their disposition:
1. Conditioning on the noisy endpoint is not conditioning on shared increments. The proof explicitly conditions on the mask plus retained values. The original and fresh values at marked sites remain independent. Checked exactly on two nonabelian finite examples.
2. Relative entropy cannot be recovered from small TV on growing alphabets. The displayed rare-diagonal example disproves this inference, with an exact information bound; `information_counterexample.json` records its values.
3. The endpoint matrix requires strictly positive p(g). It is defined only on the finite support of p, where divisions are legitimate. The claimed chi-squared criterion is sufficient only.
4. Positivity of the endpoint kernel uses a positive noise operator. This holds for independent refresh with epsilon in [0,1]; it is not asserted for arbitrary couplings. Numerical eigenvalue audits agree, and the finite scalar covariance algebra is formalized separately.
5. Finite-quotient support may be a proper subgroup of Q tensor Q. The even-word subgroup proof handles this; one must not invoke irreducibility on the full product for a bipartite walk. C6 and the transposition walk test this issue.
6. Uniformity on the residual parity coset must agree for the correlated and independent walks. Every coordinate has the same deterministic word parity at a fixed time; uniform convolution on the index-two subgroup gives the identical product-coset distribution in both cases.
7. The block minorization is uniform only within a fixed finite quotient. No exchange of quotient-size and time limits is used. This remains the main barrier to applying the finite proof to Grigorchuk.
8. A special case with virtually abelian groups is not the Liouville conjecture. The modern theorem has additional structure and aperiodicity assumptions, and its infinite groups do have virtual real homomorphisms.

Formal verification scope: `FiniteCovariance.lean` proves the two-point conditional covariance identity and its nonnegativity, together with the scalar entry identity behind the tensor difference bound. It imports only real-number basics and the ring tactic, uses no sorry or native_decide, and checks only these finite algebraic steps, not the full probability or finite-group arguments. The initial run failed because PowerShell wrote a UTF-8 BOM, blocking import parsing; the file was rewritten without BOM and checked again. Final success/failure is recorded in `lean_check.txt`.
''')
claims=[
('Shared-mask information I(X_n;C)->0 implies endpoint total-variation independence.','proved','ATTEMPT.md Section 1','No estimate proving this information limit from the conjectured hypotheses.','Full conditional-law proof; exact S3 rational checks.'),
('Total-variation convergence to the product of the marginals does not imply mutual information tends to zero on growing alphabets.','counterexample','ATTEMPT.md Section 1','This general distribution counterexample does not refute the group conjecture.','Exact rare-diagonal mixture; chain rule lower bound delta log M-h(delta).'),
('The normalized centered joint endpoint matrix is positive semidefinite; chi-squared divergence equals trace(B_n^2).','proved','ATTEMPT.md Section 2','No trace estimate under the target hypotheses; chi-squared decay is sufficient, not necessary.','Tensor noise operator diagonalization; numerical eigenvalue audit on five models.'),
('Every fixed finite quotient of a symmetric finitely supported group walk is endpoint noise sensitive, with an exponential block-minorization bound, including periodic walks.','proved_special_case','ATTEMPT.md Section 3','No uniform finite quotient bound as quotient size increases.','Full even-word subgroup/minorization proof; C5, C6 recursion; exact S3 checks.'),
('For epsilon=1/4, finite-time TV at n=80 is about .34144 on Z/nonlazy D_infinity and .02155 on four-generator aperiodic D_infinity.','numerical_evidence','experiments.json','Finite-time deterministic floating-point recursion does not prove asymptotic behavior.','experiments.py; probability mass and symmetry checked.'),
('Every Liouville Cayley SRW without a virtual real homomorphism is endpoint noise sensitive; in particular SRW on the first Grigorchuk group.','conjecture','ATTEMPT.md Remaining gap','Full target remains unproved and no counterexample found.','Kalai statement verified; bounded arXiv/Crossref/Semantic Scholar/GitHub search; OpenAlex rate-limited.')]
with Path('CLAIMS.jsonl').open('w',encoding='utf8') as f:
 for claim,status,loc,gap,checks in claims:f.write(json.dumps({'problem_id':'F0093','claim':claim,'status':status,'proof_location':loc,'remaining_gap':gap,'checks':checks},ensure_ascii=False)+'\n')
print('Recorded',len(claims),'claims and referee audit.')
