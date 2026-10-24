Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. NO SOURCE-METRIC MOVEMENT: `M_P0342 = 2/2 -> 2/2`. NEW MATHEMATICAL MOVEMENT: for every increasing concave modulus `omega`, the worst possible `sqrt(n)`-scale effect of an `omega`-continuous perturbation that vanishes on every infinite fringe tree is bounded by `sqrt(n) omega(1/n)`, and this bound is attained exactly on perfect balanced trees for every power-of-two leaf count. Consequently uniform boundary stability holds iff `sqrt(n) omega(1/n) -> 0`. Methods actually tried: B8, B21, B24.**

# P13 / P0342 — exact modulus-of-continuity criterion via Kraft geometry

Date: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Native slot: `6aa7b253b37c8191b693d8dc79298d37`.  
Own root: `proofnet24/P13-outside-successor/`.

## 1. Continuity, ownership, exclusions, and frozen metric

This invocation continues the current exclusive P13 successor `P0342`, governed by `operations/claims/P0342.md`. It does **not** reopen the retired I0051 clade-covariance target, the completed six-unchanged-run C0021 handoff, any POSTED/INDEX exclusion, or any peer-owned claim.

I reread/recovered the controlling owner directive at anchor `749da260517828ed311f6f1b1af74915c054bdf3`, `operations/NEW_METHODS_2026-09-16.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`, the P0342 claim and historical campaign packet, the newest complete P13 report, source-specific intake/attempt-history hits, current P0342 audit searches, and the newest neighboring I0054 report. The large append-only intake corpora are not credibly byte-for-byte renderable through the connector in one invocation; I used the retained inventory plus current target-specific searches and do not claim a literal visual reread of every unrelated JSONL byte.

The mandatory I0054 screen was checked first. The newest recovered R11 report is

`runs/R11/2026-09-19T14-42-25Z_i0054-inversive-u049-c070-d4f7.md`

at commit `3bb6f97ff721843f14196b0f378b1d3d155e7216`. It moves R11's own author-side model-class metric `69 -> 70`, remains **PARTIAL** at source/campaign level, and continues exclusive I0054 work. P13 therefore did not touch I0054.

The immediately preceding P13 report is

`proofnet24/P13-outside-successor/runs/2026-09-19/2026-09-19T14-12-00Z__p0342-holder-boundary-stability-sharp-half.md`.

It keeps the frozen source metric at `2/2`, proves a deterministic Holder boundary-stability theorem with sharp exponent `1/2`, and proves that the historical root-split perturbation lies outside every positive Holder class.

The frozen source metric remains exactly

`M_P0342 in {0,1,2}` = number of the `FRINGE` and `FINITE-FAILURE` obligations established simultaneously for the one fixed historical witness `Theta=Psi+Phi`.

Both obligations are already established. The denominator stays `2`; the theorem below is scope strengthening, not a third obligation and not renewed source-metric movement.

Fresh repository searches still recover no end-to-end P0342 PASS from P26 and no end-to-end P0342 PASS from a distinct OTHER research track. Historical audits of retired I0051 do not transfer. Campaign status therefore remains

`CLAIMED / METRIC-COMPLETE / SOURCE-REFUTATION-CANDIDATE / AUDITS-PENDING`.

No claim file or shared root ledger is modified in this invocation.

## 2. Source scope and fresh current-literature check

The exact source remains David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3 (18 April 2025), Open Problem 12, Section 4.10. The source asks whether, for a **given functional** whose stationary fringe-process sums satisfy a CLT, the same CLT necessarily holds for the corresponding sums over all leaf rerootings of `DTCS(n)`.

Primary source checked on 2026-09-19:

- https://arxiv.org/abs/2303.02529
- https://arxiv.org/pdf/2303.02529

The actual PDF page containing Open Problem 12 was successfully inspected this run; there is no source-page-image access gap here.

Fresh dated searches used combinations of

- `"Aldous Janson" "Open Problem 12" fringe process CLT`,
- `"critical beta-splitting" "Open Problem 12"`,
- `"almost local additive tree functionals" modulus continuity tree CLT`, and
- `"Phase Change of Limit Laws" Quicksort toll functions Hwang Neininger`.

They recovered Aldous--Janson Part III, arXiv:2412.09655, and later critical-beta work, but no checked primary source explicitly resolving exact Open Problem 12. This remains bounded negative evidence only, not a worldwide openness or priority certificate.

For the new regularity theorem below, relevant neighboring literature includes Ralaivaosaona--Sileikis--Wagner, *A central limit theorem for almost local additive tree functionals*, arXiv:1810.00467, which extends conditioned-Galton--Watson additive-functional CLTs beyond strictly local tolls, and Hwang--Neininger, *Phase Change of Limit Laws in the Quicksort Recurrence under Varying Toll Functions*, SIAM J. Comput. 31 (2002), which has a different recursive-toll phase transition around exponent `1/2`. Those papers concern different random-tree/recurrence structures and do not supply the deterministic Kraft-modulus statement proved here. I make no novelty claim from this bounded search.

## 3. Idea-before-proof receipt and the three methods

Before writing this proof I committed

`proofnet24/P13-outside-successor/artifacts/2026-09-19/2026-09-19T15-07-00Z__p0342_b8_b21_b24_modulus-kraft-idea.md`

at commit `f387f9532fcae49d1a43a38876a56f181cbdce05` and read it back from that exact commit; verified blob `5f4b5b44c9c774e8a8fda1e4e9428e7f452763f3`.

The methods are genuinely different from the preceding B4/B20/B29 triple.

**B8 — GO THE OTHER WAY AND DISCRETIZE.** Replace the topological boundary problem by the finite Kraft simplex `a_i=2^{-d_i}`, `sum_i a_i=1`. A modulus of continuity becomes a separable cost `sum_i omega(a_i)`.

**B24 — FIND THE EXTREMAL OBJECT.** Optimize that finite cost. Concavity forces the equal-weight vector; a perfect balanced binary tree realizes it whenever `n` is a power of two. A canonical distance-to-boundary functional simultaneously saturates the continuity inequality.

**B21 — ASK WHO ELSE HAS THIS SHAPE.** Compare the resulting threshold with prefix-code/Kraft optimization, almost-local additive-functional CLTs, and recursive toll-function phase transitions. The comparison is useful for scope and prior-art restraint, but the proof below is self-contained and deterministic.

No new checker is warranted: every new assertion is analytic and proved on the page; no new finite enumeration is used.

## 4. Setup: the boundary modulus class

Use the standard induced-ball local metric on leaf-rooted ordered binary trees,

\[
d_{\rm loc}(S,T)=2^{-R(S,T)},
\tag{4.1}
\]

where `R(S,T)` is the largest integer radius for which the rooted ordered induced balls agree. The preceding run kept an extra factor two to remain convention-robust when boundary degrees are encoded. Here I fix (4.1), so the exact Kraft constant is visible. Any equivalent one-radius convention changes only absolute constants and leaves the criterion unchanged.

Let

\[
\omega:[0,1]\to[0,\infty)
\]

be increasing and concave with `omega(0)=0`. Let `G_omega` be the class of all functionals `g` on finite and infinite leaf-rooted binary trees satisfying

1. `g(T)=0` for every infinite one-ended fringe tree; and
2. for all `S,T`,

\[
|g(S)-g(T)|\le \omega(d_{\rm loc}(S,T)).
\tag{4.2}
\]

For a finite full binary tree `T` with leaves `1,...,n`, let `T_i` be the tree rerooted at leaf `i`, let `o` be the original phylogenetic root, and define

\[
d_i=d_T(i,o),\qquad a_i=2^{-d_i}.
\tag{4.3}
\]

The exact Kraft identity gives

\[
\sum_{i=1}^n a_i=1.
\tag{4.4}
\]

Define the worst normalized boundary perturbation

\[
A_n(\omega):=
\sup_{T:\,|L(T)|=n}\ \sup_{g\in G_\omega}
\frac1{\sqrt n}\left|\sum_{i=1}^n g(T_i)\right|.
\tag{4.5}
\]

## 5. B8 theorem — exact universal upper bound

### Theorem 1

For every `n>=2`,

\[
\boxed{A_n(\omega)\le \sqrt n\,\omega(1/n).}
\tag{5.1}
\]

#### Proof

Fix `T`, a leaf `i`, and `g in G_omega`. Extend the finite tree past its original root `o` by an infinite binary spine, attaching one finite side leaf at every new spine vertex. Denote the resulting infinite one-ended leaf-rooted tree by `\widehat T_i`.

The rooted induced balls of `T_i` and `\widehat T_i` agree through radius `d_i`: the first extra vertex beyond the old root occurs at distance `d_i+1`. Hence

\[
d_{\rm loc}(T_i,\widehat T_i)\le2^{-d_i}=a_i.
\tag{5.2}
\]

Because `g` vanishes on every infinite one-ended tree,

\[
|g(T_i)|
=|g(T_i)-g(\widehat T_i)|
\le \omega(a_i).
\tag{5.3}
\]

Therefore

\[
\frac1{\sqrt n}\left|\sum_i g(T_i)\right|
\le
\frac1{\sqrt n}\sum_i\omega(a_i).
\tag{5.4}
\]

Concavity of `omega`, Jensen's inequality, and the Kraft identity (4.4) give

\[
\frac1n\sum_i\omega(a_i)
\le
\omega\!\left(\frac1n\sum_i a_i\right)
=\omega(1/n).
\tag{5.5}
\]

Combining (5.4)--(5.5) yields

\[
\frac1{\sqrt n}\left|\sum_i g(T_i)\right|
\le \sqrt n\,\omega(1/n).
\]

Taking both suprema proves (5.1). `square`

This contains the previous Holder theorem as the special case `omega(t)=C t^beta`; it removes the artificial restriction to pure power laws.

## 6. B24 theorem — the balanced tree attains the bound exactly

The upper bound is not merely correct in order. For every power-of-two leaf count it is the exact extremal value.

For a finite leaf-rooted tree `T`, let

\[
h(T)=\text{distance from the distinguished leaf to the original degree-two root},
\]

and set `h(T)=infinity` on an infinite one-ended tree. Define

\[
\rho(T)=2^{-h(T)},
\tag{6.1}
\]

with `2^{-infinity}=0`.

### Lemma 2 — `rho` is 1-Lipschitz

For all finite or infinite leaf-rooted trees,

\[
|\rho(S)-\rho(T)|\le d_{\rm loc}(S,T).
\tag{6.2}
\]

#### Proof

If `h(S)=h(T)`, the left side is zero. Otherwise suppose `h(S)<h(T)`, allowing `h(T)=infinity`. At distance `h(S)` from the distinguished leaf, `S` has reached its original degree-two root. In `T`, the corresponding vertex is still an interior degree-three vertex. The induced rooted balls therefore differ by radius `h(S)+1`, so their largest common radius satisfies `R(S,T)<=h(S)`. Thus

\[
d_{\rm loc}(S,T)=2^{-R(S,T)}\ge2^{-h(S)}.
\]

Meanwhile

\[
|\rho(S)-\rho(T)|
\le \rho(S)=2^{-h(S)}.
\]

This proves (6.2); the opposite ordering is symmetric. `square`

### Lemma 3 — a concave modulus is subadditive

If `omega` is increasing, concave and `omega(0)=0`, then whenever `x,y,x+y in [0,1]`,

\[
\omega(x+y)\le\omega(x)+\omega(y).
\tag{6.3}
\]

Consequently

\[
|\omega(x)-\omega(y)|\le\omega(|x-y|).
\tag{6.4}
\]

#### Proof

For `x+y>0`, concavity between `0` and `x+y` gives

\[
\omega(x)\ge\frac{x}{x+y}\omega(x+y),\qquad
\omega(y)\ge\frac{y}{x+y}\omega(x+y).
\]

Adding proves (6.3). If `x>=y`, then `omega(x)<=omega(x-y)+omega(y)` by (6.3), hence `omega(x)-omega(y)<=omega(x-y)`; symmetry gives (6.4). `square`

Define

\[
g_\omega(T)=\omega(\rho(T)).
\tag{6.5}
\]

By Lemmas 2--3 and monotonicity,

\[
|g_\omega(S)-g_\omega(T)|
\le\omega(|\rho(S)-\rho(T)|)
\le\omega(d_{\rm loc}(S,T)),
\]

and `g_omega=0` on every infinite one-ended tree. Thus `g_omega in G_omega`.

### Theorem 4 — exact extremality on powers of two

For every `h>=1`, with `n=2^h`,

\[
\boxed{A_{2^h}(\omega)=\sqrt{2^h}\,\omega(2^{-h}).}
\tag{6.6}
\]

#### Proof

Theorem 1 gives the upper bound. For the lower bound take the perfect balanced full binary tree with `n=2^h` leaves. Every leaf has depth `h`, so every rerooting satisfies `rho(T_i)=2^{-h}=1/n`. For the single functional `g_omega`,

\[
\frac1{\sqrt n}\sum_{i=1}^n g_\omega(T_i)
=
\frac n{\sqrt n}\omega(1/n)
=\sqrt n\,\omega(1/n).
\]

This matches the upper bound exactly. `square`

If `omega` is strictly concave, equality in the Jensen step forces all Kraft weights `a_i` to equal `1/n`. For `n=2^h` this forces every leaf depth to equal `h`, hence the perfect balanced shape (up to ordering/label symmetries) is the unique geometric extremizer at the Kraft-weight level.

## 7. Exact if-and-only-if stability criterion

### Corollary 5

The following are equivalent:

1. every boundary-vanishing `omega`-continuous perturbation is uniformly negligible at square-root leaf-sum scale, i.e.

\[
A_n(\omega)\longrightarrow0;
\tag{7.1}
\]

2.

\[
\boxed{\sqrt n\,\omega(1/n)\longrightarrow0.}
\tag{7.2}
\]

#### Proof

If (7.2) holds, Theorem 1 implies (7.1).

Conversely suppose `A_n(omega)->0`. By Theorem 4,

\[
f(2^h):=\sqrt{2^h}\,\omega(2^{-h})=A_{2^h}(\omega)\to0.
\]

For arbitrary `n`, choose `h` with `2^h<=n<2^{h+1}`. Monotonicity of `omega` gives

\[
\sqrt n\,\omega(1/n)
\le
\sqrt{2^{h+1}}\,\omega(2^{-h})
=\sqrt2\,f(2^h)\to0.
\]

Thus (7.2) follows. `square`

So the regularity threshold for the P0342 boundary-invisible perturbation architecture is not fundamentally “Holder exponent greater than one-half.” The exact deterministic criterion is the modulus condition (7.2).

### Critical logarithmic refinement

For any concave modulus with small-`t` asymptotics

\[
\omega(t)\asymp \sqrt t\,[\log(e/t)]^{-\gamma},
\tag{7.3}
\]

one has

\[
\sqrt n\,\omega(1/n)
\asymp [\log(en)]^{-\gamma}.
\]

Hence this mechanism is uniformly stable for `gamma>0`, critical/non-negligible for `gamma=0`, and unstable for `gamma<0`. This resolves the slowly-varying ambiguity left by the preceding pure-Holder theorem.

## 8. The historical P0342 perturbation is far outside the stable modulus class

The previous report proved only that the historical global perturbation is not Holder of any positive order. The modulus theorem gives a stronger quantitative diagnosis.

For the family

\[
\Phi_\alpha(T)=m^{-\alpha}(B_m(T)-p_m)
\]

on a finite `m`-leaf tree, and zero on infinite trees, choose the `m`-leaf comb rerooted at its deepest leaf. Its distance from that leaf to the original root is `m-1`, while its smaller root clade has size `1`; hence `B_m=1`. Since `p_m->1/2`, for all sufficiently large `m`,

\[
|\Phi_\alpha(C_m)|\ge\frac13m^{-\alpha}.
\tag{8.1}
\]

Extend the comb beyond its old root to an infinite comb. The two rooted trees agree through radius `m-1`, so

\[
d_{\rm loc}(C_m,C_\infty)\le2^{1-m}.
\tag{8.2}
\]

Therefore **any** increasing modulus `omega` satisfying a bound of the form (4.2) for `Phi_alpha` must obey

\[
\omega(2^{1-m})\ge\frac13m^{-\alpha}.
\tag{8.3}
\]

Put `N=2^{m-1}`. Then

\[
\sqrt N\,\omega(1/N)
\ge
\frac13\,2^{(m-1)/2}m^{-\alpha}
\longrightarrow\infty.
\tag{8.4}
\]

Thus the historical `alpha=1/4` witness, and indeed every fixed positive `alpha` in this family, lies not merely outside every positive Holder class but far outside **every** boundary modulus for which the universal stability criterion (7.2) could hold. Its local decay is only polynomial in root distance while the local metric approaches the boundary exponentially.

## 9. What this does and does not repair in Open Problem 12

The source-negative P0342 candidate remains about the literal universal implication for a “given functional.” The theorem above identifies an exact quantitative repair for one specific failure architecture:

> if two candidate functionals differ by a perturbation that vanishes on every infinite fringe tree and has a concave modulus `omega` with `sqrt(n) omega(1/n)->0`, then their finite `sqrt(n)`-normalized leaf sums differ by `o(1)` **uniformly over every finite full binary tree**.

This is stronger than a probabilistic `o_p(1)` statement and needs no DTCS distributional input.

It is **not** a proof that every arbitrary `omega`-continuous functional satisfying (7.2) enjoys the full fringe-to-finite CLT transfer. A general functional need not vanish on the infinite boundary, and comparing its finite values to independent or arbitrarily chosen infinite extensions does not identify the joint stationary fringe-process law. Locality/stabilization/mixing can still matter. The result is therefore a sharp stability theorem for the exact boundary-invisible perturbation mechanism used by P0342, not a replacement source theorem.

## 10. Closure gate and audit status

The frozen source metric remains

`M_P0342 = 2/2 -> 2/2`.

There is no source-level stagnation created by strengthening a metric-complete target, and I do not rename the metric to manufacture movement.

Campaign closure still requires:

1. the already-written source-matching full argument to survive a P26 end-to-end independent audit;
2. one additional end-to-end audit by a distinct OTHER research track; and
3. the final source-specific prior-art review with its limitations retained.

Fresh repository searches in this invocation recovered neither required P0342 PASS. The bounded literature search found conceptual relatives but no checked exact resolution; that is not a novelty certificate. Accordingly the status remains

`CLAIMED / METRIC-COMPLETE / SOURCE-REFUTATION-CANDIDATE / AUDITS-PENDING`.

No `paper_*` package is created prematurely.

## 11. Delivery and structured ledger delta

Idea-before-proof artifact:

`proofnet24/P13-outside-successor/artifacts/2026-09-19/2026-09-19T15-07-00Z__p0342_b8_b21_b24_modulus-kraft-idea.md`

creation commit `f387f9532fcae49d1a43a38876a56f181cbdce05`, verified read-back blob `5f4b5b44c9c774e8a8fda1e4e9428e7f452763f3`.

This report itself is immutable once created. No root ledger, peer file, canonical claim, schedule, email/Drive resource, public post, workflow, permission, or external contact is modified.

```yaml
ledger_delta:
  track: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  target: P0342
  source: Aldous-Janson arXiv:2303.02529v3 Open Problem 12
  status_before: CLAIMED / METRIC-COMPLETE / SOURCE-REFUTATION-CANDIDATE / AUDITS-PENDING
  status_after: CLAIMED / METRIC-COMPLETE / SOURCE-REFUTATION-CANDIDATE / AUDITS-PENDING
  metric_name: M_P0342
  metric_before: 2/2
  metric_after: 2/2
  source_metric_movement: false
  mathematical_movement: true
  new_result: exact concave-modulus Kraft stability criterion; A_n(omega)<=sqrt(n)omega(1/n), equality for n powers of two, and A_n->0 iff sqrt(n)omega(1/n)->0
  methods: [B8, B21, B24]
  source_scope: literal OP12 remains the source target; new theorem is only a sharp stability result for boundary-vanishing perturbations
  i0054_gate: occupied by R11; newest peer metric 69->70; untouched by P13
  retired_i0051_reopened: false
  c0021_reopened: false
  p26_end_to_end_audit: missing
  distinct_other_end_to_end_audit: missing
  independent_audit_claimed: false
  novelty_claimed: false
  paper_package_created: false
  shared_root_written: false
  peer_files_written: false
```
