Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** Fresh target metric **no movement on admission**: `W_3 = 0.9064 -> 0.9064`; methods actually tried on the fresh target: **B2 / B11 / B24**. The exhausted CKS predecessor is handed off with `L_6 >= 0 -> L_6 >= 0`; no third recovery is taken.

# HARD7-06 run 10 — STUCK3 handoff of CKS and admission of F0095; exact correlated-overlap obstruction for raw balanced 3-colouring counts

Status: **F0095 OPEN / HARD7-06 PARTIAL.**  The predecessor `CKS-2024-RREG-HYPER2COL-K3` remains OPEN/PARTIAL and is handed off by the Section-I rotation rule.

Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Required Section-I rotation: CKS gets a handoff, not a third recovery

The previous report, `2026-09-19T04-49-49Z__cycle_code_duality.md`, was the second substantive execution after `STUCK2` and explicitly marked the second and final allowed recovery.  The frozen source-facing quantity has still not moved:

\[
L_6:=\sup\{L:\liminf_n\Pr(H_{n,6,3}\text{ is 2-colourable})\ge L\},
\qquad L_6\ge0\longrightarrow L_6\ge0.
\]

Therefore this is the third stuck episode for that exact obligation.  Under Section I I do **not** produce another CKS lemma.  I leave the following source-preserving handoff and rotate.

### (a) Exact blocking statement

The first source-matching milestone still not proved is

\[
\boxed{\liminf_{n\to\infty}\Pr(H_{n,6,3}\text{ is 2-colourable})>0,}
\tag{1.1}
\]

with `H_{n,6,3}` the source's uniformly random **simple** 6-regular 3-uniform hypergraph along admissible `n`.  The conjectured endpoint is convergence to one.

Equivalently, in the exact cut-coset formulation from run 9, one needs a random-factor-graph theorem that the zero cut-code coset contains a one-hot transversal with nonvanishing probability.

### (b) Routes actually tried and the precise failure of each

1. **Raw balanced-colouring second moment / overlap variational route.**  The independent overlap is unstable at `d=6`; correlated pairs make the normalized second moment exponentially large, so the unweighted Paley-Zygmund route does not move `L_6`.
2. **Global overlap saddle / pitchfork analysis.**  It identifies the bad correlated saddle but supplies no weight for which the full pair variational problem is controlled.
3. **Minority-profile deformation.**  A profile tilt repairs a local curvature defect, but the global overlap landscape remains uncontrolled; local stability is not a probability lower bound.
4. **Cluster-level / hard-field port from random regular NAE-SAT.**  The finite warning recursion bifurcates, but its hard-field state space is too small to represent the source's unsigned global cycle sector.
5. **Factor-local soft size tilts.**  The exact two-point calculation gives a no-go: local size tilting cannot stabilize the `d=6` soft-message origin.
6. **BMS/reconstruction transfer.**  The nearest solved random-literal tree theory averages over literal/gauge sectors.  The source fixes the all-zero sector, so the tree law erases exactly the global information that must be controlled.
7. **Gauge-sector attack.**  Finite simple witnesses show satisfiability can depend on cycle flux, but a finite witness neither proves nor refutes an asymptotic high-probability source statement.
8. **Exact cut-coset / cycle-code Fourier duality.**  This gives a source-native global object, but the natural absolute nonbacktracking loop expansion fails at the exact branching factor
   \[
   (6-1)(3-1)(1/3)^2=10/9>1.
   \]
   Thus the bounded-cycle perturbative sum is outside its convergence radius at the source point.

### (c) Ingredient no tried route contains

A successful continuation needs a **nonperturbative zero-sector theorem**: either signed/root-of-unity cancellation for the cycle-code Fourier sum, or a structured-code occupancy theorem for the zero cut coset, strong enough to survive the `10/9` instability.  Tree-local literal averaging and absolute loop summation both discard the required mechanism.

### (d) Simplest source-valid special case still unproved

Exactly (1.1): positive limiting lower probability for the simple `(d,k)=(6,3)` model.  No narrower finite graph calculation substitutes for it.

### (e) Nearest solved literature analogue and what it has that this case lacks

The large-`k` random-regular NAE-SAT/colouring theory of Ding--Sly--Sun and subsequent one-step-RSB work has a cavity/cluster regime whose estimates close when `k` is sufficiently large and, in the labelled formulation, benefits from literal averaging.  The small `k=3` unsigned source has neither the large-`k` contraction/slack nor literal-sector averaging.  The 2026 exact reconstruction results on hypertrees clarify the tree threshold but do not supply the missing global-cycle zero-sector theorem.

**Handoff verdict:** `CKS-2024-RREG-HYPER2COL-K3` stays **OPEN/PARTIAL**, `L_6>=0`, and HARD7-06 relinquishes active attack after the two allowed recoveries.  Historical reports and the existing claim remain immutable evidence of the former assignment; this report is the operational handoff.

---

## 2. Fresh admission after rotation: F0095, sparse random-graph 3-colourability threshold

I reread the controlling HARD7 files, `POSTED.md`, `RESULTS.md`, `QUEUE.md`, campaign `INDEX.md` and `RANKING.md`, the F-intake ledger/catalog, the old F0095 intake attempt, the R03/F0097 history, the CKS claim and the newest neighbouring CSP reports before rotating.  Thus this is not a restart from a blank literature list.

The fresh canonical reservation is

`operations/claims/F0095.md`, owner `HARD7-06`.

It was created with create-only semantics after a direct fetch confirmed that path did not exist.  Repository searches for `F0095`, `Achlioptas Friedgut colorability`, `Dubois Mandler`, `3-colorability threshold`, and `random graph coloring threshold` found the intake row and old unreviewed attempt, plus an R7-04 screening note calling F0095 a hard classic problem, but no canonical claim or active equivalent owner.  F0097 remains a distinct small-fixed-`k` random SAT lifecycle and is not reopened.

### Exact external source statement

The canonical intake quotes Alan Frieze's ICM 2014 chromatic-number slide, PDF p. 82:

> **Conjecture:** There exists a sequence `d_k : k >= 2` such that w.h.p. `chi(G_{n,d/n}) = k` for `d_{k-1} < d < d_k`.

The exact fixed-`k=3` content relevant to this lane is the existence of a constant location for the ordinary sparse Erdős--Rényi 3-colourability transition, not merely an `n`-dependent sharp threshold.  Achlioptas--Friedgut (Random Structures & Algorithms 14 (1999), 63--70) prove the latter: for every fixed `k>=3` there is a sharp threshold sequence `d_k(n)`.  That theorem does **not** prove that `d_3(n)` converges.

An older primary formulation is Fountoulakis--McDiarmid, *Upper bounds on the non-3-colourability threshold of random graphs*, DMTCS 5 (2002), which places the 3-colour threshold question in the longstanding Erdős programme.  The fresh bounded 2026-09-19 search used the queries

- `Frieze ICM 2014 chromatic number conjecture random graph d_k k-colorability`,
- `random graph 3-colorability threshold fixed k=3 2025 2026`,
- `3-colourability threshold random graph 2026`,
- `k-colorability threshold k=3 random graph`,
- the exact Achlioptas--Moore and Dubois--Mandler titles.

It recovered the classical sharp-threshold and small-`k` bound papers, large-`k` colourability/condensation work, and Mizgerd--Perkins--Wang (RSA 2026) on the **different conditioned triangle-free random-graph model**.  It did not recover a proof that the threshold sequence for ordinary sparse Erdős--Rényi 3-colourability converges to a constant.  This is bounded negative evidence, not a worldwide-openness certificate.

## 3. Frozen metric and verified admission baseline

For the new target define

\[
W_3:=U_3-L_3,
\tag{3.1}
\]

where `L_3` is a primary-source-verified average degree below which ordinary sparse Erdős--Rényi graphs are 3-colourable w.h.p., and `U_3` is a primary-source-verified average degree above which they are non-3-colourable w.h.p., with the standard `G(n,p=d/n)` / `G(n,m=(d/2)n+o(n))` monotone-model transfer kept explicit.

The admission baseline is deliberately conservative and auditable:

- Achlioptas--Moore, *Almost all graphs with average degree 4 are 3-colorable*, JCSS 67 (2003), prove 3-colourability w.h.p. for `G(n,p=d/n)` when `d<=4.03`; hence `L_3=4.03` is certified.
- Dubois--Mandler, *On the non-3-colourability of random graphs*, arXiv:math/0209087 (2002), prove that a random graph with `m=c n(1+o(1))` edges is non-3-colourable w.h.p. for `c>=2.4682`; in average-degree units this is `U_3=4.9364`.

Therefore

\[
\boxed{W_3=4.9364-4.03=0.9064.}
\tag{3.2}
\]

A secondary historical source reports a stronger upper number around `4.854`; I do **not** promote it into the frozen metric until its exact primary theorem/model has been recovered and checked.  Thus `0.9064` is a **primary-verified campaign baseline**, not a claim that it is the current worldwide best numerical bracket.

This run develops a route obstruction rather than improving either endpoint, so

\[
\boxed{W_3:0.9064\longrightarrow0.9064\quad\text{(no movement).}}
\tag{3.3}
\]

## 4. B2 — attack the negation: the raw balanced-count second moment destabilizes before the proved colourable regime ends

Let `n` be divisible by 3 and let `Z_bal(G)` be the number of proper 3-colourings of `G(n,m)` with exactly `n/3` vertices in each colour.  Put

\[
m=\frac d2 n+o(n).
\]

For two balanced colourings `sigma,tau`, define their overlap matrix

\[
a_{ij}:=\frac1n\#\{v:\sigma(v)=i,\ \tau(v)=j\}.
\]

Then `A=(a_ij)` is doubly stochastic after scaling: every row and column sums to `1/3`.  Let

\[
H(A):=-\sum_{i,j}a_{ij}\log a_{ij}.
\]

For a uniformly random potential edge, the probability that it is bichromatic under **both** colourings is, up to the vanishing no-loop correction,

\[
Q(A)=1-\sum_i r_i^2-\sum_j c_j^2+\sum_{i,j}a_{ij}^2
=\frac13+\|A\|_F^2,
\tag{4.1}
\]

because `r_i=c_j=1/3`.  At independent overlap

\[
A_0=J/9,
\qquad Q(A_0)=4/9.
\]

The number of ordered colouring pairs of overlap type `A` is

\[
\exp\{nH(A)+o(n)\},
\]

and their probability of surviving all `m` uniformly sampled edges is

\[
\exp\left\{\frac d2 n\log Q(A)+o(n)\right\}.
\]

On the other hand

\[
\mathbb E Z_{bal}
=\exp\left\{n\log3+\frac d2n\log(2/3)+o(n)\right\}.
\]

Consequently a fixed overlap type contributes to the normalized second moment at exponential rate

\[
\boxed{
\Phi_d(A)
=H(A)-2\log3
+\frac d2\log\!\left(\frac{\frac13+\|A\|_F^2}{4/9}\right).
}
\tag{4.2}
\]

Here `Phi_d(A_0)=0`.  Thus finding any admissible `A` with `Phi_d(A)>0` proves an exponential obstruction to the naive unweighted balanced-count Paley--Zygmund argument.  It does **not** say the graph is non-colourable.

## 5. B11 — variational/Hessian dual view: an exact instability threshold at d=4

### Proposition 5.1

Let `X` be any nonzero real `3x3` matrix with every row and column sum zero.  For sufficiently small `t`, set `A(t)=A_0+tX`.  Then

\[
\boxed{
\left.\frac{d^2}{dt^2}\Phi_d(A(t))\right|_{t=0}
=\frac94(d-4)\|X\|_F^2.
}
\tag{5.1}
\]

Hence the independent balanced overlap is a strict local **minimum** of the normalized pair exponent in every nonzero tangent direction for `d>4`.

#### Proof

Since every entry of `A_0` is `1/9`, the entropy Hessian gives

\[
\left.\frac{d^2}{dt^2}H(A_0+tX)\right|_{0}
=-\sum_{i,j}\frac{X_{ij}^2}{1/9}
=-9\|X\|_F^2.
\tag{5.2}
\]

The tangent constraints imply `sum_ij X_ij=0`, so

\[
\|A_0+tX\|_F^2
=\|A_0\|_F^2+t^2\|X\|_F^2
=\frac19+t^2\|X\|_F^2.
\]

Therefore

\[
Q(A_0+tX)=\frac49+t^2\|X\|_F^2,
\]

and

\[
\left.\frac{d^2}{dt^2}\log Q(A_0+tX)\right|_0
=\frac{2\|X\|_F^2}{4/9}
=\frac92\|X\|_F^2.
\tag{5.3}
\]

Multiplying (5.3) by `d/2` and adding (5.2) yields

\[
-9\|X\|_F^2+\frac{9d}{4}\|X\|_F^2
=\frac94(d-4)\|X\|_F^2.
\]

This proves (5.1). QED.

The result is stronger as a **route diagnosis** than merely testing the target density near 4.5: the completely unweighted balanced-colouring count has already lost the independent-overlap second-moment saddle immediately above average degree 4.

## 6. B24 — extremal correlated direction: explicit one-parameter obstruction, including d<4

Consider the symmetric overlap family

\[
A_s=\frac19
\begin{pmatrix}
1+2s&1-s&1-s\\
1-s&1+2s&1-s\\
1-s&1-s&1+2s
\end{pmatrix},
\qquad 0<s<1.
\tag{6.1}
\]

It has all row and column sums `1/3` and

\[
\|A_s\|_F^2=\frac19+\frac{2s^2}{9}.
\]

Substitution into (4.2) gives the exact scalar rate

\[
\boxed{
\Phi_d(s)=
-\frac13(1+2s)\log(1+2s)
-\frac23(1-s)\log(1-s)
+\frac d2\log\left(1+\frac{s^2}{2}\right).
}
\tag{6.2}
\]

Its Taylor expansion at the independent point is

\[
\boxed{
\Phi_d(s)
=\left(\frac d4-1\right)s^2
+\frac13s^3
-\left(\frac12+\frac d{16}\right)s^4
+O(s^5).
}
\tag{6.3}
\]

Thus even at the Hessian boundary `d=4`, the positive cubic term gives

\[
\Phi_4(s)>0
\]

for all sufficiently small positive `s`.  So the obstruction is one-sided through the nominal quadratic boundary rather than disappearing there.

More importantly, an exact rational witness puts the failure strictly **below** 4.  At

\[
d=\frac{383}{100}=3.83,
\qquad s=\frac7{25}=0.28,
\]

the exact checker uses a rational atanh-series enclosure for each logarithm in (6.2) and certifies

\[
\boxed{\Phi_{3.83}(7/25)>0,}
\tag{6.4}
\]

with rigorous lower endpoint approximately

\[
7.934699731953319\times10^{-5}>0.
\]

For `n` in the compatible cell-count subsequence, this single overlap type already makes

\[
\frac{\mathbb E Z_{bal}^2}{(\mathbb E Z_{bal})^2}
\ge \exp\{c n+o(n)\}
\]

for some `c>0`.  Therefore the raw balanced-colouring count cannot prove a nonvanishing 3-colourability probability through ordinary Paley--Zygmund even at `d=3.83`, which is below the primary-verified algorithmic lower region `d<=4.03`.

This is exactly the sort of counterexample-first information the new-method rule asks for: it rules out an attractive proof mechanism rather than producing another checker around an unchanged source bound.  It is **not** a counterexample to the F0095 source conjecture and it does **not** turn a sufficient colouring bound into a necessary threshold.

## 7. Exact finite certificate and scope

Artifacts:

- `artifacts/hard7_2026-09-18/HARD7-06/2026-09-19T05-47-00Z__f0095_overlap_witness.py`
- `artifacts/hard7_2026-09-18/HARD7-06/2026-09-19T05-47-00Z__f0095_overlap_witness.out`

The script uses only `fractions.Fraction`.  It encloses

\[
\log q=2\sum_{j=0}^{N}\frac{y^{2j+1}}{2j+1}+R_N,
\qquad y=\frac{q-1}{q+1},
\]

with an explicit rational geometric tail bound and certifies (6.4) with `N=30`.  The archived output ends

`PHI_STRICTLY_POSITIVE = True`

`ALL_EXACT_CHECKS_PASS = True`.

This checker certifies only the displayed finite analytic inequality.  Proposition 5.1 and the asymptotic type-count reduction are proved on the page.  No finite simulation is used as evidence for threshold convergence.

## 8. What the failed raw count says to try next

The fresh source metric did not move, but the negation attack identifies a concrete design constraint: **any successful second-moment/interpolation variable must suppress correlated colourings without destroying first-moment mass, and it must do so already below degree 4.03.**  Merely requiring exact balance is insufficient.

For the next execution, use a different triple:

- **B5 — ADD A PARAMETER AND DIFFERENTIATE:** introduce a source-valid weighting by local colour-neighbourhood profile / whitening depth and compute the derivative of the pair free energy at zero weight;
- **B20 — FIND WHY THE ALGORITHM FAILS:** translate the Achlioptas--Moore Brelaz-process certificate into a planted/local-profile law and locate exactly why its proof stops at `4.03`;
- **B28 — REPLACE FOR ALL WITH TYPICAL:** seek a second-moment theorem only on the typical local-profile slice, with atypical colourings removed by an exponentially small first-moment estimate.

The goal is not another local Hessian for its own sake; it is either a genuinely source-valid weighted count whose full overlap exponent closes on a nontrivial interval above `4.03`, or a clean no-go showing that this entire weighting category cannot move `W_3`.

## 9. Runtime and scheduler capability honesty

The exposed native scheduler still provides task title, prompt, schedule, timing mode and enabled state, but **no model selector, no reasoning-effort selector and no guaranteed execution duration**.  GPT-6 / maximum is therefore request text only.  This run actually identifies as GPT-5.6 Sol; the reasoning level is not exposed and is recorded as `UNVERIFIED`.

Changing the scheduled model/reasoning setting would require the platform to expose those fields, or an authorized scheduler surface that already controls them; this worker cannot synthesize such a selector by editing repository text.

The repository also records historical native modification probes, including a P26 context, that returned `You cannot modify this task`.  That is an ownership/permission boundary, not a mathematical failure.  The legitimate workaround is for the owner to use the task's authorized account/workspace scheduler surface or platform support to repair ownership/permissions.  Do not bypass the denial, clone a duplicate job, or reactivate a disabled task.  No scheduler was modified in this research run.

## 10. Ledger delta

```yaml
ledger_delta:
  track: HARD7-06
  predecessor_target: CKS-2024-RREG-HYPER2COL-K3
  predecessor_status: PARTIAL_HANDOFF_SECTION_I_EXHAUSTED
  predecessor_metric: L_6
  predecessor_before: ">=0"
  predecessor_after: ">=0"
  target: F0095
  status: PARTIAL
  source_status: OPEN_UNDER_BOUNDED_CURRENT_LITERATURE_REVIEW
  primary_metric: W_3
  metric_definition: "primary-source-verified rigorous average-degree bracket width U_3-L_3"
  before: "0.9064"
  after: "0.9064"
  movement: no movement
  methods: [B2, B11, B24]
  exact_new_result: "balanced raw-count overlap Hessian = (9/4)(d-4)||X||_F^2; exact witness Phi_3.83(7/25)>0"
  interpretation: "raw balanced Paley-Zygmund count is exponentially obstructed; source conjecture not refuted"
  source_closed: false
  independent_audits: 0
  next_methods: [B5, B20, B28]
  next_obligation: "construct or rule out a source-valid typical-profile/weighted count that improves a verified endpoint of W_3"
```

No root shared ledger is edited by this worker; the delta is left for the authorized maintainer.  Closure/paper packaging is not triggered.