# FOREST / account03 B03 — two-row CLC amplification on the minimal weighted 3-connected witness

**Run:** `20260922T073110Z-account03-B03-forest-r13`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Candidate:** `FOREST-CLC-TWOROW-AMPLIFICATION-v1`  
**Parent target:** **OPEN**  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact source scope and partner state consumed

The target remains the uniform law on **all unrooted forests** of every finite simple graph, including the empty forest, disconnected forests, and every forest size. For distinct edges `e,f`, the source inequality is

`Delta(e,f)=Z_e Z_f-Z Z_ef >= 0`.

No rooted, fixed-size, spanning-tree, or unrestricted weighted statement is substituted for that target.

The assigned partner is **account04/B01**. At run start I consumed its last complete result, `FOREST-MULTIGRAPH-SIMPSON-CLOSURE-v1` (`account04-b01-20260922T061100Z-forest-r12`, report blob `7273e128225a5cbbfa2fd3a70ad7d66f3581f85a`). During this invocation the partner finalized the stronger compatible result `FOREST-Q3C-ALL-EDGE-SIMPSON-v1` (`account04-b01-20260922T071144Z-forest-r13`, report blob `68499c69733b00e6396e4e36b615f6e0a1c0aa86`), so the final argument below uses that newer source-bound state.

The partner proves that any source failure yields a lexicographically minimal **positive-rational weighted, simple, 3-vertex-connected** counterexample `G` and a violating pair `e,f`. Put

`p_i=P(X_i=1)`, `q_i=1-p_i`, `C_ij=Cov(X_i,X_j)`,
`rho_ij=C_ij/sqrt(p_i q_i p_j q_j)`, `a=rho_ef>0`, `s=p_e+p_f`.

For every third edge `g`, exact deletion/contraction minimality gives the all-edge Simpson constraint

**(S)** `rho_eg rho_fg >= a > 0`,

and hence

**(N)** `rho_eg<0`, `rho_fg<0`.

The partner also source-corrects the complete-log-concavity input to the proved degree-`m` homogenization and obtains, with `m=|E|`, `K=|F|`, `mu=E K`, `delta=m-mu`, and `c_i=Cov(X_i,K)`,

**(C1)** `T_i + sum_(h!=i) q_h rho_ih^2 <= p_i`,

where `T_i=c_i^2/(delta p_i q_i)`. Its current scalar consequence is approximately `a<1/beta`, where `beta=m-|V|+1`.

This run directly strengthens that first remaining universal obstruction by using the **off-diagonal** information in the same CLC matrix, rather than another row estimate.

## 2. The normalized CLC covariance operator

For the degree-`m` homogeneous exponent vector

`U=(m-K,X_1,...,X_m)`,

let `D=diag(EU)` and `Sigma=Cov(U)`. The source-proved log-concavity statement used by the partner is

`D-Sigma >= 0`.

Since `Sigma>=0`, the normalized matrix

`N=D^(-1/2) Sigma D^(-1/2)`

satisfies `0<=N<=I`. Consequently

`M:=N-N^2 >= 0`.                                                              (1)

For edge coordinates,

`N_ii=q_i`,
`N_ij=rho_ij sqrt(q_i q_j)` for `i!=j`.

For the homogenizing coordinate `0`,

`N_0i=-c_i/sqrt(delta p_i)`.

Define the signed normalized rank covariances

`t_i=c_i/sqrt(delta p_i q_i)`, so `T_i=t_i^2`.

## 3. Exact 2-by-2 principal block on the violating pair

Scale the `{e,f}` principal block of `M` by `diag(q_e^(-1/2),q_f^(-1/2))`. Write it as

`[[r_e, m_ef],[m_ef,r_f]]`.

Direct multiplication of `N^2` gives

`r_e = p_e-T_e-q_f a^2-sum_g q_g rho_eg^2`,                       (2)

`r_f = p_f-T_f-q_e a^2-sum_g q_g rho_fg^2`,                       (3)

and

`m_ef = a(s-1)-sum_g q_g rho_eg rho_fg-t_e t_f`,                  (4)

where every sum is over `g notin {e,f}`.

Because the scaled block is positive semidefinite, its quadratic form on `(1,1)` is nonnegative:

`r_e+r_f+2m_ef >= 0`.                                              (5)

Substituting (2)--(4), the two rank-covariance terms combine exactly as

`T_e+T_f+2t_e t_f=(t_e+t_f)^2`.

Likewise each third edge contributes

`q_g (rho_eg+rho_fg)^2`.

Hence (5) is the exact inequality

`0 <= s-(t_e+t_f)^2-(2-s)a^2+2a(s-1)`
`     - sum_g q_g (rho_eg+rho_fg)^2`.                              (6)

Now (N) makes both third-edge correlations negative, while (S) gives their product at least `a`. Therefore

`(rho_eg+rho_fg)^2 >= 4 rho_eg rho_fg >= 4a`.                      (7)

Also

`sum_g q_g = (m-2)-(mu-p_e-p_f)=delta-2+s`.                        (8)

Dropping only the nonnegative square `(t_e+t_f)^2` from (6), then applying (7)--(8), yields the new universal constraint

**(C5)**

`boxed: (2-s)a^2 + 2a(2delta-3+s) <= s.`                           (9)

This uses the same source-proved CLC theorem as the partner, but retains the two-row/off-diagonal geometry that is lost when (C1) is applied separately to `e` and `f`.

## 4. Quantitative consequence on every hypothetical minimal core

For a connected graph of rank `R=|V|-1`, every forest has at most `R` edges, so `mu<=R` and therefore

`delta=m-mu >= m-R = beta`.

Thus (9) implies

`(2-s)a^2 + 2a(2beta-3+s) <= s`.                                  (10)

Because all activities are finite and positive, `0<s<2`. Dropping the positive quadratic term gives

`a <= s/[2(2beta-3+s)] < 1/(2beta-1)`.                             (11)

So the partner's `a<1/beta` localization improves to

**(C6)** `boxed: 0<a<1/(2beta-1).`                                  (12)

A simple 3-connected graph on `v>=4` vertices has minimum degree at least three, hence `m>=3v/2` and `beta=m-v+1>=v/2+1`. Consequently every hypothetical minimal weighted 3-connected witness also obeys

**(C7)** `boxed: a<1/(v+1).`                                        (13)

This is still not a contradiction: positive rational activities do not provide a source-valid denominator bound forcing a nonzero covariance to exceed `1/(v+1)`. But it is a genuine strengthening of the first remaining all-graphs obstruction and comes from a different mechanism than the partner's scalar row budget.

## 5. Exact structured stress test: K_{3,n}

To test whether a magnitude-only contradiction could plausibly finish (12), I independently computed the complete uniform-forest pair counts for `K_{3,n}`. For `n>=3`, `K_{3,n}` is simple and 3-connected. A five-state connectivity transfer on the three-vertex side gives

`Z = 4^(n-2)(3n^2+13n+16)`,
`Z_e = 4^(n-3)(3n^2+23n+38)`.

There are three pair orbits. Their exact Rayleigh gaps are

`Delta_same-left = 2*16^(n-3)(41n^2+181n+194)`,

`Delta_disjoint  = 2*16^(n-3)(17n^2+77n+66)`,

`Delta_same-right = 16^(n-3)(n-1)(9n^3+51n^2+104n+92)`.

All are nonnegative, and all nontrivial cases are strictly positive. Thus this family is not a counterexample.

More importantly, its normalized correlations include

`rho_same-left ~ -82/(27n^2)`,
`rho_disjoint  ~ -34/(27n^2)`,
`rho_same-right -> -1/3`.

For `e=A-r_1`, `f=A-r_2`, `g=B-r_3`, the exact ratio

`R_n = rho_disjoint^2/|rho_same-left|`

has denominator-minus-numerator

`1107 n^6+16941 n^5+102441 n^4+318247 n^3+542740 n^2+488300 n+182960>0`,

so `R_n<1` for every `n>=3`, and `R_n~578/(1107 n^2)`.

This stress result does **not** challenge (S), because the marked pair in `K_{3,n}` is negatively correlated. It does rule out a generic finishing move based on “3-connectivity bounds every nonzero correlation away from zero”: honest 3-connected forest correlations can be `Theta(v^-2)`. Any lower-bound contradiction to (12) must use the **positive-pair/minimality** structure, not core connectivity alone.

The standard-library checker brute-enumerated all forests for `1<=n<=5` and verified every pair-orbit formula. Repository readback identities: checker Git blob `5c0b81c8da1a64bf34b9d41bdc4daf72ff5f7f65`; exact-output Git blob `706cdfbd539938c6a0e0b62dfe82f33b3e978eab`.

## 6. First remaining implication after this run

The first unpaid step is now narrower:

> **FOREST-POSITIVE-PAIR-AMPLIFICATION-v1.** In the minimal positive-rational weighted simple 3-connected witness supplied by `FOREST-Q3C-ALL-EDGE-SIMPSON-v1`, exploit the sign/product system (S),(N) beyond the two-row CLC contraction (9), or prove that failure of the existing path-cut/Hall transport forces a forbidden positive covariance with a third edge.

A magnitude-only argument cannot simply assert a universal `Omega(1/v)` lower bound for arbitrary nonzero forest correlations; `K_{3,n}` supplies exact `Theta(v^-2)` negative correlations. The next proof must therefore use the exceptional simultaneous configuration forced by a **positive** minimal pair: every third edge is negative to both marked edges and every product dominates `a`.

A natural next mechanism is to retain a larger principal block of `M=N-N^2` (or an exact path-cut block) rather than reduce the CLC matrix to two scalar rows. Higher powers `N-N^k` are not automatically useful because uncontrolled signs among third-edge pairs can cancel, so any such extension must preserve the all-edge sign information explicitly.

## 7. Verification and failure record

- Parent FOREST remains **OPEN**; no source-valid counterexample was found.
- The latest partner's correction to the degree-`m` CLC homogenization is preserved; no unsupported rank-homogenized theorem is used.
- No fixed-graph weighted-Cocks shortcut is used.
- `K_{3,n}` retains the actual unrooted all-size law, including empty and disconnected forests.
- The earlier intermediate report in this run isolated a minimal-core bridge, but the partner completed that bridge during this invocation. This final report supersedes that intermediate blocker without overwriting it.
- Exact checker code and output are preserved in this run directory; the earlier local stdout SHA notation is not used as repository identity. Git blob identities above are authoritative for readback.

**Outcome: `ESSENTIAL_STEP_APPLIED`.** The all-edge Simpson/3-connected witness is strengthened from a one-row CLC budget to the two-row bound (9), yielding `a<1/(2beta-1)` and `a<1/(v+1)`, while the exact `K_{3,n}` family eliminates a generic correlation-magnitude closure. The parent conjecture is not claimed solved.

## 8. Provenance

- Current owner programme: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`, control revision `2026-09-22.2`.
- Assigned partner consumed: account04/B01 r12, then compatible finalized r13 `FOREST-Q3C-ALL-EDGE-SIMPSON-v1`, report blob `68499c69733b00e6396e4e36b615f6e0a1c0aa86`.
- CLC primary source identity checked during this run: Anari--Liu--Oveis Gharan--Vinzant, *Log-Concave Polynomials III*, arXiv:1811.01600; the search result confirms the paper's central complete-log-concavity theorem for the homogenized independent-set polynomial. The exact matrix specialization used here is inherited from the partner's source-checked derivation.
- No authenticated brain retrieval or receiver-context use occurred: `WITHOUT_VERIFIED_BRAIN`.

Scoped privacy/provenance review: this file contains only mathematics and sanitized logical source identifiers. No credentials, scheduler IDs, machine paths, private transcripts, email/Drive data, benchmark gold, public posting, paid model/API/Codex call, remote workflow, or cross-account native action occurred.
