Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum.** No authenticated runtime model/effort telemetry establishes the requested GPT-6/maximum setting.

# R7-01 admission diagnostic — F0137 exact source correction, clean Dirichlet test ray, and current gate

Date checked: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Slot / native id: `R7-01` / `6aabe777361481919c9e614646464772`.  
Selection shard: `sum(ord(c) for c in canonical_id) mod 7 = 0`.  
Candidate: `F0137`; exact character sum `70+48+49+51+55 = 273 = 39*7`, hence shard 0.

## 1. Why this is a delta rather than a duplicated admission screen

R7-01's 2026-09-18 cumulative screen left `F0137` at “requires unresolved source/prior-art reconciliation.” A later neighboring R20 report (`runs/R20/2026-09-18T09-05-00Z_successor_admission_f0137_dirichlet_status_81c4e2.md`) performed a dated status check and correctly classified the full target as current-open-looking but HARD / not CLOSABLE / not claimed. I reuse that work rather than repeating it.

The new contribution here is narrower and mathematical:

1. correct the exact source locator and source endpoint;
2. exhibit a one-parameter Dirichlet family that crosses the source's explicit Theorem 6.5 sufficient-condition boundary exactly at one scalar value;
3. compute the source trap exponent `kappa`, annealed drift and an exact local beta/log-odds diagnostic on that family; and
4. use current positive author evidence to keep the full question out of the CLOSABLE queue without treating a search miss as proof of openness.

No canonical ownership claim is created by this artifact.

## 2. Exact outside source and corrected locator

Outside source:

- Christophe Sabot and Laurent Tournier,
  *Random walks in Dirichlet environment: an overview*;
- preprint arXiv:1601.08219 (2016); published in *Annales de la Faculté des sciences de Toulouse*, Série 6, 26(2) (2017), 463–509;
- public journal scan: `https://afst.centre-mersenne.org/item/10.5802/afst.1542.pdf`;
- exact location: Section 6.1, after Corollary 6.6, printed page **487** (journal scan PDF page index 25 after the cover/front matter); the preceding explicit sufficient condition is Theorem 6.5 / equation (6.1) on printed page 486.

This corrects the intake row's old navigation note “PDF p. 19.” The mathematical statement in the intake was substantially right, but the exact page locator was not.

### Source model

For `d >= 2`, let `e_1,...,e_d` be the coordinate unit vectors and `e_{i+d}=-e_i`. At every `x in Z^d`, independently sample

`(omega(x,x+e_i))_{i=1}^{2d} ~ Dirichlet(alpha_1,...,alpha_{2d})`,

with every `alpha_i>0`. Define

`d_alpha := sum_{i=1}^{2d} alpha_i e_i`

and the finite-trap integrability exponent

`kappa := 2 sum_{i=1}^{2d} alpha_i - max_{1<=i<=d}(alpha_i+alpha_{i+d})`.

The source's Definition 6.1 defines `(T)_gamma`, `0<gamma<1`, through stretched-exponential control up to the first renewal time, and defines **`(T)'`** to mean `(T)_gamma` for every `gamma<1`.

Theorem 6.5 gives the explicit sufficient condition

`sum_{i=1}^d |alpha_i-alpha_{i+d}| > 1`,                                             (6.1)

under which the RWDE satisfies a stronger ballisticity condition and hence `(T)'`.

Immediately after Corollary 6.6, the source says that (6.1) is expected not to be optimal and conjectures that at least **`(T)'`** holds whenever `d_alpha != 0`; consequently the renewal time should have finite `s`-moments for `s<kappa` in the directionally transient regime.

The exact literal endpoint is therefore `(T)'`, not merely “some `(T)_gamma`.” This is a source-scope correction to the shorthand intake title.

## 3. Current-status evidence, dated 2026-09-19

The strongest positive later-author evidence found is Adrien Perrel and Christophe Sabot, *Invariant measure for the process viewed from the particle for 2D random walks in Dirichlet environment*, arXiv:2501.06767 (submitted 2025-01-12). In its discussion of condition `(T)'`, the authors state that directional transience is conjectured to be equivalent to `(T)'`, that partial results exist, and that a full proof “seems still out of reach”; they then say specifically for Dirichlet environments that it is expected that `(T)'` holds as soon as `d_alpha != 0`. Their main transient 2D theorem still assumes `(T)'` separately.

A bounded fresh 2026-09-19 search for Dirichlet-environment directional transience / `(T)'` / Sabot / Perrel surfaced that 2025 paper and older partial criteria, but no 2026 paper claiming the full Sabot–Tournier implication. This negative search is **not** treated as a proof of worldwide openness, novelty, or priority.

Neighboring R20 had also recovered Adrien Perrel's 2024 stable-limit work in `d>=3`, where condition `(T)` remains an assumption. That evidence is reused, not re-counted as new.

Admission-status conclusion from the current evidence:

`CURRENT-OPEN-IN-LATEST-POSITIVE-AUTHOR-EVIDENCE / HARD GLOBAL REGENERATION THEOREM / NOT_ADMITTED`.

## 4. A clean one-parameter source test ray

Fix any `d>=2` and let `0<delta<=1`. Define

`alpha_1 = 1+delta`,

and

`alpha_i = 1` for every `i != 1`.

Thus the only imbalance is between `+e_1` and `-e_1=e_{1+d}`.

### Lemma 4.1 — drift and exact source-condition gap

For this family,

`d_alpha = delta e_1 != 0`,

while

`sum_{i=1}^d |alpha_i-alpha_{i+d}| = delta <= 1`.

Hence the family lies exactly in the conjectural nonsymmetric regime but outside the source's explicit Theorem 6.5 sufficient condition for every `0<delta<=1`. At `delta>1`, the source condition (6.1) turns on immediately.

**Proof.** Every opposite pair except `(e_1,-e_1)` has equal weights `1,1`; the first pair has weights `1+delta,1`. Therefore all pair differences vanish except the first, whose signed difference is `delta` and whose absolute difference is also `delta`. This gives both displayed identities. The strict source threshold is `>1`, so it fails throughout `(0,1]` and holds for `delta>1`. QED.

This is a useful exact diagnostic because there is no multidimensional parameter geometry left in the source's own sufficient condition: along this ray its entire gap is the interval `(0,1]`.

Define the admission-only source diagnostic

`W_source := length{delta in (0,1] : d_alpha !=0 but source condition (6.1) fails}`.

Then exactly

`W_source = 1`.

This is **not** a metric of progress on the conjecture; it only quantifies the part of this chosen ray not certified by the source's own Theorem 6.5.

### Lemma 4.2 — trap exponent on the same ray

On the same family,

`kappa = 4d - 2 + delta`.

In particular `kappa>1` by a very large margin for every `d>=2` and `delta>0`; in dimension two, `kappa=6+delta`.

**Proof.** The total Dirichlet weight is

`sum_i alpha_i = 2d+delta`.

The largest opposite-pair sum is

`max_i(alpha_i+alpha_{i+d}) = 2+delta`,

attained by the first coordinate pair. Substitute into the source formula:

`kappa = 2(2d+delta) - (2+delta) = 4d-2+delta`. QED.

Thus the clean gap family is not produced by a small trap exponent. The source's strongest finite two-vertex trap moment obstruction is already mild here, yet the global `(T)'` implication is not supplied by Theorem 6.5.

### Lemma 4.3 — exact annealed one-step drift

Let `alpha_0=sum_i alpha_i=2d+delta`. Since a Dirichlet coordinate has mean `alpha_i/alpha_0`,

`E_0[X_1] = d_alpha/alpha_0 = (delta/(2d+delta)) e_1`.

So even as `delta downarrow 0`, the direction of the annealed drift is exactly `e_1`, while its magnitude tends to zero linearly.

### Lemma 4.4 — exact local right/left split

At a fixed site set

`U := omega(x,x+e_1) / (omega(x,x+e_1)+omega(x,x-e_1))`.

Then

`U ~ Beta(1+delta,1)`.

Consequently

`P(U<1/2) = 2^{-(1+delta)}`

and

`E[ log(U/(1-U)) ] = psi(1+delta)-psi(1) > 0`,

where `psi` is the digamma function.

**Proof.** Use the standard gamma representation of a Dirichlet vector: take independent `Y_i~Gamma(alpha_i,1)` and set `omega_i=Y_i/sum_jY_j`. The normalized ratio inside the first opposite pair is

`U=Y_1/(Y_1+Y_{1+d})`,

hence `Beta(alpha_1,alpha_{1+d})=Beta(1+delta,1)`. Its density is `(1+delta)u^delta` on `(0,1)`, so its CDF is `u^{1+delta}` and the first probability follows. The beta log-moment identities give

`E log U = psi(1+delta)-psi(2+delta)`,

`E log(1-U)=psi(1)-psi(2+delta)`,

hence the stated difference. Since `psi` is strictly increasing and `delta>0`, it is positive. QED.

## 5. Why this does not solve or even reduce the global source theorem to 1D

The last lemma is deliberately only a local diagnostic. It is tempting to interpret `U` as a one-dimensional RWRE and invoke one-dimensional log-bias theory. That reduction is invalid: the actual walk has transverse moves, can revisit sites through transverse excursions, and samples the full coupled Dirichlet vector at every visited site. The projected first coordinate is not an autonomous nearest-neighbor RWRE with i.i.d. beta transition probabilities.

The exact blocking question remains global: prove stretched-exponential slab/backtracking control and the corresponding regeneration estimate from `d_alpha !=0` alone. The clean ray shows that even when

- the drift direction is explicit,
- the local opposite-pair log bias is explicitly positive,
- the trap exponent is `4d-2+delta`, and
- the only failure of the source's explicit sufficient criterion is the scalar inequality `delta<=1`,

the source-level conclusion still requires a genuinely multidimensional regeneration argument.

That is theorem-sized work, not a finite certificate, one sharp constant, or a short counterexample route. It therefore does not meet R7-01's CLOSABLE admission contract.

## 6. Admission disposition

`F0137` remains:

- outside source: **yes**;
- exact shard 0: **yes**;
- current source scope recovered: **yes**;
- positive later-author evidence that the full implication remains conjectural as of 2025: **yes**;
- bounded 2026-09-19 search found a later full resolution: **no**, but this is not a proof of openness;
- ownership: no canonical `operations/claims/F0137.md` found in the repository screen;
- classification for R7-01: **HARD, not CLOSABLE**;
- admission: **NO**;
- canonical claim creation: **NO**.

R7-01's actual successor metric therefore remains `UNKNOWN/UNMEASURED`; successor stagnation remains `NOT_STARTED`; no Section-B research method is charged.

## 7. Reusable handoff

If a future HARD slot lawfully takes F0137, this family is a clean first benchmark:

`alpha(delta)=(1+delta,1,...,1), 0<delta<=1`.

A source-valid advance would need to prove `(T)'` on a nontrivial subinterval of this ray (or refute it) without assuming the source's condition (6.1). The exact frozen quantities available for that future owner are

- source sufficient-condition statistic: `S(delta)=delta`;
- trap exponent: `kappa(delta)=4d-2+delta`;
- annealed drift magnitude: `delta/(2d+delta)`;
- local backward-split probability: `2^{-(1+delta)}`;
- local expected log odds: `psi(1+delta)-psi(1)`.

None of those quantities by itself proves `(T)'`.
