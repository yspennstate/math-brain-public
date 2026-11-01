Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level; the scheduler exposes no model selector or reasoning selector, so GPT-6 / maximum was not verified or claimed. Metric: **no movement** — before `(a,C,n0)=(2,1,1)`, after `(2,1,1)` for the original uniform nearest-neighbor n-step SAW on Z^2; unchanged-count = **2**.
Problem/source: planar self-avoiding-walk displacement — Paul J. Flory (1949), *The Configuration of Real Polymer Chains*; Bernard Nienhuis (1982), *Exact Critical Point and Critical Exponents of O(n) Models in Two Dimensions*. Status: **OPEN**.

# R11 immutable run report — parity acceleration and the cubic MultiUnf barrier

Run ID: `2026-09-16T15-07-31Z_saw-parity-cubic-barrier-c91e`  
Repository: `yspennstate/math-open-problems`, branch `master`  
Dated source/status refresh: 2026-09-16

## 1. Repository continuation, not restart

Before new mathematics I read the required control state:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/FLEET_2026-09-16.md` and `operations/RFLEET_2026-09-16.md`;
- newest canonical own report `runs/R11/2026-09-16T14-40-03Z_saw-quantitative-renewal-trace-b7c2.md` and its exact checker;
- newest neighboring reports actually present: R10 `runs/R10/20260916T143504Z_7b31c4e9.md`, R12 `runs/R12/2026-09-16T14-30-05Z_6d92bf.md`, and R14 `runs/R14/2026-09-16T13-53-07Z_r14-c175-baseline.md` with its checker;
- the probability-intake inventory and current `probability_1000_intake_*` / attempt-ledger paths.

The connector can enumerate the intake ledgers and perform targeted source/ownership reads, but a literal row-by-row model-visible materialization of all roughly 780 intake records exceeds its response budget. I therefore record the intake sweep as **ACCESS-LIMITED / INCOMPLETE**, rather than pretending that every JSON line was read. This does not affect R11 admission: the current fleet files and root ledger explicitly assign this outside target to R11.

`RESULTS.md` remains P26-owned. This report contains a structured `ledger_delta`; R11 does not edit the shared ledger.

The newest R11 report is the 14:40Z quantitative-renewal trace, not the older 13:37Z baseline. I retain its claims C002--C004 and X002 below instead of re-deriving the project from scratch.

Incoming independent audit already present: R10 independently checked prior R11-GH-C001 and recorded `R10-AUDIT-R11-C001-20260916 = PASS` for the **conditional compiler only**. This is not closure of the SAW problem.

## 2. Exact source formulation and current status

### Flory 1949

Paul J. Flory, *The Configuration of Real Polymer Chains*, J. Chem. Phys. 17 (1949), 303--310, DOI `10.1063/1.1747243`, is the excluded-volume polymer-scaling origin. Its abstract says that the average linear dimension should scale with a power larger than the random-flight value 1/2 and approach 0.60 for long chains in good solvent. I do **not** attribute the exact planar lattice value 3/4 directly to Flory's 1949 paper.

### Nienhuis 1982

Bernard Nienhuis, *Exact Critical Point and Critical Exponents of O(n) Models in Two Dimensions*, Phys. Rev. Lett. 49 (1982), 1062--1065, DOI `10.1103/PhysRevLett.49.1062`, is the Coulomb-gas source behind the two-dimensional SAW prediction. The published abstract says the calculation is “subject to some plausible assumptions.” The n->0 specialization predicts

\[
\nu=\frac34,
\]

which for uniform n-step nearest-neighbor SAW on Z^2 corresponds to

\[
\mathbb E_n\|\omega_n\|_2^2=n^{3/2+o(1)}.
\]

The separate counting prediction is `gamma=43/32`, i.e.

\[
c_n=\mu^n n^{11/32+o(1)}.
\]

Neither is treated as proved.

### Duminil-Copin--Hammond, arXiv:1205.0401

Current arXiv read: `https://arxiv.org/abs/1205.0401` and the full HTML proof. They use exactly the required law: `SAW_n` is uniform on n-step nearest-neighbor self-avoiding walks from 0. Their theorem says that for every fixed `v>0` there is `c(v)>0` such that

\[
\mathbb P_{\mathrm{SAW}_n}\!\left(\max_{k\le n}\|\omega_k\|>vn\right)
\le e^{-c(v)n}.
\]

Their introduction records the two-dimensional prediction `nu=3/4`, and their Question 1 asks for any fixed-power improvement below the exponent 2. Thus their result gives `o(n^2)` mean square displacement, but not a verified bound `C n^a` with fixed `a<2`.

### Later rigorous work / current-status search

Fresh dated queries included:

- `planar self avoiding walk exponent 3/4 rigorous square lattice 2026`;
- `self avoiding walk Z2 mean square displacement fixed power upper bound`;
- `quantitative sub-ballisticity self avoiding walk square lattice`;
- direct/current arXiv checks of `1205.0401` and later citing literature.

The newest directly relevant quantitative result located is D. Krachun and C. Panagiotis, *Quantitative sub-ballisticity of self-avoiding walk on the hexagonal lattice*, arXiv:2310.17299 / Ann. Probab. 54 (2026), which proves an `O(n/log n)` radius bound with high probability and polynomial critical bridge-height decay on the **hexagonal lattice**. It is not a theorem for the original square-lattice walk law.

Bounded-search conclusion on 2026-09-16: I found no accepted theorem giving the original square-lattice uniform SAW a fixed second-moment exponent `a<2`. This is a bounded literature audit, not proof that no hidden result exists.

## 3. Frozen metric and retained R11 state

The deterministic nearest-neighbor bound

\[
\|\omega_n\|_2\le n
\]

gives

\[
\boxed{\mathbb E_n\|\omega_n\|_2^2\le n^2}
\]

with

\[
\boxed{(a,C,n_0)=(2,1,1).}
\]

No theorem in this run improves that fixed exponent.

Retained canonical R11 state:

- **R11-GH-X001, PROVED logical obstruction:** fixed-v exponential sub-ballisticity with an arbitrary positive rate `c(v)` does not by itself imply any fixed power `a<2`.
- **R11-GH-C001, PROVED CONDITIONAL compiler:** a uniform small-speed modulus
  \[
  P(R_n>vn)\le e^{-c_0 n v^\kappa}
  \]
  yields `E||omega_n||^2 <= 2 n^(2-2 eta)` for every `eta<1/kappa`; `kappa<4` would suffice for upper exponent 3/2.
- **R11-GH-C002, PROVED:** a fixed-parameter DCH one-step crossing-number reduction, with Case-2 entropy cost `H(4z)` and Case-3 terminal renewal density generated by `MultiUnf`.
- **R11-GH-C003, PROVED:** exact renewal Laplace-rate compiler
  \[
  I(\delta)=\sup_{t>0}\{\delta[-\log\psi(t)]-t\},
  \]
  with `I(delta)>0` for every fixed delta but `I(delta)<=delta log mu <2 delta`.
- **R11-GH-C004, PROVED:** branch-aware quantitative DCH compiler at fixed speed.
- **R11-GH-X002, PROVED METHOD LIMITATION:** the unmodified nested parameter compiler has a doubly-exponential-in-`1/v` worst-case rate cap and therefore cannot supply the polynomial modulus required by C001.

The previous report left four possible repairs: lower the Case-2 entropy cost, improve the Case-3 terminal renewal density, batch crossing-number reductions, or replace the unfolding geometry. This run attacks the middle two first, including a refutation search before strengthening anything.

## 4. R11-GH-X003 — one full DCH unfolding pass cannot generally lower the crossing cap by four

**STATUS: PROVED finite route counterexample. This refutes only the stronger one-pass claim, not the SAW conjecture.**

Consider the 10-step bridge

\[
\gamma=((0,0),(0,1),(0,2),(1,2),(1,1),(2,1),(2,2),(3,2),(3,1),(4,1),(4,2)).
\tag{X003.1}
\]

Its crossing counts across horizontal interfaces are

\[
|\mathcal V_{0,1}|=1,
\qquad
|\mathcal V_{1,2}|=5.
\]

Its DCH zigzag set is

\[
\mathsf{ZigZag}(\gamma)=\{(7,9),(10,10)\}.
\]

Applying `Unf` to all zigzags of the original bridge (the degenerate `(10,10)` operation is inert) gives

\[
\gamma'=((0,0),(0,1),(0,2),(1,2),(1,1),(2,1),(2,2),(3,2),(3,3),(4,3),(4,4)).
\]

The output crossing counts are

\[
1,3,1,1,
\]

so

\[
\boxed{\max_h|\mathcal V_{h,h+1}(\gamma)|=5,
\qquad
\max_h|\mathcal V_{h,h+1}(\gamma')|=3.}
\tag{X003.2}
\]

Therefore a single full-unfold pass cannot universally be promoted from a two-crossing reduction to a four-crossing reduction (or to immediate crossing number 1). The exact checker reconstructs the zigzags, performs the DCH reflection/concatenation, and verifies the counts.

## 5. R11-GH-C005 — parity accelerates DCH Case 2 from `k -> k-1` to `k -> k-2`

**STATUS: PROVED.**

This is a small but rigorous quantitative strengthening of the published Case-2 bookkeeping.

Let a bridge start at height 0 and end at height `H`. For any integer interface `h` with `0<=h<H`, let `U_h` be the number of upward crossings from height `h` to `h+1` and `D_h` the number of downward crossings. Since the path begins below the interface and ends above it,

\[
U_h-D_h=1.
\tag{C005.1}
\]

Hence the total crossing number is

\[
|\mathcal V_{h,h+1}|=U_h+D_h=1+2D_h,
\]

and is therefore **odd** at every level between the bridge endpoints.

Duminil-Copin--Hammond's Case-2 estimate says that when a nondegenerate zigzag whose central section crosses an interface is unfolded, that interface's crossing number drops by at least two; after the full unfold of the original zigzag set, a level that initially has at least two crossings has had its count reduced by at least two.

Now take a level counted in `SAB^k`: its source crossing number `q` satisfies `1<=q<=k` and is odd. If `q=1`, it remains in the desired low-crossing class. If `q>1`, then `q>=3`, and the full unfold produces a corresponding level with

\[
q'\le q-2\le k-2.
\]

Therefore for every `k>=3`, the Case-2 full-unfold inclusion may be sharpened to

\[
\boxed{
\mathsf{Unf}_{\mathsf{ZigZag}_\gamma}
({\rm SAB}_{n,v,\delta}^{k})
\subseteq
{\rm SAB}_{n,v,\delta}^{k-2}.
}
\tag{R11-GH-C005}
\]

For `k=2`, parity already gives

\[
{\rm SAB}^{2}_{n,v,\delta}={\rm SAB}^{1}_{n,v,\delta}.
\]

The inverse map is unchanged, so there is **no extra entropy cost** for this acceleration.

### Quantitative consequence

The DCH iteration starts at a crossing cap `k0` of order `2/v`. The number of all-Case-2 passes falls from order `k0` to exactly

\[
\left\lfloor\frac{k_0-1}{2}\right\rfloor.
\]

This improves constants in the nested compiler, but it is still `Theta(1/v)`. Hence the doubly-exponential *class* of X002 survives; parity alone does not produce a polynomial small-speed rate.

X003 shows C005 is essentially the largest universal one-pass improvement available from crossing parity alone: a cap 5 can genuinely remain 3 after full unfolding.

## 6. R11-GH-C006 — optimized Case-3 terminal renewal density: `d(z) >= z^3/15`

**STATUS: PROVED within the retained DCH `MultiUnf` reconstruction criterion.**

The convenient parameters in C002 yielded a terminal renewal density on the order of `z^3/48`. Here I optimize the same reconstruction algebra.

Assume the Case-3 source family has more than `2 z n` zigzags and fewer than `r n` existing renewal points, with

\[
0<z\le\frac18.
\]

Choose an integer cutoff `L` and call a zigzag short when its central section has length less than `L`. Since the central sections are disjoint, at most `n/L` zigzags can be long. Thus the certified short-zigzag density is

\[
a=2z-\frac1L.
\tag{C006.1}
\]

Select `s n` short zigzags in `MultiUnf`. To obtain at least `d n` renewal points after the floor/rounding loss, take

\[
r=d,
\qquad
s=2d.
\tag{C006.2}
\]

The exact reconstruction criterion retained from C002 is

\[
\frac{a-s}{(r+3Ls)L}\ge2.
\tag{C006.3}
\]

Choose equality. Substituting C006.2 gives

\[
\boxed{
d=
\frac{a}{2+2L+12L^2}.
}
\tag{C006.4}
\]

Now set

\[
L=\left\lceil\frac{3}{4z}\right\rceil.
\tag{C006.5}
\]

Because `z<=1/8`,

\[
L\ge\frac{3}{4z}
\quad\Longrightarrow\quad
\frac1L\le\frac{4z}{3},
\]

so

\[
a\ge\frac{2z}{3}.
\tag{C006.6}
\]

Also

\[
L\le\frac{3}{4z}+1
\le\frac{7}{8z}.
\]

Multiplying the denominator in C006.4 by `z^2` and using `z<=1/8`,

\[
z^2(2+2L+12L^2)
\le
\frac1{32}+\frac7{32}+\frac{147}{16}
=
\frac{151}{16}.
\]

Therefore

\[
d
\ge
\frac{(2z/3)}{151/(16z^2)}
=
\frac{32}{453}z^3
>
\frac1{15}z^3.
\]

Thus the same DCH `MultiUnf` reconstruction supports the explicit uniform choice

\[
\boxed{d(z)\ge z^3/15.}
\tag{R11-GH-C006}
\]

This improves the retained convenient constant `1/48` by more than a factor three, but **does not improve the cubic exponent**.

The exact checker verifies the reconstruction ratio and the `z^3/15` inequality for all 6,084 reduced rationals `z=p/q` in `(0,1/8]` with `q<=400`. That finite sweep is a self-check of the displayed algebra, not asymptotic SAW evidence.

## 7. R11-GH-X004 — cubic barrier for the present worst-case Case-3 counting certificate

**STATUS: PROVED METHOD LIMITATION. Scope is the current DCH length-budget + reconstruction compiler, not every conceivable `MultiUnf` refinement.**

The preceding optimization raises a natural question: can different tuning of `L,r,s` change `z^3` into a better power while using the same worst-case short-zigzag certificate?

In the exact C002/C006 compiler the only guaranteed short-zigzag density used is

\[
a_0=2z-\frac1L,
\]

so positivity requires

\[
x:=zL>\frac12.
\]

To guarantee terminal density `d`, we need `r>=d` and, allowing for the floor loss as in C006, `s>=2d`. The reconstruction condition therefore necessarily implies

\[
a_0-2d
\ge
2dL(1+6L),
\]

hence

\[
d
\le
\frac{a_0}{2+2L+12L^2}
\le
\frac{2z-1/L}{12L^2}.
\]

Writing `x=zL`,

\[
\frac{d}{z^3}
\le
\frac{2-1/x}{12x^2}.
\tag{X004.1}
\]

For `x>1/2`,

\[
\frac{2-1/x}{12x^2}\le\frac8{81}
\]

is equivalent to the exact factorization

\[
32x^3-54x+27=(2x+3)(4x-3)^2\ge0.
\]

Therefore

\[
\boxed{d\le\frac8{81}z^3}
\tag{R11-GH-X004}
\]

for this retained worst-case certificate. The coefficient is maximized at `x=3/4`, exactly where C006 places the cutoff up to integer rounding.

Even if one sharpens the elementary long-section count from `n/L` to `n/(L+1)`, the exponent remains cubic under the same reconstruction mechanism: positivity forces `L+1>1/(2z)`; for `z<=1/8` this implies `L>3/(8z)`, while `d<=2z/(12L^2)`, so

\[
d<\frac{32}{27}z^3.
\]

Thus **parameter optimization of this length-budget/reconstruction scheme cannot change the cubic power**. A different geometric input about the distribution of zigzag lengths, or a different inverse reconstruction, is required to improve the exponent.

This resolves the previous run's proposed repair “improve Case-3 terminal density” at the level of the current compiler: constants can improve, but the `z^3` exponent cannot be removed by tuning these parameters alone.

## 8. Effect on the small-speed modulus obstruction

C005 halves the crossing-cap stages up to rounding, but the number of stages remains `Theta(1/v)`. X004 leaves the nested Case-3 relation cubic in the relevant small threshold. Consequently the X002 mechanism remains doubly exponential in `1/v`: schematically, repeated positive branch margins still force a recursion of the form

\[
z_{j-1}\lesssim z_j^3,
\]

iterated a linear number of times in `1/v`.

So this run does **not** improve the tracked exponent `a=2`.

The exact missing uniform estimate remains the C001 input

\[
\boxed{
c(v)\ge c_0v^\kappa\quad(v\downarrow0)}
\]

for some finite `kappa`; `kappa<4` would be enough for the target upper exponent `3/2` through C001.

The present route analysis narrows what must change:

1. **Case 2:** replace the inverse entropy cost from marking all zig/zag endpoints by a substantially cheaper joint code; merely reducing the number of `k` stages by parity is insufficient.
2. **Case 3:** obtain extra geometric information beyond the disjoint-length budget, or reconstruct selected zigzags with an inverse multiplicity that no longer carries the `L^2` penalty responsible for `z^3`.
3. **Alternative surgery:** use polygon insertion / endpoint redirection to batch many crossing reductions in one operation with a uniform small-speed accounting.

The highest-value next attack is now #1 or #3. Re-optimizing `L,r,s` inside the present Case-3 compiler is not a productive route after X004.

## 9. Independent R14 audit

Directed audit target: R14.

Package actually available and read:

`runs/R14/2026-09-16T13-53-07Z_r14-c175-baseline.md`.

Audit scope is **claim-scoped R14-C175**, not a full closure audit of the negative-margin perceptron problem.

R14 freezes `kappa=-1` and claims the rigorous bracket

\[
2\le\alpha_c(-1)\le
\alpha_U:=\frac1{2\bar\Phi(1)-\phi(1)}.
\]

I independently checked both theorem directions against the cited rigorous literature:

- the lower endpoint `2` is inherited from the rigorous zero-margin spherical threshold and monotonicity, because the `kappa=-1` constraints are weaker than the `kappa=0` constraints;
- Stojnic, *Negative spherical perceptron*, arXiv:1306.3980, gives the negative-margin Gardner expression as a rigorous **upper bound** on capacity, not an exact negative-margin threshold. At `kappa=-1`, its integral is
  \[
  f_{\rm gar}(-1)=\int_1^\infty(z-1)^2\phi(z)\,dz
  =2\bar\Phi(1)-\phi(1),
  \]
  by Gaussian integration by parts.

I then recomputed the finite constant independently using rational interval arithmetic: Machin bounds for `pi`, exact alternating-series bounds for `e^{-1/2}` and the Gaussian integral on `[0,1]`, and exact `Fraction` interval propagation. The independent checker certifies

\[
13.273<\alpha_U<13.274,
\]

and

\[
11.273<\alpha_U-2<11.274.
\]

The tighter independent enclosure printed by the checker is

\[
13.273199673102948<\alpha_U<13.273200081444312.
\]

Therefore:

\[
\boxed{\texttt{R11-AUDIT-R14-C175-20260916 = PASS}.}
\]

This is a **claim-scoped independent audit only**. R14 remains PARTIAL: its exact negative-margin capacity is open and no closure is inferred.

## 10. Exact checker, correction note, and limitations

Canonical exact evidence for this report:

- `artifacts/R11/2026-09-16T15-07-31Z_saw-parity-cubic-barrier-c91e_checker_v2.py`
- `artifacts/R11/2026-09-16T15-07-31Z_saw-parity-cubic-barrier-c91e_checker_v2_output.txt`
- output SHA-256: `0fc1f596cb54f62e609aeefdf4134a34bc07af558a0bc65d8858ac4739f0e85a`.

The v2 checker returned `PASS` and verifies:

1. the exact X003 bridge and `5 -> 3` full-unfold crossing counts;
2. the crossing-parity identity on the explicit source/output;
3. C006 on 6,084 reduced rational `z` values;
4. the exact factorization behind X004;
5. the corrected exact parity-accelerated stage count `floor((k0-1)/2)`;
6. the independent exact R14-C175 constant audit.

A pre-report v1 artifact was written before I noticed that its **diagnostic only** stage-count line used `k0//2`, which overcounts one Case-2 pass when `k0` is even. It does not affect C005, C006, X003, X004, or the R14 audit, but under the immutable-file rule it is retained rather than overwritten. **It is superseded and is not cited as evidence.** The v2 artifact above is the canonical checker for this report.

The local Python process that produced the pre-report v1 output also emitted an unrelated `artifact_tool` spreadsheet warmup traceback after the mathematical checker had already printed `PASS`. The canonical v2 output was rerun cleanly and exited successfully.

Exact enumeration is used here only to verify the finite X003 counterexample and finite/algebraic constants. It is **not** evidence for a SAW critical exponent.

## 11. Cumulative status / remaining obligation

Tracked metric:

\[
\boxed{(a,C,n_0)=(2,1,1)\ \longrightarrow\ (2,1,1).}
\]

Status: **OPEN**, unchanged-count **2**.

New claims this run:

- `R11-GH-X003` — **PROVED finite route counterexample**: one full unfold need not lower cap 5 below 3.
- `R11-GH-C005` — **PROVED**: bridge crossing parity upgrades DCH Case 2 to `k -> k-2` for `k>=3`, with `SAB^2=SAB^1`.
- `R11-GH-C006` — **PROVED**: optimized present `MultiUnf` parameters give terminal density `d(z)>=z^3/15`.
- `R11-GH-X004` — **PROVED METHOD LIMITATION**: the retained worst-case Case-3 length-budget/reconstruction compiler remains cubic in `z`; parameter tuning cannot change that power.
- `R11-AUDIT-R14-C175-20260916` — **PASS**, claim-scoped independent audit.

No source theorem is closed. No paper folder is created.

If the tracked metric also fails to move on the next run, the unchanged-count reaches three and the fleet stuck protocol requires a dedicated thinking/stuck report rather than another opportunistic lemma.

## 12. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: R11
  source:
    - "Paul J. Flory, 1949, The Configuration of Real Polymer Chains"
    - "Bernard Nienhuis, 1982, Exact Critical Point and Critical Exponents of O(n) Models in Two Dimensions"
  target: "For the original uniform n-step nearest-neighbor SAW on Z^2, E||omega_n||_2^2 = n^(3/2+o(1)); secondary counting prediction gamma=43/32 remains distinct."
  frozen_domain: "uniform nearest-neighbor n-step self-avoiding walks from 0 on Z^2"
  metric: "smallest rigorously verified a for which E||omega_n||_2^2 <= C n^a for all n>=n0, retaining C,n0"
  before:
    a: 2
    C: 1
    n0: 1
  after:
    a: 2
    C: 1
    n0: 1
  status: OPEN
  movement: false
  unchanged_count: 2
  exact_evidence:
    new_claims:
      - R11-GH-X003
      - R11-GH-C005
      - R11-GH-C006
      - R11-GH-X004
    checker: artifacts/R11/2026-09-16T15-07-31Z_saw-parity-cubic-barrier-c91e_checker_v2.py
    checker_output: artifacts/R11/2026-09-16T15-07-31Z_saw-parity-cubic-barrier-c91e_checker_v2_output.txt
    checker_sha256: 0fc1f596cb54f62e609aeefdf4134a34bc07af558a0bc65d8858ac4739f0e85a
  audit_ids:
    incoming:
      - "R10-AUDIT-R11-C001-20260916: PASS conditional compiler only"
    outgoing:
      - "R11-AUDIT-R14-C175-20260916: PASS claim-scoped"
  remaining_obligation: "Obtain a polynomial small-speed rate c(v)>=c0 v^kappa for square-lattice uniform SAW (some finite kappa; kappa<4 suffices for a=3/2 via C001), or a different direct power-law moment bound. Current DCH Case-3 worst-case reconstruction remains cubic and the crossing-reduction stage count remains Theta(1/v)."
  closure: false
```

## Primary references

- P. J. Flory, *The Configuration of Real Polymer Chains*, J. Chem. Phys. 17 (1949), 303--310, DOI 10.1063/1.1747243.
- B. Nienhuis, *Exact Critical Point and Critical Exponents of O(n) Models in Two Dimensions*, Phys. Rev. Lett. 49 (1982), 1062--1065, DOI 10.1103/PhysRevLett.49.1062.
- H. Duminil-Copin and A. Hammond, *Self-avoiding walk is sub-ballistic*, Commun. Math. Phys. 324 (2013), 401--423, arXiv:1205.0401.
- D. Krachun and C. Panagiotis, *Quantitative sub-ballisticity of self-avoiding walk on the hexagonal lattice*, arXiv:2310.17299; Ann. Probab. 54 (2026), 1109--1125.
- M. Stojnic, *Negative spherical perceptron*, arXiv:1306.3980 (used only for the independent R14 audit).
