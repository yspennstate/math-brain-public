Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level; GPT-6/maximum was requested, but this scheduler exposes no model or reasoning selector and GPT-6 maximum was not verified or selectable here.
Problem: planar self-avoiding-walk displacement — Flory (1949), *The Configuration of Real Polymer Chains*; Nienhuis (1982), *Exact Critical Point and Critical Exponents of O(n) Models in Two Dimensions*. Metric moved **UNMEASURED -> a=2**, with **C=1, n0=1** for the original uniform n-step nearest-neighbor SAW law on Z^2. Status: **OPEN**.

# R11 Planar SAW — canonical GitHub run

Run ID: `2026-09-16T13-37-28Z_saw-rate-modulus-a31f`
Branch: `master`
Repository: `yspennstate/math-open-problems`
Date/status search: 2026-09-16

## 1. Repository recovery and scope

Required control files read this run:
- `probability_campaign_2026_09/INDEX.md`
- `probability_campaign_2026_09/RANKING.md`
- root `POSTED.md`
- root `RESULTS.md`
- root `QUEUE.md`
- `operations/FLEET_2026-09-16.md`
- `operations/RFLEET_2026-09-16.md`
- canonical intake ledgers `probability_1000_intake_claude_20260907/problems.jsonl` and root intakes D, E, F, G, H, I
- attempt-directory inventories `probability_1000_attempts_H_20260912/` and `probability_1000_attempts_I_20260914/`.

The current fleet ledger assigns R11 to the Flory/Nienhuis planar SAW displacement problem and defines the tracked quantity as the smallest proved upper exponent `a`, retaining constants/range and the original uniform SAW law.

`runs/R11/` did not exist on `master` at the start of this run, so there was no previous immutable canonical R11 report to recover under the revised GitHub-only contract. I did **not** import email, Drive, or non-repository history. The fleet baseline in `RESULTS.md` was therefore used: `UNMEASURED`.

No current `runs/R14/` package was present; repository search found only fleet/deployment references. Therefore the requested independent R14 audit was **NOT_READY** this run rather than invented.

No posted/settled entry in the required repo control files closes this square-lattice metric-exponent problem.

## 2. Exact source formulation and current status

### Flory 1949

Primary source: Paul J. Flory, *The Configuration of Real Polymer Chains*, J. Chem. Phys. 17 (1949), 303–310, DOI 10.1063/1.1747243.

The 1949 paper is the excluded-volume polymer-scaling program. Its abstract says the average linear dimension should scale with a power exceeding 1/2 and approaching 0.60 for long chains in good solvents. I do **not** attribute a rigorous planar Z^2 SAW exponent theorem to Flory 1949.

### Nienhuis 1982

Primary source: Bernard Nienhuis, *Exact Critical Point and Critical Exponents of O(n) Models in Two Dimensions*, Phys. Rev. Lett. 49 (1982), 1062–1065, DOI 10.1103/PhysRevLett.49.1062.

The published abstract explicitly says the calculation is “subject to some plausible assumptions.” In the n->0 self-avoiding-walk specialization, the two-dimensional prediction is

\[
\nu=3/4,
\]

equivalently for the uniform n-step nearest-neighbor SAW omega on Z^2,

\[
\mathbb E_n\|\omega_n\|_2^2=n^{3/2+o(1)}.
\]

The separate counting prediction is gamma=43/32, i.e.

\[
c_n=\mu^n n^{11/32+o(1)}.
\]

Neither is treated here as rigorously proved.

### Duminil-Copin--Hammond, arXiv:1205.0401 / CMP 2013

They define `SAW_n` as the **uniform** law on injective nearest-neighbor n-step walks from 0 in Z^d. Their Theorem 1.1 says: for every fixed v>0 there exists c(v)>0 such that for every n,

\[
\mathbb P_n\left(\max_{0\le k\le n}\|\omega_k\|_2>vn\right)<e^{-c(v)n}.
\tag{DCH}
\]

Their Section 1.2 records the d=2 Coulomb-gas prediction nu=3/4, and Section 1.5 asks explicitly to show, for some epsilon>0,

\[
n^{-(2-\epsilon)}\langle\|\gamma_n\|^2\rangle\to0.
\]

Thus their theorem proves `o(n^2)` mean-square displacement but deliberately leaves open **any fixed power improvement below 2**.

Their proof route is bridge-renewal by contradiction: ballistic assumption -> positive-density renewal points -> finite mean irreducible-bridge length, while an independent stickbreak argument proves the critical irreducible-bridge mean length is infinite. The dependence on fixed speed v is qualitative; the argument does not provide a usable uniform modulus as v downarrow 0.

### Current-status search, 2026-09-16

Dated queries included:
- `planar self-avoiding walk exponent nu 3/4 rigorous 2025 2026`
- `self avoiding walk square lattice mean square displacement power upper bound 2024 2025 2026`
- `quantitative sub-ballisticity self-avoiding walk square lattice`
- direct read of arXiv:1205.0401 and searches around its Question 1.

Newest relevant rigorous paper located: D. Krachun and C. Panagiotis, *Quantitative sub-ballisticity of self-avoiding walk on the hexagonal lattice*, Ann. Probab. 54 (2026), 1109–1125, DOI 10.1214/24-AOP1730. It proves radius O(n/log n) with high probability **on the hexagonal lattice** and says that previously only the non-quantitative o(n) result of Duminil-Copin--Hammond was known. This is not the original square-lattice law and still does not give a fixed power exponent below 2.

Bounded-search conclusion: I found no accepted theorem giving `E||omega_n||^2 <= C n^a` with fixed a<2 for the original uniform square-lattice SAW. This is a dated literature audit, not a proof that no hidden result exists.

## 3. Fixed measurable quantity

Tracked quantity:

\[
a_*^{\rm verified}:=\inf\left\{a:\exists C<\infty,n_0,\ 
\mathbb E_n\|\omega_n\|_2^2\le Cn^a\ \forall n\ge n_0
\right\}
\]

where “verified” means supported by the current source audit and the original uniform SAW law.

For every nearest-neighbor n-step walk from 0,

\[
\|\omega_n\|_2\le n.
\]

Therefore, deterministically and hence under the uniform SAW law,

\[
\boxed{\mathbb E_n\|\omega_n\|_2^2\le n^2}
\]

with

\[
\boxed{a=2,\quad C=1,\quad n_0=1.}
\]

DCH improves this to `o(n^2)` but does not imply any fixed exponent `a<2`.

**Metric this run: UNMEASURED -> 2 (C=1,n0=1).** This is baseline measurement, not progress toward 3/2.

## 4. Refute first: qualitative fixed-speed sub-ballisticity does not imply any power improvement

### R11-GH-X001 — logical countermodel

**Status: PROVED (abstract quantifier obstruction; not a SAW counterexample).**

There exist nonnegative random variables X_n<=n such that, for every fixed v>0, there is c(v)>0 with

\[
\mathbb P(X_n\ge vn)\le e^{-c(v)n}\qquad\text{for every }n,
\]

yet

\[
\mathbb E X_n^2\not=O(n^{2-\epsilon})
\qquad\text{for every }\epsilon>0.
\]

Proof. Let

\[
X_n=
\begin{cases}
n/\log(n+e),&\text{with probability }1-e^{-n},\\
0,&\text{with probability }e^{-n}.
\end{cases}
\]

Fix v>0. The set `A_v={n:1/log(n+e)>=v}` is finite. If nonempty define

\[
c(v)=\min_{n\in A_v}\frac{-\log(1-e^{-n})}{n}>0;
\]

if empty choose any positive c(v). For n in A_v the exponential bound holds by definition, and outside A_v the event is empty.

But

\[
\mathbb E X_n^2=(1-e^{-n})\frac{n^2}{\log^2(n+e)},
\]

and for every epsilon>0,

\[
\frac{\mathbb E X_n^2}{n^{2-\epsilon}}
=(1-e^{-n})\frac{n^\epsilon}{\log^2(n+e)}\to\infty.
\]

So the DCH quantifier pattern “for each fixed v there exists c(v)>0” cannot by itself move the fixed exponent metric below 2.

## 5. Quantitative bridge-renewal target with the missing uniform estimate explicit

### R11-GH-C001 — speed-rate modulus compiler

**Status: PROVED CONDITIONAL REDUCTION.**

Let

\[
R_n=\max_{0\le k\le n}\|\omega_k\|_2.
\]

Assume there exist constants

\[
c_0>0,\quad \kappa>0,\quad v_0\in(0,1],\quad N_0\in\mathbb N
\]

such that uniformly for every n>=N0 and every 0<v<=v0,

\[
\boxed{
\mathbb P_n(R_n>vn)\le\exp(-c_0 n v^\kappa).
}
\tag{U_kappa}
\]

Then for every `0<eta<1/kappa`, write

\[
q=1-\kappa\eta>0.
\]

For all

\[
n\ge n_0:=
\left\lceil
\max\left\{
N_0,\ v_0^{-1/\eta},\
\left(\frac{4\eta}{e q c_0}\right)^{2/q},\
1
\right\}
\right\rceil,
\]

one has

\[
\boxed{
\mathbb E_n\|\omega_n\|_2^2\le2 n^{2-2\eta}.
}
\tag{C001}
\]

Hence the fixed metric would improve to `a=2-2eta, C=2`, with the displayed explicit n0.

Proof. Put `v=n^{-eta}`. Then

\[
\mathbb P(R_n>n^{1-\eta})\le e^{-c_0 n^q}.
\]

Since `||omega_n||<=R_n<=n`,

\[
\mathbb E\|\omega_n\|^2\le n^{2-2\eta}+n^2e^{-c_0n^q}.
\]

The elementary inequality

\[
\log x\le\frac{2}{eq}x^{q/2}\qquad(x\ge1)
\]

shows that the explicit n0 condition implies `c0 n^q >= 2 eta log n`; the second term is therefore at most `n^{2-2eta}`.

Consequences:
- **Any finite polynomial modulus** kappa in (U_kappa) gives a genuine exponent improvement `a<2`.
- To obtain the target upper exponent `a=3/2` by eta=1/4, it is sufficient to prove **kappa<4**.
- The borderline kappa=4 yields every `a>3/2` by eta<1/4, but this compiler alone does not give `C n^{3/2}`.

### Missing bridge-renewal estimate

DCH already proves a positive rate for each fixed v. The exact uniform estimate missing for fixed-metric progress is

\[
\boxed{c(v)\ge c_0 v^\kappa\quad\text{as }v\downarrow0}
\tag{MISSING}
\]

for some finite kappa; kappa<4 would be strong enough for the 3/2 upper exponent via C001.

Inspection of their proof shows where this is lost. Their fixed-v ballistic contradiction obtains v-dependent positive-density renewal parameters and then concludes finite mean irreducible-bridge length; Theorem 2.5 supplies only the qualitative contradiction `E_iSAB |gamma|=infinity`. No quantitative truncated-mean divergence is related uniformly to v. A successful quantitative bridge-renewal improvement needs a modulus connecting speed v, renewal/diamond density, a quantitative truncated irreducible-bridge mean obstruction, and the final rate c(v).

## 6. Exact checker

Artifacts:
- `artifacts/R11/2026-09-16T13-37-28Z_saw-rate-modulus-a31f.py`
- `artifacts/R11/2026-09-16T13-37-28Z_saw-rate-modulus-a31f.txt`

The checker uses exact rational arithmetic. Its archived output is:

```
kappa=1, eta=1/4: q=3/4, a=3/2
kappa=2, eta=1/4: q=1/2, a=3/2
kappa=3, eta=1/4: q=1/4, a=3/2
kappa=4, eta=1/5: q=1/5, a=8/5
kappa=5, eta=1/6: q=1/6, a=5/3
PASS: exact rational exponent arithmetic.
```

Output SHA-256: `90bd0ebef315ef704d56e94c1348fa90a119d99782fd09775f00693d13dfc965`.

This checker certifies finite/algebraic arithmetic only and is not asymptotic exponent evidence.

## 7. Failed-route state and next attack

Because no prior canonical `runs/R11/` report existed in the repository, I cannot honestly recover earlier R11 renewal/surgery failures from GitHub. I therefore do not claim them as repository history.

The verified source-level obstruction is:
- DCH bridge-renewal proves qualitative fixed-v sub-ballisticity but loses all usable v->0 modulus.
- R11-GH-X001 proves that this qualitative quantifier structure alone is insufficient for any fixed power improvement.

Next attack: quantify the DCH Section 3 multi-valued bridge map with v exposed. The first concrete subproblem is to trace every v-dependent choice in the “positive density of renewal points” step and prove or refute a polynomial lower bound

\[
\delta(v)\ge c v^p
\]

for the renewal-point density/cost parameter. If this fails, isolate the first step where a super-polynomial loss in v is unavoidable. The target is then to propagate the best polynomial modulus through the finite-mean contradiction to an explicit c(v).

Polygon surgery remains a parallel route only if it yields a **uniform** small-speed rate; without such a modulus, X001 applies again.

## 8. R14 audit

`runs/R14/` was not present on `master`, and code search exposed no current R14 package to audit. Therefore **R14 audit status: NOT_READY**. No audit ID is invented.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  task: R11
  source:
    - "Paul J. Flory, 1949, The Configuration of Real Polymer Chains"
    - "Bernard Nienhuis, 1982, Exact Critical Point and Critical Exponents of O(n) Models in Two Dimensions"
  target: "For uniform n-step nearest-neighbor SAW on Z^2, E||omega_n||^2 = n^(3/2+o(1)); secondary c_n = mu^n n^(11/32+o(1))."
  metric: "smallest verified a with E||omega_n||^2 <= C n^a for all n>=n0, original uniform SAW law"
  before: "UNMEASURED"
  after:
    a: 2
    C: 1
    n0: 1
  status: OPEN
  unchanged_count: 0
  prior_unchanged_count: UNKNOWN
  exact_evidence:
    - "deterministic ||omega_n||<=n"
    - "Duminil-Copin--Hammond Question 1 explicitly asks for any fixed power improvement below 2"
    - "R11-GH-C001 conditional uniform speed-rate compiler"
    - "R11-GH-X001 abstract quantifier countermodel"
    - "artifacts/R11/2026-09-16T13-37-28Z_saw-rate-modulus-a31f.py"
    - "artifacts/R11/2026-09-16T13-37-28Z_saw-rate-modulus-a31f.txt"
  audits:
    R14: "NOT_READY: no runs/R14 package found"
    P26: "NOT_PERFORMED_BY_R11"
  admission_status_check:
    date: "2026-09-16"
    result: "outside-source problem still open in bounded current-status search; not posted/settled in repo controls"
```

## 10. Status

**OPEN.** No exponent `a<2` for the original uniform square-lattice SAW was verified this run. The tracked metric is now baselined exactly at `a=2, C=1, n0=1`. The new substantive result is the exact uniform-rate reduction C001 and the countermodel X001 showing why DCH's fixed-v theorem alone cannot move that metric.
