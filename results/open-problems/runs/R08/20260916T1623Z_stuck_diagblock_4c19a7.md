Model: GPT-5.6 Sol. Reasoning level: UNVERIFIED — the scheduler exposes no model/reasoning selector, so GPT-6 maximum is not verified and is not claimed. **NO MOVEMENT: frozen strict-gap metric remains \(c=0\to0\); consecutive unchanged-run count = 3, so this is STUCK-PROTOCOL EPISODE 1.**
Problem/source: strict convexity of the two-dimensional first-passage-percolation limit shape — Auffinger, Damron and Hanson (2015/2017), arXiv:1511.03262, **Question 4 in §2.5.1**, catalogued again as Question 4 in §8; detailed discussion §2.8.

# R08 HARD OUTSIDE — stuck report: axis/diagonal gap bottleneck and exact finite-block recovery test

Run ID: `20260916T1623Z_stuck_diagblock_4c19a7`  
Date checked: 2026-09-16  
Repository: `yspennstate/math-open-problems`, branch `master`  
Source target: **OPEN**  
Frozen pair:
\[
u=e_1=(1,0),\qquad v=e_2=(0,1).
\]
Frozen metric:
\[
\Delta_{12}
=
\mu(e_1)+\mu(e_2)-\mu(e_1+e_2)
=
2\mu(e_1)-\mu(1,1),
\]
with tracked quantity equal to the largest positive \(c\) for which this track has proved
\[
\Delta_{12}\ge c.
\]
Before: no positive \(c\); certified lower bound \(0\).  
After: no positive \(c\); certified lower bound \(0\).  
One positive frozen-pair gap would be **PARTIAL**, not full strict convexity.

Because this is the third consecutive unchanged run, I follow the owner's stuck protocol: **no new R08 lemma is claimed in this report.** I identify the exact obstruction, catalogue the failed routes, name the missing ingredient and simplest open special case, compare with the nearest solved theorem, and choose exactly one recovery: **reduce the obstruction to an exact finite computation and run it.**

## 1. Repository recovery and source gate

Read before the stuck analysis:

- `probability_campaign_2026_09/INDEX.md`;
- `probability_campaign_2026_09/RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/FLEET_2026-09-16.md`;
- `operations/RFLEET_2026-09-16.md`;
- newest own report `runs/R08/20260916T1528Z_fpp_axis_transition_3b7c92.md`;
- newest neighboring R07 report found on master:
  `runs/R07/2026-09-16T1525Z_kpz_deep_edges_03.md`;
- newest neighboring R09 report found on master:
  `runs/R09/20260916T153057Z_5c8e2a1f.md`;
- targeted searches across the current `probability_1000_intake_*` material and campaign catalogue.

The very large intake JSONL files are truncated by the connector before a literal row-by-row model-visible read of all roughly 780 records is possible. I record intake ingestion as **PARTIAL / targeted because of connector output truncation**, not as a fictitious complete read. Current ownership/source searches found no posted/settled version of this exact Exp(1) frozen gap and no competing current owner. The pair admission was already recorded once by R08 and is not reopened.

`RESULTS.md` remains P26-owned and its R08 row lags the repository-native R08 reports. I do not edit shared root ledgers or peer files.

No Gmail, Drive, email, public posting, paid access, permission change or schedule change occurred.

## 2. Exact source locator, attribution and current literature check

Primary source, checked again 2026-09-16:

- Auffinger--Damron--Hanson, arXiv:1511.03262v2.
- §2.5 is “Properties of the limit shape.”
- **§2.5.1 is “Flat edges for limit shapes.”**
- In that section, **Question 4** is:
  “Show that if \(F\) is a continuous distribution then the limit shape is strictly convex.”
- The same question is catalogued again as **Question 4 in §8**.
- §2.8 is “Strict convexity of the limit shape”; it treats strict convexity as conjectural and distinguishes it from the stronger uniform-curvature Question 11.

Historical attribution:

- ADH attribute the **FPP model** to Hammersley--Welsh (1965).
- I found no statement in ADH attributing this exact strict-convexity Question 4 to Hammersley--Welsh themselves.
- The standard early flat-edge countermechanism is Durrett--Liggett (1981), with later percolation-cone refinement by Marchand (2002).
- Lalley (2003) gives a conditional strict-convexity theorem, not an unconditional exponential-law result.

Dated status searches on 2026-09-16 included:

1. exact ADH Question-4 wording plus `strict convexity continuous first-passage percolation`;
2. `strict convexity exponential first-passage percolation 2025 2026`;
3. `2 mu(e1) mu(1,1) first passage percolation`;
4. later-author/citing work around Dembin--Elboim--Peled, Jacquet, and current FPP notes;
5. Alm--Parviainen 2002 rigorous time-constant bounds and directional/diagonal searches.

Outcome:

- no primary-source closure of ordinary iid Exp(1) nearest-neighbor strict convexity was found in the bounded current search;
- Dembin--Elboim--Peled's quantitative planar coalescence theorem assumes the limit shape has more than 32 extreme points, so it cannot be used to prove the shape hypothesis here;
- Jacquet's strict comparison
  \(\mu(x)<\vec\mu(x)\)
  between unrestricted and directed FPP is a different inequality and does not imply
  \(2\mu(e_1)>\mu(1,1)\);
- recent differentiability work found by search concerns different continuous-action FPP models;
- Alm--Parviainen's accessible abstract confirms rigorous lower/upper time-constant bounds and exponential numerics, but the primary numerical table needed to certify a diagonal bound below the present threshold was not accessible in this run. No purchase or access bypass was attempted.

This is a bounded search outcome, not a proof that no such result exists.

## 3. Retained state that creates the current bottleneck

I do not re-prove the retained claims.

### R08-L001 — safe uniform-limit compiler

If one constructs paths \(P_n\) with
\[
\mathbb ET(P_n)
\le
\mathbb ET(0,nu)
+
\mathbb ET(nu,n(u+v))
-\gamma n+o(n),
\qquad \gamma>0,
\]
then standard \(L^1\) time-constant convergence gives
\[
\mu(u+v)\le\mu(u)+\mu(v)-\gamma.
\]

### R08-X001 — shared-bypass obstruction

Linearly many positive one-edge deletion margins need not tensorize: a single common bypass can support all of them. A positive-density surgery proof therefore needs a conflict-controlled jointly usable family or a bounded-preimage resampling map.

### R08-L002 — diamond equivalence

For the frozen pair,
\[
\Delta_{12}=0
\quad\Longleftrightarrow\quad
\mathcal B
=
\{x:|x_1|+|x_2|\le1/\mu(e_1)\}.
\]
Thus a positive frozen-pair gap is exactly the task of ruling out the \(\ell^1\)-diamond for Exp(1).

### R08-X002 — finite pointwise strictness is impossible

There are exact finite positive-probability Exp(1) cylinder events on which the concatenated axis legs are the unique geodesic and satisfy exact finite triangle equality. Therefore no proof can rely on “every finite environment has a proportional strict shortcut.”

### R08-L003 — retained certified axis lower bound

The previous run proved by a finite-memory self-avoiding-path transition-matrix certificate
\[
\mu(e_1)\ge\frac{3753}{12500}=0.30024.
\]
This is useful auxiliary information but did not move the frozen metric.

## 4. STUCK obligation (a): the exact blocking statement

The source-relevant frozen obligation is

\[
\boxed{
\Delta_{12}
=
2\mu(e_1)-\mu(1,1)>0.
}
\tag{BLOCK}
\]

Given retained L003, the following strictly stronger numerical statement is sufficient:

\[
\boxed{
\mu(1,1)
<
2\cdot\frac{3753}{12500}
=
\frac{3753}{6250}
=
0.60048.
}
\tag{BLOCK-DIAG}
\]

No route currently supplies either (BLOCK) directly or the certified directional upper bound (BLOCK-DIAG).

## 5. STUCK obligation (b): routes tried and exact failure of each

### 5.1 Independent local detours

**Failure:** R08-X001. Individual deletion margins can all be generated by one common bypass. Multiplying local improvement probabilities is invalid.

### 5.2 Pointwise finite-scale strict triangle inequality

**Failure:** R08-X002. Exact equality survives on open positive-probability finite cylinder events. Any valid argument must be typical/expected/asymptotic, not pointwise in every environment.

### 5.3 Positive-density cross-leg surgery

**Failure:** R08-L001 shows exactly what would suffice, but no argument so far proves a linear expected *jointly usable* saving after controlling conflict/overlap between cross-leg bypasses. This is the missing positive-density step, not the limit passage.

### 5.4 Busemann/coalescence

**Failure:** quantitative planar coalescence results found in the current literature either assume nontrivial shape information (for example, more than 32 extreme points) or are not strong enough to rule out a shared supporting face without differentiability/curvature hypotheses. Importing R07's KPZ target would be circular and is forbidden.

### 5.5 Lalley conditional strict convexity

**Failure:** Lalley's theorem assumes asymptotic straightness of geodesics and centered limiting passage-time distributions after rescaling. ADH explicitly describe these hypotheses as out of reach. Neither is proved here for Exp(1).

### 5.6 Directed-FPP strict comparison

**Failure:** Jacquet proves \(\mu(x)<\vec\mu(x)\) under suitable assumptions, but no theorem was found giving the missing bridge
\[
\vec\mu(1,1)\le2\mu(e_1).
\]
Thus the comparison is not direction-to-direction strict convexity.

### 5.7 Axis lower bound plus diagonal upper bound

**Failure:** L003 supplies
\[
2\mu(e_1)\ge0.60048,
\]
but the bounded literature search did not find a rigorously certified
\[
\mu(1,1)<0.60048.
\]
The accessible Alm--Deijfen simulations strongly suggest directional variation but are simulations, not a proof; the paper itself notes that available rigorous directional bounds are too crude for rigorous direction comparison.

### 5.8 Finite-size numerical extrapolation

**Failure:** a finite simulation or floating estimate for
\(\mathbb ET(0,n(1,1))/n\) does not certify the asymptotic gap without a rigorous upper construction. No KPZ convergence rate may be assumed.

## 6. STUCK obligation (c): what a successful proof must contain that current routes do not

At least one of the following genuinely new ingredients is necessary:

1. **a direction-sensitive certified upper construction**
   \[
   \mu(1,1)<0.60048,
   \]
   for example an exact finite-state/block strategy with a rigorously evaluated expected cost; or

2. **a conflict-controlled cross-leg surgery theorem** producing
   \[
   \gamma n-o(n)
   \]
   expected saving for some explicit \(\gamma>0\), which L001 would convert to the strict gap.

The current routes have local improvement mechanisms and safe limit compilers, but none has a rigorous source of linear *jointly usable* saving or an exact diagonal upper bound below 0.60048.

## 7. STUCK obligation (d): simplest special case still unproved

The simplest quantitative special case is now

\[
\boxed{
\mu(1,1)<\frac{3753}{6250}=0.60048.
}
\tag{SPECIAL}
\]

A particularly concrete sufficient finite version is to find one integer \(m\) for which

\[
\boxed{
U_m
:=
\frac1m
\mathbb E T_{[0,m]^2}\bigl((0,0),(m,m)\bigr)
<
\frac{3753}{6250}.
}
\tag{FINITE}
\]

Why (FINITE) is sufficient: translate the square block by
\((km,km)\), concatenate the within-block geodesics, and use the iid block
environment/SLLN. The resulting infinite concatenated path has asymptotic
cost \(U_m\) per diagonal increment \(n\), while unrestricted FPP is no
slower. Hence \(\mu(1,1)\le U_m\).

This is a recovery criterion, not a claimed new milestone.

## 8. STUCK obligation (e): nearest solved theorem and what it has that we lack

The nearest source-matching theorem is Lalley (2003), *Strict Convexity of
the Limit Shape in First-Passage Percolation*. For linearly independent
directions \(u,v\), Lalley proves the strict convex-combination inequality
assuming two directionwise inputs:

1. high-probability asymptotic straightness/confinement of geodesics in
   arbitrarily narrow cones;
2. a centered nondegenerate scaling limit for the passage times.

His block-percolation construction uses those hypotheses to make suitable
crossing blocks likely enough to build an infinite comparison route.

For ordinary iid Exp(1) on \(\mathbb Z^2\), neither hypothesis is available
at the required unconditional strength. That is exactly why Lalley's theorem
cannot be imported to close (BLOCK).

A second nearby solved comparison is Jacquet's unrestricted-versus-directed
strict inequality; its proof has a model-restriction asymmetry absent from
the present comparison of two undirected directions.

## 9. Exactly one recovery chosen: reduce (SPECIAL) to finite computation and run it

**Chosen recovery:** “reduce the obstruction to a finite computation and
run it.”

No other recovery option is pursued in this stuck run.

For \(m=1,2,3\), I computed
\[
\mathbb ET_{[0,m]^2}((0,0),(m,m))
\]
by exact rational dynamic programming for the exponential Richardson/FPP
infection process.

For an infected vertex set \(S\), let \(b(S)\) be the number of boundary
edges from \(S\) to its complement, and let \(r_S(v)\) be the number of
boundary edges from \(S\) to one outside vertex \(v\). Exponential
memorylessness gives the exact recursion
\[
E(S)
=
\frac1{b(S)}
+
\sum_{v\notin S}
\frac{r_S(v)}{b(S)}E(S\cup\{v\}),
\]
with \(E(S)=0\) after the target is infected. The checker evaluates this
recursion with Python `Fraction`, not floating-point arithmetic.

Exact results:

\[
U_1=\frac54=1.25,
\]
\[
U_2=\frac{30757}{28800}\approx1.0679513889,
\]
\[
U_3=
\frac{5675443731448268047}{5807171543040000000}
\approx0.9773163561.
\]

Every one is strictly larger than
\[
\frac{3753}{6250}=0.60048.
\]

Therefore:

\[
\boxed{
\text{No full-square independent-block certificate with }m\le3
\text{ proves (SPECIAL).}
}
\]

This is negative finite evidence only. It does **not** show that larger
blocks fail; indeed the finite criterion remains a viable exact route if a
scalable state compression can evaluate sufficiently large blocks.

Exact artifact:

- `artifacts/R08/20260916T1623Z_stuck_diagblock_4c19a7_checker.py`
  - creation/readback commit:
    `ad51400c6fb8485c8ec5259f2408059e7aba7483`
  - readback blob:
    `b0599ef8048e80442c637959d74de2a0486a8ec9`
  - local SHA-256:
    `847cc57c6f6c08efa559d8e37642f58d9d66abb31a3985ac16b75d28d3881aad`.

Archived output:

- `artifacts/R08/20260916T1623Z_stuck_diagblock_4c19a7_checker.out`
  - creation/readback commit:
    `f32bb9a34d7607180063ee90a9cfe846edc85b17`
  - readback blob:
    `25a1b68028977c3a758a941428b30be4e8b299d7`
  - local SHA-256:
    `1c395d9929b3dfa2c5c700aab0748cac6e9ccb04a7b7e484e0542db5cb604b97`.

The executed output ends `ALL_EXACT_CHECKS_PASS`.

### Interpretation for the next R08 run

The direct subset recursion grows too quickly to be a sensible route to
large \(m\). If the finite-block recovery is continued, the next useful
object is **not** a larger brute-force square; it is a transfer-matrix or
frontier-state compression for a fixed-width diagonal strip, with rigorous
monotone width bounds. This report does not claim such a construction.

This is stuck rescue 1. A later third stuck episode on this same problem
requires handoff/rotation under the owner protocol; no counter is reset by
the finite computation because the frozen metric did not move.

## 10. Independent audit of newest R09 package

Audit ID:
`R08-AUDIT-R09-PASSAGE-L1-01`

Package:
`runs/R09/20260916T153057Z_5c8e2a1f.md`,
claim `R09-PASSAGE-L1`.

**Verdict: PASS for the stated compiler.**

R09 defines
\[
A_L=\{0\leftrightarrow\partial[-L,L]^3\},
\qquad
R_L^{(1)}=\{0\leftrightarrow S_L\},
\quad
S_L=\{x:\|x\|_1=L\}.
\]

### 10.1 Geometric inclusion

Any nearest-neighbor path from \(0\) to the \(\ell^\infty\)-boundary of
\([-L,L]^3\) ends at a vertex whose \(\ell^1\)-norm is at least \(L\).
Along a nearest-neighbor path, the \(\ell^1\)-norm changes by exactly
\(1\) at each step. Starting from \(0\), the path must therefore first hit
\(\ell^1\)-norm exactly \(L\). Hence
\[
A_L\subseteq R_L^{(1)}.
\]
This part is correct.

### 10.2 Exact coordinate count

For \(r\ge1\),
\[
|S_r|
=
6+12(r-1)+4(r-1)(r-2)
=
4r^2+2.
\]
Therefore
\[
|B_L^{(1)}|
=
1+\sum_{r=1}^L(4r^2+2)
=
\boxed{
\frac{4L^3+6L^2+8L+3}{3}
}.
\]
The exact checker independently enumerates the lattice ball for
\(L=1,\ldots,20\) and matches this polynomial in every case.

### 10.3 Re-derivation of the arcsine passage inequality

For an increasing event \(A\) in \(N\) iid Bernoulli(\(s\)) variables, set
\[
a(s)=P_s(A),
\qquad
I_i(s)=P_s(i\text{ pivotal}),
\qquad
g_i=\frac{X_i-s}{\sqrt{s(1-s)}}.
\]
The \(g_i\)'s are orthonormal. Monotonicity gives
\[
\operatorname{Cov}(1_A,X_i)
=
s(1-s)I_i(s).
\]
Hence Bessel's inequality gives
\[
s(1-s)\sum_i I_i(s)^2
\le
a(s)(1-a(s)).
\]
Russo's formula and Cauchy--Schwarz imply
\[
a'(s)
\le
\sqrt{
\frac{N\,a(s)(1-a(s))}
{s(1-s)}
}.
\]
With
\[
\Psi(x)=\arcsin\sqrt{x},
\]
this becomes
\[
\frac{d}{ds}\Psi(a(s))
\le
\sqrt N\,\Psi'(s).
\]
Integrating from \(q\) to \(p\),
\[
\boxed{
\Psi(P_p(A))-\Psi(P_q(A))
\le
\sqrt N[\Psi(p)-\Psi(q)].
}
\]
Thus the retained `PASS.4` dependency is correct.

For site percolation in \(\mathbb Z^3\), R09 uses the elementary
\(p_c\ge1/5\) SAW union bound and the published Campanino--Russo
\(p_c<1/2\). For \(0<\delta\le1/10\),
\[
[p_c-\delta,p_c]\subset[1/10,1/2].
\]
On this interval
\[
\Psi'(s)=\frac1{2\sqrt{s(1-s)}}\le\frac53,
\]
since
\[
s(1-s)\ge\frac9{100}.
\]
The exact checker certifies the squared endpoint equality
\[
\left(\frac53\right)^2 4\frac9{100}=1.
\]

Combining with \(A_L\subseteq R_L^{(1)}\) gives exactly the R09
`PASSAGE-L1` inequality with the smaller coordinate count
\[
V_L=(4L^3+6L^2+8L+3)/3.
\]

**Independent audit verdict: PASS.**

The Campanino--Russo strict inequality is treated as a published imported
dependency, not as something re-proved by this audit.

## 11. Cumulative ledger and exact next obligation

Retained R08 mathematical state:

- `R08-X001`: PROVED route obstruction, shared bypass prevents naive
  tensorization.
- `R08-L001`: PROVED reduction, linear expected usable saving implies a
  positive strict gap.
- `R08-L002`: PROVED reduction, frozen equality iff the whole shape is the
  \(\ell^1\)-diamond.
- `R08-X002`: PROVED route obstruction, finite equality survives positive
  probability cylinder events.
- `R08-L003`: PROVED auxiliary axis lower bound
  \(\mu(e_1)\ge3753/12500\), with novelty relative to all historical
  transition-matrix bounds still not asserted.
- frozen source-relevant metric: **OPEN, \(c=0\), no movement for three
  consecutive repository-native runs**.

No new R08 lemma is added in this stuck report.

The chosen finite recovery did not cross the needed threshold. The remaining
finite-computation obligation is exactly:
\[
\text{find a scalable exact construction proving }
\mu(1,1)<0.60048,
\]
or abandon this rescue at the next stuck episode in favor of the single
alternative chosen then under the owner protocol.

## Structured ledger delta

```yaml
ledger_delta:
  task: "R08 HARD OUTSIDE"
  source: "Auffinger-Damron-Hanson, arXiv:1511.03262v2 (2015), Question 4 in §2.5.1; catalogued in §8; strict-convexity discussion §2.8"
  target: "For iid Exp(1) undirected nearest-neighbor FPP on Z^2, prove a positive strict triangle gap for the frozen pair e1,e2; one-pair success is PARTIAL toward full strict convexity"
  frozen_pair: "u=e1=(1,0), v=e2=(0,1)"
  metric: "largest proved positive c with 2*mu(e1)-mu(1,1) >= c"
  before: "no positive c; certified lower bound 0"
  after: "no positive c; certified lower bound 0"
  status: "OPEN"
  unchanged_count: 3
  stuck_protocol_episode: 1
  chosen_recovery: "reduce obstruction to finite computation and run it"
  recovery_result: "exact full-square block values m=1,2,3 all exceed 0.60048; no metric movement"
  exact_evidence:
    - "artifacts/R08/20260916T1623Z_stuck_diagblock_4c19a7_checker.py @ ad51400c6fb8485c8ec5259f2408059e7aba7483, blob b0599ef8048e80442c637959d74de2a0486a8ec9"
    - "artifacts/R08/20260916T1623Z_stuck_diagblock_4c19a7_checker.out @ f32bb9a34d7607180063ee90a9cfe846edc85b17, blob 25a1b68028977c3a758a941428b30be4e8b299d7"
  audit_ids: []
  peer_audit_given:
    - "R08-AUDIT-R09-PASSAGE-L1-01=PASS"
  remaining_obligation: "prove 2*mu(e1)>mu(1,1); within chosen finite rescue, certify mu(1,1)<3753/6250=0.60048 by a scalable exact finite-state/block construction"
```
