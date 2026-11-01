Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but this runtime exposes no authenticated applied-effort telemetry, so I do not claim GPT-6 maximum.**

# NM13-13 — T04 cluster-aware random 3-SAT: log-convex moment-tail acceleration gives a 4.3906 candidate upper bound

Date: 2026-09-20  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker root: `proofnet24/NM13-13/progress-3sat/`  
Parent: **T04 — classical iid random 3-SAT with independent fair signs on three distinct variables per clause**  
Status: **OPEN / PARTIAL; CANDIDATE_FULL for the explicit fixed-count upper endpoint 4.3906, pending later independent review**

## 0. Source threshold before / after, separate from the mechanism gain

There are three different statements and they must remain separate.

### Externally literature-supported explicit-decimal bracket

The explicit published bracket recovered this run remains

\[
\boxed{3.52\le \liminf c_n\le \limsup c_n\le 4.4898}.
\]

Hajiaghayi--Sorkin prove satisfiability w.h.p. below `3.52` for the standard independent-clause model. Díaz--Kirousis--Mitsche--Pérez-Giménez prove a.a.s. unsatisfiability at density `4.4898` and above. The 2026 Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis paper still states that the exact satisfiability threshold is known for `k=2` and sufficiently large `k`, not for fixed small `k=3`; Carenini's August 2026 scaling-window theorem sharpens the window to `O(n/log n)` but does not prove convergence of the centers to a single constant. Large-`k`, sharp-window, and `k`-wise-independent variants therefore do not settle this source.

So the **externally published explicit-decimal metric is unchanged** in this run:

\[
[3.52,4.4898]\longrightarrow[3.52,4.4898].
\]

The rigorous interpolation/1RSB literature supplies a stronger symbolic variational upper-bound architecture, but this track still does not claim an independently interval-certified decimal evaluation of the full optimized functional near the physics `4.267` benchmark.

### Project CANDIDATE_FULL explicit endpoint

The strongest actual predecessor certificate in this namespace is **4.3911**, not 4.392. The repository contains the exact 04:55 ledger delta plus the executed outward-interval artifact

`artifacts/2026-09-20T04-55-14Z__three_support_43911_interval.out`,

which certifies `A_1200<0` at `alpha=4.3911`. A later 05:22 report inadvertently restarted from the weaker 4.392 figure. I do not edit either historical file; this report restores continuity by taking the stronger preserved 4.3911 certificate as the true before-value.

This run proves the stronger candidate endpoint

\[
\boxed{4.3906}.
\]

Thus the project candidate bracket moves

\[
\boxed{[3.52,4.3911]\longrightarrow[3.52,4.3906]},
\]

with width

\[
0.8711\longrightarrow0.8706,
\]

and explicit endpoint gain

\[
\boxed{0.0005}.
\]

Relative to the historical 4.4898 explicit upper bound, the cumulative project-candidate gain is `0.0992`.

### Demonstrated mechanism gain

The predecessor only used monotonic finite truncations

\[
A\le A_K.
\]

At the new density and law below, this by itself is **inconclusive** even at `K=2400`:

\[
A_{2400}=+1.2851067265960\times10^{-5}.
\]

The new theorem uses the fact that the moment sequence `mu_k=E[Q^k]` is log-convex. It lower-bounds the omitted negative tail by

\[
1.3656658979541\times10^{-5},
\]

which turns the positive truncation into the rigorous full-functional upper bound

\[
\boxed{A\le -8.055917135809\times10^{-7}<0.}
\]

This is a genuinely new variational inequality: it extracts certified information from the infinite tail rather than merely computing a deeper truncation.

Claim ID: `NM13-13-T04-LOGCONVEX-TAIL-43906-UPPER-04`.

## 1. Short handoff and exact prior failures

The interpolation route already established, at candidate-full level, the following dependency chain:

1. the Franz--Leone / Panchenko--Talagrand diluted K-SAT interpolation bound applies to `p=3`; the K-SAT remainder is controlled by convexity on nonnegative replica quantities, so the broader even-`p` restriction from diluted spin-glass formulations is not a K-SAT obstruction;
2. for a finite-support hard-field survey, the `m downarrow 0` coefficient is the compound-Poisson functional written in Section 2 below;
3. strict negativity of that coefficient persists for finite hard-field magnitude, finite inverse temperature, and some finite `m>0` by continuity/dominated convergence;
4. a strictly negative finite-temperature interpolation upper bound plus concentration gives linear minimum violated-clause energy in the Poisson with-replacement model;
5. repeated-variable clauses are only `O_p(1)`, and same-density de-Poissonization changes the number of proper clauses by only `O_p(sqrt n)`, so linear unsatisfied energy survives transfer to the exact fixed-count proper iid source model.

The exact parked failures remain:

- arbitrary rescue stars do not compose: two children individually rescued by one root can jointly falsify another clause;
- anchored degree-one rescue matching gives a valid local strict exponent penalty, but the full Díaz `M=23` variational polytope was never globally reoptimized with it;
- positive clause-local multiplicative second moments hit the identical-pair barrier `log 2/log(5/4)=3.10628...`;
- quotienting solution-graph balls of radius `o(n/log n)` saves only `exp(o(n))`;
- quotienting whole connected components leaves an uncontrolled cross-component overlap moment;
- whitening/core counting still lacks a proved uniform exponential cluster-multiplicity lower bound;
- the q-binomial radius-two route only reached about `4.5923`;
- the equal-weight two-support hard-field family stalls near `4.4178`;
- one diagnostic split into a five-support law did not show an immediate favorable local direction, but that was never a five-support no-go theorem.

Companion NM13-06 has meanwhile proved that finite repair menus become locally complete at double-exponential depth under its majority-Palm recursion, even near the upper-density region; its remaining obstruction is global compatibility/load balancing of correlated repair trees. That constructive route is complementary and is not duplicated here.

## 2. The inherited finite-support interpolation functional

Fix a symmetric probability law `nu` for `R in (0,1)`. For one literal orientation of a root variable, incident clauses form a Poisson process with mean

\[
\lambda=\frac{3\alpha}{2}.
\]

For a warning whose other two cavity surveys are `R_1,R_2`, put

\[
P=R_1R_2.
\]

If the incident warnings are indexed by `j`, define

\[
Z=\prod_j(1-P_j),\qquad Q=1-Z.
\]

Then for every integer `j>=1`, compound-Poisson independence gives

\[
\mathbb E Z^j
=\exp\left\{\lambda\left(\mathbb E(1-R_1R_2)^j-1\right)\right\}.
\tag{2.1}
\]

Let

\[
\mu_k=\mathbb E Q^k.
\]

Binomial inversion yields

\[
\mu_k=\sum_{j=0}^k(-1)^j\binom{k}{j}\mathbb EZ^j.
\tag{2.2}
\]

For independent copies `Q_+,Q_-`, Tonelli applied to the nonnegative expansion of `-log(1-u)` gives

\[
\mathbb E\log(1-Q_+Q_-)
=-\sum_{k\ge1}\frac{\mu_k^2}{k}.
\tag{2.3}
\]

Writing

\[
L=\mathbb E\log(1-R_1R_2R_3),
\]

the hard-field zero-temperature `m downarrow0` coefficient is

\[
\boxed{
A(\alpha,\nu)
=-\sum_{k\ge1}\frac{\mu_k^2}{k}-2\alpha L.
}
\tag{2.4}
\]

For

\[
A_K=-\sum_{k=1}^K\frac{\mu_k^2}{k}-2\alpha L,
\tag{2.5}
\]

one always has `A<=A_K`. The predecessor exploited only this one-sided truncation.

## 3. New theorem: log-convexity controls the entire omitted tail

The key observation is that `(mu_k)` is a Hausdorff moment sequence because `0<=Q<=1`.

### Lemma 3.1 — ratio monotonicity

For every `k>=1`,

\[
\boxed{\mu_k^2\le \mu_{k-1}\mu_{k+1}.}
\tag{3.1}
\]

Consequently, whenever the moments are positive,

\[
\boxed{
\frac{\mu_{k+1}}{\mu_k}
\ge
\frac{\mu_k}{\mu_{k-1}}.
}
\tag{3.2}
\]

#### Proof

Apply Cauchy--Schwarz to the random variables `Q^{(k-1)/2}` and `Q^{(k+1)/2}`:

\[
(\mathbb EQ^k)^2
\le
(\mathbb EQ^{k-1})(\mathbb EQ^{k+1}).
\]

This is (3.1); division by positive moments gives (3.2). QED.

### Corollary 3.2 — finite computable lower bound on the infinite tail

Fix `K>=1` and put

\[
r_K=\frac{\mu_K}{\mu_{K-1}}.
\]

By repeated use of (3.2), for every integer `t>=1`,

\[
\boxed{
\mu_{K+t}\ge \mu_K r_K^t.
}
\tag{3.3}
\]

Therefore for every finite `T>=1`,

\[
\sum_{k>K}\frac{\mu_k^2}{k}
\ge
\mu_K^2\sum_{t=1}^T\frac{r_K^{2t}}{K+t}.
\tag{3.4}
\]

Combining (2.4), (2.5), and (3.4) yields the strengthened one-sided inequality

\[
\boxed{
A(\alpha,\nu)
\le
A_K-\mu_K^2\sum_{t=1}^T\frac{r_K^{2t}}{K+t}.
}
\tag{3.5}
\]

Unlike an extrapolation, (3.5) is rigorous for every finite `K,T`. It uses only the exact moment property `0<=Q<=1` and discards the remainder after `K+T`; discarding that remainder can only weaken the lower bound on the negative tail.

This is the new route developed in this invocation.

## 4. Exact rational trial at alpha = 4.3906

Take

\[
\alpha_0=\frac{21953}{5000}=4.3906
\]

and the symmetric three-support survey

\[
R\in\left\{
\frac{31}{625},\frac12,\frac{594}{625}
\right\}
=\{0.0496,0.5,0.9504\}
\]

with probabilities

\[
\left\{
\frac{27}{125},\frac{71}{125},\frac{27}{125}
\right\}
=\{0.216,0.568,0.216\}.
\]

All support points and weights are exact rationals; the law is invariant under `R -> 1-R`.

Set

\[
K=2400,\qquad T=10000.
\]

The executable certificate is

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T06-23-41Z__logconvex_tail_43906_interval.py`

and the archived actual output is

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T06-23-41Z__logconvex_tail_43906_interval.out`.

The script uses outward `mpmath.iv` arithmetic at 1350 decimal digits. It computes the binomial transform through an algebraically identical forward-difference table, checks every interval `mu_1,...,mu_2400` is strictly positive, and then applies the finite log-convex tail sum (3.5).

The decisive certified values are

\[
\mu_{2399}
=0.00604463223774545877793714228011\ldots,
\]

\[
\mu_{2400}
=0.00604222771810446139315343594295\ldots,
\]

and hence

\[
\boxed{
r_{2400}=0.99960220580071315832377322443019\ldots.}
\]

The raw truncation is still positive:

\[
\boxed{
A_{2400}=+0.0000128510672659603103298702471578\ldots.
}
\tag{4.1}
\]

Thus merely computing to `K=2400` would fail to prove anything at `4.3906`.

The first `T=10000` log-convexly forced tail terms satisfy

\[
\boxed{
\sum_{k>2400}\frac{\mu_k^2}{k}
\ge
0.0000136566589795412292385537932322\ldots.
}
\tag{4.2}
\]

Substituting (4.1)--(4.2) into (3.5) gives

\[
\boxed{
A(4.3906,\nu)
\le
-0.0000008055917135809189086835460744\ldots<0.
}
\tag{4.3}
\]

The archived run ends with

`CERTIFIED_A_UPPER_NEGATIVE = True`

and

`CERTIFIED_A_NEGATIVE = True because A <= A_2400 - tail_LB`.

No uncomputed positive contribution is being dropped: the omitted functional terms all enter with a minus sign, and (3.4) lower-bounds a finite part of that omitted negative tail.

## 5. Transfer to the exact source model

The new work is the tail inequality and certificate; the source transfer is inherited from the preceding candidate-full interpolation reports. For completeness, the logical chain is recorded here.

The finite-support trial has support strictly inside `(0,1)`, Poisson degrees have exponential moments, and the hard-field coefficient is strictly negative by (4.3). Under the finite-temperature K-SAT interpolation theorem, continuity and dominated convergence therefore provide finite values

\[
0<m_*<1,\qquad \beta_*<\infty,\qquad H_*<\infty
\]

and `c>0` with

\[
\frac1n\mathbb E\log Z_n(\beta_*)\le -c
\]

for all sufficiently large `n` in the Poissonized with-replacement model.

Changing one clause changes `log Z_n(beta_*)` by at most `beta_*`, so Poisson bounded-difference/Poincaré concentration gives fluctuations of order `sqrt n`. Hence with probability tending to one,

\[
\log Z_n(\beta_*)\le -\frac c2 n.
\]

If `E_min` is the minimum number of violated clauses, a minimizing assignment contributes at least `exp(-beta_* E_min)` to the partition function, so

\[
E_{\min}\ge \frac{c}{2\beta_*}n
\]

with high probability. In particular the formula is unsatisfiable with linear energy margin.

In the with-replacement clause model, clauses containing a repeated variable occur only `O_p(1)` times at fixed density. Removing them can lower `E_min` by only `O_p(1)`. The remaining proper-clause count differs from `floor(alpha_0 n)` by `O_p(sqrt n)`. Adding or deleting that many proper clauses changes minimum violated-clause energy by at most `O_p(sqrt n)`, which cannot erase a linear margin. Therefore the same-density fixed-count proper iid model obeys

\[
\boxed{
\Pr\!\left[
\Phi_{n,\lfloor4.3906n\rfloor}\text{ is satisfiable}
\right]\longrightarrow0.
}
\tag{5.1}
\]

By monotonicity in the number of clauses, the same holds for every fixed density above `4.3906`.

I label (5.1) **CANDIDATE_FULL pending later independent review**, rather than externally certified closure of T04.

## 6. Fresh bounded literature/status check

Queries were limited to the source status and nearby threshold statements needed for this run, dated 2026-09-20.

- Hajiaghayi--Sorkin, *The Satisfiability Threshold of Random 3-SAT Is at Least 3.52*, arXiv:math/0310193: standard proper independent-clause model, satisfiable w.h.p. below 3.52.
- Díaz--Kirousis--Mitsche--Pérez-Giménez, *A new upper bound for 3-SAT*, arXiv:0807.3600 / FSTTCS 2008: a.a.s. unsatisfiable at density at least 4.4898.
- Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis, *The random k-SAT Gibbs uniqueness threshold revisited*, CPC 35 (2026), published online 27 March 2026: the introduction still describes exact satisfiability thresholds as known for `k=2` and sufficiently large `k`, not fixed small `k=3`.
- Gaia Carenini, *The Scaling Window of Random k-SAT*, ECCC TR26-145, posted August 2026: proves an `O(n/log n)` window for every fixed `k>=3`; this sharpens the window but does not locate or prove convergence of the threshold centers.
- Physics/cavity values near `4.267` remain benchmarks unless accompanied by the rigorous variational upper-bound theorem and a certified evaluation; they are not silently substituted for the explicit-decimal source metric here.

This bounded check does not claim worldwide novelty of the numerical constant or the moment-tail lemma. It establishes only that the exact iid `k=3` location remains unresolved in the checked primary sources and that the classical explicit published endpoints above remain valid reference points.

## 7. Relation to NM13-06 and why this is complementary

NM13-06's newest report proves a quadratic repair-menu contraction under the majority-Palm law:

\[
y_{d+1}\le r_1 y_d^2,
\]

so finite repair menus become doubly exponentially complete locally whenever its certified `r_1y_0<1` condition holds. Its remaining issue is not local branch availability but global compatibility and load of overlapping repair trees.

This run attacks the opposite side of T04. It never tries to build a satisfying assignment. Instead it improves an upper-bound interpolation functional by exploiting a structural property of its cluster-warning moment sequence. The two workers therefore remain complementary exactly as assigned.

## 8. Residual obstruction and next attack

The new tail accelerator is generic for every finite-support survey law, not specific to three support points. The immediate next mathematical attack should keep the rigorous transfer fixed and optimize the **tail-accelerated** objective rather than `A_K` alone.

Two concrete possibilities are now justified:

1. optimize a symmetric five-support rational law using the certified objective

\[
A_K-\mu_K^2\sum_{t=1}^T\frac{r_K^{2t}}{K+t},
\]

because the earlier five-support diagnostic tested the wrong finite-`K` objective and therefore did not see this tail gain;
2. strengthen Corollary 3.2 using two or more certified consecutive moment ratios. Since the ratios are increasing, exact blocks beyond `K` can be combined with a later geometric lower envelope, potentially extracting more of the subgeometric tail without pushing the unstable binomial transform to much larger `K`.

The source threshold is still open. The concrete progress this invocation contributes is the rigorous Hausdorff-moment tail inequality plus its executed 4.3906 certificate.

## 9. Compact ledger_delta

```yaml
ledger_delta:
  worker: NM13-13
  target: T04
  status: OPEN_PARTIAL_CANDIDATE_FULL
  runtime_model: GPT-5.6 Sol
  runtime_reasoning: UNVERIFIED
  source_model: classical iid proper random 3-SAT; three distinct variables per clause; fair independent signs
  external_explicit_bracket_before: "[3.52,4.4898]"
  external_explicit_bracket_after: "[3.52,4.4898]"
  project_candidate_upper_before: 4.3911
  project_candidate_upper_after: 4.3906
  project_candidate_width_before: 0.8711
  project_candidate_width_after: 0.8706
  endpoint_gain: 0.0005
  claim_id: NM13-13-T04-LOGCONVEX-TAIL-43906-UPPER-04
  survey_support: [31/625, 1/2, 594/625]
  survey_weights: [27/125, 71/125, 27/125]
  K: 2400
  T_tail: 10000
  raw_A_K: "+1.2851067265960310e-5"
  certified_tail_lower_bound: "+1.3656658979541229e-5"
  certified_full_A_upper: "-8.055917135809189e-7"
  theorem_status: CANDIDATE_FULL_PENDING_LATER_INDEPENDENT_REVIEW
  next_attack: tail-accelerated five-support optimization or multi-ratio tail envelope
```
