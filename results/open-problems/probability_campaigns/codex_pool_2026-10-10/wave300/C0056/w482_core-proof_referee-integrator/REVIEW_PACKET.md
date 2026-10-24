# C0056 preliminary referee packet, 2026-10-10

Reviewer w482. Reviewed files: w480/STATEMENT_FOR_ADVERSARY.md and w480/CLAIMS.jsonl as seen this day; w481/INDEPENDENT_OBSTRUCTION.md and w481/CLAIMS.jsonl as seen this day. These are scoped verdicts, not a review of any later full proof packet.

| Item | Verdict | Reproduction | Remaining gap |
| --- | --- | --- | --- |
| w480 dated ranking/source-scope row C0056-W480-S0 | KEEP, scope only | Ranking row 543 says tier 5 and attempted_un; intake problems.jsonl:56 supplies extra GOE clause. Bourgade 2018 section 2.1 separates a.c. and GOE. | Update w480 SOURCE_STATUS.json's pending exact-statement field; current openness is UNKNOWN after the 2026 preprint claim. |
| w480 single-site entropy identity in STATEMENT_FOR_ADVERSARY.md | KEEP | Independent differentiation of I(c), detailed in ATTEMPT.md, gives exactly (2/lambda)log((1+sqrt(1+1/(pi*b)))/2). | The identity alone has no infinite-volume conclusion. |
| w480 conditional implication (LG) => a.c. spectrum | KEEP conditional, request explicit proof | Conditional entropy bound plus Dunford-Pettis and Poisson weak convergence prove a.s. a.c. for each site; ATTEMPT.md gives the quantifier argument. | (LG) itself remains unproved. No finite-box eta limit or first-moment averaging may replace it. |
| w481 diagonal counterexample w481.C0056.01 | KEEP as abstract counterexample | For D delta_x=X_x delta_x, mu_0=delta_X0; E Im G00<=pi/2 and int_R Im G00=pi. On X0 in [-1/2,1/2], int_{-1}^1 (Im G00)^p >=2^(1-p)eta^(1-p), and event probability is 1/2. | It has no hopping and does not refute weak-disorder Anderson. |

**Parent target:** no proof reviewed that establishes (LG) or GOE local statistics. The September 2026 public paper claims only the a.c. part in its abstract and requires independent proof review; its existence alone is not a KEEP on its theorem.

**Own proof review request:** w485 should independently check the Dunford-Pettis/Poisson implication and the no-singular-spectrum passage in ATTEMPT.md. Until then the new formulation is not an independently checked proof.

## Full packet verdicts after w480/ATTEMPT.md and w481/CAVITY_REDUCTION.md arrived

| Item | Verdict | Exact check and scope |
| --- | --- | --- |
| w480 L1 | KEEP | Substitution and differentiated integral reproduce the stated pi and lambda factors. For density bound R, the conditional bound is R/lambda times log(1+1/(pi b)); uniform law has R=1/2. |
| w480 L2 | KEEP conditional | Fatou produces an almost-sure sample-dependent bounded-entropy subsequence; splitting at K gives nu_n(O)<=K|O|+A/log(1+K). Portmanteau and outer regularity of Lebesgue measure give mu_x(N)=0 for every sample null set N; countable sites give operator purity. This proves only LG => a.c. |
| w480 L3 | KEEP | Finite spectral expansion gives b=eta(1+sum_j w_j/((e_j-E)^2+eta^2)). Away from finitely many e_j the normalized logarithm tends to one; the ratio is bounded by 2 for small eta, so dominated convergence yields |J|. The same bounded ratio permits expectation. |
| w480 C1 | KEEP | Scalar lambda V has sample atom delta_(lambda V) but bounded averaged density 1/(2 lambda); its entropy diverges. It is a counterexample to the averaged-density inference only. |
| w480 L4 | KEEP with stated cutoff | Resolvent identity and ||h||^2=6 give 6 lambda M/eta^2. Thus b_lambda>=b_free-6 lambda M/eta^2; b_free>=b_* gives positivity only when eta^2>=12 lambda M/b_*. No boundary conclusion at fixed lambda follows. |
| w480 L5 | KEEP | Positive free Fourier spectral mass in every nonempty J inside (-6,6), plus uniform ||lambda V||<=lambda M and polynomial approximation, preserves nonzero projection for sufficiently small lambda. |
| w480 LG | UNPROVED | It is a premise in L2. None of L1-L5, C1, or scalar checks establishes a uniform eta-down-to-zero bound in the infinite cavity. |
| w481 M reduction | KEEP conditional | Conditional second moment is <=pi/(4 lambda b); along the stated eta_n, Fatou and Riesz representation give L2 densities. On |a|<=lambda/2 and b<=lambda/2, direct integration over [a-b,a+b] gives the lower bound 1/(4 lambda b), locating a resonance bottleneck. M itself is unproved. |
| w481 nonzero-mass sentence | FIX support | The rare-box Weyl-sequence argument is named but not proved in its packet. w480 L5 supplies a direct uniform bounded-perturbation proof for intervals in the free band. |

### Brain draft audit

w480/bundle_001.json has seven concept-only entries and six relations. Each relation's two endpoints appear in that bundle and its rationale matches the endpoint statements. Content is KEEP as DRAFT with LG visibly unproved. **Placement FIX before ingestion:** every entry uses `probability.random-operators`, absent from the live store's `math:probability.*:<logical-name>` namespaces in a targeted read-only sqlite probe (command `python -X utf8 store_probe.py`; existing nearby namespaces include `probability.random-matrices` and `probability.open-problems`). The store already has the C0056 open-problem card; the draft should use an existing namespace or the integrator should explicitly approve a new namespace. I sent this scoped finding to w480. No ingestion or retrievability is claimed.
