Model: GPT-5.6 Sol. Reasoning level: UNVERIFIED — the runtime exposes no model/reasoning selector, so GPT-6 maximum is not verified and is not claimed. **NO MOVEMENT: frozen strict-gap metric remains c = 0 -> 0; consecutive unchanged-run count = 2.**
Problem/source: strict convexity of the two-dimensional first-passage-percolation limit shape — Auffinger, Damron and Hanson (2015), arXiv:1511.03262, Question 4 (catalogued in §8; arising in §2.5.1, with detailed discussion in §2.8).

# R08 HARD OUTSIDE — certified axis bound and strict-gap bottleneck

Run ID: `20260916T1528Z_3b7c92`
Date checked: 2026-09-16
Repository: `yspennstate/math-open-problems`, branch `master`.
Status of source target: **OPEN**.
Frozen pair: \(u=e_1=(1,0)\), \(v=e_2=(0,1)\).
Frozen metric:
\[
\Delta_{12}:=\mu(e_1)+\mu(e_2)-\mu(e_1+e_2)
            =2\mu(e_1)-\mu(1,1),
\]
and the largest proved positive lower bound \(c\) with \(\Delta_{12}\ge c\).
Before this run: no positive \(c\); certified \(c=0\).
After this run: no positive \(c\); certified \(c=0\).
A positive gap for this one pair would be a **PARTIAL** milestone, not full strict convexity.

## 1. Repository recovery and admission/status check

I started by reading the campaign control files required by the task:

- `probability_campaign_2026_09/INDEX.md`;
- `probability_campaign_2026_09/RANKING.md`;
- root `POSTED.md`;
- root `RESULTS.md`;
- root `QUEUE.md`;
- `operations/FLEET_2026-09-16.md`;
- `operations/RFLEET_2026-09-16.md`.

The current repository rules say that P26 is the sole writer of the shared root ledgers. R08 therefore does **not** edit `RESULTS.md`, `POSTED.md`, `QUEUE.md`, or another track.

I continued from the newest immutable R08 report actually present:
`runs/R08/2026-09-16T1429Z_fpp-diamond-gap-7e4a9c.md`.

The neighboring reports actually read were:

- R07: `runs/R07/2026-09-16T1425Z_kpz_weighted_overlap_02.md`;
- R09: `runs/R09/20260916T143433Z_6f3c9a8e.md`.

The intake files under the discovered `probability_1000_intake_*` trees were read-attempted through the GitHub connector. Their very large JSONL responses are truncated by the connector before all roughly 780 rows can be materialized model-side. I therefore record intake ingestion as **PARTIAL due output truncation**, not as a fictitious complete line-by-line reread. I did not use any stale `admitted=true` flag as current verification.

The `(e1,e2)` admission was recorded once in the previous R08 canonical run and is not being reopened here. The current `INDEX`, `RANKING`, `POSTED` and ownership searches still show no posted/settled result for this exact Exp(1) strict gap.

## 2. Source locator, history, and dated literature check

The original source locator is exact:

- Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262.
- Section 2.5.1 is **“Flat edges for limit shapes.”**
- Section 2.8 is **“Strict convexity of the limit shape.”**
- The summary in §8 states **Question 4**:
  “Show that if \(F\) is a continuous distribution then the limit shape is strictly convex.”

The survey also states in §1.1 that FPP was introduced by Hammersley and Welsh in 1965. Its historical discussion says their original paper addressed the first-order time-constant question. I found no source statement attributing this exact strict-convexity Question 4 to Hammersley--Welsh themselves; I therefore do not make that attribution.

Dated web/arXiv searches on 2026-09-16 covered:

1. `"Question 4" continuous distribution strictly convex first-passage percolation Auffinger Damron Hanson`;
2. `"Strict convexity of the limit shape" first passage percolation exponential 2026`;
3. `"2 mu(e_1)" "mu(1,1)" first passage percolation`;
4. `"time constant" exponential lower bound 0.298 0.300 square lattice`;
5. Alm--Parviainen 2002 transition-matrix bounds and later citations;
6. current strict-convexity / differentiability / coalescence papers.

Scope/result:

- No primary-source closure of ordinary nearest-neighbor iid Exp(1) strict convexity was found.
- Lalley (2003) gives sufficient conditions involving asymptotic straightness and centered passage-time limits; it is not unconditional closure.
- Dembin--Elboim--Peled (2024) obtain quantitative coalescence under an extreme-point hypothesis on the limit shape; this cannot be inserted here.
- Recent differentiability results surfaced for different continuous-action models, not this lattice problem.
- Jacquet's strict unrestricted-vs-directed time-constant inequality does not by itself imply \(2\mu(e_1)>\mu(1,1)\).
- A 2026 FPP lecture note still quotes the classical Exp(1) axis lower bound \(\mu(e_1)\ge0.298\), attributed to Janson (1981).
- Alm--Parviainen (2002) explicitly use a transition-matrix method for lower bounds and give exponential-distribution numerics. The accessible abstract does not expose their numerical table. Because this run's new auxiliary bound is also a transition-matrix/self-avoiding-walk certificate, **novelty is UNVERIFIED**. I do not claim that the numerical constant below improves every published bound unless the inaccessible primary table is checked.

No purchase or access bypass was attempted.

## 3. Retained strict-gap reductions and failed routes

The newest R08 state is retained, not rederived.

- `R08-L001` (PROVED reduction): if one constructs paths \(P_n\) with
  \[
  E T(P_n)\le E T(0,nu)+E T(nu,n(u+v))-\gamma n+o(n),
  \]
  then the subadditive \(L^1\) limit gives
  \(\mu(u+v)\le\mu(u)+\mu(v)-\gamma\).

- `R08-L002` (PROVED reduction): for the frozen pair,
  \[
  \Delta_{12}=0
  \iff
  \mathcal B
  =
  \{x:|x_1|+|x_2|\le1/\mu(e_1)\}.
  \]
  Thus the one-pair milestone is exactly the problem of ruling out the
  \(\ell^1\)-diamond for Exp(1).

- `R08-X001` (PROVED route obstruction): positive deletion margins at linearly many edges need not tensorize; one common bypass can support all of them.

- `R08-X002` (PROVED route obstruction): exact finite concatenation equality can hold on an open positive-probability Exp(1) cylinder event, so no pointwise finite-scale “every environment has a proportional shortcut” inequality can work.

The Busemann/coalescence route remains available only if its hypotheses are proved inside this task. Nothing from R07's KPZ target, curvature, differentiability, or a conjectural coalescence rate is imported.

## 4. R08-L003 — an exact finite-state lower bound for the axis time constant

**Label: PROVED auxiliary theorem; this does not move the frozen strict-gap metric. Novelty relative to the complete time-constant literature is UNVERIFIED.**

For ordinary iid Exp(1) FPP on \(\mathbb Z^2\),
\[
\boxed{\mu(e_1)\ge \frac{3753}{12500}=0.30024.}
\tag{L003.1}
\]

The proof is a self-avoiding-path union bound with a finite-memory transfer-matrix certificate.

### 4.1 A finite automaton that contains every simple lattice path

Use the four step directions
\[
E=(1,0),\quad W=(-1,0),\quad N=(0,1),\quad S=(0,-1).
\]

A state is a word of \(K=5\) directions whose induced six consecutive lattice vertices are all distinct. From a state, append a direction only if the new endpoint is not any of the six vertices in the current state; then drop the oldest direction.

This transition rule is deliberately stronger than mere five-step-window self-avoidance, but **every globally simple path obeys it**. Hence the language accepted by the automaton is a superset of all globally simple paths.

The exact checker reconstructs the automaton in lexicographic product order and obtains
\[
284\ \text{states},\qquad 780\ \text{transitions}.
\tag{L003.2}
\]

### 4.2 Tilted path count

Set
\[
z=\frac{22}{7}.
\]
For a transition whose appended step has horizontal displacement
\(\Delta x\in\{-1,0,1\}\), give it weight \(z^{\Delta x}\).
Let \(M=M(z)\) be the resulting \(284\times284\) nonnegative rational matrix.

The artifact contains a positive integer vector \(V\in\mathbb N^{284}\). Exact Fraction arithmetic verifies
\[
MV\le\Lambda V
\quad\text{coordinatewise},\qquad
\Lambda=\frac{2407}{500}=4.814.
\tag{L003.3}
\]
The largest exact Collatz ratio in the certificate is
\[
\frac{3194866008}{663661477}
<\frac{2407}{500}.
\tag{L003.4}
\]

Let \(A_m\) be the accepted \(m\)-step words. For \(m\ge5\), writing
\(x(\omega)\) for net horizontal displacement, the finite initial-state
factor gives a constant \(C_0<\infty\), independent of \(m\), such that
\[
\sum_{\omega\in A_m} z^{x(\omega)}
\le C_0\Lambda^{m-5}.
\tag{L003.5}
\]
Indeed, if \(\mathbf 1\) is the all-one vector and \(V_{\min}>0\), then
\(\mathbf1\le V/V_{\min}\), so
\[
M^{m-5}\mathbf1
\le
\Lambda^{m-5}V/V_{\min}.
\]
Multiplying by the finitely many initial five-step weights proves L003.5.

If \(N_{m,n}\) denotes the number of globally simple \(m\)-edge paths from
\(0\) to \(ne_1\), each such path is accepted and has tilt weight \(z^n\).
Therefore
\[
\boxed{
N_{m,n}
\le
C_0 z^{-n}\Lambda^{m-5}.
}
\tag{L003.6}
\]

### 4.3 Exact exponential Chernoff sum

Take
\[
c=\frac{3753}{12500},
\qquad
\lambda=\frac{38141}{10000}.
\]
For a fixed simple \(m\)-edge path, its passage time is
\(\Gamma(m,1)\). For any \(\lambda>0\),
\[
P\{\Gamma(m,1)\le cn\}
\le
e^{\lambda cn}(1+\lambda)^{-m}.
\tag{L003.7}
\]

Because every positive-weight geodesic is simple and any path from \(0\) to
\(ne_1\) has at least \(n\) edges, L003.6--L003.7 give for \(n\ge5\)
\[
\begin{aligned}
P\{T(0,ne_1)\le cn\}
&\le
C_0\Lambda^{-5}z^{-n}e^{\lambda cn}
\sum_{m\ge n}\left(\frac{\Lambda}{1+\lambda}\right)^m\\
&=
\frac{C_0\Lambda^{-5}}{1-\rho}
\left[
\frac{e^{\lambda c}}{z}\rho
\right]^n,
\end{aligned}
\tag{L003.8}
\]
where the exact ratio is
\[
\boxed{
\rho=\frac{\Lambda}{1+\lambda}
=\frac{48140}{48141}<1.
}
\tag{L003.9}
\]

It remains only to certify that the bracket in L003.8 is below one.
The checker uses no floating point. Put
\[
x=\lambda c.
\]
For \(N=7\),
\[
e^x
\le
\sum_{j=0}^{N}\frac{x^j}{j!}
+
\frac{x^{N+1}/(N+1)!}{1-x/(N+2)},
\tag{L003.10}
\]
because every subsequent Taylor-term ratio is at most \(x/(N+2)<1\).
Exact rational arithmetic verifies this upper bound is strictly smaller than
\[
z\frac{1+\lambda}{\Lambda}
=
\frac{529551}{168490}.
\tag{L003.11}
\]
Equivalently the exact certified upper bound on the geometric base is
\[
\boxed{
B_{\rm cert}
=
\frac{
1763031998444794647628492877476787682970207494388420720474247583237963607
}{
1763045466426177978515625000000000000000000000000000000000000000000000000
}
<1.
}
\tag{L003.12}
\]

Thus
\[
\sum_{n=1}^{\infty}P\{T(0,ne_1)\le cn\}<\infty.
\]
Borel--Cantelli implies
\[
\liminf_{n\to\infty}\frac{T(0,ne_1)}n\ge c
\quad\text{a.s.}
\]
The standard FPP time-constant limit then gives L003.1.

### 4.4 Why L003 does not move the task metric

The frozen quantity is not \(\mu(e_1)\); it is
\[
\Delta_{12}=2\mu(e_1)-\mu(1,1).
\]
L003 would yield a positive strict gap as soon as one proves the independent
upper bound
\[
\boxed{
\mu(1,1)<2\cdot\frac{3753}{12500}
=\frac{3753}{6250}
=0.60048.
}
\tag{L003.13}
\]

No rigorously certified diagonal upper bound below \(0.60048\) was found or
proved this run. Floating simulations or finite-size extrapolation are not
admissible evidence. Therefore the tracked strict-gap metric remains \(c=0\).

## 5. Adversarial search against the new route

Before accepting L003, I tested the proposed path-count mechanism against the
known failure modes.

1. **Backtracking-count bug.** Counting arbitrary \(4^m\) walks would be far
   too crude, while counting nonbacktracking walks alone gives the classical
   roughly \(0.298\) scale. The K=5 automaton explicitly forbids every return
   to any vertex in the current six-vertex history and therefore contains
   every globally simple path while removing additional impossible local
   patterns.

2. **Endpoint-tilt bug.** The transfer matrix weights only the appended
   direction, so the first five directions contribute a finite missing factor.
   L003.5 keeps this as the explicit finite constant \(C_0\); it is not
   silently discarded.

3. **Infinite path-length union bug.** A point-to-point geodesic can have
   arbitrarily many edges. L003.8 sums all \(m\ge n\), rather than truncating
   path length. The exact choice \(\rho=48140/48141<1\) makes the length sum
   geometric.

4. **Floating spectral claim.** No numerical eigenvalue is used in the proof.
   The finite core is the exact rational Collatz inequality \(MV\le\Lambda V\).

5. **Floating exponential comparison.** No floating `exp` comparison is used.
   The finite core uses the rational Taylor upper bound L003.10.

This route is independent of differentiability, curvature, Busemann
regularity, or R07's KPZ target.

## 6. Prior-art caution for L003

This run does **not** claim a new published record.

Relevant checked sources:

- Janson (1981), *An upper bound for the velocity of first-passage
  percolation*, uses self-avoiding-walk counting to lower-bound the time
  constant.
- A modern 2026 set of FPP lecture notes quotes
  \(\mu(e_1)\ge0.298\) for Exp(1), attributed to Janson.
- Alm--Parviainen (2002), *Lower and Upper Bounds for the Time Constant of
  First-Passage Percolation*, explicitly says its lower-bound method uses a
  transition matrix and gives numerical exponential-distribution bounds.

The Alm--Parviainen full numerical table was not exposed by the accessible
primary page in this run. Since L003 is structurally close to that literature,
the correct label is:

\[
\boxed{\text{L003 proved inside this repository; external novelty UNVERIFIED.}}
\]

The exact certificate is nevertheless useful internally because it converts the
frozen strict-gap target to the concrete diagonal obligation L003.13.

## 7. Independent audit of the newest R09 package

I independently audited the finite-product core of the newest R09
`R09-PASSAGE` compiler from
`runs/R09/20260916T143433Z_6f3c9a8e.md`.

Let \(A\) be an increasing event of \(N\) independent Bernoulli-\(s\)
coordinates, let \(a(s)=P_s(A)\), and let
\[
I_i(s)=P_s(i\text{ is pivotal}).
\]

R09 claims
\[
\boxed{
s(1-s)\sum_{i=1}^N I_i(s)^2
\le
a(s)(1-a(s)).
}
\tag{AUD.1}
\]

**Independent proof.**
Set
\[
g_i=\frac{X_i-s}{\sqrt{s(1-s)}}.
\]
The \(g_i\) are orthonormal in \(L^2(P_s)\). Conditioning on all coordinates
except \(i\), monotonicity gives
\[
\operatorname{Cov}(1_A,X_i)
=
s(1-s)I_i(s).
\]
Thus
\[
\langle 1_A-a(s),g_i\rangle
=
\sqrt{s(1-s)}\,I_i(s).
\]
Bessel's inequality proves AUD.1.

Russo's finite-product formula gives
\[
a'(s)=\sum_i I_i(s).
\tag{AUD.2}
\]
Cauchy--Schwarz and AUD.1 give
\[
a'(s)
\le
\sqrt{
\frac{N\,a(s)(1-a(s))}{s(1-s)}
}.
\tag{AUD.3}
\]
For
\[
\Psi(x)=\arcsin\sqrt{x},
\qquad
\Psi'(x)=\frac1{2\sqrt{x(1-x)}},
\]
AUD.3 implies
\[
\frac{d}{ds}\Psi(a(s))
\le
\sqrt N\,\Psi'(s),
\]
where boundary cases follow by continuity. Hence for \(0<q<p<1\),
\[
\boxed{
\Psi(a(p))-\Psi(a(q))
\le
\sqrt N[\Psi(p)-\Psi(q)].
}
\tag{AUD.4}
\]

The exact R08 checker independently enumerates **every monotone Boolean
event** for \(N=1,2,3,4\). It recovers the counts
\[
3,\ 6,\ 20,\ 168
\]
and at each of
\[
s\in\left\{\frac15,\frac13,\frac25,\frac35\right\}
\]
checks with exact `Fraction` arithmetic both AUD.1 and the exact polynomial
derivative identity AUD.2. Total exact assertions:
\[
1576.
\]

**Audit ID:** `R08-AUDIT-R09-PASSAGE-01`.  
**Verdict:** PASS.

No R09 conjectural/site-percolation closure is imported into R08.

## 8. Exact artifacts and receipts

Exact checker:
`artifacts/R08/20260916T1528Z_axis_transition_r09_passage_exact.py`

- locally executed successfully before upload;
- source SHA-256:
  `3c056c5d9c1b7577a672c3ca1bad097ad3ad74f12f8bd59d50a3c47fe831d642`;
- GitHub create commit:
  `238ba96260fb95406edede6c86237fceb96df60b`;
- read back at that exact commit.

Checker output:
`artifacts/R08/20260916T1528Z_axis_transition_r09_passage_exact.out`

- output SHA-256:
  `b7ec33447f883245cac18122a281cb1fa6a9388cac515139a199f74e7479522e`;
- GitHub create commit:
  `e6209f4c79cb89aa39d0724d9d4a933043f90528`;
- read back at that exact commit;
- status: `PASS`.

One initial GitHub artifact write received a transient 409 because another worker moved
`master` between the connector's read and write. The same create-only write was retried
once and succeeded; no existing file was overwritten.

## 9. Current bottleneck and next attack

The metric did not move, but L003 makes the simplest remaining quantitative route
considerably more concrete:

\[
\boxed{
\text{prove } \mu(1,1)<0.60048.
}
\tag{NEXT}
\]

A finite simulation is not enough. An acceptable proof must be one of:

1. an exact finite-state/regenerative diagonal path strategy whose expected
   asymptotic cost is certified below \(0.60048\);
2. a finite-block/subadditive construction with a rigorous expectation bound and
   no assumed convergence rate;
3. a positive-density cross-leg surgery theorem satisfying the linear-saving
   hypothesis in R08-L001.

The first attack next run should be refutational: search small regenerative
diagonal strategies and exact finite-state strip policies for a certificate below
\(0.60048\). Any policy whose exact asymptotic mean remains above \(0.60048\) is
recorded as a failed candidate rather than extrapolated.

The existing failed surgery/Busemann routes remain binding. In particular, X001
forbids multiplying local margins with a shared bypass, X002 forbids a pointwise
strict-saving claim, and no Busemann differentiability or curvature assumption is
available.

This is the second consecutive run without movement in the frozen strict-gap metric.
If the next run also leaves \(c=0\), the repository stuck protocol requires a
thinking/stuck report rather than another auxiliary lemma.

## 10. Cumulative claim ledger for the canonical GitHub phase

- `R08-X001`: PROVED route obstruction — shared bypass destroys naive
  independence of local deletion margins.
- `R08-L001`: PROVED reduction — linear expected joint saving implies a strict
  triangle gap.
- `R08-L002`: PROVED reduction — frozen equality iff the whole Exp(1) limit shape
  is the \(\ell^1\)-diamond.
- `R08-X002`: PROVED route obstruction — finite exact concatenation equality
  persists on positive-probability exponential cylinder events.
- `R08-L003`: PROVED auxiliary theorem —
  \[
  \mu(e_1)\ge3753/12500=0.30024;
  \]
  external novelty UNVERIFIED.
- `R08-AUDIT-R09-PASSAGE-01`: independent audit PASS.
- Frozen one-pair strict gap: OPEN, \(c=0\).
- Full ADH Question 4 for Exp(1): OPEN.

```yaml
ledger_delta:
  task: "R08 HARD OUTSIDE"
  source: "Auffinger-Damron-Hanson, arXiv:1511.03262 (2015), Question 4; §2.5.1 / §2.8"
  target: "For iid Exp(1) undirected nearest-neighbor FPP on Z^2, prove a positive strict triangle gap for the frozen pair e1,e2; one-pair success is PARTIAL toward strict convexity"
  metric: "largest rigorously proved positive c with 2*mu(e1)-mu(1,1) >= c"
  before: "c=0; no positive lower bound proved"
  after: "c=0; no movement. Auxiliary exact theorem: mu(e1) >= 3753/12500 = 0.30024, reducing this route to proving mu(1,1) < 0.60048"
  status: "OPEN"
  unchanged_count: 2
  exact_evidence:
    - "artifacts/R08/20260916T1528Z_axis_transition_r09_passage_exact.py @ 238ba96260fb95406edede6c86237fceb96df60b"
    - "artifacts/R08/20260916T1528Z_axis_transition_r09_passage_exact.out @ e6209f4c79cb89aa39d0724d9d4a933043f90528"
  audit_ids:
    - "R08-AUDIT-R09-PASSAGE-01 (PASS)"
  prior_art_note: "Janson 1981 self-avoiding-walk lower bound; Alm-Parviainen 2002 transition-matrix method. Full numerical table not accessible this run, so L003 novelty is UNVERIFIED."
```

No Gmail, Drive, email, public publication, purchase, permission change, or schedule change was performed.
