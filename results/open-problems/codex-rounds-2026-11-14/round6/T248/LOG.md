# T248 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
First clock reading: 15 November 2026, 11:31:19 +04 (07:31:19 UTC).

## Orientation and bounded literature check

All writes stay in this folder. The task-specific restriction overrides
the global brain, mesh and checklist write rituals. Read the startup
memory and compute state: warn/cpu_saturated, owner_away_open. No heavy
compute, subagents, git, external writes or background processes.

Read the original REPORT.md, LOG.md and SOLVED_ELSEWHERE.md; that folder
has no PROOF.md or research script. Read the round 3, 4 and 5 reports,
logs, proofs and verification scripts before selecting an extension.
Earlier folders are read-only. An initial file listing was too broad;
subsequent reads use exact paths and bounded output.

Web-search queries within the first five minutes:

- `"2610.41416" Chen Lyu Tracy Widom`
- `random features conjugate kernel Tracy Widom universality 2026`
- `"random features" "Tracy-Widom" 2026 edge universality`
- `"conjugate kernel" edge universality 2026 Tracy Widom`

Opened the full HTML of Guangchen Chen and Xing Lyu, *Tracy–Widom law
for sample covariance matrices under quadratic form concentration*,
arXiv:2610.41416v2, https://arxiv.org/html/2610.41416v2. Inspected
Assumptions 1.1–1.2, Theorem 1.3, Corollary 1.4 and Remark 1.5.
No newer full solution found. No SOLVED_ELSEWHERE.md is warranted.
This is a bounded search, not exhaustive coverage.

## Earlier result: independent audit in progress

Re-derived the conditional covariance from the Gaussian Hermite generating
function and checked the projection exactly: the q/d times all-ones matrix
vanishes on e-perp, whereas the scalar -q/d term remains. Thus
Tr(T-vI)=-e^T(Sigma-vI)e, with leading term -q(N-1)/d.
The finite-size edge normalization is also consistent with equality of
nonzero singular-value squares. No error found so far. A read-only rerun
of the predecessor script will complete this check before the extension
is selected.

## Earlier result holds; selected extension

Ran the round 5 script without writing bytecode or editing its folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r5/briefs/T248/verify_projection.py
```

Output:

```text
nice: setpriority: Operation not permitted
Effective nice value: 20
Exact rational P^2=P, trace, Frobenius identity, and spike removal:
  N=2,...,8 and q=0,2/7,3/4 all passed
Independent Fourier integrations at d=2: pair=0.023437500000, star=0.015625000000, cycle=0.007812500000
Cosine covariance: characteristic-function / Hermite max error 2.776e-17
  quadratic spike ratio q*alpha*sqrt(b)/v=0.460336797; projection identity independent of ratio
  quadratic spike ratio q*alpha*sqrt(b)/v=1.000000000; projection identity independent of ratio
  quadratic spike ratio q*alpha*sqrt(b)/v=7.365388754; projection identity independent of ratio
Nonzero-trace edge lemma: max solver disagreement 1.776e-15
  linear-mean / quadratic-variance expansion max relative error 3.415e-05
Projected N-1 normalization in both orientations: scale error 2.220e-16, center error 3.553e-15
Trace-defect sign: n*(shifted-reference)=-1.748455710; limit coefficient=-1.748528137
Interlacing failure example: lambda1(K)=104, lambda1(K_P)=4, lambda2(K)=3
  The projected top cannot be identified with the original second by interlacing.
PASS: algebra checks only; elapsed 0.033s; peak RSS 13.8 MiB
```

The launcher warning did not prevent the inherited effective nice value
20 from satisfying the script's >=15 guard. Independent proof audit:
the covariance decomposition and nonzero projected trace defect hold;
the exact scalar resolvent identity retains the linear mean defect and
the quadratic defect; the resulting edge displacement is O_p(N^-1);
the singular-value normalization agrees in both rectangular orientations.
The earlier theorem holds conditional on its explicitly cited universality
input. No error identified in that stated model.

Selected ONE extension, before proving it: replace the fixed Lipschitz
activation in the round 5 projected spherical theorem by any fixed
nonzero polynomial of degree k with a_0=a_1=0. This addresses its stated
non-Lipschitz exclusion. The covariance proof uses only Gaussian L2
coefficients and therefore survives; the missing part is a uniform
Hilbert–Schmidt quadratic-form moment bound for polynomial feature rows.
Use Gaussian Poincare plus finite-degree hypercontractivity, keeping
projection inside the calculation. Degree stays fixed as dimensions grow.
No eigenvalue-sticking claim for the unprojected spiked model is selected.

For the classical hypercontractivity input opened Yuu Hariya,
*A unification of the hypercontractivity and its exponential variant of
the Ornstein-Uhlenbeck semigroup*, arXiv:1707.03163v2,
https://arxiv.org/html/1707.03163. Equation (1.1) is the dimension-free
Ornstein–Uhlenbeck Lp-to-Lq contraction. Its finite-degree polynomial
consequence will be derived explicitly. Also opened Svante Janson,
*On hypercontractivity for multipliers on orthogonal polynomials*,
https://archive.ymsc.tsinghua.edu.cn/pacm_download/116/7386-11512_2006_Article_BF02384302.pdf,
whose introduction gives the same contraction and whose first section
defines the Hermite-degree multiplier. No result specific to that paper
is needed. This source lookup verifies a tool for the selected proof;
the initial five-minute search for a newer solution had already ended.

## Polynomial extension proved and independently checked

Wrote PROOF.md with the full projected polynomial theorem and its covariance,
edge and conditional-limit details. The new concentration lemma is stronger
than needed for this application: for any deterministic unit-column U of
bounded operator norm and any orthonormal Q, the projected feature vector
z=Q^T sigma(U^Tg) obeys

    ||z^T A z-Tr(AT)||_p
      <= 2 C_U ||sigma'(Z)||_4 3^(k/2) sqrt(||T||op) (p-1)^k ||A||F.

It only requires a_0=0, not a_1=0. It uses the projected covariance T
rather than the ambient covariance. Gaussian Poincare controls the variance
through the exact gradient 2U diag(sigma') QAz. Cauchy–Schwarz handles
derivative/feature dependence; hypercontractivity of the degree-k coordinates
of QAz controls their fourth moments. Hypercontractivity of the centered
degree-2k quadratic form then gives every fixed p. All constants are uniform
in dimension for a fixed polynomial. The covariance and edge estimates give
the same O_p(N^-1) random centering error as round 5.

Created verify_polynomial.py, using exact rational polynomial arithmetic,
Gaussian monomial moments and an independent conversion to product Hermite
coefficients. Dimensions are at most four and activation degree at most
five. A 60-second CPU limit, wall-time guard, one-thread environment and
effective-priority guard bound its run. Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B verify_polynomial.py
```

Complete output:

```text
nice: setpriority: Operation not permitted
Effective nice value: 20
  orthogonal: He2, v=2, q=2: passed
  orthogonal: He3, v=6, q=0: passed
  orthogonal: He4+He2/3, v=218/9, q=2/9: passed
  orthogonal: He5+He3/2+He2/5, v=6079/50, q=2/25: passed
  correlated: He2, v=2, q=2: passed
  correlated: He3, v=6, q=0: passed
  correlated: He4+He2/3, v=218/9, q=2/9: passed
  correlated: He5+He3/2+He2/5, v=6079/50, q=2/25: passed
  repeated_antipodal: He2, v=2, q=2: passed
  repeated_antipodal: He3, v=6, q=0: passed
  repeated_antipodal: He4+He2/3, v=218/9, q=2/9: passed
  repeated_antipodal: He5+He3/2+He2/5, v=6079/50, q=2/25: passed
Exact polynomial covariance / gradient / concentration chains: 36 cases
Monomial Gaussian moments and independent Hermite Parseval: exact agreement
Dependence failure: E[sigma'^2 L^2]=40; product of means=8
  Var(He2(Z)^2)=56 exceeds naive derivative bound 32
Hermite fourth moments: He2=60, He3=3348, He4=368064, two exact routes
PASS: exact algebra only; max degree 5; elapsed 0.842s; peak RSS 17.3 MiB
```

All 36 cases passed. Covariances were computed both by direct Gaussian
moments and Hermite correlation identities. Variances and gradient energies
were computed both by monomial integration and independent Hermite Parseval.
The exact gradient formula, each inequality in the variance bound, and the
projected trace identity passed for orthogonal, correlated, repeated and
antipodal directions and three choices of symmetric A, including an indefinite
one. These test the algebra and concentration argument, not a numerical TW
limit. Effective nice value 20 satisfies the author's limit despite the
launcher's failed attempt to adjust it again.

An actual failed shortcut: for sigma=He2 and L=He2, treating sigma' and L
as independent would replace E[sigma'^2 L^2]=40 by 8. It would even predict
Var(He2^2)<=32, whereas the exact variance is 56. The proof retains their
dependence and uses Cauchy–Schwarz instead. The fixed-degree qualification
is essential to this proof: its constants grow with k.

## Final mathematical audit and failure cases

Independently re-derived dimension-uniform concentration without Poincare
or hypercontractivity of the full quadratic form. Gaussian rotation gives

    ||F-EF||_p <= (pi/2)||Z||_p || |grad F| ||_p.

To check this, introduce independent g', integrate along
g_theta=g cos(theta)+g' sin(theta), and condition on g_theta; its tangent
is an independent standard Gaussian. Conditional Jensen and Minkowski give
the displayed inequality. For the gradient in Section 2, Minkowski in
Lp/2 followed by Holder yields

    || |grad F| ||_p^2
      <=4 C_U^2 sum_j ||sigma'(u_j^Tg) L_j||_p^2
      <=4 C_U^2 ||sigma'(Z)||_(2p)^2 (2p-1)^k sum_j E L_j^2
      <=4 C_U^2 ||sigma'(Z)||_(2p)^2 (2p-1)^k C_T ||A||F^2.

This independently gives the required fixed-p bound, with a different
finite constant. Polynomial degree remains fixed and every derivative
moment exists. No factor depending on N or d appears in either derivation.

Rechecked exponents: E Tr B^4=O(N^-1) divided by the fourth power of
N^-1/8 gives failure O(N^-1/2); E||R||F^2=O(N^-1) divided by N^-1/4
gives O(N^-3/4). The squared-defect cutoff N^1/6 fails with probability
O(N^-1/6). On the good event, the edge error is O(N^-5/6), so multiplication
by m^2/3 gives O(N^-1/6). The sharper stochastic edge error is O_p(N^-1).
The projected trace defect is retained, rather than set to zero.

The normalization also agrees with the singular-value reference center
v(sqrt(m)+sqrt(N-1))^2/N. Its difference from v(1+sqrt(m/N))^2 is O(N^-1).
The scale is the reciprocal of the standard rectangular singular-value
edge scale, agreeing with the predecessor's independently checked formulas.

Degenerate deterministic designs can have singular projected covariance;
the concentration lemma still holds, but the external universality theorem
is used only on the random-design event where T is uniformly positive.
Repeated/antipodal-direction algebra tests are not asserted to satisfy the
asymptotic random-design hypotheses. If k grows, hypercontractive constants
need not stay bounded; no such extension follows. Random column norms lose
conditional centering, and a linear component changes covariance structure.
Those branches are not covered. The aspect-one exclusion remains.

Read the identity and relationship memory cards read-only and consulted
the T248 entries in TOPICS. The two T248 cards' advertised paths were stale
(file-not-found); no shared brain files were changed or fabricated. The
earlier proofs and logs supply the actual area-specific prior results.

Wrote REPORT.md with the theorem, the concentration lemma, commands and
exact output summaries, failed independence shortcut, external inputs,
scope limits and the suggested unprojected subcritical polynomial target.
One combined log/proof update patch needed a retry due to patch formatting;
the failed patch made no partial file change. This was a document-tool
issue, not a mathematical failure.

Final read-only document audit passed: all four artifacts exist; REPORT.md
starts with the required verdict and explicitly leaves the full T248
problem unresolved; display equations and split environments are balanced;
no control characters are present; the new script parses successfully.
The check ran with the one-thread nice environment and required effective
priority at least 15. Read REPORT.md back in full. No additional numerical
run was needed after the exact checks, because only documents changed.
