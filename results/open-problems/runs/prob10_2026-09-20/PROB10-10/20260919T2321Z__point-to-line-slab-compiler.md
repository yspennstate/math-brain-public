Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT in the frozen source defect: `c_*: 0 -> 0`. Methods tried: B2 / B11 / B19. Auxiliary source-relevant movement: certified diagonal upper bound `0.9773163561... -> 0.7900933667...` with an explicit finite-to-infinite error.**

# PROB10-10 — random-endpoint slab optimization with an explicit finite-to-infinite error

Status: **PARTIAL / OPEN**. This run does not prove strict convexity of the Exp(1) limit shape and does not prove a positive strict-triangle defect. It establishes a different dependence-controlled block mechanism and a materially stronger rigorous diagonal upper bound.

## 1. Exact target, model, and metric

Model is frozen throughout:

- graph: undirected nearest-neighbor `Z^2`;
- edge weights: iid `Exp(1)`;
- passage time: unrestricted undirected FPP;
- deterministic time constant: `mu(x)` in the standard normalization `T(0,nx)/n -> mu(x)`.

Primary source target: Auffinger–Damron–Hanson, *50 years of first passage percolation*, arXiv:1511.03262, Question 4 (§2.5.1, discussion §2.8): for continuous passage-time distributions, prove strict convexity of the limit shape. Here only the Exp(1) special case is claimed.

The frozen source-level milestone inherited from R08 is

\[
\Delta_{12}:=2\mu(e_1)-\mu(1,1).
\]

Tracked source defect:

\[
c_*:=\sup\{c\ge0:\Delta_{12}\ge c\text{ is rigorously proved in this track}\}.
\]

Before: `c_*=0`.  
After: `c_*=0` (**no movement**).

A proof `c_*>0` would still be only a **PARTIAL one-pair result**, not global strict convexity.

This run separately tracks an auxiliary but source-relevant quantity:

\[
U_{\rm diag}:=\text{best rigorous upper bound on }\mu(1,1)
\text{ produced by the recovered finite-block routes}.
\]

The old exact R08 fixed-corner `m=3` block certificate was

\[
U_{\rm diag}^{\rm old}
=\frac{5675443731448268047}{5807171543040000000}
=0.9773163561\ldots .
\]

This run proves

\[
\boxed{
U_{\rm diag}^{\rm new}
=\frac{93432902428288084006412573734630991128481810947182059}
{118255520636422191487470974373871068060057600000000000}
=0.790093366681362\ldots .}
\]

This does **not** yet meet the old sufficient threshold `0.60048`, so the source defect remains zero.

Directional scope of the new bound: **exactly the diagonal direction `(1,1)`**. No neighboring-angle curvature is claimed.

## 2. Required predecessor handoff and ownership

The owner refocused the native HARD7-03 slot. Before writing FPP research artifacts I preserved the actual latest D0025 particle-system state in

`runs/prob10_2026-09-20/PROB10-10/20260919T2321Z__handoff-hard7-03-d0025.md`

commit

`e0bb680de7150739ac0c0451f1b5f890eeb865b2`.

That handoff records the newest D0025 report commit `3ba46c2f0cdddfeaf82bc8c4ad27bd4a3919b776`, its exact four-step sign-atlas closure, and its moved plateau lower bound. D0025 history/claim was not overwritten.

For the present FPP target, a direct preflight fetch of `operations/claims/PROB10-10.md` returned 404. Repository-wide searches for exact strict-convexity/FPP aliases recovered the retired R08 attempt and the new PROB10 owner assignment but no active canonical owner of this exact Exp(1) parent. I therefore created, using create-only semantics,

`operations/claims/PROB10-10.md`

at commit

`0f47d1c9a19a7edaa72a9cd4716aef5d90affe1d`.

Readback succeeded. If a hidden/unindexed collision is later discovered, this run must be narrowed or handed off rather than used to overwrite another claim.

## 3. Recovered FPP history: what must not be repeated

The relevant repository-native R08 chain was recovered and retained:

1. `runs/R08/2026-09-16T1329Z_fpp-axis-gap-a1c93e.md`.
   - froze `Delta_12`;
   - `R08-X001`: linearly many local deletion margins may share one bypass, so naive independent local surgery does not tensorize;
   - `R08-L001`: a genuine `gamma n-o(n)` expected joint saving would compile to a strict triangle gap.

2. `runs/R08/2026-09-16T1429Z_fpp-diamond-gap-7e4a9c.md`.
   - `R08-L002`: `Delta_12=0` iff the full limit shape is the corresponding l1 diamond;
   - `R08-X002`: exact finite triangle equality persists on positive-probability Exp(1) cylinder events, so no pointwise finite-environment proportional strict-saving theorem can work.

3. `runs/R08/20260916T1528Z_fpp_axis_transition_3b7c92.md`.
   - exact auxiliary axis lower bound
     \[
     \mu(e_1)\ge3753/12500=0.30024;
     \]
   - hence a sufficient diagonal target is
     \[
     \mu(1,1)<3753/6250=0.60048.
     \]

4. `runs/R08/20260916T1623Z_stuck_diagblock_4c19a7.md`.
   - stuck episode 1 after three unchanged source-defect runs;
   - exact fixed-corner full-square blocks gave
     `U_1=1.25`, `U_2=30757/28800`, and the `U_3` value displayed above, all too large;
   - the old route was then retired from R08, which moved to I0082. Later R08 explicitly records the FPP assignment as `RETIRED_FROM_R08_SLOT / mathematically OPEN`.

The neighboring old R07 FPP/KPZ chain was also recovered, including

- `runs/R07/2026-09-16T1425Z_kpz_weighted_overlap_02.md`,
- `runs/R07/2026-09-16T1525Z_kpz_deep_edges_03.md`,
- `runs/R07/2026-09-16T1624Z_kpz_stuck_recovery_01.md`.

Those reports concern variance/KPZ overlap mechanisms and audits of narrow R08 claims. Their fluctuation assumptions are **not** imported as curvature or strict convexity here. R07 later rotated to another source.

Other indexed FPP claims (for example fluctuation, max-flow and unrelated modern FPP questions) were checked as non-equivalent; no ownership bypass is minted from them.

## 4. Current source/literature status — bounded check on 20 September 2026

Primary/source navigation and bounded current searches covered the exact ADH Question 4 wording, `strict convexity first-passage percolation exponential`, Busemann/strict-convexity aliases, and recent 2024–2026 follow-ups.

The distinctions relevant to this run remain:

- Auffinger–Damron–Hanson, arXiv:1511.03262, is the source navigation for Question 4.
- Lalley (2003) is a conditional strict-convexity theorem, not an unconditional Exp(1) solution.
- Dembin–Elboim–Peled, GAFA 2024 / arXiv:2204.02332, prove quantitative planar coalescence under an assumption that the limit shape has more than 32 extreme points; using that hypothesis here would be circular.
- Jacquet, arXiv:2412.20779 (2024), proves strict inequality between unrestricted and directed FPP time constants. It does not provide the missing comparison `directed_mu(1,1) <= 2 mu(e1)` and therefore does not close `Delta_12>0`.
- Bakhtin–Dow, arXiv:2406.09652 (2024), treat differentiability in different continuous-action FPP models, not ordinary nearest-neighbor lattice Exp(1) FPP.
- Krishnan, *Variational Formula for the Time Constant of First-Passage Percolation* (CPAM 2016; arXiv:1311.0316), gives an exact HJB/duality variational formula. It is relevant to B11 below but no explicit Exp(1) corrector furnishing the needed strict directional defect was found.

No primary-source theorem closing ordinary iid Exp(1) nearest-neighbor strict convexity surfaced in this bounded check. This is **bounded negative search evidence**, not a claim of exhaustive worldwide openness.

## 5. Three genuinely different approaches tried

The idea was written before the checker in

`artifacts/prob10_2026-09-20/PROB10-10/20260919T2321Z__idea-point-to-line-slab-compiler.md`

commit

`356b96a12d01e5df1fc98450615a47d93a9cf511`.

This run used **B2 / B11 / B19**.

### B2 — attack the negation / hidden failure modes

I tried to invalidate the random-endpoint block idea before accepting it.

Three possible failures were isolated and removed:

1. adaptive block endpoints might drift linearly and change the asymptotic direction;
2. random spatial translation might destroy iid block structure;
3. correcting the final transverse displacement might reuse revealed edges and create an unpaid dependence term.

The proof in §6 deals with all three exactly: reflection gives zero drift, antidiagonal level sets give disjoint block edge sigma-fields, and the final connector is placed entirely on the fresh next edge level.

### B11 — dualize through HJB/Busemann variables

Krishnan's variational formula and Busemann/corrector language make strict convexity look like strict separation of directional support values. This is structurally attractive, but the present route still lacks an explicit stationary Exp(1) corrector/cocycle with a quantitative strict defect. Existing coalescence results found in the source check require nontrivial shape information. I therefore do **not** convert this route into a theorem this run.

### B19 — make it an algorithm

This is the successful route. Instead of forcing every finite block to end at a deterministic corner, allow each independent antidiagonal slab to choose its cheapest oriented exit. The exit direction is random but symmetric, so the accumulated transverse displacement is sublinear. This retains the within-block dependence exactly and removes the fixed-corner reset cost.

## 6. Main theorem: random-endpoint antidiagonal slab compiler

For integer `m>=1`, define antidiagonals

\[
H_k:=\{x\in\mathbb Z^2:x_1+x_2=2mk\}.
\]

Set `X_0=0`. Given `X_k in H_k`, consider only paths using `+e_1,+e_2` edges and ending anywhere on `H_{k+1}`. Let `tau_k` be the minimum passage time among these paths, and let `X_{k+1}` be its endpoint. Exp(1) continuity makes the minimizing endpoint unique almost surely.

Write

\[
X_{k+1}-X_k=(m+D_k,m-D_k),\qquad |D_k|\le m.
\tag{6.1}
\]

Let

\[
q_m:=\mathbb E\tau_0.
\]

### Theorem 6.1

For every integer `m>=1` and `n>=1`,

\[
\boxed{
\frac{\mathbb E T(0,nm(1,1))}{nm}
\le
\frac{q_m}{m}+\frac{2}{\sqrt n}.
}
\tag{6.2}
\]

Consequently,

\[
\boxed{\mu(1,1)\le q_m/m.}
\tag{6.3}
\]

This is a theorem about the original **undirected** FPP model: the oriented slab paths are merely an admissible subclass used to construct an upper bound.

### Proof

Partition oriented edges by the lower endpoint's `l1` level. Slab `k` uses only edges joining levels

\[
2mk,2mk+1,\ldots,2m(k+1).
\]

More precisely, every used edge has lower level in

\[
[2mk,2m(k+1)-1].
\]

These global edge-level sets are disjoint across `k`. `X_k` is measurable with respect to earlier slabs, and conditional on `X_k`, translation invariance along `H_k` makes the fresh slab environment have exactly the same law as slab 0. Therefore

\[
(\tau_k,D_k)_{k\ge0}
\]

are iid.

Reflection `(x_1,x_2) -> (x_2,x_1)` preserves the Exp(1) environment and sends the unique minimizing endpoint displacement `D_k` to `-D_k`. Hence

\[
\mathbb E D_k=0.
\tag{6.4}
\]

Put

\[
S_n:=\sum_{k=0}^{n-1}D_k.
\]

Then

\[
X_n=(mn+S_n,mn-S_n).
\tag{6.5}
\]

Concatenating the `n` slab minimizers gives a valid undirected path from `0` to `X_n` of cost

\[
\sum_{k=0}^{n-1}\tau_k.
\tag{6.6}
\]

It remains to connect `X_n` to the deterministic diagonal point `Y_n=(mn,mn)` without paying a linear hidden error.

If `S_n>0`, repeat the two-step move north then west exactly `S_n` times. If `S_n<0`, repeat east then south exactly `|S_n|` times. Every connector edge lies between levels `2mn` and `2mn+1`. No earlier slab used an edge with lower level `2mn`, so these connector edges are fresh conditional on the entire block history, including `S_n`. They are distinct iid Exp(1) edges. Thus

\[
\mathbb E[\text{connector cost}\mid S_n]=2|S_n|.
\tag{6.7}
\]

Since the increments are iid, centered, and satisfy `|D_k|<=m`,

\[
\mathbb E|S_n|
\le
\sqrt{\mathbb E S_n^2}
=\sqrt{n\,\mathbb E D_0^2}
\le m\sqrt n.
\tag{6.8}
\]

Using (6.6)–(6.8),

\[
\mathbb E T(0,Y_n)
\le nq_m+2m\sqrt n.
\tag{6.9}
\]

Divide by `nm` to obtain (6.2). Standard `L^1` convergence of FPP passage times to the time constant applies because Exp(1) is integrable; taking `n->infinity` along the subsequence `nm` gives (6.3). QED.

### What the theorem pays and what it does not pay

The finite-to-infinite error is explicit:

\[
\boxed{2/\sqrt n.}
\]

There is no unproved KPZ rate, no sampled curvature, no assumed differentiability, and no independence assumption inside one block. All dependence inside a slab is absorbed in the single exact finite quantity `q_m`.

## 7. Exact finite computation of `q_m` for `m=1,2,3`

For level `L=2m`, let

\[
V_L:=\{(x,y)\in\mathbb Z_{\ge0}^2:x+y<L\}.
\]

Run the oriented Exp(1) infection from `(0,0)` until the first infection on `x+y=L`. For an infected set `S subset V_L`, let

- `b(S)` be the number of directed boundary edges from `S` either to an uninfected vertex of `V_L` or to the absorbing target line;
- `r_S(v)` be the number of boundary edges from `S` to an uninfected transient vertex `v`.

Exponential memorylessness gives the exact recursion

\[
E(S)
=
\frac1{b(S)}
+
\sum_{v\in V_L\setminus S}
\frac{r_S(v)}{b(S)}E(S\cup\{v\}),
\tag{7.1}
\]

with zero future cost on jumps to the target line. This is an exact finite-state calculation; no simulation enters the certificate.

The executed Fraction-arithmetic checker gives

\[
q_1=\frac{11}{12},
\qquad
\frac{q_1}{1}=0.9166666666\ldots,
\]

\[
q_2=\frac{5927950393}{3556224000},
\qquad
\frac{q_2}{2}
=\frac{5927950393}{7112448000}
=0.833461333284967\ldots,
\]

and

\[
q_3=
\frac{93432902428288084006412573734630991128481810947182059}
{39418506878807397162490324791290356020019200000000000},
\]

so

\[
\boxed{
\frac{q_3}{3}
=
\frac{93432902428288084006412573734630991128481810947182059}
{118255520636422191487470974373871068060057600000000000}
=0.790093366681362\ldots .}
\tag{7.2}
\]

The memoized exact recursion visits 4, 96, and 10,564 states respectively for `m=1,2,3`.

The checker also proves exactly

\[
q_3/3<U_3^{\rm old}.
\]

Thus this is not a finite-size fit: (7.2), together with Theorem 6.1, is a rigorous asymptotic diagonal upper bound for the original undirected model.

## 8. Exact artifacts and execution

Idea before code:

- `artifacts/prob10_2026-09-20/PROB10-10/20260919T2321Z__idea-point-to-line-slab-compiler.md`
- commit `356b96a12d01e5df1fc98450615a47d93a9cf511`

Exact checker:

- `artifacts/prob10_2026-09-20/PROB10-10/point_to_line_exact_20260919T2321Z.py`
- commit `bc892157dad82c048d9269d9f6d88a3af3dfecb0`

Executed output:

- `artifacts/prob10_2026-09-20/PROB10-10/point_to_line_exact_20260919T2321Z.out`
- commit `a128adccd70632093c682c4851738de61d5ad453`
- final line: `ALL_EXACT_CHECKS_PASS = True`.

All three artifacts were read back at their returned commits before this report was written.

## 9. Why the source defect still does not move

The retained R08 axis certificate gives

\[
2\mu(e_1)\ge0.60048.
\]

The new diagonal certificate gives only

\[
\mu(1,1)\le0.7900933667\ldots .
\]

These inequalities do not order the two quantities in the direction needed for

\[
2\mu(e_1)-\mu(1,1)>0.
\]

Therefore `c_*=0` remains the honest source-level value.

The meaningful advance is that the old finite-corner reset overhead is removed with a proved `O(n^{-1/2})` finite-to-infinite correction. The remaining task is now genuinely finite inside each slab: improve/certify `q_m/m` far enough, or combine this compiler with a stronger direction-sensitive lower bound, without assuming curvature.

## 10. Next mathematical obligation

The next run should **not** return to the retired generic local-detour proof. It should choose one of the following within this source:

1. derive a scalable rigorous upper certificate for `q_m` beyond the exact-state limit `m=3`, preferably using a compressed front-state Markov chain / Bellman super-solution with interval or rational error control; or
2. pursue the overlap-controlled second-moment route for fast directed point-to-line paths, with the split/rejoin overlap kernel written explicitly; or
3. use Krishnan's variational duality to build a finite-state sub/super-corrector whose directional defect can be certified without shape assumptions.

A mere larger Monte Carlo estimate of `q_m` is not progress. A valid next source movement is either a certified `q_m/m` reduction with a proof/error budget, or a positive lower bound for `Delta_12` itself.

## 11. Independent validation state

This run is a **self-check**, not an independent audit. No source closure is claimed and no audit was requested from another task in this execution. The exact finite checker validates only the finite `q_m` recursion/results; Theorem 6.1 is proved on the page above.

## 12. Ledger delta for the designated reconciler

```yaml
ledger_delta:
  task: "PROB10-10"
  source: "Auffinger-Damron-Hanson, arXiv:1511.03262, Question 4; Exp(1) Z^2 undirected special case"
  canonical_claim: "operations/claims/PROB10-10.md"
  target: "strict convexity of the full Exp(1) planar FPP limit shape"
  frozen_pair: "e1,e2"
  source_metric: "largest proved c>=0 with 2 mu(e1)-mu(1,1)>=c"
  before: "0"
  after: "0"
  movement: "NO MOVEMENT in source defect"
  status: "PARTIAL / OPEN"
  auxiliary_metric: "rigorous diagonal upper bound mu(1,1)"
  auxiliary_before: "5675443731448268047/5807171543040000000 = 0.9773163561... (old R08 m=3 fixed-corner block)"
  auxiliary_after: "93432902428288084006412573734630991128481810947182059/118255520636422191487470974373871068060057600000000000 = 0.790093366681362..."
  direction_range: "diagonal (1,1) only"
  finite_to_infinite_error: "E T(0,nm(1,1))/(nm) <= q_m/m + 2/sqrt(n)"
  methods: [B2, B11, B19]
  audits: []
```
