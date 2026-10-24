Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Old source metric `d_sym: 3 -> 3` (**NO MOVEMENT; mandatory handoff after Section-I exhaustion**). Fresh admitted source metric `d_Makai: 2 -> 2` (**NO MOVEMENT**). Methods: terminal Mahler recovery **B8/B15/B27**; fresh Makai target **B2/B5/B11**.

# HARD7-01 — terminal Mahler recovery proves all-planar DF2; mandatory rotation to Makai Jr.; Makai is proved for every three-dimensional pyramid

**Status:** old target `PARTIAL / SOURCE OPEN / RELEASED`; fresh target `PARTIAL / SOURCE OPEN / CLAIMED`.

This run does two things required by the lifecycle. First, it completes the second and final recovery route on the released symmetric Mahler target with a genuine all-parameter theorem, but the source-level dimension does not move, so the target is handed off rather than given a forbidden third stuck-recovery cycle. Second, it admits a genuinely distinct externally posed hard problem in the same lane—Makai Jr.'s polar difference-body conjecture—and immediately proves the full conjectured three-dimensional bound for **every pyramid**, not by sampling but by an exact dimension reduction to Eggleston's planar theorem.

Neither result proves a full new source dimension. In particular, symmetric Mahler remains open in dimension four and Makai Jr. remains open for arbitrary three-dimensional convex bodies.

## 1. Required continuity, ownership, and evidence consumed

At the beginning of the invocation I reread/reconciled the controlling material:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the then-current canonical Mahler claim;
- the newest HARD7-01 checkpoint `runs/hard7_2026-09-18/HARD7-01/2026-09-20T1015Z__stuck2_constant_width_radon_route.md`;
- current neighbouring Gaussian/probability material surfaced by repository search;
- repository/intake aliases for both the old Mahler target and the fresh Makai target.

I did not claim a byte-for-byte reread of every large intake JSONL. I did perform target/alias ownership searches across the repository before the fresh claim. They found the Makai name only in this track's previous Mahler-route discussion, not in a canonical Makai claim or another active owner's work.

The old canonical claim was changed to

`UNASSIGNED AFTER HARD7-01 HANDOFF / RELEASED BY HARD7-01 AFTER SECTION-I EXHAUSTION`

at commit `8456dd3899cb5cc4e456da541916e801027a21e3`.

The fresh canonical claim was created without overwriting any existing owner:

`operations/claims/MAKAI-POLAR-DIFFERENCE-BODY.md`

at commit `daf741b67147d2608fa5ec84773eceb615dbb8fc`.

The terminal Mahler route was written before its checker at

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T1105Z__mass_radon_sandwich_idea.md`

(commit `d57995501dab5bf3dd1cc6ef7c7dfccee4cda58e`). The fresh Makai route was likewise written before its checker at

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T1132Z__makai_pyramid_idea_before_code.md`

(commit `9852df425f4bb8e2d192fc8de5281456acd0e728`).

## 2. Terminal symmetric-Mahler recovery: the all-planar DF2 inequality

The STUCK2 report left the exact pyramidal blocker

\[
 (|K-K|+2|K|)|(K-K)^\circ|\ge 12,
 \qquad K\subset\mathbb R^2,
\tag{DF2}
\]

initially only for pentagons. It proposed strengthening to all planar bodies through the central symmetral

\[
M:=\frac{K-K}{2}
\]

and the largest-area affine-regular hexagon `H` inscribed in `M`.

The missing candidate one-body inequality was

\[
\boxed{(3|M|-|H|)|M^\circ|\ge18.}
\tag{C}
\]

The STUCK2 note proved `(C)` only on the Radon locus. The new point of this run is that a direct monotonicity theorem for the nonsmooth functional is unnecessary: two different estimates already present in Z. Lángi, *On a normed version of a Rogers--Shephard type problem*, Israel J. Math. 212 (2016), 203--217, arXiv:1308.2500, sandwich the non-Radon defect tightly enough to prove `(C)` globally.

### 2.1 Published ingredients, with constants frozen

Let `M=-M` be a planar convex disk. Let `P` be a maximum-area parallelogram inscribed in `M`, and let `H` be a maximum-area affine-regular hexagon inscribed in `M`.

Affine-normalize so that

\[
|P|=2.
\tag{2.1}
\]

Write

\[
A:=|M|,
\qquad
B:=|M^\circ|,
\qquad
h:=|H|.
\]

Because `P subset M`,

\[
A\ge2.
\tag{2.2}
\]

**Ingredient I: Chakerian fixed-symmetral minimization.** Lángi records Chakerian's theorem in exactly the needed normalization: among planar bodies whose relative norm has unit disk `M`, a minimum-area body of constant width two is a Reuleaux triangle, with area

\[
|K_0|=2A-\frac43h.
\tag{2.3}
\]

**Ingredient II: Gromov mass lower bound.** Lángi's Theorem 2.3 states

\[
 c_{tr}^{m}(K)\ge6,
\tag{2.4}
\]

and his formula (10) is

\[
 c_{tr}^{m}(K)=\frac{2(|K|+2|P|)}{|P|}
 =4+\frac{2|K|}{|P|}.
\tag{2.5}
\]

Apply this to the Chakerian minimizer `K_0`. With `|P|=2`, (2.3)--(2.5) yield

\[
2A-\frac43h\ge2,
\]

or equivalently

\[
\boxed{h\le\frac32(A-1).}
\tag{2.6}
\]

This is exactly the hexagon/area coupling that the preceding Mahler attempts lacked.

**Ingredient III: Radon completions in the Holmes--Thompson proof.** In the same normalization Lángi writes the polar area as

\[
B=A+2x_1+2x_2,
\qquad 0\le x_1,x_2\le\frac12,
\tag{2.7}
\]

and constructs two Radon disks `M_1,M_2` containing `M`, each still having maximum inscribed parallelogram area `2`, with respective areas

\[
|M_1|=A+2x_2,
\qquad
|M_2|=A+2x_1.
\tag{2.8}
\]

For a Radon unit disk whose maximum parallelogram has area `2`, the Gromov-mass area is just Euclidean area in this normalization; the sharp bound cited and used by Lángi is

\[
|M_i|\ge3.
\tag{2.9}
\]

Thus, whenever `2<=A<=3`, (2.8)--(2.9) imply

\[
x_1,x_2\ge\frac{3-A}{2}.
\]

Substitution into (2.7) gives

\[
\boxed{B\ge6-A,\qquad 2\le A\le3.}
\tag{2.10}
\]

Lángi's same normalization also gives the inclusion of `M` in the quarter-turn of `M^circ`; hence

\[
\boxed{B\ge A}
\tag{2.11}
\]

for every `A` in the normalization.

### 2.2 Proof of the one-body inequality `(C)`

From (2.6),

\[
3A-h\ge \frac32(A+1).
\tag{2.12}
\]

There are two ranges.

If `2<=A<=3`, use (2.10):

\[
\begin{aligned}
(3A-h)B
&\ge \frac32(A+1)(6-A)\\
&=18+\frac32(A-2)(3-A)\\
&\ge18.
\end{aligned}
\tag{2.13}
\]

If `A>=3`, use (2.11):

\[
\begin{aligned}
(3A-h)B
&\ge\frac32 A(A+1)\\
&=18+\frac32(A-3)(A+4)\\
&\ge18.
\end{aligned}
\tag{2.14}
\]

This proves `(C)` for **every** origin-symmetric planar convex disk `M`.

### 2.3 `(C)` implies `(DF2)` for every planar convex body

Now let `K` be an arbitrary planar convex body and set

\[
M=\frac{K-K}{2}.
\]

The body `K` has constant width two in its relative norm with unit disk `M`. By Chakerian,

\[
|K|\ge 2|M|-\frac43|H|.
\tag{2.15}
\]

Since `K-K=2M`, in dimension two

\[
|K-K|=4|M|,
\qquad
|(K-K)^\circ|=\frac14|M^\circ|.
\tag{2.16}
\]

Consequently

\[
\begin{aligned}
(|K-K|+2|K|)|(K-K)^\circ|
&=\left(|M|+\frac{|K|}{2}\right)|M^\circ|\\
&\ge \frac23(3|M|-|H|)|M^\circ|\\
&\ge12
\end{aligned}
\tag{2.17}
\]

by `(C)`. Hence:

> **Theorem A (terminal Mahler-route theorem).** For every planar convex body `K`,
> \[
> \boxed{(|K-K|+2|K|)|(K-K)^\circ|\ge12.}
> \]

This is an all-parameter theorem, not a finite computation. It closes every pyramidal case of the three-dimensional `DF6` obstruction from the previous four-dimensional local-minimizer program. It does **not** prove `DF6` for arbitrary three-dimensional bodies and therefore does not prove four-dimensional symmetric Mahler.

The exact algebra self-check is

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T1117Z__mass_radon_sandwich_check.py`

with archived output

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T1117Z__mass_radon_sandwich_check.out`.

The output ends

`ALL_EXACT_CHECKS_PASS = True`

and verifies the two polynomial factorizations and exact equality constants at a parallelogram and a triangle. The checker is a self-check of the finite algebra/endpoints; the theorem itself is the written argument above.

### 2.4 Terminal Mahler method outcomes

- **B8 — discretize:** successful. Instead of differentiating a continuum Radonization, the non-Radon defect is represented by exactly two scalars `x_1,x_2` from Lángi's construction.
- **B15 — break symmetry:** successful. Keeping the non-Radon defect rather than assuming a Radon endpoint produces the sharper envelope `B>=6-A` on `2<=A<=3`.
- **B27 — swap quantifiers:** successful. The proof does not need a deformation along which every maximizing hexagon behaves monotonically. It uses existential Radon completions plus a universal mass inequality and then eliminates the auxiliary variables.

## 3. Mandatory Section-I handoff of symmetric Mahler

The old source metric is

\[
d_{\rm sym}=3\longrightarrow3.
\]

Both permitted stuck-recovery cycles on this hard target had already been consumed. The run therefore cannot use Theorem A as an excuse to begin a third recovery cycle on the same source problem. The canonical claim has been released, with the exact remaining state preserved:

- full symmetric Mahler remains open in `n>=4`;
- Theorem A closes all planar `DF2` and hence all pyramidal `DF6` cases;
- the unresolved local-minimizer route still needs the genuinely three-dimensional non-pyramidal part of `DF6` or a completely different four-dimensional mechanism.

This is a handoff, not a closure claim.

## 4. Fresh hard target admitted: Makai Jr. polar difference-body conjecture

The new target is Arkadiy Aliev, *Mahler-type volume inequality for convex bodies with tetrahedral symmetry*, arXiv:2511.14991v1 (19 November 2025), **Conjecture 1.3 (Makai Jr [20])**. The exact displayed statement in that primary source is:

\[
\boxed{
 |K|\,|(K-K)^\circ|\ge\frac{n+1}{n!}
 \quad\text{for every convex body }K\subset\mathbb R^n,
}
\tag{M}
\]

with equality if and only if `K` is a simplex.

Aliev attributes the conjecture to E. Makai Jr., *On the thinnest non-separable lattice of convex bodies*, Studia Sci. Math. Hungar. 13 (1978), 19--27. Makai's own author page exposes the original PDF, but that link returned HTTP 403 to this runtime. I therefore quote the exact displayed quantifiers from Aliev's primary 2025 Conjecture 1.3 rather than inventing text from an inaccessible 1978 scan.

Fresh current-status checks on 20 September 2026 found:

1. Aliev records Eggleston's full planar theorem, giving the sharp `3/2` bound and triangle equality.
2. Aliev proves the three-dimensional `2/3` bound only for bodies with tetrahedral symmetry and explicitly states that the general bound available from symmetric Mahler plus Rogers--Shephard is `8/15`, below the conjectured `2/3`.
3. Fresh searches for `Makai Jr conjecture difference body polar 2026`, `Makai Jr convex body 3D 2/3 2026`, and `Makai conjecture convex difference body 2026` found no full three-dimensional resolution. A current MathDB entry also labels the exact conjecture open. This is bounded negative evidence, not bibliographic omniscience.
4. Repository searches for `Makai difference body polar`, `Conjecture 1.3 Makai`, `polar difference body conjecture`, and aliases found no pre-existing canonical claim/owner. The hits were this track's old Mahler notes mentioning Makai as neighboring literature.
5. Targeted searches for `Makai pyramid convex body difference body polar`, `Makai Jr pyramid tetrahedron difference body inequality`, and `pyramid polar difference-body volume product` found no published all-pyramids theorem. Priority of Theorem B below remains **UNVERIFIED** pending a broader dedicated search/audit.

The frozen source metric is

`d_Makai = largest d such that (M) is established for every convex body in R^d`.

The verified admission baseline is

\[
d_{\rm Makai}=2.
\]

A theorem for pyramids does not move this source metric.

## 5. B2/B5/B11: Makai's conjecture is true for every three-dimensional pyramid

### Theorem B

Let `L` be any nondegenerate three-dimensional pyramid. Then

\[
\boxed{|L|\,|(L-L)^\circ|\ge\frac23.}
\tag{5.1}
\]

Within the pyramid family, equality holds if and only if `L` is a tetrahedron.

### Proof

The functional in (5.1) is invariant under invertible affine linear changes and under translation of `L`. An affine shear parallel to the base lets us place the apex vertically above any chosen point of the base. After a translation and vertical scaling, we may therefore write

\[
0\in B\subset\mathbb R^2,
\qquad
L=\operatorname{conv}(B\times\{0\},(0,1)),
\tag{5.2}
\]

for an arbitrary planar convex body `B`.

Set

\[
A:=|B|,
\qquad
E:=B-B.
\]

The pyramid volume is

\[
|L|=\frac A3.
\tag{5.3}
\]

It remains to compute the polar volume of the difference body exactly. Let a dual point be `(u,s) in R^2 x R`. The support function of the pyramid is

\[
h_L(u,s)=\max\{h_B(u),s\}.
\tag{5.4}
\]

Therefore, with `D=L-L`,

\[
h_D(u,s)=\max\{h_B(u),s\}+\max\{h_B(-u),-s\}.
\tag{5.5}
\]

Fix `u` and put

\[
a=h_B(u),
\qquad
b=h_B(-u).
\]

Because `0 in B`, `a,b>=0`. The condition `(u,s) in D^circ` is `h_D(u,s)<=1`. From (5.5), such an `s` exists if and only if

\[
a+b=h_E(u)\le1,
\tag{5.6}
\]

and whenever (5.6) holds, the full admissible interval is

\[
a-1\le s\le1-b,
\tag{5.7}
\]

of length

\[
2-h_E(u).
\tag{5.8}
\]

Hence

\[
|D^\circ|
=\int_{E^\circ}(2-h_E(u))\,du.
\tag{5.9}
\]

On `E^circ`, the support function `h_E` is the gauge of `E^circ`: in dimension two,

\[
|\{u\in E^\circ:h_E(u)\le t\}|=t^2|E^\circ|,
\qquad 0\le t\le1.
\tag{5.10}
\]

Thus

\[
\int_{E^\circ}h_E(u)\,du
=\frac23|E^\circ|,
\tag{5.11}
\]

and (5.9) becomes

\[
\boxed{|(L-L)^\circ|=\frac43|(B-B)^\circ|.}
\tag{5.12}
\]

Combining (5.3) and (5.12),

\[
|L|\,|(L-L)^\circ|
=\frac49|B|\,|(B-B)^\circ|.
\tag{5.13}
\]

Now apply Eggleston's sharp planar theorem,

\[
|B|\,|(B-B)^\circ|\ge\frac32,
\tag{5.14}
\]

with equality if and only if `B` is a triangle. Equations (5.13)--(5.14) give

\[
|L|\,|(L-L)^\circ|
\ge\frac49\cdot\frac32
=\frac23.
\]

Equality occurs exactly when the base is a triangle, which is exactly the tetrahedral case among nondegenerate pyramids. QED.

### 5.1 Why this is a genuine counterexample-oriented first run

**B2 — ATTACK THE NEGATION FIRST.** A pyramidal counterexample to Makai in dimension three would, by (5.13), produce a planar body with

\[
|B|\,|(B-B)^\circ|<\frac32,
\]

contradicting Eggleston. Thus the entire pyramid family is eliminated as a counterexample source, exactly rather than numerically.

**B5 — ADD A PARAMETER AND DIFFERENTIATE/DEFORM.** Apex height and horizontal apex location are added geometric parameters, but affine scaling and a shear remove them completely. This shows that the Makai functional on a pyramid is governed only by the affine class of the base through the single planar product in (5.13). There is no hidden apex parameter left to optimize.

**B11 — DUALIZE.** The decisive step is not a primal volume estimate. It is the exact fiber description of `(L-L)^circ`, yielding the factor `4/3` in (5.12). After dualization the three-dimensional conjectured constant becomes exactly Eggleston's planar constant.

## 6. Exact self-check for the fresh theorem

The exact rational checker is

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T1140Z__makai_pyramid_check.py`

with output

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T1140Z__makai_pyramid_check.out`.

It verifies the exact reduction constant `4/9`, the tetrahedral equality endpoint `2/3`, and a non-extremal square-base pyramid value `8/9`. The archived output ends

`ALL_EXACT_CHECKS_PASS = True`.

The checker is labelled a finite self-check. The universal pyramid theorem rests on the proof in Section 5, not on two sampled bases.

## 7. Source metrics and honest labels

Old released target:

```text
source_target: MAHLER-SYMMETRIC-VOLUME-PRODUCT
status: PARTIAL / SOURCE OPEN / RELEASED
metric: d_sym
before: 3
after: 3
movement: NO
new_restricted_theorem: DF2 for every planar convex body
section_I: EXHAUSTED -> HANDOFF
```

Fresh current target:

```text
source_target: MAKAI-POLAR-DIFFERENCE-BODY
owner: HARD7-01
status: PARTIAL / SOURCE OPEN / CLAIMED
metric: d_Makai
before: 2
after: 2
movement: NO
new_restricted_theorem: full conjectured 3D bound for every pyramid
methods: [B2, B5, B11]
closure: false
priority: UNVERIFIED
```

No numerical example is represented as the full three-dimensional conjecture. No old Mahler local-minimizer theorem is represented as moving `d_sym`. No claim is labelled PROVED or CLOSED at source level.

## 8. Runtime / scheduler capability honesty

The automation interface exposed to this runtime still provides prompt/title/schedule/enabled controls but **no model selector, no reasoning-effort selector, no authenticated runtime-model telemetry field, and no guaranteed execution-duration field**. Therefore `GPT-6 / maximum` remains a prompt request only. Actual conversation runtime is **GPT-5.6 Sol**; reasoning level is **UNVERIFIED**.

The repository records the historical P26 scheduler error `You cannot modify this task`; later authorized context also records successful P26 updates. The valid remedy for a task that genuinely refuses modification remains to use the authorized owning account/workspace/interface or platform support. It is not permission to bypass ownership or create a duplicate schedule. No schedule was modified or created in this run.

## 9. Next checkpoint

The fresh target is not stuck: this is its admission run and it produced a new all-parameter class theorem. The next invocation should resume `MAKAI-POLAR-DIFFERENCE-BODY` and should not return to symmetric Mahler unless a future explicit reassignment occurs.

A natural next source-facing obstruction is the smallest three-dimensional non-pyramidal polytope class. The first task should again be counterexample-oriented: identify the minimal combinatorial class not covered by Theorem B, derive an exact polar decomposition, and ask whether each candidate violation would force a planar Eggleston violation or whether a genuinely three-dimensional defect term appears. A new Section-B triple must be used rather than repeating B2/B5/B11.