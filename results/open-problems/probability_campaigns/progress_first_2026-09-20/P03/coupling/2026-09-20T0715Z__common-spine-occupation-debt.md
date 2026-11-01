Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.

# P03-B coupling report — common-spine occupation bound and a two-sided history-debt certificate

**Status:** PROVED PARTIAL / NEW COUPLING LEMMAS. The full Lyons–Pemantle–Peres speed-monotonicity conjecture remains unresolved. This run removes a real restriction from the preceding P03-B theorem: instead of controlling repeated returns to one selected ancestor only when the opposite branch is fresh, it controls **all visits by both coupled walks to the entire pre-split common ancestral spine**, with arbitrary prior exploration of those vertices. The remaining obstruction is debt generated entirely inside post-split self-history, plus non-overlapping assignment of debt across successive split episodes.

**Native role:** P03-B, `6aabe777361481919c9e614646464772`, probabilistic regeneration/coupling role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`.

**Captured master before write:** `280de0f714bf4ba07e4c2fc43212526dd005443c`.

**Previous own checkpoint:** `probability_campaigns/progress_first_2026-09-20/P03/coupling/2026-09-20T0618Z__selected-ancestor-stack-envelope.md`, creation commit `85f2bde3b975967d17619d6cb72f37037f7d0791`.

**Complementary P03-A checkpoint consumed, not duplicated:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T0603Z__critical-edge-speed-asymptotic.md`, creation commit `76cc4d0d07441f633977c9c2978d13fdce90d1cb`. P03-A proves a new speed asymptotic as parent bias approaches `E Z`; the present report stays in the coupling regime `beta d>1`, equivalently parent bias `<d`, and does not redo its recursive escape analysis.

## 1. Minimal source continuity and normalization

Primary source: Gérard Ben Arous, Alexander Fribergh and Vladas Sidoravicius, *A proof of the Lyons-Pemantle-Pere[s] monotonicity conjecture for high biases*, arXiv:1111.5865, https://arxiv.org/abs/1111.5865 . The source is a supercritical Galton–Watson tree without leaves,

\[
P(Z=0)=0,
\]

and uses **outward child bias** `beta`: at a non-root vertex with `k` children,

\[
q_k(\beta):=P_\beta(\text{parent})=\frac1{1+\beta k},
\qquad
P_\beta(\text{each specified child})=\frac\beta{1+\beta k}.
\tag{1.1}
\]

Thus larger `beta` points farther from the root. The full source conjecture is increasing speed throughout the transient interval `beta>1/EZ`. The old arXiv abstract gives the historical high-bias constant `717`; it is not treated as the current frontier.

Bowditch--Tokushige, arXiv:1906.07913, prove differentiability in the ballistic/CLT regime and express the derivative through a Gaussian covariance, but do not prove its sign. Song--Wang--Xiang, *J. Appl. Probab.* 62 (2025), 1044--1052, prove in reciprocal parent bias `lambda=1/beta`, for minimum offspring `d>=2`, strict speed decrease on

\[
0\le \lambda\le \frac{d}{1+\sqrt{1-1/d}}.
\tag{1.2}
\]

A bounded literature refresh on 20 September 2026 found no checked source-wide resolution. This negative search is not a novelty or openness certificate.

The fixed full-source metric remains

`R_full: 1 -> 1`.

For the coupling theorem below assume the source-valid restricted family

\[
2\le d\le Z\le D<\infty,
\qquad \beta d>1.
\tag{1.3}
\]

The extra condition `beta d>1` is a coupling hypothesis, stronger than source transience in general. No claim outside (1.3) is made.

## 2. Inherited obstruction and what is improved here

The preceding P03-B report introduced

\[
Q=q_Z(\beta),\quad
\mu=EQ,\quad
a=q_d(\beta),\quad b=q_D(\beta),
\quad r=\frac1{\beta d},
\tag{2.1}
\]

and proved an exact posterior-selection identity plus a return-stack bound for one outward-selected ancestor. It showed that the whole repeated-return stack at that one ancestor is harmless under an explicit support-ratio condition, but only under a **clean comparator restriction**: at every synchronized comparison with the selected ancestor, the opposite branch had to be fresh.

That restriction is too strong for the real coupling. After a favorable split, either walk can revisit the whole ancestral history shared before the split. The aim here is therefore different:

> Bound, without any freshness assumption, the total amount of reverse-mismatch debt accumulated whenever either walk visits the **pre-split common ancestral spine**.

The key is not another posterior estimate. It is a quenched geometric occupation lemma for a geodesic spine.

## 3. Quenched distance-hitting bound

The previous report proved the distance-one form of the following lemma. The distance-`h` extension is what is needed for the more-biased branch.

### Lemma 3.1 — hitting an ancestor `h` levels away

Fix any rooted tree in which every vertex has at least `d` children and let a `beta`-biased walk satisfy `beta d>1`. If `v` is an ancestor of `w` at graph distance `h`, then

\[
\boxed{
P_w(T_v<\infty)\le r^h,
\qquad r:=\frac1{\beta d}<1.
}
\tag{3.1}
\]

The bound is quenched: it uses only the deterministic minimum degree and remains valid after arbitrary conditioning on previously explored parts of the tree.

#### Proof

Let `H_n=d(X_n,v)` until the walk hits `v`. At every non-root vertex on this stopped process, if the current vertex has `k>=d` children, the probability of decreasing `H` by one is

\[
q_k(\beta)=\frac1{1+\beta k}\le a:=\frac1{1+\beta d},
\]

while the probability of increasing `H` is at least `1-a`. Put

\[
r=\frac{a}{1-a}=\frac1{\beta d}.
\]

Then

\[
q_k r^{-1}+(1-q_k)r
\le a r^{-1}+(1-a)r=1.
\]

Hence `r^{H_n}` is a supermartingale until hitting `0`; stopping first between levels `0` and `N` and then sending `N->infinity` gives

\[
P_w(T_v<\infty)\le r^{H_0}=r^h.
\]

QED.

## 4. New geodesic-spine occupation lemma

Let `Gamma` be a fixed ancestral geodesic: at every vertex of `Gamma`, at most one child also belongs to `Gamma`. The walk may have explored arbitrary side branches before the time at which we start counting visits.

Define

\[
N_\Gamma:=\#\{n\ge0:X_n\in\Gamma\}
\]

from a time at which the walk is on `Gamma`.

### Lemma 4.1 — geometric occupation of an ancestral spine

Under (1.3), put

\[
\boxed{
s=s(\beta,d)
:=\frac{\beta(d-1)}{1+\beta d}
\left(1-\frac1{\beta d}\right)
=\frac{(d-1)(\beta d-1)}{d(1+\beta d)}.
}
\tag{4.1}
\]

Then, **for every previously explored environment and every starting vertex on `Gamma`**,

\[
\boxed{
P(N_\Gamma\ge n)\le(1-s)^{n-1},\qquad n\ge1,
}
\tag{4.2}
\]

and therefore

\[
\boxed{E N_\Gamma\le\frac1s.}
\tag{4.3}
\]

No freshness or independence of the vertices of `Gamma` is required.

#### Proof

Suppose the current spine vertex has `k>=d` children. At most one child lies on `Gamma`, so at least `k-1` children are off the spine. The probability that the next step chooses an off-spine child is

\[
\frac{\beta(k-1)}{1+\beta k}
\ge
\frac{\beta(d-1)}{1+\beta d},
\tag{4.4}
\]

because `(k-1)/(1+beta k)` increases with `k`.

After stepping to any such off-spine child, Lemma 3.1 with `h=1` says that the probability ever to return to the current spine vertex is at most `r=1/(beta d)`. Hence with conditional probability at least

\[
\frac{\beta(d-1)}{1+\beta d}(1-r)=s
\]

the walk leaves through an off-spine child and never comes back to the current vertex.

On a tree, every path from that off-spine subtree back to **any** point of `Gamma` must pass through the current spine vertex. Therefore on this event there are no further visits to `Gamma` at all.

Crucially, this argument is quenched and can be repeated after every spine visit, regardless of previous returns or explored side branches. Thus, conditional on having accumulated `n-1` visits, the probability of one more visit is at most `1-s`. Induction gives (4.2), and summing its tail gives (4.3). QED.

### Sharpness of the mechanism

For the regular `d`-ary tree, the one-step probability of taking an off-spine child is exactly

\[
\frac{\beta(d-1)}{1+\beta d},
\]

and the return probability from such a child to its parent is exactly `1/(beta d)`. Thus the side-escape hazard in (4.1) is exact for the regular geometry (away from root boundary effects). In particular, as `x=beta d downarrow1`,

\[
\frac1s\asymp\frac1{x-1}.
\tag{4.5}
\]

So any argument that uses only this support-uniform side-escape hazard cannot remove the near-critical `1/(beta d-1)` occupation growth. A future improvement has to use the actual degree/selection law, not merely `d` and `D`.

## 5. Application to a favorable split: all pre-split common-history visits

Couple a `beta` walk `X^-` and a more outward-biased `(beta+epsilon)` walk `X^+` with the same uniform random variable at each time, as in the source coupling. Suppose they are together at a vertex `x` and a favorable mismatch occurs:

* `X^+` moves to a child `y` of `x`;
* `X^-` moves to the parent `p=x^*`.

The radial gap therefore receives the deterministic credit

\[
\Delta_{\rm split}=+2.
\tag{5.1}
\]

Let `Gamma` be the **old common ancestral spine beginning at `p`** and continuing toward the root. The less-biased walk starts on `Gamma`, whereas the more-biased walk starts at distance two from `p`.

Define

\[
R_\epsilon
:=\left[q_d(\beta+\epsilon)-q_D(\beta)\right]_+.
\tag{5.2}
\]

At an arbitrary synchronized step, conditional on the two current offspring counts `K^+,K^-`, the expected radial-gap increment is

\[
2\{q_{K^-}(\beta)-q_{K^+}(\beta+\epsilon)\}.
\tag{5.3}
\]

Hence its adverse part is bounded by

\[
2\left[q_{K^+}(\beta+\epsilon)-q_{K^-}(\beta)\right]_+
\le2R_\epsilon.
\tag{5.4}
\]

This bound makes **no freshness assumption** on either current vertex.

### Theorem 5.1 — two-sided common-spine debt bound

Let `N^-_Gamma,N^+_Gamma` be the total numbers of visits of the two walks to `Gamma` after the favorable split (or the numbers before any earlier stopping time). Then

\[
\boxed{E N^-_\Gamma\le\frac1s,}
\tag{5.5}
\]

and

\[
\boxed{E N^+_\Gamma\le\frac{r^2}{s}.}
\tag{5.6}
\]

Consequently, the expected total **negative radial-gap increment occurring at times when at least one branch is on the pre-split common spine** is at most

\[
\boxed{
\mathcal D_{\rm common}(\epsilon)
\le
2R_\epsilon\frac{1+r^2}{s}.
}
\tag{5.7}
\]

In particular, the favorable `+2` split credit plus this entire common-history debt has expected value at least

\[
\boxed{
2\left[1-R_\epsilon\frac{1+r^2}{s}\right].
}
\tag{5.8}
\]

#### Proof

Equation (5.5) is Lemma 4.1 because `X^-` begins at `p in Gamma`.

For `X^+`, the starting vertex `y` is distance two from `p`; every route from `y` to `Gamma` must hit `p`. Lemma 3.1 for the `(beta+epsilon)` walk gives

\[
P_y(T_\Gamma<\infty)
\le\frac1{((\beta+\epsilon)d)^2}
\le r^2.
\]

After the first hit on `Gamma`, Lemma 4.1 applies with `beta+epsilon`. Since `s(beta,d)` is increasing in `beta`, the post-hit expected occupation is at most `1/s(beta,d)`. This proves (5.6).

At each time at which at least one walk lies on `Gamma`, (5.4) bounds the adverse expected increment by `2R_epsilon`. Counting a time twice if both walks lie on `Gamma` only enlarges the bound, so Tonelli and (5.5)--(5.6) give (5.7). Adding the initial credit (5.1) gives (5.8). QED.

### One-sided version

If one charges only negative increments that occur while the **less-biased branch** lies on the old common spine, then

\[
\boxed{
\mathcal D^-_{\rm common}(\epsilon)
\le\frac{2R_\epsilon}{s},
}
\tag{5.9}
\]

and the corresponding split-plus-debt subledger is positive whenever `R_epsilon<s`.

This is useful because it isolates exactly how much extra cost comes from allowing the more-biased branch itself to return two levels back into pre-split history: only the factor `r^2`.

## 6. Explicit support-ratio certificates

Set

\[
x:=\beta d>1,
\qquad
\kappa:=\frac Dd\ge1.
\tag{6.1}
\]

Then

\[
r=\frac1x,
\qquad
s=\frac{(d-1)(x-1)}{d(1+x)},
\tag{6.2}
\]

and at `epsilon=0`,

\[
R_0=q_d(\beta)-q_D(\beta)
=\frac{x(\kappa-1)}{(1+x)(1+\kappa x)}.
\tag{6.3}
\]

Because `q_d(beta+epsilon)<=q_d(beta)`,

\[
R_\epsilon\le R_0.
\tag{6.4}
\]

Therefore a finite-epsilon sufficient condition for positivity of the full two-sided common-spine subledger is

\[
\boxed{R_0(1+r^2)<s.}
\tag{6.5}
\]

After clearing positive denominators, (6.5) is exactly

\[
\boxed{
P_{d,\kappa}(x)
:=\kappa(d-1)x^3
-(2d-1)(\kappa-1)x^2
-(d-1)x
-d(\kappa-1)>0.
}
\tag{6.6}
\]

For every `d>=2` and `kappa>1`, `P_{d,kappa}(1)=-2d(kappa-1)<0`, while `P_{d,kappa}(x)->infinity`. Also

\[
P''_{d,\kappa}(x)
=6\kappa(d-1)x-2(2d-1)(\kappa-1)>0
\quad (x\ge1),
\tag{6.7}
\]

because at `x=1` the right side equals

\[
2\{\kappa(d-2)+2d-1\}>0.
\]

Thus `P'` is strictly increasing on `[1,infinity)`, so (6.6) has a unique root `x_cs>1`; the common-spine certificate holds exactly for `x>x_cs`.

For the one-sided less-biased-spine subledger, `R_0<s` is equivalent to the simpler quadratic condition

\[
\boxed{
\kappa(d-1)x^2
-(2d-1)(\kappa-1)x
-(d-1)>0.
}
\tag{6.8}
\]

### Example 1: offspring support `{2,3}`

Here `d=2`, `kappa=3/2`. The full two-sided common-spine condition is

\[
\boxed{3x^3-3x^2-2x-2>0.}
\tag{6.9}
\]

Its unique root above one is

\[
x_{cs}=1.64929530779172\ldots
\]

so the certificate holds for

\[
\boxed{
\beta>0.82464765389586\ldots,
\qquad
\lambda=1/\beta<1.21263911353622\ldots .
}
\tag{6.10}
\]

This is **not** a speed-monotonicity theorem on that interval. It says that, in this family, once a favorable split occurs, *all debt generated by both branches revisiting the entire pre-split common spine* is already dominated by the split credit throughout (6.10). The published source-uniform `d=2` theorem reaches parent bias `2/(1+1/sqrt(2))=1.171572875...`; thus the component certificate itself remains valid somewhat beyond that general interval.

The one-sided condition is

\[
3x^2-3x-2>0,
\]
which is equivalent to

\[
\boxed{\lambda<\frac{\sqrt{33}-3}{2}=1.372281323\ldots .}
\tag{6.11}
\]

### Example 2: offspring support `{3,4}`

Here `d=3`, `kappa=4/3`. The full two-sided condition becomes

\[
\boxed{8x^3-5x^2-6x-3>0,}
\tag{6.12}
\]

whose root is

\[
x_{cs}=1.37132673545661\ldots .
\]

Thus the full common-spine debt is dominated whenever

\[
\boxed{
\lambda<2.18766244574170\ldots .
}
\tag{6.13}
\]

Again this is a component theorem, not a replacement for the stronger restricted-family analytic intervals already proved by P03-A/NM13-05.

For the less-biased branch alone, (6.8) reduces to

\[
8x^2-5x-6>0,
\]
so

\[
\boxed{
\lambda<\frac{\sqrt{217}-5}{4}=2.432729965\ldots .
}
\tag{6.14}
\]

## 7. What this proves about the negative derivative mechanism

The previous local obstruction showed that individual score-response terms can be negative and that a single outward-selected ancestor produces a genuine first-order negative contribution. The clean-stack theorem then controlled repeated returns to one such ancestor when the comparator was fresh.

The present run proves something qualitatively stronger:

1. **Freshness of the old history is unnecessary.** Lemmas 3.1 and 4.1 are quenched and survive arbitrary previous exploration and conditioning.
2. **The entire common ancestral spine is controlled at once.** There is no need to sum a separate posterior debt estimate for each ancestor.
3. **The more-biased branch returning into old history is explicitly charged.** Its extra expected occupation costs only the factor `r^2`, because it starts two levels below the first old ancestor.
4. **The near-critical obstruction is now localized.** The support-uniform spine occupation necessarily scales like `(beta d-1)^{-1}`. Therefore a route that keeps the worst pair `R_0=q_d-q_D` cannot reach `beta d downarrow1` for a fixed nontrivial support width. Any near-critical advance must replace `R_0` by an annealed heterogeneity term that shrinks with the selected degree law, or move to P03-A's critical-edge machinery.

This is a rigorous localization of the negative contributions, not a heuristic simulation.

## 8. Remaining obstruction

The full source conjecture is still open. The theorem above controls only reverse debt at times when at least one branch lies on the **pre-split common spine**. It does **not** yet control reverse mismatches generated while both branches are off that spine but revisiting vertices created after the split.

That post-split self-history is now the precise coupling bottleneck. A naive repetition of Theorem 5.1 for every later path segment would double-count overlapping spines and split credits. Therefore the next proof step must be an **episode decomposition** assigning each historical reverse mismatch to a unique most-recent frontier/side-escape episode.

The natural candidate is:

* use Lemma 4.1 to end an episode whenever a branch takes an off-current-spine child and never returns;
* use the exact downcrossing chain from `2026-09-20T032221Z__exact-backstep-law-and-backstep-only-debt.md` as the clock for returns before that terminal side escape;
* replace the worst-pair `R_0` inside each episode by the posterior mean threshold deficit from the outward-selection identities of the `0512Z` and `0618Z` reports;
* prove that the resulting episode debts are disjoint and summable against the favorable split hazard.

If no non-overlapping assignment exists, the correct output of the next run should be a finite source-valid cylinder demonstrating that overlap is an intrinsic obstruction to this coupling architecture, followed by a pivot to the Bowditch--Tokushige covariance/spine representation.

## 9. Obligation ledger

| Item | Before | After this run |
|---|---|---|
| Full LPP monotonicity | OPEN | OPEN |
| One selected ancestor, fresh comparator | controlled | retained |
| Arbitrary previous exploration of old ancestors | unresolved | **controlled quenched** |
| All pre-split ancestors simultaneously | unresolved | **controlled by one geodesic occupation lemma** |
| More-biased branch returning to common history | unquantified | **extra factor `r^2`** |
| Post-split self-history off old spine | unresolved | unresolved; now isolated |
| Near `beta d=1` worst-pair divergence | qualitative | **proved `1/(beta d-1)` spine-occupation mechanism** |
| Simulation dependence | none needed | none |

**Result type:** PROVED PARTIAL. No full-source closure, no publication claim, no independent audit claim.

**Next attack:** construct a non-overlapping post-split episode decomposition and combine the geodesic side-escape hazard with the exact downcrossing chain and posterior threshold tilts. The first target is `{2,3}`, because (6.10) already removes the complete pre-split common-history debt slightly beyond the published source-uniform low-parent-bias interval, leaving a sharply isolated post-split term to estimate.
