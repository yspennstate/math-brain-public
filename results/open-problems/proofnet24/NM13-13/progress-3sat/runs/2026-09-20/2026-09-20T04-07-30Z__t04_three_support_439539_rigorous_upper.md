Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but this runtime exposes no authenticated applied-reasoning telemetry, so I do not claim GPT-6 maximum.**

# NM13-13 — T04 cluster-aware 3-SAT: a three-support 1RSB trial gives an explicit 4.39539 upper bound

Date: 2026-09-20  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker root: `proofnet24/NM13-13/progress-3sat/`  
Parent: **T04 — classical iid random 3-SAT with uniform independent signs on three distinct variables**  
Status: **OPEN / PARTIAL; theorem below is CANDIDATE_FULL for the stated explicit upper bound, pending later independent review**

## 0. Source-threshold status before / after

Two different notions must remain separate.

### Literature-supported symbolic frontier

For fixed `k=3`, existence of a single limiting satisfiability threshold is still open. Hajiaghayi--Sorkin prove satisfiability w.h.p. below density `3.52`. Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis (CPC 2026) state that for small fixed `k` a uniform threshold remains open and that the interpolation method yields a rigorous upper variational functional matching the 1RSB prediction. Their table reports the physics value

\[
d_{\rm sat}(3)\approx 12.801,
\qquad \alpha\approx 4.267,
\]

under the convention `d=3 alpha`. This worker has still not reconstructed a rigorous interval evaluation of the full `U_{1RSB}(3)` infimum at that decimal. Therefore the strongest theorem-form source status I can support is still

\[
3.52\le \liminf c_n\le \limsup c_n\le U_{1\mathrm{RSB}}(3),
\]

with the published physics numerical value near `4.267`. **That literature frontier does not move in this run.**

### Independently reconstructed explicit-decimal upper bound in this track

The previous NM13-13 run gave a complete candidate proof at fixed-count density `4.418`, based on a two-support hard-field survey certificate at Poisson density `4.4178`. This run replaces that trial by a richer three-support symmetric survey and also removes the predecessor's unnecessary positive-density de-Poissonization slack.

The new candidate theorem is

\[
\boxed{
\Pr\!\left[\Phi_{n,\lfloor 4.39539 n\rfloor}\text{ is satisfiable}\right]\to0.
}
\tag{0.1}
\]

Thus the independently reconstructed explicit-decimal bracket moves

\[
\boxed{[3.52,4.418]\longrightarrow[3.52,4.39539]},
\]

and its width moves

\[
0.898\longrightarrow0.87539.
\]

The explicit upper endpoint improves by

\[
\boxed{0.02261}.
\]

Claim ID: `NM13-13-T04-THREE-SUPPORT-439539-UPPER-02`.

This is a genuine source-level movement for the exact iid proper fixed-count model, subject to later independent review of the complete argument below. It is **not** claimed to improve the stronger symbolic `U_{1RSB}(3)` literature frontier.

## 1. Short predecessor handoff and exact prior failures

The preceding run established the rigorous odd-`p=3` K-SAT interpolation transfer and an explicit two-support trial. For

\[
R\in\{0.22,0.78\}\quad\text{equiprobably}
\]

it certified a negative hard-field coefficient at Poisson density `4.4178`, then used a `0.0002` positive density slack to conclude a fixed-count `4.418` upper endpoint. The finite-temperature interpolation, concentration and improper-clause deletion parts of that proof survive unchanged.

The following older failures remain preserved and are not silently recycled as progress:

1. arbitrary rescue **stars** do not compose: two children that are individually rescued by the same root can jointly falsify another clause;
2. anchored degree-one rescue matching is valid and gives an exact hypergeometric/Maclaurin exponent penalty, but the full Díaz polytope was never globally reoptimized with that penalty;
3. positive clause-local multiplicative second-moment weights hit the identical-pair barrier
   \[
   \alpha\le \frac{\log2}{\log(5/4)}=3.1062837\ldots;
   \]
4. quotienting satisfying assignments by solution-graph balls of radius `o(n/log n)` changes counts only by `exp(o(n))`;
5. full-component quotienting leaves an unpaid cross-component overlap moment;
6. whitening/core history counting lacks a proved uniform exponential cluster-multiplicity lower bound;
7. the exact q-binomial radius-two calculation reaches only about `4.5923`, so it is weaker than the historical explicit upper bound;
8. the inherited equal-weight two-support hard-field family crosses only near `4.4178` and cannot reach the density certified here.

The companion NM13-06 is complementary rather than duplicated: its latest constructive report proves that the static blocked-majority hypergraph remains subcritical even at `4.4898`, and isolates **dynamic promotion** of previously zero-break variables as the constructive obstruction. This report stays entirely on the cluster-aware variational upper-bound side.

## 2. The interpolation input retained from the predecessor

Panchenko--Talagrand's diluted K-SAT interpolation gives, for every finite inverse temperature `beta`, Parisi parameter `0<m<1`, and admissible one-step random measure `zeta`,

\[
F_N(\beta)=\frac1N\mathbb E\log Z_N(\beta)
\le \Phi_1(\zeta,m).
\tag{2.1}
\]

Although their umbrella presentation also treats even-`p` diluted spin glasses, the K-SAT specialization works for all integers `p>=2`. The remainder polynomial has the form

\[
R_p(x,y)=x^p-pxy^{p-1}+(p-1)y^p,
\]

and in K-SAT the relevant replica averages are nonnegative. Convexity of `t^p` on `[0,\infty)` gives `R_p(x,y)>=0`. Panchenko later states explicitly that the Franz--Leone upper-bound argument works for every `p` in K-SAT.

Therefore the one-step interpolation theorem used in the predecessor is available at `p=3` and need not be reproved here.

## 3. New mechanism: a three-support symmetric hard-field survey

Fix

\[
\alpha_0=\frac{439539}{100000}=4.39539,
\tag{3.1}
\]

and let the outer survey variable `R` take the three values

\[
\boxed{
R\in\left\{\frac{47}{800},\frac12,\frac{753}{800}\right\}
}
\tag{3.2}
\]

with probabilities

\[
\boxed{
\left(\frac{4179}{20000},\frac{5821}{10000},\frac{4179}{20000}\right).
}
\tag{3.3}
\]

The law is symmetric under `R -> 1-R`, so it preserves the fair-sign gauge symmetry. Conditional on `R`, the inner hard-field law assigns probability `R` to the literal-unsatisfying spin and `1-R` to the satisfying spin.

For one incoming clause warning into a root variable, the two other cavity spins jointly violate their literals with probability

\[
P=R_1R_2.
\]

Root-literal signs split the incident Poisson clause process into two independent orientations, each with mean

\[
\lambda=\frac{3\alpha_0}{2}.
\]

For one orientation put

\[
Z=\prod_j(1-P_j),\qquad Q=1-Z.
\tag{3.4}
\]

Here `Z` is the inner probability that no hard warning arrives on that side. Exactly as in the predecessor, the root factor in the zero-temperature hard-field limit gives

\[
\mathbb E\log(1-Q_+Q_-),
\]

while the clause factor gives

\[
-2\alpha_0\,\mathbb E\log(1-R_1R_2R_3).
\]

Thus after multiplying the one-step functional by `m` and taking the justified hard-field / zero-temperature / `m downarrow 0` limit, the coefficient is

\[
A(\alpha_0;\nu)
=
\mathbb E\log(1-Q_+Q_-)
-2\alpha_0\,\mathbb E\log(1-R_1R_2R_3),
\tag{3.5}
\]

where `nu` is the three-support law (3.2)--(3.3).

The same dominated-convergence proof as in the predecessor applies. All support points lie strictly inside `(0,1)`, hence every warning activation is bounded away from one; Poisson counts have exponential moments; the clause factor is uniformly bounded away from zero. Therefore strict negativity of `A` implies that some finite hard-field magnitude, finite `beta`, and finite `m>0` already have a negative rigorous interpolation value.

## 4. Exact compound-Poisson reduction for an arbitrary finite support

The new three-support law needs no new probabilistic approximation. For integer `j>=1`, compound-Poisson independence gives

\[
\mathbb E Z^j
=
\exp\left\{\lambda\left(\mathbb E(1-R_1R_2)^j-1\right)\right\}.
\tag{4.1}
\]

Writing

\[
\mu_k=\mathbb E Q^k,
\]

binomial inversion gives

\[
\mu_k
=
\sum_{j=0}^k(-1)^j\binom{k}{j}\mathbb E Z^j.
\tag{4.2}
\]

Since `0<=Q<1`, Tonelli's theorem applied to the nonnegative expansion of `-log(1-u)` yields

\[
\mathbb E\log(1-Q_+Q_-)
=-\sum_{k\ge1}\frac{\mu_k^2}{k}.
\tag{4.3}
\]

Put

\[
L=\mathbb E\log(1-R_1R_2R_3).
\]

Then

\[
A=-\sum_{k\ge1}\frac{\mu_k^2}{k}-2\alpha_0L.
\tag{4.4}
\]

For every finite `K`, define

\[
A_K=-\sum_{k=1}^K\frac{\mu_k^2}{k}-2\alpha_0L.
\tag{4.5}
\]

Every omitted term in the infinite series is nonnegative before the leading minus sign, so

\[
\boxed{A\le A_K.}
\tag{4.6}
\]

This one-sided direction is crucial: a finite truncation with `A_K<0` is already a rigorous certificate, with no tail estimate.

## 5. Executed outward-interval certificate

I wrote and executed

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T04-07-30Z__three_support_439539_interval.py`

and archived its actual output in

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T04-07-30Z__three_support_439539_interval.out`.

The script uses only the exact rationals (3.1)--(3.3), `K=300`, and outward `mpmath.iv` arithmetic at 280 decimal digits. It verifies that every computed `mu_k` interval is strictly positive and certifies

\[
A_{300}
\in
[-8.0399644427720096895986749714497\times10^{-7},
 -8.0399644427720096895986749714497\times10^{-7}]
\]

up to the much smaller outward interval width printed in the archived output. In particular,

\[
\boxed{A\le A_{300}<0.}
\tag{5.1}
\]

The output ends

`CERTIFIED_A_K_NEGATIVE = True`

and

`CERTIFIED_A_NEGATIVE = True because A <= A_K`.

This is the decisive finite calculation.

### Mechanism-level comparison with the predecessor

At the new density `4.39539`, the predecessor's equal-weight two-support law `R in {0.22,0.78}` has the same `K=300` truncated coefficient approximately

\[
A_{300}^{(2)}\approx +0.00271034376107,
\]

whereas the certified three-support law has

\[
A_{300}^{(3)}<-8.03\times10^{-7}.
\]

Thus inserting a large central `R=1/2` mass changes the compound-warning distribution by an exponential-rate amount of about `0.002711` at this density. This comparison explains the gain but is **not** a proof that all two-support laws fail there; the threshold theorem uses only the rigorous negativity of the three-support trial.

## 6. From the negative coefficient to linear minimum energy

By Sections 2--5 and the strict inequality in (5.1), there exist finite constants `m in (0,1)`, `beta<infinity`, hard-field magnitude `H<infinity`, and `c>0` such that the rigorous interpolation theorem gives, for all large `N`,

\[
\frac1N\mathbb E\log Z_N(\beta)\le -c
\tag{6.1}
\]

for the Poissonized with-replacement 3-SAT model at density `alpha_0`.

Adding one clause changes `log Z_N` by a value in `[-beta,0]`. The Poisson Poincare inequality therefore gives

\[
\operatorname{Var}(\log Z_N)\le \alpha_0N\beta^2.
\tag{6.2}
\]

Chebyshev implies

\[
\Pr\left[\log Z_N>-\frac{cN}{2}\right]\to0.
\tag{6.3}
\]

If `E_min` is the minimum number of violated clauses, one minimizing assignment contributes at least `exp(-beta E_min)` to `Z_N`, hence

\[
\log Z_N\ge-\beta E_{\min}.
\]

Combining with (6.3),

\[
\boxed{
E_{\min}\ge \delta N\quad\text{w.h.p.},
\qquad \delta=\frac{c}{2\beta}>0.
}
\tag{6.4}
\]

Thus the with-replacement Poisson model is linearly far from satisfiable, not merely UNSAT.

## 7. New transfer lemma: exact same-density de-Poissonization

The predecessor spent positive density slack to move from its Poisson certificate at `4.4178` to fixed count `4.418`. Linear minimum energy makes that slack unnecessary.

### Step 1: delete repeated-variable clauses

A with-replacement ordered triple is proper with probability

\[
p_N=\frac{(N)_3}{N^3}=1-\frac3N+\frac2{N^2}.
\tag{7.1}
\]

Poisson thinning splits the formula into an independent proper part and a repeated-variable part. The number `B_N` of repeated-variable clauses is Poisson with mean

\[
\alpha_0N(1-p_N)=3\alpha_0+O(N^{-1}),
\]

so `B_N=O_p(1)`. Deleting one clause can reduce `E_min` by at most one. Therefore (6.4) implies that the proper Poisson subformula still satisfies

\[
E_{\min}^{\rm proper}\ge \frac{\delta}{2}N
\quad\text{w.h.p.}
\tag{7.2}
\]

for all sufficiently large `N`.

Its clause count is

\[
M_N'\sim\operatorname{Poisson}(\alpha_0Np_N),
\]

and conditional on `M_N'`, its clauses are iid uniform signed proper 3-clauses — exactly the source clause law.

### Step 2: couple to exactly floor(alpha_0 N) clauses

Let

\[
m_N=\lfloor\alpha_0N\rfloor.
\]

Because

\[
\mathbb EM_N'=\alpha_0N-O(1),
\qquad \operatorname{Var}(M_N')=O(N),
\]

we have

\[
M_N'-m_N=O_p(\sqrt N)=o_p(N).
\tag{7.3}
\]

Conditional on `M_N'`, order the proper clauses iid.

- If `M_N'<=m_N`, append `m_N-M_N'` new iid proper clauses. Satisfiability can only decrease.
- If `M_N'>m_N`, delete the final `M_N'-m_N` clauses. The first `m_N` clauses are still iid proper source clauses, and deleting `D` clauses can reduce minimum violated-clause energy by at most `D`.

By (7.2)--(7.3), in the second case the resulting exact-count formula still has positive minimum energy w.h.p. Thus in both cases the coupled formula with exactly `m_N` clauses is UNSAT w.h.p. and has exactly the source distribution.

Therefore

\[
\boxed{
\Pr\!\left[\Phi_{N,\lfloor(439539/100000)N\rfloor}\text{ is SAT}\right]\to0.
}
\tag{7.4}
\]

This proves the candidate theorem (0.1) at the **same density** as the Poisson certificate. No `+epsilon` density slack is needed.

## 8. Relation to the historical 4.396 calculation

Franz--Leone--Ricci-Tersenghi--Zecchina's 2001 factorized one-step physics ansatz reported a 3-SAT variational value around

\[
4.3962.
\]

That paper itself explicitly described a mathematically rigorous derivation as future work. Franz--Leone subsequently proved general rigorous replica/interpolation bounds for random K-SAT, and Panchenko--Talagrand later simplified the interpolation framework.

The present three-support law is **not claimed to be algebraically identical** to the 2001 factorization ansatz. It was obtained here by finite-support optimization inside the already-rigorous interpolation family and then interval-certified. Numerically it crosses below the historical `4.3962` value:

\[
4.39539<4.3962.
\]

This is useful evidence that even a tiny finite support captures more of the one-step order parameter than the inherited two-atom trial.

The stronger modern `U_{1RSB}(3)` variational upper frontier, numerically reported near `4.267`, remains well below both numbers. The present run does not claim to certify that full numerical evaluation.

## 9. Fresh bounded literature check, 2026-09-20

Essential sources checked for this run:

- Hajiaghayi--Sorkin, *The Satisfiability Threshold of Random 3-SAT Is at Least 3.52*, arXiv:math/0310193: rigorous lower endpoint `3.52`.
- Díaz--Kirousis--Mitsche--Pérez-Giménez, *A new upper bound for 3-SAT*, arXiv:0807.3600 / FSTTCS 2008: explicit classical upper endpoint `4.4898`.
- Franz--Leone, *Replica bounds for optimization problems and diluted spin systems*, cond-mat/0208280 / J. Stat. Phys. 111 (2003): rigorous variational bounds for random K-SAT.
- Panchenko--Talagrand, *Bounds for diluted mean-fields spin glass models*, arXiv:math/0405357: simplified general interpolation bound.
- Franz--Leone--Ricci-Tersenghi--Zecchina, *Exact solutions for diluted spin glasses and optimization problems*, PRL 87 (2001): historical factorized 3-SAT value about `4.396` and its then-nonrigorous status.
- Chatterjee et al., *The random k-SAT Gibbs uniqueness threshold revisited*, published online 27 March 2026: fixed small-`k` threshold convergence still open; interpolation upper functional matches the 1RSB prediction; table reports `d_sat(3)≈12.801` from physics.

This bounded search does not establish worldwide novelty of the exact rational trial (3.1)--(3.3). The mathematical claim here is the complete internally checked candidate proof, not a priority assertion.

## 10. What this run establishes and what it does not

### CANDIDATE_FULL, pending later independent review

- a legal three-support one-step K-SAT order parameter at `p=3`;
- an exact compound-Poisson formula for its hard-field coefficient;
- an outward-interval finite certificate `A<0` at `alpha=4.39539`;
- finite-parameter pullback from the strict hard-field limit;
- linear minimum violated-clause energy in the Poisson with-replacement model;
- deletion of `O_p(1)` improper clauses;
- a same-density de-Poissonization lemma using `O_p(sqrt N)` clause-count fluctuations and linear energy;
- the exact-source fixed-count upper endpoint `4.39539`.

### Not established

- existence of a single limiting 3-SAT threshold;
- any lower-bound improvement beyond `3.52`;
- equality of the threshold with a cavity/replica prediction;
- an interval-certified numerical evaluation of the full modern `U_{1RSB}(3)` functional near `4.267`;
- global optimality of the three-support survey law;
- final publication-level certification without later independent review.

## 11. Next attack

The two-support obstruction is gone. The next mathematically efficient step is to keep Sections 2, 4, 6 and 7 fixed and enlarge only the outer survey family.

First target: a symmetric five-support law

\[
\{s_1,s_2,1/2,1-s_2,1-s_1\}
\]

with symmetric weights. Optimize its hard-field coefficient numerically, freeze simple rational parameters, and interval-certify a density strictly below `4.39539`. If that family stalls, reconstruct a finite-support approximation of the full `U_{1RSB}(3)` order parameter rather than returning to Díaz counting.

This remains complementary to NM13-06's dynamic-promotion constructive lower-bound route.

## 12. Durable artifacts and ledger delta

Executed interval code:

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T04-07-30Z__three_support_439539_interval.py`

creation commit: `1ace56599b5b797827b5e7ed42dfda1040e2d1db`.

Archived actual output:

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T04-07-30Z__three_support_439539_interval.out`

creation commit: `469ffab33874c86b76b28f71857c7f9c03db0c03`.

Structured ledger delta:

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/2026-09-20T04-07-30Z__ledger_delta.json`

creation commit: `9a8ce5d9e3f50fe07ad6ea0057913af4b5f07844`.
