Model: GPT-5.6 Sol. Reasoning level: UNVERIFIED — the scheduler exposes no model/reasoning selector, so GPT-6 maximum is not verified and is not claimed. NO MOVEMENT: frozen metric c remains 0 -> 0.
Problem: strict convexity of the 2D first-passage-percolation limit shape — Auffinger–Damron–Hanson, *50 years of first passage percolation* (arXiv:1511.03262), Question 4 in §2.5.1; detailed discussion §2.8.

# R08 HARD OUTSIDE — axis-pair gap, diamond equivalence, and exact finite obstruction

Run ID: `2026-09-16T1429Z_fpp-diamond-gap-7e4a9c`
Date checked: 2026-09-16
Status: **OPEN**

## 1. Repository recovery, source, and admission state

Read before working:
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/FLEET_2026-09-16.md`, `operations/RFLEET_2026-09-16.md`;
- root inventory / current probability-intake metadata and targeted `probability_1000_intake_*` searches;
- newest own report `runs/R08/2026-09-16T1329Z_fpp-axis-gap-a1c93e.md`;
- neighboring newest R07 and R09 reports.

The large intake JSONL files cannot all be materialized row-by-row in one connector response because the GitHub connector truncates oversized resources. I therefore record intake ingestion as **PARTIAL / targeted** rather than claiming a complete literal read of ~780 rows. The current admission does not rely on a stale intake `admitted=true` field.

The previous R08 run already recorded the one-time admission decision. I do not re-admit or silently switch pairs here. The frozen pair remains
\[
u=e_1=(1,0),\qquad v=e_2=(0,1),
\]
and the fixed metric remains
\[
\Delta_{12}:=\mu(e_1)+\mu(e_2)-\mu(e_1+e_2)
=2\mu(e_1)-\mu(1,1),
\]
with tracked lower bound
\[
c_*:=\sup\{c>0:\Delta_{12}\ge c\text{ has been proved by R08}\}.
\]

Before this run: no positive bound; certified numerical lower bound `c=0` by the triangle inequality.

After this run: **no positive bound; `c=0` remains the largest certified lower bound in this track.**

This is the first unchanged run after the repository-native baseline, so `unchanged_count: 1`. It is not yet a stuck-protocol run.

A proof that \(\Delta_{12}>0\) would remain only a **PARTIAL one-pair milestone**, not full strict convexity.

## 2. Original source locator / historical attribution / current status

Primary source checked 2026-09-16:
- Auffinger–Damron–Hanson, arXiv:1511.03262, **Question 4 in §2.5.1 (“Flat edges for limit shapes”)** asks: show that if the passage-time distribution is continuous, then the limit shape is strictly convex.
- The same survey's **§2.8 (“Strict convexity of the limit shape”)** discusses strict convexity as conjectural and treats uniform positive curvature separately.
- Lalley (2003) is cited there as a conditional strict-convexity theorem, not a solution for iid Exp(1).
- The survey attributes the FPP model/program itself to Hammersley–Welsh (1965). I found no source attribution saying that Hammersley–Welsh themselves formulated this exact numbered strict-convexity question.

Dated current-status checks, 2026-09-16:
- searched the exact Question-4 wording and combinations of `first passage percolation strict convexity continuous exponential limit shape`;
- searched for a theorem specifically proving \(2\mu(e_1)>\mu(1,1)\);
- checked Lalley (2003) scope;
- checked Dembin–Elboim–Peled (GAFA 2024): their quantitative coalescence theorem assumes the limit shape has more than 32 extreme points; their many-sides theorem applies to bounded near-constant laws such as `Uniform[1,1+epsilon]`, not Exp(1);
- checked Jacquet (2024) strict comparison of unrestricted and directed FPP time constants: this is a different inequality and does not imply the frozen directional strict triangle gap;
- checked Bakhtin–Dow differentiability results: they concern a different continuous-action FPP model;
- checked van den Berg–Kesten strict monotonicity / “more variable” FPP comparison and Alm–Parviainen finite/numerical time-constant bounds as nearby techniques.

No primary-source resolution of ordinary iid Exp(1) nearest-neighbor FPP strict convexity, and no proof of the frozen gap \(\Delta_{12}>0\), was found in this bounded current search. This is a search outcome, not a proof of nonexistence.

Access limitation: the full Alm–Parviainen numerical table was not available through the publisher text reached in this run; only bibliographic/abstract/search snippets were available. No unverified numerical diagonal bound is imported.

## 3. R08-L002 — the frozen gap is exactly the non-diamond problem

**Status: PROVED reduction.**

Let
\[
a:=\mu(e_1)=\mu(e_2)>0,
\]
where equality follows from the dihedral symmetries of iid nearest-neighbor FPP on \(\mathbb Z^2\). Let
\[
\mathcal B=\{x:\mu(x)\le1\}.
\]
Then
\[
\boxed{
\Delta_{12}=0
\quad\Longleftrightarrow\quad
\mathcal B=
\left\{x\in\mathbb R^2:|x_1|+|x_2|\le\frac1a\right\}.
}
\tag{L002}
\]

### Proof

Put
\[
p=\frac{e_1}{a},\qquad q=\frac{e_2}{a}.
\]
By positive homogeneity of the time constant,
\[
\mu(p)=\mu(q)=1,
\]
so \(p,q\in\partial\mathcal B\).

Assume first that \(\Delta_{12}=0\). Then
\[
\mu(e_1+e_2)=2a.
\]
For the midpoint
\[
m=\frac{p+q}{2}=\frac{e_1+e_2}{2a},
\]
positive homogeneity gives
\[
\mu(m)=\frac{\mu(e_1+e_2)}{2a}=1,
\]
so \(m\in\partial\mathcal B\).

Because \(\mathcal B\) is a compact convex set and \(m\) is a boundary point, there is a supporting linear functional \(\ell\) such that
\[
\ell(x)\le1\quad(x\in\mathcal B),
\qquad
\ell(m)=1.
\]
Since
\[
1=\ell(m)=\frac{\ell(p)+\ell(q)}2
\]
and \(p,q\in\mathcal B\) imply \(\ell(p),\ell(q)\le1\), both must equal 1. Thus the supporting line contains both \(p\) and \(q\). Its equation is
\[
x_1+x_2=\frac1a,
\]
and therefore
\[
\mathcal B\subseteq\left\{x:x_1+x_2\le\frac1a\right\}.
\]

The law is invariant under coordinate sign flips. Applying those symmetries to the preceding support inequality gives all four inequalities
\[
\pm x_1\pm x_2\le\frac1a.
\]
Their intersection is the \(\ell^1\)-diamond
\[
D:=\left\{x:|x_1|+|x_2|\le\frac1a\right\}.
\]
Hence \(\mathcal B\subseteq D\).

Conversely, \(\pm p,\pm q\in\mathcal B\), and convexity implies their convex hull lies in \(\mathcal B\). But that convex hull is exactly \(D\). Therefore \(D\subseteq\mathcal B\), and
\[
\mathcal B=D.
\]

For the converse, if \(\mathcal B=D\), then its Minkowski functional is
\[
\mu(x)=a(|x_1|+|x_2|).
\]
Thus
\[
\mu(e_1+e_2)=2a=\mu(e_1)+\mu(e_2),
\]
so \(\Delta_{12}=0\). \(\square\)

### Consequence

For this frozen pair, the one-pair milestone is not merely “one local strict triangle inequality”; it is equivalent to excluding the **entire \(\ell^1\)-diamond** as the Exp(1) limit shape.

This does not solve the milestone: no source-verified theorem ruling out that diamond for Exp(1) was found this run.

## 4. R08-X002 — exact finite counterexample to pointwise finite-scale strict saving

**Status: PROVED route obstruction. This does not refute the source problem or the frozen asymptotic gap.**

For every integer \(m\ge1\), consider the finite nearest-neighbor box
\[
\{0,1,\ldots,m\}^2.
\]
Let
\[
A=(0,0),\qquad B=(m,0),\qquad C=(m,m).
\]
Assign weight 1 to every bottom horizontal edge and every right-boundary vertical edge. Assign
\[
H=10m+1
\]
to every other edge.

The L-shaped route
\[
A\to B\to C
\]
has cost \(2m\). Every competing \(A\)-to-\(B\), \(B\)-to-\(C\), or \(A\)-to-\(C\) path uses at least one off-L edge and therefore costs at least \(H>2m\). Consequently
\[
T(A,B)=m,
\qquad
T(B,C)=m,
\qquad
T(A,C)=2m,
\]
and all three minimizers are unique. In particular,
\[
\boxed{T(A,C)=T(A,B)+T(B,C)}.
\tag{X002.1}
\]

This equality is not a measure-zero artifact. Put
\[
\delta=\frac{1}{100m}.
\]
On the open cylinder event in which every L-route edge lies in
\[
(1,1+\delta)
\]
and every off-L edge lies in
\[
(H,H+\delta),
\]
the L-route cost is strictly less than
\[
2m(1+\delta)<H,
\]
while every competitor costs more than \(H\). Hence the same concatenated L-route remains the unique geodesic. Under iid Exp(1), this finite cylinder event has strictly positive probability.

Therefore there can be no proof of the frozen asymptotic strict gap based on a deterministic or almost-sure **uniform finite-box strict-saving inequality valid in every environment**. Positive-density / expected / typical-environment input is genuinely necessary.

Exact checker:
- `artifacts/R08/2026-09-16T1429Z_fpp-diamond-gap-7e4a9c_checker.py`
- write/readback commit `c521a0b5b1f4ded8cde8d235b20212ddcf12ee3f`;
- blob SHA `cf36d2b7b4c29aa0a8192dfcabba49a358e9ac1a`.

Archived output:
- `artifacts/R08/2026-09-16T1429Z_fpp-diamond-gap-7e4a9c_checker.out`
- write/readback commit `d626fe26642083db5cbc38fc5278a6669477b197`;
- blob SHA `227874d9589b090d1662db9dee2df25ec836a105`.

The exact `Fraction`/Dijkstra checker verifies \(m=1,\ldots,12\), uniqueness, exact finite triangle equality, and the positive-volume cylinder inequality.

## 5. Failed / insufficient quantitative routes checked this run

### 5.1 Axis-lower-bound plus diagonal-upper-bound route

The literature search surfaced a rigorous lower-bound snippet of the form
\[
\mu(e_1)>0.298
\]
attributed to the Alm--Parviainen line of work. To turn this into a strict gap one would need a rigorously sourced upper bound
\[
\mu(1,1)<0.596.
\]
I did not locate such a certified diagonal upper bound in an accessible primary source this run.

Exploratory directed finite-block calculations were not elevated to a theorem: without an exact expectation bound and a proof that the finite-block value beats `0.596`, a simulation or floating-point estimate is not evidence for the fixed metric.

### 5.2 Directed-FPP comparison route

Jacquet's strict inequality between unrestricted and directed FPP time constants gives a real strict comparison for the same direction, but I found no valid theorem of the form
\[
\vec\mu(1,1)\le2\mu(e_1).
\]
Without that missing comparison, Jacquet's theorem does not imply \(\Delta_{12}>0\).

### 5.3 van den Berg--Kesten positive-density bypass route

The strict-monotonicity method for comparing passage-time distributions is a genuine nearby positive-density surgery technique. But the geometry needed here is different. The concatenation relevant to
\[
\mu(e_1)+\mu(e_2)
\]
consists of geodesic legs. A bypass whose endpoints lie on only one leg cannot improve that leg, by geodesicity. A profitable directional surgery must connect across the two legs or otherwise change their global concatenation. R08-X001 shows that many one-edge margins may share one bypass; R08-X002 now shows that at finite scale the two legs can be isolated so completely that equality persists on an open cylinder event.

Thus the missing statement is a **typical positive-density cross-leg interaction theorem**, not merely a local-detour theorem.

### 5.4 finite-size bias warning

Even if one constructs a finite block whose expected diagonal route is strictly cheaper than a particular finite concatenation, a proof of the asymptotic gap must control
\[
\mathbb E T(0,Le_1)-L\mu(e_1)
\]
without assuming KPZ, curvature, or an unproved convergence rate. Retained R08-L001 remains the clean safe limit compiler: prove a linear expected saving directly relative to the two finite point-to-point passage times, with only \(o(n)\) loss.

## 6. Independent audit of R09-PASSAGE-02

**Audit status: PASS.**

Audited package:
- `runs/R09/20260916T133200Z_dd3613bd0a.md`;
- claim `R09-PASSAGE-02`.

R09 states: if \(E\) is an increasing event depending on \(N\) independent Bernoulli coordinates and
\[
0\le q\le p\le1,
\]
then
\[
0\le P_p(E)-P_q(E)
\le
1-(1-(p-q))^N
\le
N(p-q).
\tag{A1}
\]

### Independent proof

Take iid \(U_1,\ldots,U_N\sim\mathrm{Uniform}[0,1]\), and define
\[
X_i^{(q)}=1_{\{U_i\le q\}},
\qquad
X_i^{(p)}=1_{\{U_i\le p\}}.
\]
Then coordinatewise
\[
X^{(q)}\le X^{(p)}.
\]
Since \(E\) is increasing,
\[
1_E(X^{(q)})\le1_E(X^{(p)}),
\]
which proves nonnegativity in (A1). If the two indicators differ, at least one coordinate must differ, hence at least one \(U_i\in(q,p]\). Therefore
\[
P_p(E)-P_q(E)
\le
P(\exists i:U_i\in(q,p])
=1-(1-(p-q))^N.
\]
Finally Bernoulli's inequality / the union bound gives
\[
1-(1-x)^N\le Nx
\qquad(0\le x\le1).
\]
This proves (A1). \(\square\)

### Exact finite audit

The R08 checker independently enumerates **all monotone Boolean events** on \(N=1,2,3,4\) coordinates. The counts are
\[
3,6,20,168,
\]
respectively, and four rational \((q,p)\) pairs are checked exactly with `Fraction` arithmetic. Total exact event/parameter checks:
\[
788.
\]
All pass.

Audit evidence:
- checker commit `c521a0b5b1f4ded8cde8d235b20212ddcf12ee3f`;
- output commit `d626fe26642083db5cbc38fc5278a6669477b197`.

No R09 conjectural conclusion is imported into R08.

## 7. Cumulative R08 state relevant to the current route

Retained from the previous repository-native run:
- `R08-X001` — many positive individual deletion margins can share one common bypass; naive productization fails.
- `R08-L001` — a linear expected jointly usable saving \(\gamma n-o(n)\) against the two finite passage times implies the strict asymptotic gap \(\Delta_{12}\ge\gamma\).

New this run:
- `R08-L002` — \(\Delta_{12}=0\) iff the entire Exp(1) limit shape is the \(\ell^1\)-diamond with axis radius \(1/\mu(e_1)\).
- `R08-X002` — exact positive-probability finite environments can preserve concatenation equality at every chosen finite scale; pointwise finite strict saving is impossible as a route.
- independent audit `R09-PASSAGE-02 = PASS`.

No positive metric movement: \(c=0\to0\).

## 8. Next attack

The frozen-pair target can now be restated safely as:
\[
\boxed{\text{prove that the iid Exp(1) limit shape is not the }\ell^1\text{-diamond}.}
\]

Two source-relevant routes remain worth pursuing.

### Route A — certified finite diagonal upper bound

Find a rigorous primary-source or exactly certified finite-block upper bound for \(\mu(1,1)\), and combine it with the strongest rigorous lower bound for \(\mu(e_1)\). The quantitative target is explicitly
\[
U_{\rm diag}<2L_{\rm axis}.
\]
No floating-point simulation counts. The finite-block expectation and all passage-time inequalities must be certified, and the asymptotic comparison must use subadditivity without an unproved finite-size rate.

### Route B — positive-density cross-leg surgery

Port the logic, not the conclusion, of van den Berg--Kesten strict monotonicity. The new theorem would need to prove that for the axis-axis concatenation there are linearly many **cross-leg** opportunities whose gains survive a bounded-conflict extraction / bounded-preimage resampling. R08-X001 and X002 are mandatory adversarial tests for any candidate inequality. Retained L001 then turns a verified linear expected saving into a positive \(c\).

The Busemann route remains available, but nothing from R07's KPZ target, curvature, or differentiability may be assumed.

## 9. ledger_delta

```yaml
ledger_delta:
  task: "R08 HARD OUTSIDE"
  source: "Auffinger–Damron–Hanson, arXiv:1511.03262, Question 4 (§2.5.1; detailed discussion §2.8)"
  target: "iid Exp(1) undirected nearest-neighbor FPP on Z^2 has no nontrivial boundary line segment"
  frozen_pair:
    u: "(1,0)"
    v: "(0,1)"
  metric: "largest proved positive c with mu(u)+mu(v)-mu(u+v) >= c"
  before: "0 certified; no c>0 proved"
  after: "0 certified; no c>0 proved"
  movement: "no movement"
  status: "OPEN"
  unchanged_count: 1
  exact_evidence:
    - "R08-L002 complete diamond-equivalence proof in this report"
    - "R08-X002 exact checker: artifacts/R08/2026-09-16T1429Z_fpp-diamond-gap-7e4a9c_checker.py @ c521a0b5b1f4ded8cde8d235b20212ddcf12ee3f"
    - "checker output: artifacts/R08/2026-09-16T1429Z_fpp-diamond-gap-7e4a9c_checker.out @ d626fe26642083db5cbc38fc5278a6669477b197"
  audit_ids:
    - "R09-PASSAGE-02@runs/R09/20260916T133200Z_dd3613bd0a.md"
    - "R08-independent-audit-certificate@c521a0b5b1f4ded8cde8d235b20212ddcf12ee3f/d626fe26642083db5cbc38fc5278a6669477b197"
```

No Gmail, Drive, email, public publication, permission change, purchase, or schedule change occurred.
