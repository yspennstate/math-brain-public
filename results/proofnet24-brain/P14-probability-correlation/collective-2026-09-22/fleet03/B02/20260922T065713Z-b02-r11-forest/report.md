# fleet03/B02 FOREST report — covariance-inverse squeeze in the irreducible 3-connected core

Status: `AUXILIARY_ONLY`; parent FOREST target remains `OPEN`.
Execution context: `WITHOUT_VERIFIED_BRAIN`.
Run: `20260922T065713Z-b02-r11-forest`.

Exact assignment: prove a useful minimal-counterexample reduction covering a genuinely unresolved three-connected obstruction, not merely another finite graph class.

Assigned partner: `fleet04/B03`.

## 1. Fresh state and named cross-account result consumed

Fresh owner control is revision `2026-09-22.2`, programme `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. The old installation/benchmark assignment is superseded.

I consumed the latest completed assigned-partner result:

`proofnet24/P14-probability-correlation/collective-2026-09-22/fleet04/B03/20260922T053904Z-B03-forest-r13/report.md`

blob `343a7f8f5aa2583e5fac80b1fb1f2d1ce2b8cbd5`, candidate `FOREST-3CONN-VARIANCE-SQUEEZE-v1`.

Its source-exact input is the following minimal-counterexample package. Let `(G,e,f)` be a lexicographically minimal simple counterexample, let `G0=G-{e,f}`, and let `H` be uniform on all forests of `G0`. Put

- `X=1{H+e is a forest}`,
- `Y=1{H+f is a forest}`,
- `S=1{H+e+f is a forest}`,
- `x=E X`, `y=E Y`, `r=E S`,
- `delta=r-xy>0`.

For every third edge `g in E(G0)`, put `T_g=1{g in H}`, `v_g=Var(T_g)`,
`a_g=-Cov(X,T_g)`, and `b_g=-Cov(Y,T_g)`. The partner result supplies

`a_g>0`, `b_g>0`, and `a_g b_g >= delta v_g`.                 (1.1)

It then obtains the rank bound
`delta <= sqrt(x(1-x)y(1-y))/rho`, where `rho=r(M(G0))`.

I also preserve my preceding B02 result: after the exact 2-sum closure calculation, any minimal loopless-multigraph counterexample can be reduced to a genuine 3-connected cycle-matroid obstruction. This run does not repeat the 2-sum or theta-gadget arguments.

## 2. New theorem: replace rank by the whole third-edge covariance geometry

Let `q=|E(G0)|=|E(G)|-2`. Write

`Sigma = Cov((T_g)_{g in E(G0)})`

and `D=diag(v_g)`.

### Lemma 2.1 — Sigma is positive definite

The uniform forest law gives positive probability to the empty forest and to every singleton forest. If `c^T T` were almost surely constant, the empty forest forces that constant to be zero, and the singleton `{g}` then forces `c_g=0` for every `g`. Hence `Sigma` is positive definite.

Minimality makes every distinct pair of third edges negatively correlated in `G0`, so

`Sigma_gh <= 0` for `g != h`.                                  (2.1)

Thus, after normalization,

`P := D^(-1/2) Sigma D^(-1/2) = I-N`

where `N` is symmetric, entrywise nonnegative, and has zero diagonal. Since `P` is positive definite, the Perron eigenvalue of `N` is strictly below one. Therefore

`P^(-1) = I + N + N^2 + ...`

entrywise, with absolute convergence. In particular `Sigma^(-1)` is entrywise nonnegative.

Define the exact covariance-complexity parameter

`kappa := sum_g v_g (Sigma^(-1))_gg = tr(P^(-1)).`             (2.2)

The Neumann series gives

`kappa >= q + tr(N^2)
       = q + sum_{g != h} Corr(T_g,T_h)^2
       >= q.`                                                   (2.3)

If at least one third-edge covariance is nonzero, the first inequality is strict.

### Theorem 2.2 — covariance-inverse deficit squeeze

Under the partner's minimal-counterexample hypotheses,

`delta <= sqrt(x(1-x)y(1-y)) / kappa
       <= 1/(4 kappa)
       <= 1/(4 q).`                                             (2.4)

**Proof.** Regard `a=(a_g)` and `b=(b_g)` as column vectors. From (1.1), entrywise nonnegativity of `Sigma^(-1)`, and (2.2),

`a^T Sigma^(-1) b
 >= sum_g a_g b_g (Sigma^(-1))_gg
 >= delta sum_g v_g (Sigma^(-1))_gg
 = delta kappa.`                                                (2.5)

The joint covariance matrix of `(X,T)` is positive semidefinite. Since `Sigma` is positive definite, its Schur complement gives

`a^T Sigma^(-1) a <= Var(X)=x(1-x).`                           (2.6)

Similarly,

`b^T Sigma^(-1) b <= Var(Y)=y(1-y).`                           (2.7)

Cauchy-Schwarz in the positive-definite `Sigma^(-1)` inner product now gives

`a^T Sigma^(-1) b
 <= sqrt[(a^T Sigma^(-1)a)(b^T Sigma^(-1)b)]
 <= sqrt[x(1-x)y(1-y)].`                                       (2.8)

Combine (2.5)-(2.8), then use `x(1-x),y(1-y)<=1/4` and (2.3). QED.

This strictly strengthens the partner's rank-only squeeze throughout the genuine 3-connected regime: `q=|E(G)|-2`, whereas `rho=|V(G)|-1`. For a simple 3-connected graph on `n>=4` vertices, minimum degree at least three gives `|E(G)|>=3n/2`, hence

`delta <= 1/[4(|E(G)|-2)] <= 1/[4(3n/2-2)].`                  (2.9)

The still sharper version in (2.4), with `kappa`, retains the actual normalized pairwise covariance geometry of all third edges rather than only their number.

## 3. Why this is a genuine mechanism change

The preceding B02 run used matroid 2-sums and two-terminal theta gadgets. The present argument uses a different mechanism: the inverse of the full third-edge covariance matrix and a Schur-complement projection of the two addability observables. It therefore does not rerun the same separator calculation.

The key gain is that all pointwise inequalities (1.1) are aggregated with the *inverse covariance metric*. Negative third-edge correlations make that inverse entrywise nonnegative, so every off-diagonal contribution helps rather than being discarded. The previous rank argument compressed all third-edge dependence into `Var(|H|)`; (2.4) sees the entire covariance matrix.

## 4. Direct attack on the next missing universal implication

The new bound is still not a contradiction. A positive target deficit is a rational count difference divided by the square of a forest count, so it may be much smaller than `1/q`; a bare integrality lower bound is exponentially too weak.

The first genuinely graph-specific debt is therefore sharper:

> **3CONN-COVARIANCE-GEOMETRY debt.** Use that `X` and `Y` are endpoint-addability events in an actual forest, not arbitrary Bernoulli observables, to force either a stronger lower bound on `kappa` or a lower bound on the positive deficit `delta` that contradicts (2.4).

One concrete direction is the unique-path representation. On `{X=0}`, the forest `H` contains the unique path joining the endpoints of `e`; similarly for `Y`. The coefficients `a_g=-Cov(X,T_g)` measure how strongly edge `g` participates in destroying addability. In a 3-connected graph there are multiple internally disjoint endpoint routes. A successful next lemma must turn that path/cut redundancy into a quantitative lower bound on `tr(P^(-1))`, or into enough mass in the `a_g,b_g` vectors to beat the Cauchy upper bound in (2.8). Merely replacing `q` by a slightly larger constant does not close the target.

I explicitly did **not** assume a universal nonnegative residual-covariance statement for the linear regressions of `X` and `Y`; such a statement is not supplied by the target hypotheses and would simply replace the debt by an unsupported condition.

## 5. Exact finite regression of the matrix facts

`covariance_inverse_check.py` beside this report independently enumerates every nonempty labelled simple graph on 2,3,4,5 vertices and all of its forests. It forms the exact integer covariance-numerator matrix, inverts it over `fractions.Fraction`, and checks:

1. all off-diagonal third-edge covariances are nonpositive on this finite baseline;
2. the covariance inverse is entrywise nonnegative;
3. `v_g (Sigma^(-1))_gg >= 1` after common scalar cancellation;
4. `kappa>=q`, with strict inequality for every cyclic graph tested.

Captured output:

    graphs_checked=1094
    cyclic_graphs_checked=760
    violations=0
    minimum_cyclic_kappa_minus_m=10/403
    minimum_cyclic_meta_n_m_rank_kappa=(5, 5, 4, 2025/403)
    STATUS=PASS

Checker SHA-256:
`d9eb217af9aa36af236b629989e40a7aa068771e2b50766ab22ea5fe2dd2064f`.

Output SHA-256:
`ddfbafca701b747e3786835c022a8f90c60e427bae7f3f9fc0ba23886b13c91d`.

The enumeration is regression evidence only. The all-graph matrix statements in Section 2 are proved symbolically.

## 6. Status and next recipient

Outcome: `AUXILIARY_ONLY`.

What changed:
- partner rank squeeze `rho` is strengthened to the exact covariance-complexity `kappa`;
- universally `kappa>=q=|E(G)|-2`, so every irreducible 3-connected counterexample would satisfy the stronger edge-count deficit bound (2.4);
- existing negative covariance among third edges strengthens the denominator further by the explicit `sum Corr^2` term.

What remains:
- no contradiction with `delta>0` has yet been derived;
- the parent FOREST conjecture is not promoted;
- the complete-graph/Cocks/minor route remains a separate candidate and is not certified by this auxiliary reduction.

Next recipients: assigned partner `fleet04/B03` and FOREST lead `fleet01/B01`. The most useful follow-up is to combine their endpoint-connectivity/path structure with (2.2)-(2.5), not to repeat a finite census.

No authenticated brain retrieval/context activation occurred. No installation, benchmark, scheduler, email, Drive, workflow, paid-model/API, credential, or cross-account native action was used.
