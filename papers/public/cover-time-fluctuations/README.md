# Cover-time fluctuations beyond the maximal hitting-time scale

Yitzchak Shmalo
Einstein Institute of Mathematics, The Hebrew University of Jerusalem

Manuscript, exact-arithmetic checks and a Lean 4 development for the paper
answering Question 5.2 of Ding, Lee and Peres (Ann. of Math. 2012) in the
negative: the standard deviation of a graph cover time is not universally
bounded by the maximal hitting time, and the centered cover time need not have
an exponential tail on that scale, even when `t_cov / t_hit` tends to infinity.

The paper is [`paper/main.pdf`](paper/main.pdf); its LaTeX source is beside it
and is self-contained, with the bibliography inline.

## The results

An explicit unweighted clique-star graph `G_k` (a centre with `k` leaves and a
`k`-clique hanging off one edge) has

    t_hit(G_k) = 2k^2 + k + 1,
    E_x tau_cov = k^2 log k + (gamma + chi(x)) k^2 + o(k^2),
    Var_x(tau_cov) = 2k^4 log k + (2 gamma + pi^2/6 + chi(x)) k^4 + o(k^4),

so that `Var(tau_cov) ~ t_hit t_cov` and `(tau_cov - t_cov)/sqrt(t_hit t_cov)`
is asymptotically standard normal from every starting vertex, with a
Berry-Esseen bound of order `(log k)^{-1/2}` and Gaussian moderate deviations.

For a fixed connected core `F` with `k` pendant leaves at every vertex, the
cover time fluctuates on the scale `2qk sqrt(log k)` around `2qk log k`, and
the limit law is the maximum of a centred Gaussian vector with covariance twice
the pseudoinverse of the core Laplacian. For the two-vertex core, the double
star `D_k` (a tree of diameter three), the limit is half-normal and
`t_hit(D_k) = 6k + 3`. Diameter three is the smallest diameter at which a
family of trees can do this.

## What is proved where

| | |
|---|---|
| Paper | the theorems, including the probabilistic limit arguments |
| `checks/` | exact-arithmetic and numerical verification of the finite identities |
| `formal/` | the finite statements the proofs rest on, in Lean 4 against Mathlib |

The Lean development and the Python checks cover the finite content of the
argument by different means. Neither proves the limit theorems, and the paper
does not use either as a substitute for a proof.

## The exact checks

Run from `checks/` with Python 3 (`sympy`, `numpy` and `mpmath` are needed):

    python clique_star_exact.py
    python pgf_and_moments.py
    python decorated_cores.py
    python double_star_exact.py
    python spectral_and_operational.py

Their recorded output is in `checks/output/`. In outline:

* `clique_star_exact.py` solves the full first-step system on all `2k+1`
  vertices of `G_k` with rational arithmetic for `3 <= k <= 14` and reproduces
  the hitting table, `t_hit`, `E_x T_s` and `Var_x T_s`; a lumped absorbing
  chain on (position type, visited leaves, visited clique vertices) gives the
  exact mean and variance of the leaf-completion clock and of the cover time
  itself for `3 <= k <= 12` from all four start types, confirming (4.6)-(4.7)
  and the bracket (5.3); the lumping is checked against the full visited-set
  chain for `k <= 5`.
* `pgf_and_moments.py` recovers the excursion transform (3.2) from the
  random-sum structure and its moments by symbolic differentiation, the stage
  transform (4.1) and its moments, the coupon-clock formulas (4.5)-(4.10) for
  `r <= 6` with `k` symbolic, the polynomial identities of Section 3, and the
  constants of Sections 9.1 and 10.
* `decorated_cores.py` checks (9.1)-(9.3) and (9.11) on nine cores with equal
  decorations `k <= 4` and with every leaf vector in `{1,2,3}^q`, the Penrose
  equations for each pseudoinverse, and `t_hit(D_k) = 6k + 3` for `k <= 25`.
* `double_star_exact.py` computes the exact cover-time moments of `D_k` for
  `k <= 16` (checked against the full visited-set chain for `k <= 3`) and of
  stars for `k <= 30`, and tabulates the slow approach of the double-star
  moments to the leading terms (10.3)-(10.4) up to `k = 3000`.
* `spectral_and_operational.py` checks the perturbation identities of
  Lemma 8.1 numerically to 1e-16 on the same cores, the occupation covariance
  (8.1) by simulation, and samples the physical cover time of `D_k` exactly in
  law through the operational construction of Section 7.1; at `k = 1000` the
  sampler agrees with the exact lumped chain.

## The Lean development

`formal/CoverTime/CliqueStar.lean` and `formal/CoverTime/DecoratedCore.lean`
formalise the finite content of the argument, statement by statement in the
order of the paper: the first-step systems of the hitting table and their
solutions, the comparison polynomial, the composition of generating functions
in (3.2), the derivative of the transform at 1 and its second-order Taylor
data, the algebra behind the moment-generating bound, the stage transform and
its geometric parameters, the stage-by-stage sums giving (4.6)-(4.10), the
third-moment bounds of Lemma 4.2, the union bound of Lemma 5.1, the initial
variances (5.5), the scaling in the moderate-deviation proof, the
interpolation exponent (2.7), the second-order mean expansion (2.2) with an
explicit error term, the perturbation coefficients of Lemma 8.1 and the
explicit two-vertex eigenvalue, the threshold tails of Lemma 8.2, the leaf
elimination and Dirichlet linearity of Proposition 9.1, the hitting times on
the double star and on the decorated three-vertex path, the two-vertex
pseudoinverse, the two-vertex limit variable with its mean and variance, the
star bound of Proposition 10.2, the constants of Theorem 10.1, and the
variance identity of Proposition 11.1.

The development builds against Mathlib (Lean `v4.33.1`, the Mathlib commit
pinned in `formal/lake-manifest.json`):

    cd formal
    lake exe cache get
    lake build
    lake env lean CoverTime/AxiomCheck.lean    # prints the axioms each theorem uses

Every theorem depends only on `propext`, `Classical.choice` and `Quot.sound`.
There is no `sorry` and no added axiom. The build log and the axiom listing
are in `formal/output/`.

## Audit

`audit/AUDIT.md` records the line-by-line verification of the manuscript:
every proof re-derived, the checks above, and the changes made to the text.
