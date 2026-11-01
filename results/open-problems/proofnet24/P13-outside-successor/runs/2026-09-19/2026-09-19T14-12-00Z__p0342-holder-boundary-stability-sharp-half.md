Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. NO SOURCE-METRIC MOVEMENT: `M_P0342 = 2/2 -> 2/2`. NEW MATHEMATICAL MOVEMENT: a deterministic Holder boundary-stability theorem shows that every boundary-vanishing perturbation of local exponent `beta>1/2` is uniformly negligible at the `sqrt(n)` leaf-sum scale on every finite full binary tree; the exponent `1/2` is sharp for this deterministic mechanism, and the historical P0342 root-split perturbation is outside every positive Holder class. Methods actually tried: B4, B20, B29.**

# P13 / P0342 — Holder boundary stability, a sharp one-half regularity barrier, and why the counterexample evades it

Date: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Native slot: `6aa7b253b37c8191b693d8dc79298d37`.  
Own root: `proofnet24/P13-outside-successor/`.

## 1. Continuity, ownership, exclusions, and frozen metric

This invocation continues the current exclusive P13 successor `P0342`, governed by `operations/claims/P0342.md`. It does **not** reopen the retired I0051 clade-covariance target, the completed six-unchanged-run C0021 handoff, any POSTED/INDEX exclusion, or any peer-owned claim.

I reread the controlling owner directive at anchor `749da260517828ed311f6f1b1af74915c054bdf3`, `operations/NEW_METHODS_2026-09-16.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`, the P0342 canonical claim, the newest complete P13 report, source-specific historical/intake hits, current P0342 audit searches, and the newest neighboring I0054 report.

The mandatory I0054 screen was checked first. The newest recovered R11 report is

`runs/R11/2026-09-19T13-40-00Z_i0054-cyclic-rank-u048-c069-5e2a.md`.

It moves R11's own author-side model-class metric `68 -> 69`, remains **PARTIAL** at source/campaign level, and continues exclusive I0054 work. P13 therefore did not touch I0054.

The immediately preceding P13 report is

`proofnet24/P13-outside-successor/runs/2026-09-19/2026-09-19T13-18-00Z__p0342-critical-mixture-stable-gaussianization.md`.

It keeps the frozen source metric at `2/2`, proves that the local size-three orientation statistic is scaffold-stably Gaussian, identifies the exact critical two-Gaussian mixture at perturbation exponent `alpha=1/2`, and gives the complete three-regime phase diagram for the explicit family `Phi_alpha`.

The frozen source metric remains exactly the claim-file metric:

`M_P0342 in {0,1,2}` = the number of FRINGE and FINITE-FAILURE obligations established simultaneously for the one fixed historical witness `Theta=Psi+Phi`.

Both obligations are already established. This run does not inflate the denominator, replace the witness, or count an auxiliary theorem as renewed source movement.

Repository-wide searches on 2026-09-19 still recover no P0342 end-to-end PASS from P26 and no P0342 end-to-end PASS from a distinct OTHER research track. Historical P12/P13 audits concern retired I0051 and do not transfer. Thus the campaign label remains

`CLAIMED / METRIC-COMPLETE / SOURCE-REFUTATION-CANDIDATE / AUDITS-PENDING`.

No claim file is created or modified in this invocation.

## 2. Exact source scope and current-status check

The exact source remains David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3 (18 April 2025), Section 4.10, Open Problem 12.

The current source says that its fringe distribution is the local weak limit of DTCS(n) relative to a uniform random leaf, formally a distribution on infinite binary trees with countably many leaves, one distinguished leaf-root, and a unique end. It then states first-order convergence for “suitable functionals” and asks, literally, whether for a **given functional** a CLT for the stationary fringe-process sum necessarily transfers to the corresponding sum over the `n` leaf rerootings of DTCS(n).

Source PDF: https://arxiv.org/pdf/2303.02529v3 . This run successfully inspected the actual page image containing Open Problem 12 (printed page 45 / PDF page index 44). There is therefore no source-page-image access gap in this invocation.

Fresh dated web searches on 2026-09-19 used combinations of

- `"critical beta-splitting" "Open Problem 12" fringe CLT`,
- `"critical beta-splitting" fringe functional CLT finite tree`,
- `"fringe tree" Holder local functional central limit theorem finite rooted trees`, and
- `"local convergence" additive functional tree CLT fringe Holder`.

The search recovered Aldous--Janson Part III (arXiv:2412.09655), later critical-beta work, and general additive/fringe-functional CLTs for other random-tree models, but no checked primary source explicitly resolving this exact Open Problem 12 implication or stating the Holder/Kraft barrier proved below. General fringe-tree and additive-functional CLT literature is therefore relevant prior art, not evidence of novelty. This is a bounded search, not a worldwide openness or priority certificate.

## 3. Why another theorem is useful after the source metric is complete

The completed P0342 counterexample has a very specific architecture.

1. `Psi` is a genuinely local mark with a positive-variance Gaussian fringe CLT.
2. `Phi` is a global perturbation which is **exactly zero on every infinite fringe tree**, so adding it does not alter the fringe process at all.
3. On a finite `n`-leaf tree, the same small value of `Phi` is seen by all `n` leaf rerootings because the original root and the total leaf count are globally recoverable.
4. Those `n` coherent copies accumulate at the `sqrt(n)` scale.

The previous run found the amplitude threshold `n^{-1/2}` inside one explicit family. The present question is more structural:

> How quantitatively local must a boundary-vanishing perturbation be before this coherent-accumulation mechanism becomes impossible on **every** finite full binary tree?

The answer below is: Holder exponent strictly greater than `1/2` in the local metric is enough, and `1/2` is the sharp deterministic threshold for this mechanism.

This does **not** prove a positive transfer theorem for arbitrary Holder functionals. It proves a complete stability theorem for the precise class of perturbations that are invisible on every infinite fringe tree, which is the mechanism used by P0342.

## 4. Idea-before-proof receipt and the three methods

Before writing the proof I committed

`proofnet24/P13-outside-successor/artifacts/2026-09-19/2026-09-19T14-04-30Z__p0342_b4_b20_b29_holder-boundary-idea.md`

at commit `3b3f196fbc109e0e4367350f5bed3c9d4a1102f9` and read it back from that exact commit; verified blob `03b8cb2d2988c86cf4bd5fa1277dc37c069d0bac`.

The methods are genuinely different from the preceding run's B2/B7/B12 triple.

**B29 — ADD THE POINTS AT INFINITY.** Treat the infinite one-ended fringe trees as the boundary of the finite leaf-rooted tree space. Compare each finite leaf rerooting with an explicit infinite one-ended extension beyond its original root. The distance to that boundary is exponentially small in the leaf-to-root depth.

**B20 — FIND WHY THE ALGORITHM FAILS.** The counterexample algorithm needs a boundary-invisible perturbation that decays too slowly to be summable over all leaf rerootings. Holder regularity turns the decay into `2^{-beta d_i}`; Kraft equality turns those terms into a deterministic global bound and kills the mechanism when `beta>1/2`.

**B4 — PROVE SOMETHING WEAKER, COMPLETELY.** Rather than claim a new universal transfer theorem, prove the exact perturbation-stability statement, prove its exponent sharp by an explicit balanced-tree family, and then verify that the actual historical perturbation evades the hypothesis on an explicit comb sequence.

No new code is needed because every new claim is analytic and proved below. No finite-enumeration claim is introduced.

## 5. Tree-space convention and the finite-to-infinite extension

Work with the source's leaf-rooted ordered full binary trees. A finite phylogenetic tree, viewed without its original rooting orientation but with one distinguished leaf as the local root, has one distinguished **original phylogenetic root**: it is the unique non-leaf vertex of graph degree two. All other non-leaf vertices have degree three. In the infinite fringe limit this degree-two boundary vertex has escaped to infinity; the source's limit trees have a unique end.

Let `d_loc` denote any standard exponential local metric inducing rooted local convergence. For definiteness one may take

\[
d_{\rm loc}(S,T)=2^{-R(S,T)},
\tag{5.1}
\]

where `R(S,T)` is the largest radius for which the rooted ordered radius-`R` balls agree. Whether the degree of the last boundary sphere is encoded changes the bounds below by at most one radius and hence only by a fixed multiplicative constant. I keep that convention-robust constant explicit.

For a finite full binary tree `T` and leaf `i`, write `T_i` for the tree rerooted at `i`, and let

\[
d_i=d_T(i,o)
\tag{5.2}
\]

be the graph distance from `i` to the original phylogenetic root `o`.

### Lemma 1 — one-ended extension estimate

There is an infinite one-ended leaf-rooted ordered binary tree `\widehat T_i` such that

\[
R(T_i,\widehat T_i)\ge d_i-1,
\qquad
 d_{\rm loc}(T_i,\widehat T_i)\le 2^{1-d_i}.
\tag{5.3}
\]

#### Proof

Starting from the original root `o`, attach one new edge leaving `o` away from the finite tree. This changes the graph degree of `o` from two to three, as required for an interior vertex in an infinite binary tree. Continue this new edge as an infinite spine. At each new spine vertex attach one finite side branch consisting, for example, of a single leaf; preserve an arbitrary fixed left/right ordering. Every new spine vertex then has degree three and the resulting tree has exactly one end.

The only new edge incident to the old finite tree is the edge leaving `o`. From the distinguished leaf `i`, that edge first appears strictly beyond distance `d_i` from `i`. Under the convention that a truncated rooted ball does not record edges exiting its last sphere, the radius-`d_i` balls already agree; under the stronger boundary-degree convention, radius `d_i-1` certainly agrees. Thus the convention-independent estimate in (5.3) holds. `square`

The factor `2` in (5.3) is irrelevant to every exponent below; with the usual induced-ball convention it can be removed.

## 6. Kraft equality converts local decay into global summability

The numbers `d_i` are exactly the ordinary root-to-leaf depths of the original rooted full binary tree.

### Lemma 2 — Kraft equality

For every finite rooted full binary tree with leaves `1,...,n`,

\[
\boxed{\sum_{i=1}^n 2^{-d_i}=1.}
\tag{6.1}
\]

#### Proof

Induct on the number of leaves. A one-leaf tree has depth zero and the sum is one. Otherwise the original root has two full binary child subtrees. If their internal leaf depths are `(a_i)` and `(b_j)`, induction gives

\[
\sum_i2^{-a_i}=1,
\qquad
\sum_j2^{-b_j}=1.
\]

Every global leaf depth is one plus the corresponding subtree depth, so the global sum is

\[
\frac12\sum_i2^{-a_i}+\frac12\sum_j2^{-b_j}
=\frac12+\frac12=1.
\]

` square`

This is the prefix-code Kraft equality, used here deterministically rather than probabilistically.

### Lemma 3 — the sharp power sum bound

Put `a_i=2^{-d_i}`. For `0<beta<=1`,

\[
\boxed{\sum_{i=1}^n a_i^\beta\le n^{1-\beta}.}
\tag{6.2}
\]

For `beta>=1`,

\[
\boxed{\sum_{i=1}^n a_i^\beta\le1.}
\tag{6.3}
\]

#### Proof

For `0<beta<=1`, `x^beta` is concave. Jensen and `sum_i a_i=1` give

\[
\frac1n\sum_i a_i^\beta
\le
\left(\frac1n\sum_i a_i\right)^\beta
=n^{-\beta},
\]

which is (6.2). For `beta>=1`, `0<=a_i<=1` implies `a_i^beta<=a_i`; summing and using (6.1) gives (6.3). `square`

## 7. B29/B20 theorem — Holder boundary perturbations above one-half cannot change a square-root limit

Call a functional `g` **boundary-vanishing** if

\[
g(T)=0
\tag{7.1}
\]

for every infinite one-ended leaf-rooted binary tree in the source fringe tree-space.

Assume additionally that for some `beta>0` and `C<infinity`,

\[
|g(S)-g(T)|\le C\,d_{\rm loc}(S,T)^\beta
\tag{7.2}
\]

for every pair of finite or infinite trees in this space. This is a global Holder hypothesis; a local-at-the-infinite-boundary version with a uniform constant would be enough for the proof.

### Theorem 4 — deterministic boundary stability

For every finite `n`-leaf full binary tree `T`,

\[
\boxed{
\frac1{\sqrt n}\sum_{i=1}^n |g(T_i)|
\le C2^\beta
\begin{cases}
 n^{1/2-\beta},&0<\beta\le1,\\
 n^{-1/2},&\beta\ge1.
\end{cases}}
\tag{7.3}
\]

In particular, if `beta>1/2`, then

\[
\boxed{
\sup_{T:\,|L(T)|=n}
\left|\frac1{\sqrt n}\sum_{i=1}^n g(T_i)\right|
\longrightarrow0.}
\tag{7.4}
\]

Therefore a boundary-vanishing Holder perturbation of exponent strictly greater than `1/2` cannot change the `sqrt(n)`-scale weak limit, tightness, or CLT of **any** other finite-tree leaf-sum statistic to which it is added.

#### Proof

Fix a leaf `i` and use the infinite extension `\widehat T_i` from Lemma 1. Boundary vanishing gives `g(\widehat T_i)=0`. Hence the Holder condition and (5.3) yield

\[
|g(T_i)|
=|g(T_i)-g(\widehat T_i)|
\le C\,2^{\beta(1-d_i)}
=C2^\beta (2^{-d_i})^\beta.
\tag{7.5}
\]

Sum over leaves and apply Lemma 3. For `0<beta<=1`,

\[
\frac1{\sqrt n}\sum_i|g(T_i)|
\le
C2^\beta n^{-1/2}\sum_i(2^{-d_i})^\beta
\le C2^\beta n^{-1/2}n^{1-\beta}
=C2^\beta n^{1/2-\beta}.
\tag{7.6}
\]

For `beta>=1`, Lemma 3 instead gives

\[
\frac1{\sqrt n}\sum_i|g(T_i)|
\le C2^\beta n^{-1/2}.
\tag{7.7}
\]

This proves (7.3), and both bounds tend to zero when `beta>1/2`, proving (7.4).

Finally let `F` be any other functional and write

\[
X_n(F)=n^{-1/2}\sum_iF(T_i).
\]

Then

\[
|X_n(F+g)-X_n(F)|
\le n^{-1/2}\sum_i|g(T_i)|\to0
\]

deterministically and uniformly over all `n`-leaf trees. Slutsky's theorem therefore shows that `F` and `F+g` have exactly the same subsequential weak limits whenever either family is defined, and deterministic `o(1)` perturbation also preserves tightness. `square`

### What Theorem 4 does and does not say

It says more than a DTCS(n)-in-probability estimate: the perturbation is `o(1)` after `sqrt(n)` normalization **uniformly over every deterministic finite full binary tree**.

It does **not** say that every Holder functional satisfying a fringe CLT automatically satisfies the same finite-tree CLT. A general functional need not vanish on infinite trees, and replacing each finite rerooting by an arbitrary infinite extension does not produce the source stationary fringe process jointly. The theorem closes only the boundary-invisible additive perturbation mechanism used by P0342. This scope guard is essential.

## 8. B4 sharpness — the exponent one-half cannot be improved for deterministic uniform stability

The preceding upper bound has an exact extremal family.

For a finite leaf-rooted tree `T`, let `h(T)` be the distance from its distinguished leaf to the unique degree-two original root. For an infinite one-ended tree put `h(T)=infinity`. Define

\[
\rho(T)=
\begin{cases}
2^{-h(T)},&T\text{ finite},\\
0,&T\text{ infinite}.
\end{cases}
\tag{8.1}
\]

The tiny trees for which the degree-two convention degenerates can be defined arbitrarily; they do not affect any asymptotic statement.

### Lemma 5 — `rho` is Lipschitz up to a universal metric-convention constant

There exists a universal `C_0` (one may take `C_0=2` under the conservative boundary-degree convention) such that

\[
|\rho(S)-\rho(T)|\le C_0 d_{\rm loc}(S,T).
\tag{8.2}
\]

#### Proof

Suppose the radius-`R` rooted balls of `S` and `T` agree. If the original degree-two root of either finite tree occurs strictly inside that common ball, then the corresponding unique degree-two vertex occurs at the same depth in the other tree, so the two `rho` values are equal.

Otherwise neither tree has exposed its finite original root by radius `R-1`. Each finite tree among the pair then has `h>=R`, while an infinite tree has `rho=0`. Thus each nonzero `rho` value is at most `2^{-R}` and

\[
|\rho(S)-\rho(T)|\le2^{-R}=d_{\rm loc}(S,T)
\]

under the induced-ball convention. Allowing one radius of boundary-degree ambiguity multiplies the right-hand side by at most two. `square`

For `0<beta<=1`, set

\[
g_\beta(T)=\rho(T)^\beta.
\tag{8.3}
\]

Since `|x^beta-y^beta|<=|x-y|^beta` for nonnegative `x,y`, Lemma 5 shows that `g_beta` is beta-Holder and boundary-vanishing.

Now take the perfect balanced tree of height `h`, with

\[
n=2^h
\]

leaves. Every leaf has depth exactly `h`, so every leaf rerooting has

\[
g_\beta(T_i)=2^{-\beta h}=n^{-\beta}.
\]

Hence

\[
\boxed{
\frac1{\sqrt n}\sum_{i=1}^n g_\beta(T_i)
=n^{1/2-\beta}.}
\tag{8.4}
\]

Consequently:

- if `beta=1/2`, the normalized sum is identically `1` along this family;
- if `0<beta<1/2`, it diverges to infinity;
- if `beta>1/2`, Theorem 4 forces it to zero on every tree.

Thus

\[
\boxed{\beta=1/2}
\tag{8.5}
\]

is the **sharp deterministic regularity threshold** for uniform `sqrt(n)`-scale invisibility of boundary-vanishing Holder perturbations.

Again, this sharpness is a deterministic statement about the mechanism, not a claim that balanced trees occur with significant DTCS(n) probability.

## 9. Why the actual P0342 perturbation lies outside every positive Holder class

The historical family is

\[
\Phi_\alpha(T)=
\begin{cases}
 n^{-\alpha}(B_n(T)-p_n),&T\text{ finite with }n\ge9\text{ leaves},\\
 0,&T\text{ infinite or }n<9,
\end{cases}
\tag{9.1}
\]

where `B_n` is the event that the smaller original root-clade has size at most `floor(sqrt(n))`, and `p_n=E B_n -> 1/2`.

The previous P13 reports established the phase transition at `alpha=1/2` for its finite DTCS(n) leaf sum. The present theorem explains **topologically** why this family is not ruled out by Theorem 4.

### Proposition 6 — `Phi_alpha` is not Holder of any positive exponent

For every `alpha>0` and every `beta>0`, there is no finite constant `C` such that

\[
|\Phi_\alpha(S)-\Phi_\alpha(T)|
\le C d_{\rm loc}(S,T)^\beta
\tag{9.2}
\]

for all finite/infinite leaf-rooted trees.

#### Proof

Let `C_n` be the `n`-leaf binary comb: the original root splits as `1|(n-1)`, the large child again splits as `1|(n-2)`, and so on. Distinguish a deepest terminal leaf. The distance from that leaf to the original root is `n-1` (up to the immaterial first/last-edge convention).

Extend the comb indefinitely beyond the original root to obtain the infinite one-ended comb `C_infty`. By the same local-ball argument as Lemma 1,

\[
d_{\rm loc}(C_n,C_\infty)\le 2^{2-n}
\tag{9.3}
\]

under the conservative convention.

The smaller original root-clade of `C_n` has size `1`, hence for every large `n`,

\[
B_n(C_n)=1.
\]

Since `p_n->1/2`, eventually `1-p_n>=1/3`. Therefore

\[
|\Phi_\alpha(C_n)-\Phi_\alpha(C_\infty)|
= n^{-\alpha}(1-p_n)
\ge \frac13n^{-\alpha}.
\tag{9.4}
\]

But `\Phi_alpha(C_infty)=0`. If a beta-Holder bound (9.2) held, then (9.3)--(9.4) would imply

\[
\frac13n^{-\alpha}
\le C 2^{\beta(2-n)}.
\tag{9.5}
\]

Multiplying by `2^{\beta n}` gives a left-hand side growing exponentially divided by a polynomial, which tends to infinity, while the right-hand side is constant. Contradiction. `square`

### Proposition 7 — its boundary modulus is only polynomial in the visible radius

If a finite leaf rerooting has root distance `h`, then its tree has at least `h+1` leaves. Therefore, for every `alpha>0`,

\[
|\Phi_\alpha(T)|\le n^{-\alpha}\le(h+1)^{-\alpha}.
\tag{9.6}
\]

Along the comb sequence, (9.4) gives the matching lower order `c h^{-alpha}`. Hence the worst finite-to-infinite boundary decay of this mechanism is polynomial in the visible radius `h`, equivalently logarithmic in inverse local distance:

\[
|\Phi_\alpha|\asymp h^{-\alpha}
\asymp \bigl(\log (1/d_{\rm loc})\bigr)^{-\alpha}
\tag{9.7}
\]

along an explicit boundary-approaching sequence.

This is the precise reason mere continuity is too weak. Local distance decays **exponentially** with how far the original root has escaped, whereas the counterexample was designed to decay only **polynomially** in a global size parameter that can grow linearly with that escape distance.

## 10. What the three approaches accomplished

### B29 — succeeded

Adding the infinite boundary converted the vague phrase “global but continuous” into an exact distance-to-boundary estimate. Every finite leaf rerooting has an explicit infinite one-ended extension at local distance `O(2^{-d_i})`.

### B20 — succeeded

The exact point where the P0342 algorithm would fail under stronger regularity is now identified:

\[
\boxed{
\text{Holder decay }2^{-\beta d_i}
\quad+\quad
\text{Kraft }\sum_i2^{-d_i}=1
\quad\Longrightarrow\quad
n^{-1/2}\sum_i|g(T_i)|=o(1)
}
\]

for `beta>1/2`.

This is not an appeal to mixing, expectation, or typical-tree behavior; it is deterministic.

### B4 — succeeded, with a sharp endpoint

The narrower repair theorem is complete and its threshold is exact. The explicit function `rho^{1/2}` on perfect balanced trees shows that `beta=1/2` cannot be included in a uniform deterministic theorem. The comb calculation then proves that the historical `Phi_alpha` bypasses every positive Holder hypothesis, so there is no contradiction with the completed P0342 counterexample.

## 11. Source interpretation and proposed repaired direction

The source's prose says first-order fringe convergence holds for “suitable functionals,” while Open Problem 12 asks about a “given functional.” P0342 exploits the absence of a quantitative admissibility condition in that numbered implication.

Theorem 4 supplies one mathematically natural guard against exactly this pathology:

> boundary-invisible perturbations should have a local modulus stronger than exponent `1/2` if one wants them to be automatically harmless at the square-root leaf-sum scale.

This is **not** claimed as the optimal hypothesis for a genuine positive transfer theorem. A useful positive theorem could instead be based on cylinder locality, stabilization, summable dependence, an explicit finite/infinite coupling, or a direct aggregate approximation of order `o(sqrt(n))`. The present result only says that a Holder boundary modulus above one-half is one sufficient way to defeat the P0342 global-perturbation mechanism, and that the one-half exponent is sharp for uniform deterministic control.

## 12. Verification / audit discipline

No new finite search, numerical constant, or bounded-enumeration universality claim appears in this report. The new result is a theorem proved analytically on the page, so manufacturing a checker would add receipt volume without testing a finite core.

The earlier P0342 exact checker/output remains a **P13 self-check only**. It is not promoted to an independent audit.

Current closure gates remain unsatisfied in repository evidence:

1. no recovered P26 end-to-end P0342 PASS;
2. no recovered distinct OTHER-track end-to-end P0342 PASS;
3. the bounded prior-art search is recorded but is not a novelty certificate.

Accordingly this report does not label P0342 CLOSED or create a `paper_*` package. P12's directed audit duty follows this actual successor, but P13 does not fabricate or write that peer audit itself. P13's separate directed audit duty toward P14 remains unchanged; previously completed audits are not repeated here.

## 13. Metric, stagnation, and next action

Frozen source metric:

\[
\boxed{M_{\rm P0342}:2/2\longrightarrow2/2.}
\]

There is **no source-metric movement** because source obligations were already complete. There is genuine mathematical movement: the mechanism now has a sharp regularity barrier and an exact topological diagnosis.

This is not a six-run unchanged-source rotation situation: the claimed source theorem is metric-complete and is waiting on mandated independent closure gates, while current runs are strengthening and stress-testing scope. I do not rename the metric or reset any historical counter.

The next mathematically useful direction, if audits still have not arrived, is to stress-test the boundary theorem against weaker moduli `omega(2^{-d})`: characterize exactly which moduli satisfy

\[
\sup_{\{d_i:\sum2^{-d_i}=1\}}
 n^{-1/2}\sum_i\omega(2^{-d_i})\to0,
\]

rather than proving another special exponent. That would identify the maximal deterministic regularity class excluding P0342-type invisible perturbations. This is a future route, not a result claimed here.

## 14. Structured `ledger_delta` for P26 / coordinator

```yaml
ledger_delta:
  track: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  target: P0342
  source: Aldous-Janson arXiv:2303.02529v3 Open Problem 12 section 4.10
  lane: CLOSABLE_OUTSIDE
  metric_name: M_P0342
  metric_before: "2/2"
  metric_after: "2/2"
  metric_denominator_frozen: true
  source_metric_movement: false
  mathematical_movement: >-
    Proved deterministic Holder boundary stability: any boundary-vanishing
    beta-Holder perturbation with beta>1/2 contributes o(1) uniformly after
    sqrt(n) normalization on every finite full binary tree; proved beta=1/2
    sharp for this deterministic mechanism; proved historical Phi_alpha is
    not Holder of any positive exponent and has polynomial-in-depth boundary decay.
  methods: [B4, B20, B29]
  previous_methods: [B2, B7, B12]
  current_status: CLAIMED_METRIC_COMPLETE_SOURCE_REFUTATION_CANDIDATE_AUDITS_PENDING
  mandatory_i0054_screen: "occupied by R11; newest recovered R11 metric 68->69; untouched"
  source_page_image: "SUCCESS this run; Open Problem 12 inspected on source PDF page index 44"
  prior_art: "bounded 2026-09-19 search; no checked exact OP12 resolution found; no novelty claim"
  p26_end_to_end_audit: MISSING_IN_RECOVERED_REPOSITORY_EVIDENCE
  second_other_track_audit: MISSING_IN_RECOVERED_REPOSITORY_EVIDENCE
  self_check: "historical P13 checker retained; not an independent audit"
  claim_modified: false
  shared_root_ledger_modified: false
  peer_files_modified: false
  schedule_modified: false
  paper_package_created: false
```

## 15. Delivery scope

One idea artifact and this one immutable run report are the only P13 writes in this invocation. No historical report, canonical claim, shared root ledger, peer file, scheduler, email/Drive resource, public posting, paid compute, permission, workflow, or external contact was modified.
