Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum, and I do not claim otherwise. SOURCE-LEVEL BEFORE/AFTER since the preceding P13 report: companion P02 moves the true binary-LCS interval from `L <= gamma_2 <= U_W` to `L <= gamma_2 <= U_S < U_W`, with `L=0.792665992`. P13 MECHANISM BEFORE/AFTER: the true correlated width-6 finite-to-infinite additive constant moves strictly from `2036624461477/5000000 = 407324.8922954` to `820311293209/2500000 = 328124.5172836 < 328125`, a 19.444% reduction.**

# P13 / T02 — DC/BC two-defect synchronizers and a sharper width-6 transfer

## 1. Scope, exact model, continuity, and handoff

This run follows `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`, and its LIVE20 assignment of P13 to T02: determine

\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]

for two independent iid uniform binary strings.

The model here is the actual dependent LCS grid. In one strip column the same fresh `Y` bit is compared with every active `X` bit. No independent Bernoulli matching array is substituted.

Necessary dependencies only were recovered:

- preceding P13 report `proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T06-18-02Z__two-defect-synchronizers-width6-transfer.md`;
- newest available P02 companion report `proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T06-05-32Z__label-support-two-step-report.md`, blob `9deebe890c88ce94bde9a0a754dc2ee97a02ba1e`;
- the inherited dependence-preserving boundary recursion, one-defect theorem, first-`C` / second-`D` two-defect theorem, and synchronizing-language transfer proved in the preceding P13 lineage.

Fresh source navigation on 2026-09-20 retained Alexander Tiskin, `arXiv:2212.01582v2`, revised 2024-08-13. The arXiv record still calls the coefficient unresolved and explicitly states that claims in the original preprint about the stochastic process and `gamma` were incorrect and removed in v2, while retaining a supported estimate. The rigorous public lower endpoint retained here is

\[
L=0.792665992=\frac{99083249}{125000000}
\]

from Heineman--Miller--Reichman--Salls--Sarkozy--Soiffer, `arXiv:2407.10925`.

Short pre-LIVE20 handoff only: P0342 had already been terminally handed off at frozen `2/2`; the later P0205 screen admitted no successor because its source notation could not be frozen source-faithfully. The retired I0051/clade work remains retired and was not reopened.

## 2. Source-level movement is P02's; mechanism movement is P13's

The preceding P13 report had source interval

\[
L\le\gamma_2\le U_W.
\]

Since then P02 proved its label-support two-step Collatz defect and exact strict endpoint

\[
\boxed{U_S<U_W},
\qquad
\boxed{L\le\gamma_2\le U_S},
\]

with the certified separator

\[
U_S<0.826275942762282625015106581537296632823461996193190023880806183312562944430299551<U_W.
\]

That is the source-level strict interval shrink in this invocation. It is companion-derived and is not attributed to the boundary recursion below. P02 remains on the complementary covering/cone variational route; P13 does not duplicate it.

The P13 quantity improved below is the rigorous finite-to-infinite transfer at the first currently useful strip width `w=6`. The preceding bound was

\[
C_{\rm prev}=\frac{2036624461477}{5000000}=407324.8922954.
\]

This run proves

\[
\boxed{C_{\rm new}=\frac{820311293209}{2500000}=328124.5172836<328125.}
\]

Thus for every exact finite horizon expectation at width 6, the certified transfer radius shrinks from `C_prev/N` to `C_new/N`; this is a demonstrated asymptotic-transfer gain, but by itself it does not raise the retained source lower endpoint `L`.

## 3. The true-source boundary recursion

Fix strip half-width `w`, put `m=2w`, and write a formal boundary state as

\[
S=(x_1,\ldots,x_m;g_1,\ldots,g_m)\in\{0,1\}^{2m}.
\]

For a fresh actual source pair `(u,v)`, define

\[
d_0=0,
\qquad
d_i=(1-g_i)\bigl(d_{i-1}\vee\mathbf1_{\{x_i=v\}}\bigr),
\quad1\le i\le m,
\tag{3.1}
\]

then

\[
x'=(x_2,\ldots,x_m,u),
\tag{3.2}
\]

\[
g'_i=g_{i+1}+d_{i+1}-d_i,\quad1\le i<m,
\tag{3.3}
\]

\[
g'_m=(1-d_m)\mathbf1_{\{u=v\}}.
\tag{3.4}
\]

Use the four equiprobable source-pair letters

\[
A=(0,1),\quad B=(1,0),\quad C=(0,0),\quad D=(1,1).
\]

The shared `v` in (3.1) is precisely the dependence absent from independent Bernoulli matching.

Call a state `k-zero-tailed` when its last `k` pairs `(x_i,g_i)` equal `(0,0)`.

Two inherited elementary facts are used repeatedly and are reproved in the precise form needed here.

### Lemma 3.1 — tail evolution

If a state is `k-zero-tailed`, then an `A` step makes it `min(k+1,m)`-zero-tailed. If `k>=1`, a `C` step leaves it at least `k-zero-tailed`.

**Proof.** For `A`, throughout the old zero tail one has `x_i=0 != v=1` and `g_i=0`, so the carry is constant there. Therefore every difference `d_{i+1}-d_i` inside the shifted tail is zero, while the appended terminal pair is `(0,0)`. The first shifted tail cell also has zero gradient because its old `g` is zero and its carry equals the carry immediately to its left. Thus the zero tail grows by one.

For `C`, on the first old zero-tail cell `x_i=v=0` and `g_i=0`, so the carry becomes one and remains one through the rest of that tail. All internal carry differences there vanish and the terminal `C` pair has gradient `1-d_m=0`; hence the old zero-tail length is preserved. QED.

### Lemma 3.2 — one localized marker under `A`

Suppose states `R,M` agree except at position `j`, where

\[
R_j=(0,0),\qquad M_j=(1,b),\quad b\in\{0,1\},
\]

and every position to the right is `(0,0)` in both. Under one common `A` step, if `j>1` the outputs again agree except at `j-1`, where the reference pair is `(0,0)` and the marked pair is

\[
(1,1-c),
\]

with `c` the common carry entering position `j`. If `j=1`, the marker exits and the outputs agree.

**Proof.** Up to `j-1` the carries agree; call the common incoming carry `c`. At the reference marker, `x_j=0!=1` and `g_j=0`, hence `d_j^R=c`. At the marked position, `x_j=1=v`, so

\[
d_j^M=(1-b)(c\vee1)=1-b.
\]

Equation (3.3) gives reference outgoing gradient `0` and marked outgoing gradient

\[
b+(1-b)-c=1-c.
\]

To the right all raw bits and gradients are zero; each carry is constant along that zero region, so all further carry differences telescope to zero. The raw marker shifts left one site. For `j=1` it shifts out of the window and the same cancellation leaves no discrepancy. QED.

## 4. New collision-normalization lemma

The missing two-defect cases are controlled by what a `C` column does to a marker already sitting inside a sufficiently long zero tail.

### Lemma 4.1 — `C` followed by `A` erases marker-gradient memory

Let `R,M` satisfy the hypotheses of Lemma 3.2 at a position `j>=2`. Assume moreover that, during a common `C` step, the common carry entering position `j` equals one. Then after that `C` step and one subsequent common `A` step, the two outputs agree except possibly at position `j-2` (or agree completely if that position has left the window). At the surviving position the reference pair is `(0,0)` and the marked pair is

\[
(1,1-q),
\]

where `q` is the common `A`-carry entering position `j-1`. In particular the result is independent of the old marker gradient `b`.

**Proof.** Let the common `C`-carry entering the marker be one. At position `j`, the reference has `(0,0)`, so its outgoing `C`-carry is one. The marked chain has `(1,b)`, hence its outgoing carry is `1-b`. At the next zero cell to the right (if present), `v=0` matches the raw zero and restores the marked carry to one.

Using (3.3), after the `C` step the reference is zero at `j-1,j` while the marked chain has a raw marker `(1,0)` at `j-1` and, possibly, a pure gradient `b` at `j`; all positions farther right agree and are zero.

Now apply `A`. Let `q` be the common carry entering `j-1`. The reference zero at `j-1` propagates carry `q`; the marked raw `1` forces carry one. At `j`, the marked gradient `b` changes that carry to `1-b`, and thereafter the carries remain constant on the zero region. Equation (3.3) therefore gives marked gradient

\[
1-q
\]

at the shifted raw marker `j-2`, while at `j-1` the two marked contributions cancel exactly:

\[
b+(1-b)-1=0.
\]

Every position to the right has zero gradient difference. Thus the old `b` has disappeared and only the standard localized marker of Lemma 3.2 remains. QED.

This is the new dependence-preserving mechanism: a common `C` column uses the *same* incoming bit across the whole tail to force the carry to one before the marker, and the next `A` column converts the resulting two-site disturbance back to one marker.

## 5. New synchronizer family I: `D ... C`

### Theorem 5.1

For every `r,t>=1`, `s>=0` with

\[
r+s+t=m,
\]

the word

\[
\boxed{A^r D A^s C A^t}
\tag{5.1}
\]

is a constant boundary map on all formal states. By bit-complement symmetry, so is its `B`-family complement.

**Proof.** Compare the actual word with the reference word obtained by replacing `D` by `A`:

\[
W_0=A^{r+1+s}CA^t.
\]

After the common prefix `A^r`, Lemma 3.1 gives an `r`-zero tail. `D` and `A` share `v=1`, hence have the same carry vector; their outputs differ only at the new terminal site, where `A` appends `(0,0)` and `D` appends `(1,b)` for `b=1-d_m`. Thus the two chains differ by one localized terminal marker, while the reference has an `(r+1)`-zero tail.

After the next `s` common `A` steps, Lemma 3.2 moves that marker to position `j=m-s`, and the reference has a zero tail of length `r+s+1`. There are exactly `r>=1` reference zero cells in that tail before the marker. Therefore, on the following `C` step, the first such zero cell matches `v=0` and forces the common carry to one before it reaches the marker. Lemma 4.1 applies. Since `t>=1`, the first trailing `A` converts the disturbance to one standard marker independent of the previous marker gradient.

The remaining `A` steps transport that marker left by Lemma 3.2. The reference `W_0` is already independent of the initial state before its final `A`: its first `m+1` letters are

\[
A^{r+1+s}CA^{t-1},
\]

which contain exactly `m` copies of `A` and one defect `C`, so the inherited one-defect theorem applies. Moreover every source letter of `W_0` has appended raw bit `u=0`; by the time the final `A` is read, its entire raw window is `0^m`. Hence the `A` carry vector on that last step starts at zero and stays zero. The final surviving marker, if any, therefore has fixed gradient one. The actual final state is independent of the initial state. QED.

## 6. New synchronizer family II: `B ... C` after two leading `A`s

### Theorem 6.1

For every `r>=2`, `t>=1`, `s>=0` with `r+s+t=m`, the word

\[
\boxed{A^r B A^s C A^t}
\tag{6.1}
\]

is a constant boundary map on all formal states. Its bit-complement family is also synchronizing.

**Proof.** Compare with

\[
W_0=A^r C A^s C A^t.
\]

After `A^r`, both chains have an `r`-zero tail. `B` and `C` share `v=0`, so they have the same carry vector. Since the zero tail is nonempty, the common `C/B` carry has reached one by the terminal site. Consequently `C` appends `(0,0)`, while `B` appends `(1,0)`; the two states differ by a localized terminal marker with gradient zero. The reference still has an `r`-zero tail.

After `A^s`, Lemma 3.2 moves the marker to `j=m-s` and the reference has an `(r+s)`-zero tail. Because `r>=2`, there is at least one zero-tail cell strictly before the marker. Thus the following common `C` step has carry one on entry to the marker. Lemma 4.1 and the first trailing `A` reduce the disturbance to a standard localized marker with no memory of its earlier gradient.

The reference word `W_0` is synchronizing by the previously proved first-`C` two-defect theorem (`first defect C`). It remains only to rule out hidden dependence in the marker's final gradient. Before the final `A`, at least `m` source letters of `W_0` have already been read, and every one has `u=0`; hence the reference raw window is exactly `0^m`. Under `A=(0,1)`, starting from `d_0=0`, no raw bit matches `v=1`, so every carry is zero regardless of the reference gradients. Lemma 3.2 therefore gives the final marker a fixed gradient one. The actual final state is fixed. QED.

### The `r>=2` hypothesis is real

The tempting extension to `r=1` is false. At `m=3`,

\[
W=ABACA
\]

has `r=s=t=1`, but exact recursion gives

\[
(000;000)\xrightarrow{W}(000;000),
\]

while

\[
(000;001)\xrightarrow{W}(000;100).
\]

Thus the extra leading zero-tail cell in Theorem 6.1 is mathematically necessary for this proof family, not a bookkeeping artifact.

## 7. Width-6 reset language and exact hitting-time certificate

Now take `w=6`, `m=12`. Start from the preceding 728-word minimal reset language:

1. `A^12`, `B^12`;
2. all inherited one-defect words;
3. all inherited two-defect words whose first defect is `C` or second defect is `D`, together with complements.

Theorem 5.1 contributes every internal `D ... C` placement. There are

\[
2\binom{12}{2}=132
\]

new words including complements.

Theorem 6.1 contributes the `B ... C` placements with `r>=2`. For the `A` family there are

\[
\sum_{r=2}^{11}(12-r)=55
\]

such internal placements, hence 110 including complements.

After removing any word containing an earlier reset word, the exact checker obtains

\[
\boxed{970}
\]

minimal reset patterns. Their prefix automaton has

\[
\boxed{4291}
\]

nonabsorbing states.

Let `tau` be the first end time of one of these reset patterns in the iid source-pair stream. A sparse floating solve was used only to propose an integer Bellman supersolution. With denominator

\[
Q=10^7,
\]

the checker verifies over integers, for every nonabsorbing prefix state `s`,

\[
4H(s)-4Q-\sum_{a:\,sa\text{ nonabsorbing}}H(sa)\ge0.
\tag{7.1}
\]

The minimum exact residual numerator is `9>0`. Therefore `h=H/Q` is a rigorous supersolution of the hitting-time equations, and first-step comparison gives

\[
\mathbf E\tau\le h(\varnothing)
=\frac{3281245172836}{10^7}
=\boxed{\frac{820311293209}{2500000}}
=328124.5172836<328125.
\tag{7.2}
\]

No floating output is used as a certificate; only the exact integer inequalities (7.1) are claimed.

Relative to the preceding P13 value,

\[
C_{\rm prev}-C_{\rm new}
=\frac{396001875059}{5000000}
=79200.3750118,
\]

and

\[
\frac{C_{\rm prev}}{C_{\rm new}}
=1.2413729265\ldots.
\]

Thus the additive transfer penalty falls by `19.444030...%` in this run.

## 8. Finite-to-infinite theorem

Let `R_N` be the cumulative width-6 strip reward for the true correlated chain, and let `gamma_6` be its stationary reward rate.

### Theorem 8.1

For every formal starting boundary state `s` and every `N>=1`,

\[
\boxed{
\left|\mathbf E_sR_N-N\gamma_6\right|
\le\frac{820311293209}{2500000}<328125.
}
\tag{8.1}
\]

Consequently

\[
\boxed{
\gamma_2\ge\gamma_6\ge
\frac{\mathbf E_sR_N}{N}
-
\frac{820311293209}{2500000N}.
}
\tag{8.2}
\]

**Proof.** Couple two strip chains from arbitrary initial states using the same actual iid source-pair stream. Every reset pattern above is a constant boundary map, so the two chains coincide at the first reset time `tau` and remain identical thereafter. Their one-step rewards lie in `{0,1}`, so before coalescence their cumulative reward discrepancy is at most one per step. Hence

\[
|\mathbf E_sR_N-\mathbf E_tR_N|
\le \mathbf E(\tau\wedge N)
\le \mathbf E\tau
\le C_{\rm new}.
\]

The presence of `A^12` among the reset words also makes `tau` almost surely finite with finite mean, so the common-noise coupling gives uniqueness of the stationary law. Taking `t` distributed according to that stationary law gives `\mathbf E_tR_N=N\gamma_6`, proving (8.1). The inherited strip restriction embeds every width-6 path as an admissible LCS path in the full problem, hence `gamma_2>=gamma_6`; dividing (8.1) by `N` gives (8.2). QED.

This is the required proved finite-to-infinite transfer. A finite computation of `E_sR_N` becomes a source-valid lower bound only after subtracting the explicit `C_new/N`; no finite value is promoted directly to `gamma_2`.

## 9. Exact checks, failures, and what did not move

Executed checker:

`proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T07-13-05Z__dc_bc_sync_certificate.py`

Executed output:

`proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T07-13-05Z__dc_bc_sync_certificate.out`

The checker:

- rebuilds the exact true-source recursion;
- exhaustively verifies Theorem 5.1 and complements on every formal state through `m=6`;
- exhaustively verifies Theorem 6.1 and complements on every formal state through `m=6`;
- checks the sharpness counterexample `ABACA` exactly;
- builds the 970-word prefix automaton and all 4291 nonabsorbing states;
- verifies every Bellman supersolution inequality over integers with minimum residual numerator `9`;
- verifies the exact old/new constants and strict decrease;
- ends `ALL_EXACT_CHECKS_PASS`.

These finite checks are self-checks supporting the on-page all-`m` proofs; they are not substitutes for those proofs and are not independent review.

Failure/obstruction retained honestly: not every two-defect word with `m` copies of `A` synchronizes. The preceding run already exhibited `ABABA`; this run adds the source-valid failure `ABACA` for the naive `BC` extension at `r=1`. Therefore the reset language cannot be enlarged merely by counting defects. The remaining generic width-6 constant is still large (`~3.28e5`), so this mechanism alone does not yet beat the public lower endpoint.

## 10. Next attack

The most promising immediate continuation is to classify the two remaining partially synchronizing defect orders rather than enumerate arbitrary words blindly:

- `A^r D A^s B A^t` empirically has a trailing-tail threshold;
- `A^r B A^s B A^t` has both leading- and trailing-tail obstructions.

The proof target is a two-sided marker-collision lemma identifying exactly when the second defect sees a forced carry. If proved, those families can be inserted into the same prefix automaton and the Bellman certificate rerun. If that only gives a small constant-factor gain, the next materially different route is event-specific coupling for the mixed terminal suffix in the inherited identity `gamma_w = 2/3 + pi_w(B_w)/3`, avoiding full-state synchronization.

No source lower endpoint movement is claimed from the new P13 theorem until an exact finite expectation plus (8.2) actually exceeds `L`.

## 11. ledger_delta

```yaml
ledger_delta:
  slot: P13
  assignment: T02_binary_LCS_dependence_preserving_boundary_recursion
  status: PARTIAL
  model: two_independent_iid_uniform_binary_strings
  independent_Bernoulli_matching_used: false
  source_metric_before:
    interval: "L <= gamma_2 <= U_W"
    L: "0.792665992"
  source_metric_after:
    interval: "L <= gamma_2 <= U_S < U_W"
    movement_origin: "P02 companion label-support two-step certificate"
  p13_mechanism_before:
    width: 6
    additive_constant: "2036624461477/5000000"
    decimal: "407324.8922954"
  p13_mechanism_after:
    width: 6
    additive_constant: "820311293209/2500000"
    decimal: "328124.5172836"
    strict_simple_bound: "<328125"
    reduction_decimal: "79200.3750118"
    reduction_fraction: "0.19444030185703046"
  new_theorem_scope:
    - "A^r D A^s C A^t synchronizes for r,t>=1, r+s+t=m, plus complement"
    - "A^r B A^s C A^t synchronizes for r>=2,t>=1, r+s+t=m, plus complement"
    - "finite-to-infinite width-6 error <= 820311293209/2500000"
  decisive_counterexample:
    word: ABACA
    m: 3
    outputs_differ: true
  exact_checker:
    patterns: 970
    automaton_nonabsorbing_states: 4291
    bellman_denominator: 10000000
    minimum_exact_residual_numerator: 9
    output: ALL_EXACT_CHECKS_PASS
  previous_P13_successor_handoff:
    P0342: "terminally handed off at frozen 2/2"
    P0205: "screened but not admitted"
    I0051_clade: RETIRED_NOT_REOPENED
  shared_root_ledgers_modified: false
  peer_files_modified: false
  next_attack: "derive exact forced-carry thresholds for DB/BB two-defect families; otherwise switch to event-specific suffix coupling"
```

No peer file, historical report, shared root ledger, canonical claim, schedule, workflow, permission, email/Drive resource, public post, paid compute, or external contact was modified.
