Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — no authenticated applied-effort telemetry is exposed, so I do not claim a stronger setting.**

# NM13-13 — T04 cluster-aware random 3-SAT: direct product-measure Gaussian quadrature gives 4.388865

Date: 2026-09-20  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker root: `proofnet24/NM13-13/progress-3sat/`  
Parent: **T04 — classical iid random 3-SAT with independent fair signs on three distinct variables per clause**  
Status: **OPEN / PARTIAL; CANDIDATE_FULL for fixed-count upper endpoint 4.388865, pending later independent review**

Claim ID: `NM13-13-T04-PRODUCT-GAUSS9-4388865-UPPER-09`.

## 0. Source threshold before / after, separately from mechanism gain

The exact source model is `m=floor(alpha*n)` iid uniformly sampled proper signed 3-clauses, i.e. three distinct variables and independent fair literal signs.

A fresh bounded literature check on 2026-09-20 still supports the published explicit-decimal bracket

\[
\boxed{3.52\le \liminf c_n\le\limsup c_n\le4.4898}.
\]

Hajiaghayi--Sorkin prove satisfiability below `3.52`; Díaz--Kirousis--Mitsche--Pérez-Giménez prove asymptotic unsatisfiability at `4.4898`. Carenini's August 2026 theorem gives an `O(n/log n)` scaling window for every fixed `k>=3` but does not locate the `k=3` center. Large-`k` threshold theorems, Gibbs-uniqueness thresholds, and k-wise-independent clause variants are different statements. Thus the **published explicit source metric is unchanged**:

\[
\boxed{[3.52,4.4898]\to[3.52,4.4898]}.
\]

The preceding NM13-13 run established a project **CANDIDATE_FULL** endpoint `4.3888762` by four-node Gaussian quadrature on the one-variable tilted warning law. This run proves a strictly smaller project endpoint

\[
\boxed{4.3888762\to4.388865},
\]

so the internal candidate bracket moves

\[
\boxed{[3.52,4.3888762]\to[3.52,4.388865]},
\]

with width `0.8688762 -> 0.868865` and endpoint gain

\[
\boxed{1.12\times10^{-5}}.
\]

This is not claimed to improve any stronger symbolic interpolation/1RSB literature frontier; it is an independently reconstructed explicit finite-support project candidate pending review.

## 1. Short handoff and exact parked failures

The predecessor represented

\[
A(\alpha,\nu)=-\sum_{k\ge1}{\mu_k^2\over k}-2\alpha L,
\qquad \mu_k=\mathbb E Q^k,
\qquad 0\le Q<1,
\tag{1.1}
\]

and lower-bounded the omitted tail after `K=2300` by first applying Gaussian quadrature to the `Q^K`-tilted one-variable law and then squaring the resulting moment lower bounds. Four nodes gave the candidate endpoint `4.3888762`. The numerical obstruction was that the square of a one-dimensional lower envelope does not use the full moment structure of the squared sequence `mu_k^2`.

The following failures remain parked, not relabeled as progress:

- arbitrary rescue stars do not compose because two individually safe child flips can jointly falsify a third clause;
- anchored degree-one rescue matching gives a valid local penalty but has not been globally optimized in the Díaz type polytope;
- positive clause-local multiplicative second moments hit the identical-pair barrier `log(2)/log(5/4)=3.10628...`;
- quotienting sublinear solution balls yields only `exp(o(n))` savings;
- whole-component quotienting leaves an uncontrolled cross-component overlap moment;
- whitening/core counting lacks a uniform exponential cluster-multiplicity theorem;
- the q-binomial radius-two calculation only reached about `4.5923`;
- the equal-weight two-support hard-field survey stalls near `4.4178`.

Companion NM13-06 remains on the constructive side. Its latest report proves the fresh-copy two-menu collision branching parameter `C_2(alpha)=2u(alpha)S_*(alpha)^2` and finds its best-case surrogate transition near `3.5806856`; this identifies a global compatibility obstruction for that algorithm architecture and does not duplicate the present upper-bound interpolation route.

## 2. New product-measure tail lemma

Let `Q,Q'` be iid with the warning-law `rho`, and put

\[
X=QQ'.
\]

Then

\[
\mathbb E X^j=\mu_j^2.
\tag{2.1}
\]

Fix `K>=1` with `mu_K>0`, and tilt the law `sigma` of `X` by `X^K`:

\[
d\sigma_K(x)={x^K\over\mu_K^2}\,d\sigma(x).
\tag{2.2}
\]

Its moments are therefore

\[
s_j:=\mathbb E_{\sigma_K}X^j={\mu_{K+j}^2\over\mu_K^2}
=\left({\mu_{K+j}\over\mu_K}\right)^2.
\tag{2.3}
\]

The omitted tail in (1.1) is exactly

\[
\sum_{t\ge1}{\mu_{K+t}^2\over K+t}
=\mu_K^2\,\mathbb E_{\sigma_K} h_K(X),
\qquad
h_K(x)=\sum_{t\ge1}{x^t\over K+t}.
\tag{2.4}
\]

### Lemma 2.1 — direct product Gaussian lower bound

Let `x_1,...,x_r` and positive `w_1,...,w_r` be the `r`-node Gaussian quadrature rule for `sigma_K`, exact through degree `2r-1`. Then

\[
\boxed{
\mathbb E_{\sigma_K}h_K(X)
\ge \sum_{i=1}^r w_i h_K(x_i).
}
\tag{2.5}
\]

Hence

\[
\boxed{
A(\alpha,\nu)
\le A_K-\mu_K^2\sum_{i=1}^r w_i h_K(x_i),
}
\tag{2.6}
\]

where

\[
A_K=-\sum_{k=1}^K {\mu_k^2\over k}-2\alpha L.
\tag{2.7}
\]

### Proof

For finite `T`, let

\[
h_{K,T}(x)=\sum_{t=1}^T{x^t\over K+t}.
\]

For every `r`, its `2r`-th derivative is nonnegative on `[0,1]`: terms of degree `<2r` vanish and every surviving monomial has a nonnegative coefficient. Let `H_T` be the Hermite interpolant of degree at most `2r-1` matching value and first derivative at the `r` Gaussian nodes. The Hermite remainder is

\[
h_{K,T}(x)-H_T(x)
={h_{K,T}^{(2r)}(\xi_x)\over(2r)!}
\prod_{i=1}^r(x-x_i)^2\ge0.
\]

Integrating and using Gaussian exactness gives

\[
\mathbb E h_{K,T}(X)\ge\sum_i w_i h_{K,T}(x_i).
\]

Because every node lies strictly below `1`, the right side increases to `sum_i w_i h_K(x_i)`. The left side increases by monotone convergence to `E h_K(X)` (possibly `+infinity`, in which case the inequality is trivial). This proves (2.5), and (2.6) follows from (2.4). QED.

### Why this is materially different from the predecessor

The predecessor first lower-bounded each tilted moment `m_t=E_K Q^t` and then squared that lower bound. Here the square is absorbed exactly by the product variable `X=QQ'`, so the available moments are the exact sequence `s_t=m_t^2`. Gaussian quadrature is then applied to the **product law itself**. This uses the cross-moment geometry before any one-sided relaxation.

At `alpha=4.388865`, a high-precision diagnostic with the same survey and `K=2300` gives the predecessor four-node one-variable tail bound about

\[
4.9222460984761\times10^{-5},
\]

which leaves its corresponding `A` upper bound positive by about

\[
1.4672745\times10^{-6}.
\]

The new nine-node product-law bound is about

\[
5.0757242977747\times10^{-5},
\]

a tail gain of about

\[
\boxed{1.5347820\times10^{-6}},
\]

and this changes the sign. Those comparison decimals are diagnostic; the theorem claim below uses outward intervals.

## 3. Exact compound-Poisson specialization

Use the same exact symmetric five-support survey as the predecessor:

\[
R\in\left\{{33\over5000},{49\over625},{1\over2},{576\over625},{4967\over5000}\right\},
\]

with weights

\[
\left\{{139\over2500},{1831\over10000},{2613\over5000},{1831\over10000},{139\over2500}\right\}.
\tag{3.1}
\]

For one literal orientation, the warning count is Poisson with mean `lambda=3alpha/2`. With independent survey variables `R_1,R_2`, put `P=R_1R_2`, `Z=prod_j(1-P_j)`, and `Q=1-Z`. Then

\[
\mathbb E Z^j=
\exp\left\{\lambda\left(\mathbb E(1-R_1R_2)^j-1\right)\right\},
\tag{3.2}
\]

and binomial inversion gives

\[
\mu_k=\mathbb E(1-Z)^k
=\sum_{j=0}^k(-1)^j{k\choose j}\mathbb E Z^j.
\tag{3.3}
\]

The clause term remains

\[
L=\mathbb E\log(1-R_1R_2R_3).
\tag{3.4}
\]

Thus all moments `s_0,...,s_17` required by a nine-node Gaussian rule are explicit from `mu_K,...,mu_{K+17}`.

## 4. Rigorous nine-node certificate at alpha = 4.388865

Take

\[
\alpha_0={877773\over200000}=4.388865,
\qquad K=2300,
\qquad r=9.
\tag{4.1}
\]

The executed interval checker is

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T11-12-00Z__product_gauss9_4388865_interval.py`

created at commit `476584833fecdba0d46a3a3902b46e33b972c463`. Its archived actual stdout is

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T11-12-00Z__product_gauss9_4388865_interval.out`

created at commit `e77bd5f95849d2916b884a33fe92648fcde579cb`.

The checker uses exact rational inputs and 850-decimal-digit outward `mpmath.iv` arithmetic. It computes `mu_1,...,mu_2318`, forms the product-tilted moments (2.3), and conditions the moment problem with `Y=1000(1-X)`. Interval Gaussian elimination certifies all nine positive elimination pivots for the degree-nine orthogonality system. Nine disjoint sign-change brackets certify all nine roots, all inside `(0,1000)` in the `Y` coordinate, hence all product nodes `x_i=1-Y_i/1000` lie strictly in `(0,1)`. Lagrange-moment formulas certify every Gaussian weight positive, and degree `0,...,8` moment matching is interval-contained; orthogonality then gives exactness through degree 17.

The raw truncation remains positive:

\[
A_{2300}
=5.0689735487468019675868317941571\times10^{-5}>0.
\tag{4.2}
\]

The complete direct-product Gaussian tail is rigorously bounded below by

\[
\boxed{
\mu_K^2\sum_{i=1}^9w_i h_K(x_i)
\ge
5.0757242977747182632610902543446\times10^{-5}.
}
\tag{4.3}
\]

Therefore

\[
\boxed{
A(4.388865,\nu)
\le
-6.7507490279162956742584601875\times10^{-8}<0.
}
\tag{4.4}
\]

The archived output ends with

`CERTIFIED_STRUCTURAL_CHECKS = True`,

`CERTIFIED_A_UPPER_NEGATIVE = True`, and

`CERTIFIED_A_NEGATIVE = True because A <= A_K - complete_direct_product_Gauss9_tail_LB`.

This is a strict interval certificate; no omitted moment tail or floating extrapolation is used.

## 5. Transfer to classical iid proper random 3-SAT

The transfer theorem used in the preceding finite-support interpolation reports is unchanged; I restate the dependency rather than silently assuming it.

1. In the K-SAT specialization of the Franz--Leone / Panchenko--Talagrand diluted interpolation, the replica quantities entering the remainder are nonnegative and ordinary convexity of `x^3` on `[0,infinity)` gives the required remainder sign. Thus the K-SAT upper-bound interpolation applies at `p=3`; the even-`p` restriction in broader diluted-spin-glass statements is not a 3-SAT obstruction.
2. The survey (3.1) is finite and strictly inside `(0,1)`, while the compound-Poisson warning count has exponential moments. Consequently the hard-field `m downarrow 0` coefficient depends continuously on finite hard-field magnitude, inverse temperature and positive Parisi parameter. The strict margin in (4.4) therefore persists for some finite parameter triple, yielding a strictly negative rigorous interpolation upper bound.
3. The finite-temperature bound implies that the Poisson with-replacement K-SAT formula has minimum violated-clause energy at least `delta n` with high probability for some `delta>0`; the predecessor supplied the standard Poisson Poincare/concentration step converting the negative expected free-energy gap into this linear-energy statement.
4. Clauses with a repeated variable occur only `O_p(1)` times in the with-replacement interpolation model. Removing them changes minimum energy by only `O_p(1)`, so the proper-clause Poisson model remains linearly unsatisfiable.
5. If `M_n` is the proper Poisson clause count with mean `alpha_0 n`, then `M_n-floor(alpha_0n)=O_p(sqrt n)`. Add clauses when below the target count, and delete the excess when above. Adding clauses cannot restore satisfiability; deleting `D` clauses lowers minimum violated-clause energy by at most `D`. Since `D=o_p(n)`, the linear energy survives. Conditional on the final count, the retained/appended clauses are iid uniform proper signed 3-clauses. Hence the exact fixed-count source model at `floor(alpha_0 n)` is a.a.s. unsatisfiable.

Therefore this run establishes the project theorem candidate

\[
\boxed{
\Pr[\Phi_{n,\lfloor4.388865n\rfloor}\text{ is satisfiable}]\to0.
}
\tag{5.1}
\]

Per project policy this remains **CANDIDATE_FULL pending later independent review**, not external certification and not a proof that the limiting threshold exists.

## 6. Residual obstruction and next attack

The direct product-law reduction removes the main inefficiency of squaring one-dimensional moment lower bounds. At the certified point the margin is still only about `6.75e-8`, so blindly adding more quadrature nodes is likely to give only incremental movement unless the survey is reoptimized against the product-law objective.

The next attack should therefore optimize a rational symmetric five- or seven-support survey directly against

\[
A_K-\mu_K^2\sum_iw_i h_K(x_i),
\]

where the nodes and weights come from the product-tilted moment sequence `s_j=(mu_{K+j}/mu_K)^2`. A distinct fallback is an endpoint-aware Gauss--Radau / Markov--Stieltjes lower envelope on the product law if it provably dominates ordinary Gaussian quadrature. Do not return to rescue-star composition or another unchanged one-variable tail truncation.

## 7. Sources checked this run

- Hajiaghayi--Sorkin, *The Satisfiability Threshold of Random 3-SAT Is at Least 3.52*, arXiv:math/0310193.
- Díaz--Kirousis--Mitsche--Pérez-Giménez, *A new upper bound for 3-SAT*, FSTTCS 2008 / arXiv:0807.3600, explicit upper bound `4.4898`.
- Gaia Carenini, ECCC TR26-145, *The Scaling Window of Random k-SAT*, August 2026: `O(n/log n)` fixed-`k` scaling window, not a threshold-location theorem.
- Predecessor NM13-13 report `2026-09-20T09-53-37Z__t04_four_node_gaussian_tail_43888762.md` and latest NM13-06 report `2026-09-20T12-25-17__t04_two_menu_collision_branching.md`.

No historical or peer file was overwritten; POSTED exclusions were respected; no email, Drive, public posting, paid compute, access, permission, workflow, or schedule changes were made.
