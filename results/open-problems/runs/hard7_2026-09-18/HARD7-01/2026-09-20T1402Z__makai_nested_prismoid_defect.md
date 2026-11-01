Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Source metric `d_Makai: 2 -> 2` (**NO MOVEMENT**). Methods: **B3 / B15 / B30**.

# HARD7-01 RECOVERY1 — a quantitative nested-difference-body theorem for triangular prismoids

**Status:** `PARTIAL / SOURCE OPEN / CLAIMED / RECOVERY1`.

This run executes the recovery selected in the preceding STUCK1 report: port the stability/defect philosophy behind the planar Eggleston theorem into the exact three-dimensional prismoid formula. The source-wide metric does not move, so this is not closure. It does, however, prove a stronger quantitative inequality on a genuinely non-homothetic family and shrinks the first six-vertex obstruction to the crossing/non-nested case.

## 1. Continuity, ownership, exclusions, and required reads

I resumed the existing exclusive canonical claim

`operations/claims/MAKAI-POLAR-DIFFERENCE-BODY.md`

owned by `HARD7-01`. I did not restart admission, mint a bypass alias, or overwrite another owner's claim.

At run start I reread/reconciled:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the current Makai claim;
- newest own checkpoint `runs/hard7_2026-09-18/HARD7-01/2026-09-20T1303Z__makai_stuck1_projection_maximin.md`;
- the newest surfaced neighboring HARD7 Gaussian/probability report, HARD7-05's integrated-fBM persistence update, which remains a distinct source target;
- repository/intake aliases for Makai, polar difference body, non-symmetric difference-body Mahler, and the constants `3/2` and `2/3`.

Repository search still surfaces the Makai claim/reports only under HARD7-01; no competing owner or posted equivalent was found. `POSTED.md` and the settled campaign index do not list the unrestricted Makai source statement as settled or posted. A bounded current-status search on 20 September 2026 again found Aliev's three-dimensional `2/3` theorem only under tetrahedral symmetry, not for arbitrary convex bodies. These are bounded checks, not a worldwide novelty certificate.

## 2. Runtime/model capability honesty

The exposed automation interface still has prompt/title, schedule or relative start, timing mode, and enabled-state controls, but no model selector, no reasoning-effort selector, and no authenticated guaranteed execution duration. Therefore `GPT-6 / maximum` remains prompt text only; this report records the actual model identity available to this run as GPT-5.6 Sol and the reasoning level as `UNVERIFIED`.

Changing this would require the product/runtime to expose authenticated model/reasoning controls (or an authorized backend/task context that does). The historical P26 message `You cannot modify this task` was a permissions/context restriction; the current root ledger records a later successful P26 update from a different authorized context. The compliant workaround is therefore an authorized account/workspace task interface or platform support, not a bypass or duplicate schedule. This run did not create, modify, disable, re-enable, or probe any other schedule.

## 3. Frozen source statement and metric

The controlling external statement remains Makai Jr.'s conjecture as recorded in Arkadiy Aliev, *Mahler-type volume inequality for convex bodies with tetrahedral symmetry*, arXiv:2511.14991, Conjecture 1.3:

\[
\boxed{
 |K|\,|(K-K)^\circ|\ge \frac{n+1}{n!}
 \qquad(K\subset\mathbb R^n\text{ convex}),
}
\tag{M}
\]

with equality conjectured only for simplices.

The frozen source metric is

`d_Makai = largest d for which (M) is proved for every convex body in R^d`.

The incoming and outgoing values are

\[
\boxed{d_{\rm Makai}:2\longrightarrow 2.}
\]

Thus this run is **NO MOVEMENT** at source level. In dimension three the full obligation is still

\[
\inf_{K\subset\mathbb R^3\ \mathrm{convex}}
|K|\,|(K-K)^\circ|\stackrel{?}{\ge}\frac23.
\tag{3.1}
\]

## 4. Recovery idea: replace abstract Banach--Mazur surplus by an exact nesting defect

The STUCK1 report showed that a bare one-projection use of Eggleston reduces to an independent open Busemann--Petty maximin problem. It therefore selected a quantitative defect route rather than another constant-only estimate.

The first clean frontier was the six-vertex triangular prismoid

\[
K=\operatorname{conv}(A\times\{0\},C\times\{1\}),
\qquad A,C\subset\mathbb R^2\text{ triangles},
\tag{4.1}
\]

with non-homothetic bases.

The 2013 Böröczky--Makai--Meyer--Reisner stability theorem suggests that one should retain a geometric defect rather than discard all information after the sharp planar constant. In the prismoid setting there is an even more direct defect available: the relative inclusion scale of the two planar difference bodies.

For a triangle `T` and an arbitrary planar convex body `C`, put

\[
B:=T-T,\qquad E:=C-C,
\tag{4.2}
\]

and, whenever `E\subset B`, define

\[
\boxed{
\alpha:=\inf\{\lambda>0:E\subset \lambda B\}\in[0,1].
}
\tag{4.3}
\]

The point of this run is that `alpha` simultaneously controls the primal mixed-area term and the dual support-function term with opposite signs. That produces an explicit positive surplus over `2/3` for every `0<alpha<1`.

## 5. New theorem

### Theorem — nested-difference-body triangular prismoids

Let `T\subset\mathbb R^2` be a nondegenerate triangle and `C\subset\mathbb R^2` a compact convex set such that

\[
C-C\subset T-T.
\tag{5.1}
\]

Let `alpha` be as in (4.3), and set

\[
K:=\operatorname{conv}(T\times\{0\},C\times\{1\})\subset\mathbb R^3.
\tag{5.2}
\]

Then

\[
\boxed{
|K|\,|(K-K)^\circ|
\ge
\frac{(1+\alpha)(2-\alpha)}{3}
=
\frac{2+\alpha-\alpha^2}{3}
\ge \frac23.
}
\tag{5.3}
\]

In particular, Makai's three-dimensional bound holds for this entire family. The lower bound in (5.3) is strictly larger than `2/3` whenever `0<alpha<1`.

### Corollary — comparable triangular bases

If both `A` and `C` in (4.1) are triangles and their difference bodies are comparable by inclusion,

\[
A-A\subset C-C
\qquad\text{or}\qquad
C-C\subset A-A,
\tag{5.4}
\]

then

\[
|K|\,|(K-K)^\circ|\ge\frac23.
\tag{5.5}
\]

Thus, among the first genuinely non-homothetic six-vertex triangular prismoids, the remaining case is the **crossing/non-nested** configuration in which neither difference body contains the other.

## 6. Proof

The proof is analytic and complete on the page; no finite exhaustive claim is being made.

### 6.1 Affine normalization and the inclusion defect

The product `|K|||(K-K)^\circ|` is invariant under invertible linear maps of `\mathbb R^3`: volume picks up `|det L|` and polar volume picks up its reciprocal. Likewise the inclusion ratio `alpha` is unchanged if the same invertible planar map is applied to `T` and `C`.

We may therefore normalize

\[
T=\operatorname{conv}\{0,e_1,e_2\},
\qquad |T|=\frac12.
\tag{6.1}
\]

Then

\[
B=T-T
=\operatorname{conv}\{\pm e_1,\pm e_2,\pm(e_1-e_2)\}
\tag{6.2}
\]

and its exact half-space representation is

\[
B=\{x\in\mathbb R^2:
|x_1|\le1,
|x_2|\le1,
|x_1+x_2|\le1\}.
\tag{6.3}
\]

Because `E=C-C` is centrally symmetric, (6.3) gives

\[
\boxed{
\alpha=
\max\{h_E(e_1),h_E(e_2),h_E(e_1+e_2)\}
=
\max\{w_C(e_1),w_C(e_2),w_C(e_1+e_2)\},
}
\tag{6.4}
\]

where

\[
w_C(u):=h_C(u)+h_C(-u).
\tag{6.5}
\]

### 6.2 B30: the three facet directions glue into the mixed area

Let `V(T,C)` denote the standard planar mixed area, so

\[
|T+tC|=|T|+2tV(T,C)+t^2|C|.
\tag{6.6}
\]

For the normalized triangle, the three outward edge normals and edge lengths give the exact support formula

\[
2V(T,C)
=h_C(-e_2)+h_C(e_1+e_2)+h_C(-e_1).
\tag{6.7}
\]

Denote the right-hand side by `S`. Support-function subadditivity yields

\[
h_C(e_1)\le h_C(e_1+e_2)+h_C(-e_2),
\]

hence

\[
w_C(e_1)\le S.
\tag{6.8}
\]

Likewise,

\[
h_C(e_2)\le h_C(e_1+e_2)+h_C(-e_1)
\]

gives

\[
w_C(e_2)\le S,
\tag{6.9}
\]

and

\[
h_C(-e_1-e_2)\le h_C(-e_1)+h_C(-e_2)
\]

gives

\[
w_C(e_1+e_2)\le S.
\tag{6.10}
\]

Combining (6.4) and (6.7)--(6.10),

\[
\alpha\le 2V(T,C).
\tag{6.11}
\]

Since `|T|=1/2`, this is exactly

\[
\boxed{V(T,C)\ge \alpha |T|.}
\tag{6.12}
\]

By the affine-invariance argument above, (6.12) holds in the unnormalized coordinates as well.

### 6.3 Primal three-dimensional volume

The exact prismoid formula proved earlier on this track is

\[
|K|
=\frac{|T|+V(T,C)+|C|}{3}.
\tag{6.13}
\]

Using `|C|\ge0` and (6.12),

\[
\boxed{
|K|\ge \frac{|T|(1+\alpha)}{3}.
}
\tag{6.14}
\]

### 6.4 Dual volume and the same defect with the opposite sign

The exact dual fibre formula from the earlier prismoid run is

\[
|(K-K)^\circ|
=
\int_{B^\circ\cap E^\circ}
\bigl(2-h_B(y)-h_E(y)\bigr)\,dy.
\tag{6.15}
\]

Since `E\subset B`, polarity reverses inclusion:

\[
E^\circ\supset B^\circ,
\tag{6.16}
\]

so the integration domain in (6.15) is `B^\circ`. More strongly, by definition of `alpha`,

\[
E\subset \alpha B
\quad\Longrightarrow\quad
h_E(y)\le \alpha h_B(y)
\qquad\text{for every }y.
\tag{6.17}
\]

Therefore

\[
|(K-K)^\circ|
\ge
\int_{B^\circ}
\bigl(2-(1+\alpha)h_B(y)\bigr)\,dy.
\tag{6.18}
\]

Because

\[
B^\circ=\{y:h_B(y)\le1\},
\]

the sublevel sets of `h_B` are `tB^\circ`. In dimension two, layer-cake/radial integration gives

\[
\int_{B^\circ} h_B(y)\,dy
=\frac23|B^\circ|.
\tag{6.19}
\]

Hence

\[
\boxed{
|(K-K)^\circ|
\ge
\frac{2(2-\alpha)}{3}|B^\circ|.
}
\tag{6.20}
\]

### 6.5 Multiply and use the sharp triangle identity

For a triangle, Eggleston's planar inequality is attained with equality:

\[
|T|\,|(T-T)^\circ|=rac32.
\tag{6.21}
\]

Since `B=T-T`,

\[
|B^\circ|=\frac{3}{2|T|}.
\tag{6.22}
\]

Multiplying (6.14), (6.20), and (6.22),

\[
\begin{aligned}
|K|\,|(K-K)^\circ|
&\ge
\frac{|T|(1+\alpha)}3
\cdot
\frac{2(2-\alpha)}3
\cdot
\frac{3}{2|T|}\\
&=
\frac{(1+\alpha)(2-\alpha)}3.
\end{aligned}
\tag{6.23}
\]

Finally, for `0\le\alpha\le1`,

\[
(1+\alpha)(2-\alpha)
=2+\alpha-\alpha^2
=2+\alpha(1-\alpha)
\ge2.
\tag{6.24}
\]

This proves (5.3). `QED`.

## 7. Why this is a real recovery rather than another certificate

The source metric remains `2`, so this is not represented as source-level movement. The mathematical obligation nevertheless narrows in a way the preceding three restricted results did not:

- pyramids were the one-base-degenerate case;
- positive-homothety frusta controlled a one-parameter same-shape family;
- affine circuits controlled every polytope with at most five vertices;
- this theorem controls a genuinely non-homothetic six-vertex region by a quantitative defect parameter and, for triangular bases, leaves only the non-nested crossing geometry.

The new structural fact is the two-sided use of the same parameter `alpha`:

\[
V(T,C)\ge\alpha|T|
\qquad\text{while}\qquad
h_{C-C}\le\alpha h_{T-T}.
\tag{7.1}
\]

The first inequality raises primal volume and the second lowers the dual penalty. That is the defect coupling the STUCK1 report was seeking, but here it is obtained directly from the three facet directions of a triangle rather than from an abstract Banach--Mazur stability constant.

## 8. Section-B outcomes

### B3 — PROVE SOMETHING STRONGER

Instead of proving only the endpoint `2/3`, the run proved the explicit defect bound

\[
|K|\,|(K-K)^\circ|
\ge\frac23+\frac{\alpha(1-\alpha)}3.
\tag{8.1}
\]

**Outcome:** successful. The surplus is quantitative and positive throughout `0<alpha<1`.

### B15 — BREAK THE SYMMETRY ON PURPOSE

The second base `C` is arbitrary: it need not be a triangle, centrally symmetric, homothetic to `T`, or related by tetrahedral symmetry. Only the inclusion of difference bodies is used.

**Outcome:** successful. The proof leaves the symmetry classes already handled in previous runs and certifies a substantially larger asymmetric region.

### B30 — ONE SCALE / ONE DIRECTION AT A TIME

For a triangle difference body, inclusion is controlled by only three facet-normal widths. Each individual width is bounded by the same mixed-area support sum, and those three one-direction estimates glue into (6.12).

**Outcome:** successful. The exact point where this ceases to work is now visible: when the difference bodies cross, neither polar domain contains the other and the common scalar `alpha` moves beyond the interval where (6.24) closes.

## 9. Remaining obstruction

For two arbitrary triangular bases `A,C`, the first unresolved six-vertex family is now

\[
A-A\not\subset C-C,
\qquad
C-C\not\subset A-A.
\tag{9.1}
\]

In this crossing case the exact product is still

\[
\frac{|A|+V(A,C)+|C|}{3}
\int_{(A-A)^\circ\cap(C-C)^\circ}
\bigl(2-h_{A-A}-h_{C-C}\bigr),
\tag{9.2}
\]

but the dual domain is a strict common refinement/intersection of two hexagonal polar fans. The nested proof fails for two precise reasons:

1. neither polar domain contains the other, so the integral cannot be taken over one full `B^\circ`;
2. the smallest scalar containing one difference body in the other is `>1`, so the polynomial defect `2+alpha-alpha^2` no longer has the required sign.

This is now the simplest special case still unproved on the Makai track.

## 10. Literature/current-status record

The current source/prior-art picture used this run remains:

- Arkadiy Aliev, arXiv:2511.14991 (2025), Conjecture 1.3: general Makai statement; planar `3/2`; three-dimensional `2/3` proved under tetrahedral symmetry only.
- K. Böröczky, E. Makai Jr., M. Meyer, S. Reisner, *On the volume product of planar polar convex bodies—Lower estimates with stability*, Studia Sci. Math. Hungar. 50 (2013), 159--198, DOI `10.1556/SScMath.50.2013.2.1235`: stability around the planar triangle equality case, motivating the defect-first recovery.
- H. Martini, Z. Mustafaev, S. M. Zarbaliev, *Some new minimax inequalities for centered convex bodies*, Aequationes Math. 99 (2025), 1143--1152, DOI `10.1007/s00010-024-01109-6`: the same-body section-width maximin obstruction isolated in STUCK1 remains open.

Fresh bounded searches on 20 September 2026 for `Makai prismoid triangles difference body`, `nested difference bodies Makai`, `polar difference body triangular prism`, and the canonical conjecture aliases found no source matching theorem (5.3) or a full unrestricted three-dimensional solution. This is negative search evidence only. Priority/novelty remains **UNVERIFIED** pending dedicated prior-art review and independent audit.

## 11. Verification scope

No finite enumeration or numerical universal claim is made, so a checker would add bookkeeping without testing the central idea. The theorem-sized claim is instead supplied with a complete analytic proof above. Existing exact prismoid formulas are reused from the prior HARD7-01 checkpoint rather than re-certified merely to show activity.

No Gmail, Drive, public posting, shared-ledger rewrite, other-track edit, schedule mutation, or audit request was performed.

## 12. Next route

This run used B3/B15/B30, which differs from the preceding B12/B21/B22 triple. For the crossing case, the next active triple will be methods not yet used on the Makai target:

- **B8 — DISCRETIZE:** classify the finite common-refinement types of the two hexagonal support fans and reduce each crossing type to explicit parameter inequalities;
- **B13 — FIND WHAT ONLY INCREASES:** move one crossing support line toward first contact and test whether the Makai product or a sharp lower surrogate is monotone until reaching the nested boundary already solved;
- **B27 — SWAP THE QUANTIFIERS:** instead of controlling every relative orientation uniformly, prove that every crossing pair admits one of finitely many dominant fan sectors/directions carrying enough primal-dual surplus.

This is still the first recovery cycle after STUCK1. Because the source metric did not move, no source closure is claimed; because the concrete six-vertex obligation has genuinely narrowed, this report does not fabricate STUCK2 merely from the unchanged global dimension metric.

## Ledger delta

```text
track: HARD7-01
source_target: MAKAI-POLAR-DIFFERENCE-BODY
owner: HARD7-01
status: PARTIAL / SOURCE OPEN / CLAIMED / RECOVERY1
metric: d_Makai
before: 2
after: 2
movement: NO MOVEMENT
methods_this_run: B3 / B15 / B30
new_theorem_claim: nested-difference-body triangular-prismoid defect theorem
quantitative_bound: |K||(K-K)^circ| >= (1+alpha)(2-alpha)/3
special_case_advanced: all triangular-prismoids with comparable difference bodies
remaining_first_case: two triangular bases with crossing/non-nested difference bodies
next_methods: B8 / B13 / B27
closure: NO
```
