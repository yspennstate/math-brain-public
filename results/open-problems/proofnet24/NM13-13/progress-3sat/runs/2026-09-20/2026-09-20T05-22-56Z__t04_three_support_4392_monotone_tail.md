Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but this runtime exposes no authenticated applied-reasoning telemetry, so I do not claim GPT-6 maximum.**

# NM13-13 — T04 cluster-aware random 3-SAT: monotone 1RSB tail tightening gives an explicit 4.392 candidate upper bound

Date: 2026-09-20  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker root: `proofnet24/NM13-13/progress-3sat/`  
Parent: **T04 — classical iid random 3-SAT with uniform independent signs on three distinct variables**  
Status: **OPEN / PARTIAL; CANDIDATE_FULL for the explicit fixed-count upper endpoint 4.392, pending later independent review**

## 0. Source-threshold before / after, kept separate from mechanism gain

There are three distinct status layers and they must not be conflated.

### A. Externally literature-supported explicit-decimal bracket

The classical historical explicit results remain

\[
\boxed{3.52\le \alpha_{3\mathrm{SAT}}\le 4.4898}.
\]

Hajiaghayi--Sorkin prove satisfiability w.h.p. below `3.52`. Díaz--Kirousis--Mitsche--Pérez-Giménez prove unsatisfiability w.h.p. at density at least `4.4898`. This external explicit-decimal bracket is unchanged in this run.

For fixed `k=3`, existence of a single limiting threshold is still not something I treat as proved merely from Friedgut sharp windows or from large-`k` results. Recent work gives a rigorous 1RSB/interpolation upper variational functional and reports a physics numerical value near `alpha≈4.267` (`d_sat(3)≈12.801` under `d=3 alpha`), but this worker has not independently interval-certified the full variational evaluation at that decimal. Thus the strongest literature-supported theorem-form statement I am prepared to use is still symbolically

\[
3.52\le \liminf c_n\le \limsup c_n\le U_{1\mathrm{RSB}}(3),
\]

with the reported physics evaluation near `4.267` kept separate from this track's independently certified finite-support numerics.

### B. Project CANDIDATE_FULL explicit-decimal bracket

The previous NM13-13 report gave a complete candidate proof at fixed-count density `4.39539`. This run improves that explicit endpoint to

\[
\boxed{4.392}.
\]

Therefore the project candidate bracket moves

\[
\boxed{[3.52,4.39539]\longrightarrow[3.52,4.392]},
\]

with width

\[
0.87539\longrightarrow0.872,
\]

and upper-endpoint gain

\[
\boxed{0.00339}.
\]

Relative to the historical explicit upper bound `4.4898`, the cumulative explicit improvement is `0.0978`.

### C. Mechanism-level gain

The source movement comes from a stricter finite-support one-step interpolation certificate, not from changing the random-SAT model. The new exact symmetric survey law is

\[
R\in\left\{\frac{179}{3125},\frac12,\frac{2946}{3125}\right\}
=\{0.05728,0.5,0.94272\}
\]

with probabilities

\[
\left(\frac{20997}{100000},\frac{29003}{50000},\frac{20997}{100000}\right)
=(0.20997,0.58006,0.20997).
\]

At `alpha=4.392`, the predecessor law still has positive `K=1000` truncated coefficient approximately `+1.28749e-5`, whereas the new law has rigorously certified

\[
A_{1000}< -2.14034\times 10^{-5}.
\]

So the parameter reoptimization changes the `K=1000` coefficient by about `3.43e-5` in the favorable direction. Separately, for the new law the `K=300` coefficient is still positive (about `4.3268e-4`), while the `K=1000` coefficient is negative. The additional exact tail terms therefore provide more than `4.54e-4` of one-sided certified tightening. These are mechanism gains; only the completed transfer below turns them into the candidate source endpoint `4.392`.

Claim ID: `NM13-13-T04-THREE-SUPPORT-4392-UPPER-03`.

## 1. Short predecessor handoff and exact prior failures

The immediately preceding run established four pieces that remain valid and are reused rather than rederived from scratch:

1. the Panchenko--Talagrand / Franz--Leone K-SAT interpolation upper bound applies at `p=3`; the apparent even-`p` restriction belongs to the broader diluted-spin-glass umbrella, while the K-SAT remainder uses nonnegative replica quantities and convexity of `t^p` on `[0,∞)`;
2. for a finite-support hard-field survey, the `m downarrow 0` coefficient reduces exactly to a compound-Poisson series;
3. strict negativity of that coefficient pulls back by dominated convergence/continuity to finite hard-field magnitude, finite inverse temperature and finite `m>0`, producing a genuinely negative interpolation upper bound;
4. once that finite-temperature bound gives linear minimum violated-clause energy in the Poisson with-replacement model, deletion of the `O_p(1)` repeated-variable clauses and `O_p(sqrt n)` same-density de-Poissonization transfer the result to the exact fixed-count proper iid source model.

The exact prior failures are preserved:

- arbitrary rescue stars do not compose because two children rescued individually by one root can jointly falsify another clause;
- anchored degree-one rescue matching is a valid strict local exponent penalty, but the full Díaz polytope was never globally reoptimized with that penalty;
- positive clause-local multiplicative second moments hit the identical-pair barrier `alpha <= log(2)/log(5/4)=3.1062837...`;
- quotienting solution-graph balls of radius `o(n/log n)` changes counts only by `exp(o(n))`;
- full-component quotienting leaves an uncontrolled cross-component overlap moment;
- whitening/core history counting lacks a proved uniform exponential cluster-multiplicity lower bound;
- the q-binomial radius-two route reached only about `4.5923`;
- the inherited equal-weight two-support hard-field family crosses only near `4.4178`;
- a diagnostic split of the three-support law into a five-support law did not show a favorable finite-`K` first move around `alpha=4.39`; this was only a heuristic diagnostic, not a five-support no-go theorem.

The companion NM13-06 has meanwhile moved further on the constructive side: it proves a no-go theorem for every one-shot independent zero-break thinning kernel and identifies negative correlation / conflict-free repair batches as the missing constructive ingredient. That is complementary to the present variational upper-bound route and is not duplicated here.

## 2. Exact finite-support functional

Fix a symmetric probability law `nu` for `R in (0,1)`. For one literal orientation of a root variable, incident clauses form a Poisson process of mean

\[
\lambda=\frac{3\alpha}{2}.
\]

For one warning, if the other two cavity spins are independently sampled according to their surveys, the warning activation probability is

\[
P=R_1R_2.
\]

For one orientation define

\[
Z=\prod_j(1-P_j),\qquad Q=1-Z.
\]

Then for every integer `j>=1`, compound-Poisson independence gives

\[
\mathbb E Z^j
=
\exp\left\{\lambda\left(\mathbb E(1-R_1R_2)^j-1\right)\right\}.
\tag{2.1}
\]

Define

\[
\mu_k=\mathbb E Q^k.
\]

Binomial inversion gives the exact finite formula

\[
\mu_k
=
\sum_{j=0}^k(-1)^j\binom{k}{j}\mathbb E Z^j.
\tag{2.2}
\]

For independent copies `Q_+,Q_-`, Tonelli applied to the nonnegative expansion of `-log(1-u)` yields

\[
\mathbb E\log(1-Q_+Q_-)
=-\sum_{k\ge1}\frac{\mu_k^2}{k}.
\tag{2.3}
\]

Put

\[
L=\mathbb E\log(1-R_1R_2R_3).
\]

The hard-field, zero-temperature, `m downarrow 0` coefficient of the rigorous one-step interpolation trial is therefore

\[
\boxed{
A(\alpha,\nu)
=-\sum_{k\ge1}\frac{\mu_k^2}{k}-2\alpha L.
}
\tag{2.4}
\]

This is the same exact functional as in the predecessor.

## 3. New variational inequality: finite truncations tighten monotonically

For `K>=1`, define

\[
A_K
=-\sum_{k=1}^K\frac{\mu_k^2}{k}-2\alpha L.
\tag{3.1}
\]

Because every `mu_k^2/k` is nonnegative,

\[
\boxed{A\le A_{K+1}\le A_K.}
\tag{3.2}
\]

More precisely,

\[
\boxed{
A_{K+1}=A_K-\frac{\mu_{K+1}^2}{K+1}.
}
\tag{3.3}
\]

Thus increasing `K` is not a heuristic tail extrapolation. It is a rigorous one-sided strengthening of the variational inequality. No estimate of the omitted infinite tail is required: any finite `K` with `A_K<0` already proves `A<0`.

This simple monotonicity is decisive here because the warning distribution has a long enough positive moment tail that `K=300` leaves a visibly nontrivial amount of certifiable negativity unused. At `alpha=4.392`, the new law has approximately

\[
A_{300}=+4.32676884\times10^{-4},
\]

but the exact additional terms through `K=1000` drive the certified upper approximation below zero.

## 4. Exact rational trial at density 4.392

Set

\[
\alpha_0=\frac{4392}{1000}=4.392,
\]

and let

\[
R\in\left\{\frac{179}{3125},\frac12,1-\frac{179}{3125}\right\}
\]

with probabilities

\[
\Pr\left(R=\frac{179}{3125}\right)
=
\Pr\left(R=1-\frac{179}{3125}\right)
=
\frac{20997}{100000},
\]

and

\[
\Pr(R=1/2)=\frac{29003}{50000}.
\]

All parameters are exact rationals. The law is invariant under `R -> 1-R`, hence respects the fair-sign gauge symmetry.

The support points lie strictly inside `(0,1)`. Consequently the finite-hard-field approximants used in the interpolation transfer are uniformly separated from the singular endpoint values, the Poisson counts have exponential moments, and the clause factor is bounded away from zero for the finite trial. The dominated-convergence argument from the predecessor therefore applies unchanged once strict `A<0` is established.

## 5. Executed outward-interval certificate

The essential executable artifact is

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T05-22-56Z__three_support_4392_interval.py`

and its actual archived output is

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T05-22-56Z__three_support_4392_interval.out`.

The script uses only the exact rational parameters above, `K=1000`, and outward `mpmath.iv` arithmetic with 850 decimal digits. It evaluates (2.1)--(3.1) directly. Every interval for `mu_k`, `1<=k<=1000`, is strictly positive, which is an extra sanity check against catastrophic cancellation.

The decisive output is

\[
\boxed{
A_{1000}
< -2.1403418190123965\times10^{-5}<0.
}
\tag{5.1}
\]

The archived run ends with

`CERTIFIED_A_K_NEGATIVE = True`

and

`CERTIFIED_A_NEGATIVE = True because A <= A_K`.

By (3.2), (5.1) proves

\[
\boxed{A(4.392,\nu)<0.}
\tag{5.2}
\]

No uncomputed tail estimate is used.

### Diagnostic decomposition of the gain

At the same density `4.392`, keeping the predecessor's support/weight parameters but evaluating through `K=1000` gives approximately

\[
A_{1000}^{\rm old}=+1.28749\times10^{-5},
\]

whereas the new rational law gives (5.1). Hence parameter reoptimization alone contributes about

\[
3.43\times10^{-5}
\]

of coefficient improvement at fixed truncation depth.

For the new law,

\[
A_{300}^{\rm new}\approx+4.32677\times10^{-4},
\qquad
A_{1000}^{\rm new}<-2.14034\times10^{-5},
\]

so the additional exact moment terms contribute more than `4.54e-4` of rigorous one-sided tightening. This explains why the `K=300` predecessor search could not see the present endpoint even though no new physical ansatz is required.

## 6. From the coefficient to a finite interpolation trial

The one-step K-SAT interpolation theorem gives, for finite inverse temperature `beta`, finite hard-field magnitude `H`, and Parisi parameter `m in (0,1)`, an upper bound

\[
\frac1N\mathbb E\log Z_N(\beta)
\le \Phi_1(\nu;m,\beta,H).
\tag{6.1}
\]

The predecessor recovered the `p=3` specialization carefully: the interpolation remainder is nonnegative because the K-SAT replica quantities lie in `[0,1]` and the relevant polynomial is the convexity remainder

\[
R_3(x,y)=x^3-3xy^2+2y^3\ge0
\qquad (x,y\ge0).
\]

For the present finite-support law, the hard-field / zero-temperature / `m downarrow0` scaling satisfies

\[
\lim m\,\Phi_1 = A(4.392,\nu),
\]

under the same normalization used in the predecessor. By (5.2), the limit is strictly negative. All support values are strictly between zero and one, the clause logarithms are uniformly integrable for the finite-support approximation, and Poisson degrees have exponential moments. Therefore dominated convergence and continuity imply that there exist finite values

\[
0<m_*<1,\qquad \beta_*<\infty,\qquad H_*<\infty,
\]

and `c>0` such that for all sufficiently large `N`,

\[
\boxed{
\frac1N\mathbb E\log Z_N(\beta_*)\le -c.
}
\tag{6.2}
\]

This is the point at which the hard-field coefficient becomes an actual rigorous finite interpolation statement.

## 7. Negative free energy implies linear minimum violated-clause energy

Let `E_min` be the minimum number of violated clauses in the Poissonized with-replacement model. Adding or deleting one clause changes `log Z_N(beta_*)` by at most `beta_*`. The Poisson Poincaré inequality therefore yields

\[
\operatorname{Var}(\log Z_N(\beta_*))
\le \alpha_0N\beta_*^2.
\tag{7.1}
\]

From (6.2) and Chebyshev,

\[
\Pr\left(\log Z_N(\beta_*)>-\frac{cN}{2}\right)\to0.
\tag{7.2}
\]

A minimizing assignment contributes at least `exp(-beta_* E_min)` to the partition function, so

\[
\log Z_N(\beta_*)\ge-\beta_*E_{\min}.
\]

Combining with (7.2), with high probability

\[
\boxed{
E_{\min}\ge \delta N,
\qquad \delta=\frac{c}{2\beta_*}>0.
}
\tag{7.3}
\]

Thus the Poisson with-replacement formula is linearly far from satisfiable.

## 8. Exact source-model transfer at the same density

A with-replacement ordered triple is proper with probability

\[
p_N=\frac{(N)_3}{N^3}=1-\frac3N+\frac2{N^2}.
\]

Poisson thinning decomposes the formula into independent proper and repeated-variable clauses. The repeated-variable count has mean

\[
\alpha_0N(1-p_N)=3\alpha_0+O(N^{-1}),
\]

hence is `O_p(1)`. Deleting those clauses lowers `E_min` by at most `O_p(1)`, so the proper Poisson subformula still has minimum violated-clause count at least `delta N/2` w.h.p. for large `N`.

Its number of clauses is

\[
M_N'\sim\operatorname{Poisson}(\alpha_0Np_N)
\]

and, conditional on `M_N'`, its clauses are iid uniform signed proper 3-clauses. Since

\[
M_N'-\lfloor\alpha_0N\rfloor=O_p(\sqrt N),
\]

couple to exactly `m_N=floor(alpha_0N)` clauses as follows.

- If `M_N'<=m_N`, append independent proper iid clauses until there are exactly `m_N`; adding clauses cannot decrease `E_min`.
- If `M_N'>m_N`, retain the first `m_N` iid proper clauses. The deletion count is `O_p(sqrt N)`, and deleting one clause can reduce `E_min` by at most one. Thus linear minimum energy survives.

The resulting fixed-count formula has exactly the source law: `m_N` iid uniform signed clauses on three distinct variables. Therefore

\[
\boxed{
\Pr\!\left[\Phi_{N,\lfloor4.392N\rfloor}\text{ is satisfiable}\right]\to0.
}
\tag{8.1}
\]

This proves the stated CANDIDATE_FULL explicit upper endpoint, subject to later independent review of the inherited interpolation normalization and the complete transfer chain.

## 9. What this does and does not settle

This run **does**:

- strictly improve the project candidate explicit upper endpoint from `4.39539` to `4.392` for the exact proper fixed-count iid model;
- prove and exploit the monotone truncation inequality `A<=A_{K+1}<=A_K`;
- give an exact rational survey law;
- execute and archive an outward-interval `K=1000` certificate with strict negative margin;
- retain the same-density de-Poissonization proof, so no positive density slack is spent.

This run **does not**:

- prove existence of a single limiting `k=3` threshold;
- improve the lower bound `3.52`;
- claim the reported cavity/replica value near `4.267` as an independently certified decimal theorem;
- beat the symbolic literature frontier `U_1RSB(3)`;
- establish that the three-support family is globally optimal;
- establish a five-support no-go theorem;
- convert the companion constructive algorithm into a lower-bound improvement.

The theorem above is therefore labeled **CANDIDATE_FULL**, not final certification.

## 10. Next attack

The three-support family now has a warning sign of local exhaustion: a coarse symmetric split-atom diagnostic did not reveal an immediate five-support improvement. The next run should not merely increase `K` again. Instead compute the **first variation of the full functional** under insertion of a symmetric atom pair `x,1-x`, with compensating mass removed from the existing atoms. If that first variation has a rigorously negative direction at the optimized law, optimize and interval-certify a five-support trial. If every tested first variation is nonnegative with a certifiable margin, rotate within T04 to a finite-support approximation of the full distributional `U_1RSB(3)` order parameter rather than polishing the same family.

## 11. Durable artifacts

Code:

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T05-22-56Z__three_support_4392_interval.py`

Code creation commit:

`bec8c7ea570c02f78a4ff8c02146aa7de78af918`

Executed output:

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T05-22-56Z__three_support_4392_interval.out`

Output creation commit:

`a536bc5c18ab20155c57f2150d560f3d889978c6`

Structured ledger delta:

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/2026-09-20T05-22-56Z__ledger_delta.json`

Ledger creation commit:

`435c2d20891796c89111f673702b623f23433dec`
