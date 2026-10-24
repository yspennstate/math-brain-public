Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. NO SOURCE-METRIC MOVEMENT: `M_P0342 = 2/2 -> 2/2`. NEW MATHEMATICAL MOVEMENT: the Kraft/modulus extremal problem is solved exactly for every leaf count `n`, not only powers of two: every concave boundary modulus is maximized by a quasi-complete binary tree whose leaf depths differ by at most one, giving an explicit dyadic-shell formula and a nontrivial critical `beta=1/2` log-periodic profile. Methods actually tried: B1, B13, B30.**

# P13 / P0342 — exact all-`n` dyadic Kraft extremizer

Date: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Native slot: `6aa7b253b37c8191b693d8dc79298d37`.  
Own root: `proofnet24/P13-outside-successor/`.

## 1. Continuity, mandatory first screen, ownership, and exclusions

This invocation continues the exclusive P13 successor `P0342`, governed by `operations/claims/P0342.md`. It does **not** reopen the retired I0051 / Aldous--Janson Open Problem 9 clade-covariance target, the completed six-unchanged-run C0021 handoff, old AF4.49(ii)/PROB20-13, the DLA exponent route, P22/P23/P25, paused P17/P18, or any POSTED/INDEX exclusion.

I reread/recovered the controlling owner directive at anchor `749da260517828ed311f6f1b1af74915c054bdf3`, `operations/NEW_METHODS_2026-09-16.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md` and `QUEUE.md`, the P0342 canonical claim, the preceding P13 report and the terminal C0021 handoff, current P0342 audit searches, and the newest neighboring I0054 report. Target-specific repository searches also recovered the preserved historical P0342 packet. The connector permits targeted search/fetch, not a credible literal visual reread of every byte of every very large append-only intake JSONL; I do not claim otherwise.

The mandatory I0054 screen was performed first. The newest recovered R11 report is

`runs/R11/2026-09-19T15-40-00Z_i0054-power-inversive-u050-c071-a6e3.md`.

It moves R11's own author-side model-class metric `70 -> 71`, still labels exact Open Problem 18 **PARTIAL** at source/campaign level, and continues R11's I0054 ownership. P13 therefore did not touch I0054 or its claim.

The current P13 claim is instead:

`operations/claims/P0342.md` — David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3, Open Problem 12, Section 4.10.

Its frozen metric remains

`M_P0342 in {0,1,2}` = number of the `FRINGE` and `FINITE-FAILURE` obligations established simultaneously for the one fixed witness `Theta=Psi+Phi`.

Both obligations have already been proved in earlier immutable P13 reports, so

`M_P0342 = 2/2 -> 2/2`.

The denominator is not changed. The theorem below is a genuine strengthening of the boundary-regularity analysis around the completed counterexample, not a third source obligation and not renewed source-metric movement. As in the immediately preceding report, a metric-complete source claim awaiting independent audits is not assigned a fictitious new stagnation counter merely because a strengthening keeps `2/2` fixed.

Fresh repository searches still recover no end-to-end P0342 PASS from P26 and no end-to-end P0342 PASS from a distinct OTHER research track. Historical P12/P13 audits concern the retired I0051 target and do not transfer. Campaign status therefore remains

`CLAIMED / METRIC-COMPLETE / SOURCE-REFUTATION-CANDIDATE / AUDITS-PENDING`.

No claim file or shared root ledger is modified in this invocation.

## 2. Exact source scope and fresh current-literature check

The current v3 source still asks, literally, whether if a CLT holds for a **given functional** along the stationary fringe process, the same CLT necessarily holds for the corresponding DTCS(`n`) leaf sum. The source's nearby prose speaks of “suitable functionals,” but the numbered Open Problem 12 itself does not impose a quantitative locality, Holder, stabilization, or boundary-modulus hypothesis. P0342 therefore remains a candidate negative answer only to that literal universal implication, not to every intended strengthened formulation.

Primary source checked again on 2026-09-19:

- `https://arxiv.org/abs/2303.02529`
- `https://arxiv.org/pdf/2303.02529`

The source PDF page containing Open Problem 12 had already been successfully inspected in the preceding source check; there is no page-image access gap carried into this run.

A fresh dated bounded search using combinations of

- `"Aldous Janson" "Open Problem 12" fringe CLT critical beta splitting`,
- `"Critical Beta-splitting Random Tree" fringe CLT transfer Open Problem 12`, and
- later critical-beta author/paper names

recovered the overview source and adjacent later critical-beta literature but no checked primary paper explicitly announcing a resolution of exact Open Problem 12. This is bounded negative evidence only, not a worldwide openness, novelty, or priority certificate.

For the new theorem below I also searched the coding-theory analogue using combinations of `concave`, `Kraft`, `prefix code`, `codeword lengths`, and `uniform`. The classical Kraft--McMillan theorem and standard Huffman/uniform-source facts recover the well-known prefix-code interpretation and the two-adjacent-depth shape of optimal uniform codes. I did not locate in this bounded search a checked primary source stating the exact arbitrary-concave reward extremum `sum omega(2^{-d_i})` with the formula proved below. The coding analogy is therefore used as a method and prior-art warning, not as a novelty claim.

## 3. Idea-before-proof receipt and the three methods

Before writing the proof I committed

`proofnet24/P13-outside-successor/artifacts/2026-09-19/2026-09-19T16-02-32Z__p0342_b1_b13_b30_dyadic-extremizer-idea.md`

at commit `96319711128a8f34333f3529256ca35f9c4d03ac` and read it back at that exact commit; verified blob `3b8d81227bad4803a9fd9650f2e1485ef4b7ab12`.

The methods differ from the preceding B8/B21/B24 triple.

**B1 — CHANGE THE CATEGORY.** Replace a full binary tree by its complete binary prefix code. Leaf depths are codeword lengths and the weights `2^{-d_i}` are the Kraft masses. The topological boundary problem becomes an exact discrete optimization problem over complete prefix codes.

**B13 — FIND WHAT ONLY INCREASES.** Construct a local balancing exchange that never decreases the concave Kraft reward and strictly decreases total external path length. This gives a terminating proof that every extremizer can be flattened to two adjacent depths.

**B30 — DO ONE SCALE AT A TIME.** On each dyadic shell `2^h <= n < 2^{h+1}`, solve the two depth counts exactly. For power moduli this exposes an explicit scale-periodic profile that Jensen's previous all-`n` upper bound hid.

No new checker is warranted: the new assertions are analytic identities/inequalities proved below and use no finite enumeration. The historical exact P0342 script/output remains a P13 self-check only.

## 4. Recovered boundary-modulus setup

Use the local metric

\[
d_{\rm loc}(S,T)=2^{-R(S,T)},
\]

where `R(S,T)` is the largest rooted induced-ball radius on which the ordered leaf-rooted trees agree.

Let

\[
\omega:[0,1]\to[0,\infty)
\]

be increasing and concave with `omega(0)=0`. Let `G_omega` be the class of functionals `g` satisfying

1. `g(T)=0` for every infinite one-ended fringe tree; and
2.

\[
|g(S)-g(T)|\le \omega(d_{\rm loc}(S,T)).
\tag{4.1}
\]

For a finite rooted full binary tree `T` with leaves `1,...,n`, let `d_i` be leaf `i`'s depth from the original phylogenetic root. Then the exact Kraft identity is

\[
\sum_{i=1}^n2^{-d_i}=1.
\tag{4.2}
\]

Let `T_i` denote the same finite tree rerooted at leaf `i`, and define

\[
A_n(\omega)=
\sup_{T:\,|L(T)|=n}\ \sup_{g\in G_\omega}
\frac1{\sqrt n}\left|\sum_{i=1}^n g(T_i)\right|.
\tag{4.3}
\]

The preceding report proved the universal Jensen estimate

\[
A_n(\omega)\le \sqrt n\,\omega(1/n)
\tag{4.4}
\]

and exact attainment when `n` is a power of two. The present run removes the power-of-two restriction and computes `A_n(omega)` exactly for every `n`.

## 5. B1 reduction — exact equality with a complete-prefix-code optimization

For each leaf `i`, extend `T_i` beyond the original phylogenetic root by an infinite binary spine. Call the resulting infinite one-ended tree `\widehat T_i`. The finite and infinite rerootings agree through radius `d_i`, so

\[
d_{\rm loc}(T_i,\widehat T_i)\le 2^{-d_i}.
\]

Since every `g in G_omega` vanishes on `\widehat T_i`, (4.1) gives

\[
|g(T_i)|\le\omega(2^{-d_i}).
\tag{5.1}
\]

Therefore

\[
A_n(\omega)
\le
\frac1{\sqrt n}
\max_{T:\,|L(T)|=n}
\sum_{i=1}^n\omega(2^{-d_i}).
\tag{5.2}
\]

The preceding report also proved that the boundary gauge

\[
\rho(U)=2^{-h(U)}
\]

for a finite leaf-rooted tree, where `h(U)` is the distinguished leaf's distance to the original degree-two root, extended by `rho=0` on infinite one-ended trees, is 1-Lipschitz for `d_loc`. Concavity and `omega(0)=0` imply subadditivity, hence

\[
g_\omega(U)=\omega(\rho(U))
\tag{5.3}
\]

belongs to `G_omega`.

For every finite rerooting `T_i`, `rho(T_i)=2^{-d_i}`. Thus the single functional (5.3) attains the right side of (5.1) with the same sign at every leaf. Consequently the inequality (5.2) is exact:

### Proposition 1 — exact prefix-code reduction

\[
\boxed{
A_n(\omega)=
\frac1{\sqrt n}
\max_{T:\,|L(T)|=n}
\sum_{i=1}^n\omega(2^{-d_i}).
}
\tag{5.4}
\]

Equivalently, the problem is to maximize the symmetric concave reward `sum omega(a_i)` over the dyadic Kraft masses `a_i=2^{-d_i}` of complete binary prefix codes with exactly `n` codewords.

This B1 change of category is useful because tree topology now enters only through the dyadic Kraft constraint.

## 6. B13 balancing exchange

The key new ingredient is a local exchange that flattens any nonbalanced depth profile without lowering the objective.

Define

\[
G(t)=2\omega(t/2)-\omega(t),\qquad 0\le t\le1.
\tag{6.1}
\]

### Lemma 2 — `G` is nondecreasing

If `omega` is concave, then `G` is nondecreasing on `[0,1]`.

#### Proof

Take `0<=s<t<=1` and put

\[
\delta=(t-s)/2.
\]

Then

\[
G(t)-G(s)
=2[\omega(s/2+\delta)-\omega(s/2)]
-[\omega(s+2\delta)-\omega(s)].
\tag{6.2}
\]

Write

\[
A=\omega(s/2+\delta)-\omega(s/2),
\]

and split the last increment into two equal-length increments

\[
B_1=\omega(s+\delta)-\omega(s),\qquad
B_2=\omega(s+2\delta)-\omega(s+\delta).
\]

For a concave function, increments over a fixed interval length are nonincreasing as the starting point moves to the right. Since `s/2 <= s <= s+delta`,

\[
A\ge B_1,\qquad A\ge B_2.
\]

Hence `2A>=B_1+B_2`, which is exactly `G(t)-G(s)>=0` in (6.2). `square`

If `omega` is strictly concave and `s<t`, the same comparison is strict, so `G` is strictly increasing.

### Lemma 3 — one balancing exchange never decreases the reward

Suppose a full binary tree has minimum leaf depth `d` and maximum leaf depth `D>=d+2`. Then there is another full binary tree with the same number of leaves whose reward

\[
\sum_i\omega(2^{-d_i})
\]

is at least as large, and whose total external path length `sum_i d_i` is smaller by `D-d-1`.

#### Proof

Choose a leaf at depth `d`. Choose a deepest leaf at depth `D`. Its sibling must also be a leaf at depth `D`: if that sibling were internal it would have a descendant at depth at least `D+1`, contradicting maximality of `D`.

Perform two local moves simultaneously:

1. split the depth-`d` leaf into an internal vertex with two leaf children at depth `d+1`;
2. collapse the deepest sibling pair into their parent, now a leaf at depth `D-1`.

The first move adds one leaf and the second removes one, so the leaf count is unchanged. The result is again a full binary tree.

Put

\[
x=2^{-d},\qquad y=2^{-D}.
\]

The change in reward is

\[
\begin{aligned}
\Delta
&=2\omega(x/2)+\omega(2y)-\omega(x)-2\omega(y)\\
&=G(x)-G(2y).
\end{aligned}
\tag{6.3}
\]

Because `D>=d+2`,

\[
2y=2^{-(D-1)}\le 2^{-(d+1)}=x/2<x.
\]

Lemma 2 therefore gives `Delta>=0`. If `omega` is strictly concave, `Delta>0`.

The change in total external path length is

\[
[2(d+1)+(D-1)]-[d+2D]
=d+1-D
=-(D-d-1)\le-1.
\tag{6.4}
\]

This proves both assertions. `square`

The path-length drop is the B13 monovariant. Repeating the exchange cannot continue forever because `sum_i d_i` is a nonnegative integer that drops at each step. When no exchange is possible, maximum and minimum leaf depths differ by at most one.

## 7. B30 — solve each dyadic shell exactly

Write

\[
h=\lfloor\log_2 n\rfloor,
\qquad
2^h\le n<2^{h+1}.
\tag{7.1}
\]

After the balancing process, every leaf depth is either `h` or `h+1` (with the power-of-two case having only depth `h`). Let

- `a` = number of leaves at depth `h`;
- `b` = number of leaves at depth `h+1`.

The equations

\[
a+b=n,
\qquad
a2^{-h}+b2^{-(h+1)}=1
\tag{7.2}
\]

have the unique solution

\[
\boxed{
a=2^{h+1}-n,\qquad
b=2n-2^{h+1}.
}
\tag{7.3}
\]

Such a full binary tree exists: start with the perfect depth-`h` tree with `2^h` leaves and split exactly `n-2^h` of those leaves. This creates exactly the counts (7.3).

Combining Proposition 1 and Lemma 3 gives the exact all-`n` answer.

### Theorem 4 — exact all-`n` modulus extremum

For every integer `n>=2`, every increasing concave `omega` with `omega(0)=0`, and `h=floor(log_2 n)`,

\[
\boxed{
A_n(\omega)
=
\frac{
(2^{h+1}-n)\,\omega(2^{-h})
+(2n-2^{h+1})\,\omega(2^{-(h+1)})
}{\sqrt n}.
}
\tag{7.4}
\]

#### Proof

By Proposition 1 it suffices to maximize the Kraft reward over full binary trees. Lemma 3 transforms every tree, without decreasing reward, into one whose leaf depths differ by at most one. Equations (7.1)--(7.3) force every such terminal tree to have the same two depth counts, so every original reward is at most the numerator of (7.4).

Conversely a tree with exactly those depth counts exists, and the single admissible functional `g_omega` in (5.3) attains termwise equality. Therefore the upper bound is attained and (7.4) is exact. `square`

If `omega` is strictly concave, every balancing move with depth spread at least two is strictly improving. Hence every maximizing depth profile must already have spread at most one. For non-power-of-two `n`, the leaf-depth multiset (7.3) is therefore forced. There can still be multiple ordered tree shapes realizing that same multiset; I do not claim shape uniqueness beyond the forced depth data.

For `n=2^h`, (7.4) reduces to

\[
A_n(\omega)=\sqrt n\,\omega(1/n),
\]

recovering the preceding power-of-two equality as a special case.

## 8. Power moduli: exact dyadic-shell profile

Take

\[
\omega(t)=C t^\beta,
\qquad 0<\beta\le1.
\tag{8.1}
\]

Let

\[
x=\frac{n}{2^h}\in[1,2).
\tag{8.2}
\]

Substituting (8.1)--(8.2) into (7.4) yields

\[
\boxed{
A_n(Ct^\beta)
=C n^{1/2-\beta}R_\beta(x),
}
\tag{8.3}
\]

where

\[
\boxed{
R_\beta(x)=
\frac{(2-x)+2^{1-\beta}(x-1)}{x^{1-\beta}}.
}
\tag{8.4}
\]

The previous Jensen estimate implies `R_beta(x)<=1`; equality occurs at the dyadic endpoints. Formula (8.4) gives the exact amount of Jensen slack between those endpoints.

Thus the sharp square-root boundary remains:

- if `beta>1/2`, then `A_n -> 0`;
- if `beta=1/2`, the worst effect stays order one and does not vanish;
- if `beta<1/2`, it grows on the order `n^{1/2-beta}`.

This conclusion was known qualitatively from the preceding Holder theorem. The new content is the exact all-`n` coefficient and its dyadic oscillation.

## 9. Critical exponent `beta=1/2`: an explicit nonconvergent profile

At the critical exponent,

\[
R_{1/2}(x)
=
\frac{(2-x)+\sqrt2(x-1)}{\sqrt x}
=
\frac{2-\sqrt2}{\sqrt x}
+(\sqrt2-1)\sqrt x.
\tag{9.1}
\]

This equals `1` at `x=1` and in the limit `x->2`. Differentiating the elementary right side, or using AM--GM, shows that its unique interior minimum occurs at

\[
x=\frac{2-\sqrt2}{\sqrt2-1}=\sqrt2.
\tag{9.2}
\]

The minimum value is

\[
\boxed{
R_{1/2}(\sqrt2)
=2\sqrt{(2-\sqrt2)(\sqrt2-1)}
=2\sqrt{3\sqrt2-4}
\approx0.98517.
}
\tag{9.3}
\]

Consequently, for the exact worst boundary effect at critical regularity,

\[
\boxed{
\limsup_{n\to\infty}\frac{A_n(C\sqrt t)}C=1,
\qquad
\liminf_{n\to\infty}\frac{A_n(C\sqrt t)}C
=2\sqrt{3\sqrt2-4}.
}
\tag{9.4}
\]

The limsup is attained along `n=2^h`. For the liminf take integers `n_h` nearest to `sqrt(2) 2^h`, so `n_h/2^h -> sqrt(2)` and use continuity of (9.1).

Thus the critical square-root class has a genuine dyadic log-periodic extremal profile rather than a single asymptotic constant. This feature is invisible in the previous Jensen upper bound.

## 10. What this does and does not say about Open Problem 12

The theorem is a precise repair diagnostic, not a new positive solution of a strengthened Open Problem 12.

It says that for the specific architecture “add a perturbation that vanishes on every infinite fringe tree but is controlled at the finite/infinite boundary by a concave modulus,” the worst possible aggregate square-root-scale finite-tree effect is exactly (7.4). In particular, the criterion

\[
\sqrt n\,\omega(1/n)\to0
\]

remains necessary and sufficient for **uniform** negligibility, and Theorem 4 now gives its exact finite-`n` envelope.

It does **not** say that every arbitrary `omega`-continuous functional with nonzero infinite-tree values inherits a finite-tree CLT, nor that the intended “suitable functional” version of Open Problem 12 has been characterized. Such a positive transfer theorem could also require stabilization, mixing, cancellation, or a quantitative coupling of the finite rerooting field to the stationary fringe process.

The historical P0342 root-split perturbation is already known from the preceding reports to violate every stable positive-Holder boundary class by an exponential margin on comb trees. The present exact optimization sharpens the regularity picture around that counterexample but does not alter the frozen source witness or metric.

## 11. Prior-art restraint

The B1 coding translation is classical in spirit:

- leaf depths of a full binary tree are complete binary prefix-code lengths;
- their masses satisfy Kraft equality;
- standard uniform-source coding gives a two-adjacent-depth optimal tree.

Those facts make the extremizer plausible and are not claimed as new. The proof above is included because P0342 needs the exact arbitrary-concave reward `sum omega(2^{-d_i})`, the pointwise boundary functional attaining it, and the resulting critical modulus profile. A bounded current search did not locate a checked source stating precisely this combined theorem. That is not a novelty certificate.

Likewise, the fresh Open Problem 12 literature search found no checked resolution announcement, but a bounded search cannot prove global openness. The report therefore retains `SOURCE-REFUTATION-CANDIDATE`, not `REFUTED/CLOSED`.

## 12. Method accounting

**B1 succeeded.** The complete-prefix-code translation removed irrelevant tree geometry and identified the exact finite feasible object: dyadic Kraft masses.

**B13 succeeded.** The monotone balancing exchange and external-path-length monovariant prove that any reward maximizer can be flattened to adjacent depths; strict concavity forces that depth profile for every maximizer.

**B30 succeeded.** Solving one dyadic shell at a time gives the forced counts (7.3), the exact formula (7.4), and the scale-periodic power-law profile (8.4). At the critical exponent it exposes the explicit liminf/limsup pair (9.4).

No method was credited merely for a receipt or verification action.

## 13. Audit, closure, and delivery status

The source-level P0342 mathematics remains metric-complete at `2/2`, but campaign closure is still blocked by external gates rather than by a missing P13 lemma:

1. no recovered P26 end-to-end P0342 PASS;
2. no recovered distinct OTHER-track end-to-end P0342 PASS;
3. prior-art searches are bounded and explicitly not novelty certificates.

P12's directed audit duty follows this actual successor, while P13's own secondary directed audit duty toward P14 remains unchanged. P13 does not fabricate either peer audit.

Therefore I do **not** label P0342 `CLOSED` or create a `paper_*` package in this invocation. The older exact P0342 checker/output remains a P13 self-check and is not promoted to independent evidence.

No peer file, shared root ledger, canonical claim, schedule, email/Drive resource, workflow, permission, public post, paid-compute resource, or external contact was modified.

## 14. Structured ledger delta for P26

```yaml
ledger_delta:
  track: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  own_root: proofnet24/P13-outside-successor
  target: P0342
  claim: operations/claims/P0342.md
  source: Aldous-Janson arXiv:2303.02529v3 Open Problem 12
  lane: CLOSABLE_OUTSIDE
  metric_name: M_P0342
  metric_before: 2/2
  metric_after: 2/2
  source_metric_movement: false
  mathematical_movement: exact all-n concave-modulus Kraft extremum and critical dyadic profile
  exact_all_n_formula: A_n(omega)=n^(-1/2)*[(2^(h+1)-n)omega(2^(-h))+(2n-2^(h+1))omega(2^(-(h+1)))], h=floor(log2 n)
  methods: [B1, B13, B30]
  idea_before_proof:
    path: proofnet24/P13-outside-successor/artifacts/2026-09-19/2026-09-19T16-02-32Z__p0342_b1_b13_b30_dyadic-extremizer-idea.md
    commit: 96319711128a8f34333f3529256ca35f9c4d03ac
    blob: 3b8d81227bad4803a9fd9650f2e1485ef4b7ab12
  i0054_first_screen:
    owner: R11
    newest_metric: 70->71
    status: PARTIAL
  p26_end_to_end_audit: MISSING
  distinct_other_end_to_end_audit: MISSING
  prior_art_scope: bounded 2026-09-19 source/coding search; no global openness or novelty claim
  status_after: CLAIMED / METRIC-COMPLETE / SOURCE-REFUTATION-CANDIDATE / AUDITS-PENDING
  self_check_status: historical P13 self-check retained; no new checker needed for analytic theorem
  shared_root_write: false
  peer_write: false
  scheduler_write: false
```
