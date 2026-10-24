Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# Admission-side correction for `AK-KATZIN-C41-EQUALITY`: the literal biconditional already fails in dimension 1

Date: 2026-09-19 UTC  
Worker: `R7-05 Sharp Inequality Research`  
Native ID: `6aabe805f32881919992996e1c5cfad6`  
Repository: private `yspennstate/math-open-problems`, `master`  
Captured pre-write master: `4f3aac9c1285708a5ae5ccabee2136f6826f08a8`

This is **not** an ownership claim on `AK-KATZIN-C41-EQUALITY`. The canonical claim is already owned by HARD7-01. This note is an independent source/hypothesis check prompted by a new residue-4 lifecycle event. It corrects a metric interpretation in the newly added claim/report and leaves R7-05 at `PENDING_ADMISSION`.

## 1. Exact source text and scope

Primary source:

Shiri Artstein-Avidan and David Katzin, *Isotropic measures and maximizing ellipsoids: Between John and Loewner*, Proc. Amer. Math. Soc. 146 (2018), 5379–5390, arXiv:1612.01128, Section 4, Conjecture 4.1.

The source defines

\[
\phi(s)=\operatorname{Vol}_n(e^{s\Lambda}K\cap B_2^n)
\]

and conjectures midpoint log-concavity

\[
\phi(t/2)^2\ge \phi(t)\phi(0)
\]

for every real `t` and diagonal `Lambda`. It then literally prints:

> equality is attained if and only if one of the following hold: `K subset B_2^n`, `B_2^n subset K`, or `Lambda=lambda I_n`.

The current HARD7-01 claim freezes

`n_bad = smallest dimension n >= 1 in which the literal equality classification ... has an exact counterexample at some nonzero t`

and says dimension one is safe because every `1 x 1` diagonal matrix is scalar. That argument checks only the **necessity** direction

`equality => one of the listed alternatives`.

It does not check the converse direction of the printed **if and only if**.

## 2. B1 — solve the complete one-dimensional case

Restrict to the centrally symmetric one-dimensional bodies relevant to the surrounding discussion. Every such convex body is

\[
K=[-a,a],\qquad a>0,
\]

and every diagonal matrix is scalar,

\[
\Lambda=[\lambda].
\]

Since `B_2^1=[-1,1]`, for every real `s`

\[
\phi(s)
=\operatorname{length}([-ae^{\lambda s},ae^{\lambda s}]\cap[-1,1])
=2\min\{ae^{\lambda s},1\}.
\]

Put

\[
u=\log a,\qquad v=\lambda t.
\]

Then

\[
\log \phi(s)=\log2+\min\{\log a+\lambda s,0\}.
\]

Therefore the exact logarithmic midpoint gap is

\[
\Gamma(u,v)
:=\log\frac{\phi(t/2)^2}{\phi(0)\phi(t)}
=2\min\{u+v/2,0\}-\min\{u,0\}-\min\{u+v,0\}.
\]

This piecewise-linear expression can be evaluated completely.

If `u` and `u+v` have the same weak sign, the segment does not cross the unique kink at `0`, so `log phi` is affine on the whole segment and

\[
\Gamma(u,v)=0.
\]

If `u` and `u+v` have opposite strict signs, then the segment crosses the kink and

\[
\boxed{\Gamma(u,v)=\min\{|u|,|u+v|\}>0.}
\]

Consequently the complete one-dimensional equality criterion is

\[
\boxed{
\phi(t/2)^2=\phi(0)\phi(t)
\iff
(\log a)(\log a+\lambda t)\ge0.
}
\]

Equivalently, equality holds exactly when the two endpoint radii `a` and `a e^{lambda t}` lie on the same side of the unit radius (allowing an endpoint to equal one). Equality is strict exactly when the scalar dilation crosses the unit-ball boundary between the two endpoints.

This is a full one-dimensional classification, not a numerical observation.

## 3. B27 — explicit exact dimension-one false positive

Take

\[
K=[-1/2,1/2],\qquad \Lambda=[1],\qquad t=2\log2.
\]

Then

\[
\phi(0)=1,
\qquad
\phi(t/2)=2,
\qquad
\phi(t)=2.
\]

Hence

\[
\boxed{
\phi(t/2)^2=4>2=\phi(t)\phi(0).
}
\]

The source equality is **strict**.

Nevertheless two of the printed right-hand alternatives hold simultaneously:

- `K subset B_2^1`;
- every `1 x 1` diagonal matrix is scalar, so `Lambda=lambda I_1`.

Thus, if Conjecture 4.1's printed phrase is read literally as a biconditional for equality in (4.1), it already has an exact counterexample in dimension

\[
\boxed{n=1.}
\]

No floating-point calculation is involved. The three lengths are exact.

There is an infinite family: choose any `a != 1`, `lambda != 0`, and nonzero `t` for which

\[
(\log a)(\log a+\lambda t)<0.
\]

Then the listed scalar-`Lambda` alternative holds but equality is strict.

## 4. The peer dimension-two example remains valuable: split the two logical directions

HARD7-01 independently found the exact two-dimensional example

\[
K=[-1/2,1/2]\times[-2,2],\quad
\Lambda=\operatorname{diag}(0,1),\quad
t=2\log2,
\]

for which equality holds although none of the three printed alternatives holds.

That example is a **false negative** of the printed characterization:

`equality` but `no listed alternative`.

The present dimension-one example is the opposite logical failure, a **false positive**:

`listed alternative` but `strict inequality`.

This distinction resolves the apparent disagreement with HARD7-01's statement that dimension one is safe. Dimension one is indeed safe for the one-way implication

\[
\text{equality}\Longrightarrow\text{listed alternative},
\]

because every one-dimensional diagonal matrix is scalar. It is **not** safe for the full printed biconditional.

Therefore the mathematically unambiguous split metrics are

\[
\boxed{n_{\mathrm{false\ positive}}=1,}
\]

and, using the existing HARD7-01 witness plus the one-dimensional scalar observation,

\[
\boxed{n_{\mathrm{false\ negative}}=2.}
\]

If the canonical metric `n_bad` is intended literally for any counterexample to the printed `iff`, then its value should be `1`, not `2`. If instead it is intended only for an **unlisted equality case**, then the existing value `2` is correct but the metric should be renamed or its direction stated explicitly.

R7-05 does not edit the HARD7-01-owned canonical claim; coordinator/owner-track reconciliation is required.

## 5. B6 — relation to Proposition 4.2 and the actual uniqueness question

This correction does **not** undermine the logical purpose of the equality statement in Proposition 4.2 in the same way.

In the uniqueness argument, the relevant situation has

- `K` neither contained in `B_2^n` nor containing `B_2^n` (intermediate radius);
- a diagonal `Lambda` with `tr Lambda=0`;
- equality forced by maximality.

The proof only needs the **necessity** statement

\[
\boxed{
\text{if equality holds, }K\not\subset B_2^n,\ B_2^n\not\subset K,
\text{ and }\operatorname{tr}\Lambda=0,
\text{ then }\Lambda=0.
}
\]

It never needs the converse assertion that `K subset B`, `B subset K`, or scalar `Lambda` automatically makes (4.1) an equality.

So the dimension-one false positive exposes an overstrong literal biconditional but does not itself refute the desired maximal-intersection uniqueness implication. HARD7-01's two-dimensional inactive-coordinate example attacks the necessity direction, while its separate determinant-one deformation shows that particular box is not globally maximal. The corrected hard geometric target must therefore incorporate maximality/stationarity, not merely the raw printed biconditional.

## 6. A repair template for the obvious sufficient cases

The source's three short alternatives are not sufficient as written because the deformation can cross a containment boundary.

Two genuinely sufficient mechanisms are instead:

1. if `e^{s Lambda}K subset B_2^n` for every `s` between `0` and `t`, then
   \[
   \phi(s)=e^{s\operatorname{tr}\Lambda}\operatorname{Vol}(K),
   \]
   so `log phi` is affine and midpoint equality holds;

2. if `B_2^n subset e^{s Lambda}K` for every `s` between `0` and `t`, then
   \[
   \phi(s)=\operatorname{Vol}(B_2^n),
   \]
   so equality again holds.

The one-dimensional classification shows exactly why endpoint-independent statements such as merely `K subset B` or merely `Lambda` scalar cannot be sufficient: the path may cross from one regime to the other.

## 7. Source/current-literature guard

The exact wording above was checked against arXiv:1612.01128, p. 9. The source indeed says `for all t` and `all diagonal Lambda`, followed by the literal `if and only if` equality sentence; no trace-zero hypothesis appears in Conjecture 4.1 itself.

The inequality half is now known from Cordero-Erausquin--Rotem (Ann. Probab. 2023) for the relevant rotationally invariant class. The 2023 paper *Stability and the equality case in the B-theorem* is by Herscovici, Livshyts, Rotem and Volberg, not Eli Putterman; it concerns the Gaussian strong `(B)` equality/stability setting and maximal Gaussian-measure position. Eli Putterman's separate 2026 preprint *Sharp stability for the (B)-theorem*, arXiv:2608.08472, builds on that work and says its method extends to strong/functional `(B)` inequalities. None of these bounded checks changes ownership or supplies a source correction to the literal 2018 sentence.

Search misses are not novelty or openness certificates.

## 8. Admission consequence for R7-05

The exact case-sensitive ID `AK-KATZIN-C41-EQUALITY` has character-code sum `1530`, hence

\[
1530\bmod7=4,
\]

so it lies in R7-05's selection partition. But it is **not selectable**:

- it is canonically owned by HARD7-01;
- the literal source clause is already mathematically refuted as printed;
- this note only corrects the logical direction/minimal-dimension accounting.

No successor source is admitted. R7-05 remains `PENDING_ADMISSION`, with successor metric `UNKNOWN/UNMEASURED` and no successor stagnation count.

## 9. Ledger delta for this artifact

```yaml
worker: R7-05
native_task_id: 6aabe805f32881919992996e1c5cfad6
report_kind: substantive_admission_side_peer_hypothesis_correction
captured_master_sha: 4f3aac9c1285708a5ae5ccabee2136f6826f08a8
candidate_id: AK-KATZIN-C41-EQUALITY
candidate_shard_sum: 1530
candidate_shard_mod7: 4
candidate_owner: HARD7-01
candidate_disposition: OWNED_AND_LITERAL_SOURCE_ALREADY_REFUTED_NOT_ADMISSIBLE
methods: [B1, B27, B6]
new_exact_result: complete one-dimensional equality criterion and exact dimension-one false-positive witness
canonical_metric_correction:
  literal_biconditional_min_counterexample_dimension: 1
  unlisted_equality_min_counterexample_dimension: 2
canonical_claim_edited: false
target_after: PENDING_ADMISSION
successor_metric_before: UNKNOWN_UNMEASURED
successor_metric_after: UNKNOWN_UNMEASURED
successor_stagnation_count: NOT_INSTANTIATED
```
