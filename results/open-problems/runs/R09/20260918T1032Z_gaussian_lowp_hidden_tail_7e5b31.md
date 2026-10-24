Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO MOVEMENT on active R09 successor `CHEN-WANG-2025-GAUSSIAN-SUBUNIFORM`: `p_cert = 1/2 -> 1/2`; this is the second supported unchanged run after the admission-run movement. Tang periodic-tree and G0013 remain retired/frozen. Methods actually used: B7 TAKE THE LIMIT, B25 COUNT THE SAME THING TWICE, B30 DO ONE SCALE / ONE DIRECTION AT A TIME.**

# R09 CLOSABLE OUTSIDE — Gaussian harmonic-mean subuniformity: fixed-correlation hidden-tail theorem

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only.

## 1. Continuity, repository state, and source/current-status gate

I did **not** reopen Pengfei Tang Question 4.11 or G0013.

- Tang's periodic-tree clause remains **REFUTED / RETIRED** with the physical percolation branch and periodicity hypotheses already verified in the retired package; its metric remains frozen at `UNBOUNDED_ABOVE`. The transitive-graph clause remains open.
- G0013 / Catalano--Lavenant remains **OPEN_CURRENT / PARTIAL / HANDOFF_READY / retired from active R09** after its six-run CLOSABLE handoff, with frozen upper endpoint
  \[
  U_*=\frac{1289727882057511}{11918000000000000}=0.10821680500566462\ldots.
  \]
- The active exclusive R09 claim is still `operations/claims/CHEN-WANG-2025-GAUSSIAN-SUBUNIFORM.md`.

At run start I reread/refreshed the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the active claim, the newest complete R09 report

`runs/R09/20260918T0932Z_gaussian_comonotone_first_variation_c4f2e9.md`,

and current neighboring R08/R10 directory state. The newest visible R08 report is on the unrelated E0011 catalyst successor, so it creates no ownership collision. Repository-wide exact-key search continues to identify this Gaussian-subuniformity source as R09-owned.

### Current literature check, 2026-09-18

Primary source: Yuyu Chen, Ruodu Wang, Yuming Wang and Wenhao Zhu, *Subuniformity of harmonic mean p-values*, Canadian Journal of Statistics, DOI `10.1002/cjs.70017`, arXiv:2405.01368. The served full text says in Section 7 that the positive-Gaussian case is not known in the literature and in Section 8 explicitly conjectures subuniformity for Gaussian copulas with positive correlation coefficients. It also remarks that the inflation issue is expected to be less severe at extremely small significance levels.

Fresh searches on the exact title, arXiv identifier, `Gaussian copulas with positive correlation coefficients`, `harmonic mean p-values Gaussian copula subuniformity 2026`, and the low-tail / Huesler--Reiss terminology recovered the source and general Gaussian-extreme-value literature but no later primary paper that resolves this exact conjecture. This is bounded negative evidence, **not** a novelty certificate.

A later author paper, Chen--Lin--Wang, *Universal Value-at-Risk superadditivity*, arXiv:2606.22884 (22 June 2026), develops UVS/WUVS and preservation machinery. The bounded search still did not locate a theorem there specifically establishing WUVS for standard Pareto margins under arbitrary positive Gaussian copulas. The WUVS reformulation from the preceding R09 report therefore remains useful but does not itself close the source.

## 2. Frozen metric

The controlling metric is

`p_cert` = smallest lower endpoint such that the source inequality is rigorously proved simultaneously for every `p in [p_cert,1)`, every dimension, every positive-correlation Gaussian copula, every source-valid positive weight vector, and every `r<=-1`.

Smaller is better. The admission run proved the full upper-half theorem, so the supported value is `1/2`. The theorem below is bivariate and its small-`p` endpoint depends on `(rho,w)`, hence it does **not** move the full-source metric:

\[
\boxed{p_{\rm cert}:\frac12\longrightarrow\frac12.}
\]

Supported unchanged count on this target: `1 -> 2`.

## 3. B7 — take the limit: the hidden lower-tail measure of a Gaussian copula

The previous run solved a neighborhood of the comonotone covariance for every fixed significance window bounded away from zero. The complementary singular question is what happens as `p downarrow 0` at a **fixed** positive correlation.

Fix a bivariate standard Gaussian pair `(X,Y)` with correlation

\[
0<\rho<1,
\]

and put

\[
U=\Phi(X),\qquad V=\Phi(Y),\qquad
C_\rho(u,v)=\Pr(U\le u,V\le v).
\]

Define

\[
\beta:=\frac1{1+\rho}\in\left(\frac12,1\right).
\]

### Lemma R09-GAUSS-HIDDEN-TAIL

For every fixed `a,b>0`,

\[
\boxed{
\frac{C_\rho(pa,pb)}{C_\rho(p,p)}\longrightarrow (ab)^\beta
\qquad(p\downarrow0).
}
\tag{3.1}
\]

Equivalently, on bounded continuity sets in `(0,\infty)^2`, the rescaled measures

\[
\nu_p(A):=\frac{\Pr\{(U/p,V/p)\in A\}}{C_\rho(p,p)}
\]

converge vaguely to the measure

\[
\boxed{
\nu(da\,db)=\beta^2 a^{\beta-1}b^{\beta-1}\,da\,db.
}
\tag{3.2}
\]

### Proof

Write

\[
z_p=\Phi^{-1}(p)=-s,
\qquad s\to\infty.
\]

The normal tail ratio gives, for each fixed `a>0`,

\[
\Phi^{-1}(pa)
=-s+\frac{\log a}{s}+o(s^{-1}).
\tag{3.3}
\]

Set positive lower-tail score thresholds

\[
s_a:=-\Phi^{-1}(pa)
=s-\frac{\log a}{s}+o(s^{-1}),
\]

and similarly `s_b`. By symmetry,

\[
C_\rho(pa,pb)=\Pr(X\ge s_a,Y\ge s_b).
\]

The bivariate Gaussian density has exponent

\[
Q(x,y)=\frac{x^2-2\rho xy+y^2}{2(1-\rho^2)}.
\]

Make the corner scaling

\[
x=s_a+\frac r s,
\qquad
y=s_b+\frac t s,
\qquad r,t\ge0.
\]

Uniformly on bounded `(r,t)`, expansion around `(s,s)` yields

\[
Q(x,y)
=
\frac{s^2}{1+\rho}
+\frac{r+t-\log a-\log b}{1+\rho}
+o(1).
\tag{3.4}
\]

The Jacobian is `s^{-2}`. Dominated Laplace comparison outside a fixed corner box is supplied by the positive definite quadratic form and gives the same exponential envelope for numerator and denominator. Hence the ratio of the two corner integrals tends to

\[
\exp\!\left(\frac{\log a+\log b}{1+\rho}\right)
=(ab)^\beta,
\]

which proves (3.1). Rectangular increments of (3.1) give (3.2). `QED`

This is the hidden-regular-variation scale that the ordinary asymptotic-independence statement suppresses: for fixed `rho<1`, the simultaneous lower tail is smaller than order `p`, but after normalizing by `C_rho(p,p)` it has a nontrivial homogeneous limit.

## 4. B25 — count the same tail twice: strips versus the harmonic wedge

Now fix a weight

\[
0<w<1
\]

and the weighted harmonic mean

\[
H_w=\left(\frac wU+\frac{1-w}{V}\right)^{-1}.
\]

The source inequality in this bivariate case is

\[
\Pr(H_w\le p)\ge p.
\]

Two disjoint mechanisms compete at small `p`.

### 4.1 Single-big-jump strips

Each of

\[
E_1=\{U\le wp\},\qquad E_2=\{V\le(1-w)p\}
\]

implies `H_w<=p`. Therefore

\[
\Pr(E_1\cup E_2)
=p-C_\rho(wp,(1-w)p).
\tag{4.1}
\]

So the union of the obvious one-coordinate events falls **below** `p` by exactly the simultaneous-overlap term. A proof must recover at least that much mass from points for which neither coordinate alone is extreme enough.

### 4.2 Interior harmonic wedge

Scale

\[
a=U/p,\qquad b=V/p.
\]

Outside the two strips, the remaining part of `{H_w<=p}` is the wedge

\[
D_w:=\left\{a>w,\ b>1-w,\ \frac wa+\frac{1-w}{b}\ge1\right\}.
\tag{4.2}
\]

For a finite `M`, let

\[
D_{w,M}=D_w\cap\{a\le M,b\le M\}.
\]

This is a bounded continuity set for the limit measure, and it is disjoint from `E_1\cup E_2`. Hence

\[
\Pr(H_w\le p)-p
\ge
\Pr\{(U/p,V/p)\in D_{w,M}\}
-C_\rho(wp,(1-w)p).
\tag{4.3}
\]

By the hidden-tail lemma,

\[
\liminf_{p\downarrow0}
\frac{\Pr(H_w\le p)-p}{C_\rho(p,p)}
\ge
\nu(D_{w,M})-[w(1-w)]^\beta.
\tag{4.4}
\]

Letting `M->infinity` by monotone convergence reduces the sign to one explicit integral.

Scale `a=wx`, `b=(1-w)y`. Then

\[
\nu(D_w)=[w(1-w)]^\beta J_\beta,
\tag{4.5}
\]

where

\[
J_\beta
:=
\beta^2\iint_{\substack{x>1,y>1\\x^{-1}+y^{-1}\ge1}}
 x^{\beta-1}y^{\beta-1}\,dx\,dy.
\]

Solving the wedge boundary for `y` gives

\[
J_\beta
=
\beta\int_1^\infty
x^{\beta-1}\left[\left(\frac{x}{x-1}\right)^\beta-1\right]dx
\tag{4.6}
\]

and, with `r=1/x`,

\[
J_\beta
=
\beta\int_0^1
r^{-\beta-1}\bigl[(1-r)^{-\beta}-1\bigr]dr.
\tag{4.7}
\]

The integrand is positive and integrable for `1/2<beta<1`. Evaluating the convergent difference by the incomplete-Beta formula before passing to the endpoints (equivalently, by the positive binomial series and the standard Beta summation) gives

\[
\boxed{
J_\beta
=1+(2\beta-1)B(1-\beta,1-\beta)>1.
}
\tag{4.8}
\]

Thus the interior wedge has strictly more hidden-tail mass than is lost to the overlap of the two single-coordinate strips.

Combining (4.4)--(4.8) and then `M->infinity` gives the quantitative lower-tail margin

\[
\boxed{
\liminf_{p\downarrow0}
\frac{\Pr(H_w\le p)-p}{C_\rho(p,p)}
\ge
[w(1-w)]^\beta(2\beta-1)B(1-\beta,1-\beta)>0.
}
\tag{4.9}
\]

### Theorem R09-GAUSS-BIVARIATE-LOW-P

For every fixed

\[
0<\rho<1,\qquad 0<w<1,
\]

there exists

\[
p_0=p_0(\rho,w)>0
\]

such that

\[
\boxed{
\Pr\!\left\{\left(\frac wU+\frac{1-w}{V}\right)^{-1}\le p\right\}>p
\quad\text{for every }0<p<p_0,
}
\tag{4.10}
\]

when `(U,V)` has the bivariate Gaussian copula with correlation `rho`.

Since generalized power means are increasing in their order,

\[
M_r^{(w,1-w)}(U,V)\le M_{-1}^{(w,1-w)}(U,V)=H_w
\qquad(r\le-1),
\]

so the same strict subuniformity conclusion holds for every source order `r<=-1` on this fixed bivariate low-threshold regime.

### Why this is genuinely different from the previous run

The comonotone first-variation theorem controls `rho` near one for thresholds bounded away from zero. The present theorem instead fixes **any** `rho<1`, however close to one, and enters the singular `p->0` tail. Neither theorem contains the other.

This also turns the source paper's qualitative remark that extreme significance levels should be less problematic into an explicit rigorous theorem for the full bivariate positive-Gaussian family at each fixed correlation and fixed interior weight.

## 5. B30 — one scale at a time: the only bivariate boundary layer left

The fixed-correlation proof deliberately does **not** claim uniformity as `rho->1`. Its normalization itself signals where it must fail to be uniform.

The classical Gaussian triangular-array extreme-value transition occurs when

\[
4\log n\,(1-\rho_n)\to\gamma,
\]

the Huesler--Reiss scale. Translating the extreme-tail size `n` to a significance level `p` identifies the singular joint regime

\[
\boxed{
1-\rho\asymp\frac1{\log(1/p)}.
}
\tag{5.1}
\]

The two existing R09 mechanisms now cover the complementary non-singular directions:

1. **Fixed `rho<1`, `p->0`:** solved by Theorem R09-GAUSS-BIVARIATE-LOW-P above.
2. **`rho->1`, `p` bounded below by `p_0>0`:** solved locally by the previous comonotone first-variation theorem.

What neither covers is the coupled boundary layer (5.1), in which `p->0` and `rho->1` together. That is now the exact bivariate obstruction, rather than a vague statement that near-comonotone numerical quadrature is difficult.

The natural next object is a Huesler--Reiss-type limiting measure for

\[
\frac{\Pr(H_w\le p)-p}{p}
\quad\text{or a matched simultaneous-tail scale}
\]

under

\[
(1-\rho)\log(1/p)\to c\in(0,\infty).
\]

If its limiting margin can be shown nonnegative uniformly in `c` and `w`, the fixed-correlation theorem and the previous comonotone theorem become candidates for a complete **bivariate** proof by compactness/matching. That would still be PARTIAL relative to the source, because arbitrary dimension and arbitrary positive-correlation matrices remain.

### Why I did not jump to `n>2`

The strip/wedge decomposition is exact and clean in two dimensions. In dimension `n>=3`, inclusion--exclusion creates pair, triple, and higher simultaneous-tail corrections, while the harmonic interior region can compensate them in overlapping ways. A pairwise argument is not automatically valid for a general positive-correlation matrix. In particular, the source target is not reduced to bivariate margins. I therefore do **not** promote (4.10) to the full source conjecture and do not move `p_cert`.

## 6. Method outcomes

- **B7 TAKE THE LIMIT — success.** The bivariate Gaussian lower tail has an exact hidden-homogeneous limit with exponent `beta=1/(1+rho)`, yielding a tractable limiting measure for the harmonic event.
- **B25 COUNT THE SAME THING TWICE — success.** The subuniformity deficit from double-counting the two one-coordinate strips is exactly a copula-overlap term; the interior harmonic wedge beats that overlap by the positive Beta constant in (4.9).
- **B30 ONE SCALE / ONE DIRECTION AT A TIME — success as an obstruction isolation.** Fixed positive correlation is now solved at sufficiently small `p`; the remaining bivariate singular direction is the Huesler--Reiss boundary layer `1-rho ~ 1/log(1/p)`.

This is research movement in theorem scope, but **not movement of the frozen full-source metric**.

## 7. Status, novelty discipline, and closure obligations

Status remains **PARTIAL / OPEN_CURRENT**.

What is proved on the page here:

- an exact fixed-`rho` hidden-tail scaling lemma for the bivariate Gaussian copula;
- an explicit positive asymptotic lower bound (4.9);
- strict low-`p` subuniformity for every fixed bivariate `rho in (0,1)` and every fixed interior weight `w`;
- the same conclusion for all source orders `r<=-1` by power-mean monotonicity.

What is **not** proved:

- a `p_0` uniform in all `rho,w`;
- the singular joint `p->0`, `rho->1` boundary layer;
- arbitrary dimension or arbitrary positive-correlation matrices;
- the full source conjecture;
- publication novelty.

The Gaussian corner Laplace asymptotic and Huesler--Reiss scaling are classical mechanisms and must be cited as such in any paper. The particular harmonic-wedge comparison and Beta margin have not been located in the bounded search, but negative search evidence is not a priority certificate.

There is no finite core in this analytic theorem, so I did not manufacture an exact-arithmetic checker merely to produce a receipt. The proof is written on the page, as required.

## 8. Next route

If the next run again fails to move `p_cert`, it will be the third supported unchanged run and must execute the full Section-I stuck protocol rather than append another ordinary lemma.

The most useful next attack, if undertaken before/inside that protocol, is to work on the singular matched scale rather than repeat fixed-`rho` tail asymptotics. Fresh method numbers reserved for the next attempt are **B12** (find the conserved exponent/intensity measure in the Huesler--Reiss interpolation), **B19** (turn the limiting margin into a one-parameter certified algorithm in `c` and `w`), and **B27** (swap the quantifiers to test whether a uniform bivariate threshold can be proved before attempting arbitrary dimension).

## 9. Structured ledger delta

```yaml
ledger_delta:
  track: R09
  allocation: CLOSABLE_OUTSIDE
  active_target: CHEN-WANG-2025-GAUSSIAN-SUBUNIFORM
  metric: p_cert
  before: 1/2
  after: 1/2
  movement: no
  supported_unchanged_before: 1
  supported_unchanged_after: 2
  status: PARTIAL / OPEN_CURRENT
  methods_used: [7, 25, 30]
  new_result:
    - fixed-rho bivariate Gaussian hidden-tail measure
    - strict low-p harmonic-mean subuniformity for every fixed rho in (0,1) and w in (0,1)
    - liminf margin = at least [w(1-w)]^beta (2beta-1) B(1-beta,1-beta) times C_rho(p,p)
  remaining_bivariate_obstruction: "joint p->0, rho->1 boundary layer, (1-rho) log(1/p)=Theta(1)"
  tang_q411_periodic_tree: RETIRED / REFUTED / FROZEN
  g0013: RETIRED / HANDOFF_READY / FROZEN
  shared_roots_modified: false
  peer_files_modified: false
  email_or_drive: false
  scheduler_modified: false
```

## 10. Model / scheduler-control statement

The actual runtime metadata available to this report identifies the model as **GPT-5.6 Sol**; reasoning effort is **UNVERIFIED**. The exposed scheduler-management schema still has controls for prompt/title/schedule/timing/enabled state but no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model telemetry, and no guaranteed hour-long execution. Therefore the requested GPT-6/maximum setting remains prompt text only in this environment.

The historical P26 `You cannot modify this task` result is an authorization-context issue. The legitimate remedies remain the owning authorized context, an ownership/admin transfer where supported, or platform support. Duplicating the task or bypassing permissions is not a valid workaround. No scheduler or permission operation was attempted in this run.
