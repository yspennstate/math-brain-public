Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Source metric `d_Makai: 2 -> 2` (**NO MOVEMENT**). Methods: **B1 / B16 / B25**.

# HARD7-01 — Makai on every affine-circuit polytope via a cube-section concentration inequality

**Status:** `PARTIAL / SOURCE OPEN / CLAIMED`.

This bounded iteration resumes the exclusive Makai Jr. polar difference-body target from the newest checkpoint `runs/hard7_2026-09-18/HARD7-01/2026-09-20T1210Z__makai_prismoid_frustum.md`. The source-level dimension does not move: the full inequality for arbitrary three-dimensional convex bodies remains open. The substantive new result is dimension-free: the conjectured Makai constant holds for every full-dimensional convex polytope with exactly `n+2` vertices in affine-circuit position. In dimension three, combining this with the preceding all-pyramids theorem proves the conjectured `2/3` bound for **every convex polytope with at most five vertices**.

The new route was written before any checker at

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T1220Z__makai_circuit_cube_slice_idea_before_code.md`

creation commit `9cc58d51a70958f5066638cc88efa3949adcd5a2`, and was read back successfully before verification code was added.

## 1. Continuity, exclusions, ownership, and capability honesty

At run start I reread/reconciled the controlling `CONTROL.md`, the current new-methods policy and owner directive, campaign `INDEX.md`/`RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the canonical Makai claim, the newest own report, and neighboring Gaussian/HARD7 material. Repository/intake alias searches again found no competing owner or posted equivalent for the exact Makai target. The canonical claim remains

`operations/claims/MAKAI-POLAR-DIFFERENCE-BODY.md`

owned by `HARD7-01`; no claim was overwritten or reminted.

The exposed scheduling interface still has title/prompt/schedule/timing/enabled controls but no authenticated model selector, no reasoning-effort selector, and no guaranteed execution duration. Thus GPT-6/maximum remains a prompt request only. The earlier `You cannot modify this task` result for a P26 context is a permissions/context issue; the compliant remedy is an authorized account/workspace interface or platform support, never a repository workaround or duplicate task. This run did not create, modify, disable, re-enable, or probe another schedule.

## 2. Source target and frozen metric

The admitted source is Arkadiy Aliev, *Mahler-type volume inequality for convex bodies with tetrahedral symmetry*, arXiv:2511.14991 (2025), Conjecture 1.3, attributed there to Makai Jr.:

\[
\boxed{|K|\,|(K-K)^\circ|\ge \frac{n+1}{n!}}
\tag{M}
\]

for every convex body `K subset R^n`, with equality iff `K` is a simplex.

The frozen source metric is

`d_Makai = largest d for which (M) is established for every convex body in R^d`.

The verified incoming and outgoing values are

\[
\boxed{d_{\rm Makai}:2\longrightarrow2.}
\]

This is **NO MOVEMENT**. The theorem below is a genuine all-parameter restricted theorem, not a source-dimensional closure.

## 3. Current-literature / alias check, 20 September 2026

Fresh bounded searches used the combinations

- `Makai n+2 vertices convex difference body`;
- `Makai affine circuit convex body difference body`;
- `Makai conjecture polytope five vertices difference body`;
- `polar difference body affine circuit cube section`;
- the exact source title and arXiv identifier.

They again recovered Aliev's 2025 paper, whose three-dimensional theorem assumes tetrahedral symmetry, and older Makai/difference-body and cube-section literature, but no theorem matching the affine-circuit class below and no full three-dimensional resolution. This is bounded negative evidence only. **Priority/novelty of the restricted theorem remains UNVERIFIED** pending a dedicated literature audit. The argument below is therefore recorded as mathematical progress, not as a publication-priority certificate.

## 4. New-method work: B1 / B16 / B25

The previous run used B6/B18/B24, so this run uses a different triple.

- **B1 — change the category.** The polar difference-body functional for an `n+2`-point affine circuit is converted exactly into a central hyperplane-section density for an `(n+2)`-cube.
- **B16 — compute every smallest genuine case and stare at the sequence.** Exact five-vertex three-dimensional circuit examples expose the dependence only on the absolute affine-circuit coefficients and suggest the sharp universal density lower bound `1`.
- **B25 — count the same thing twice.** The cube section is evaluated once through the Jacobian of affine-function evaluations and once through the density of a weighted sum of independent uniforms. The two descriptions isolate a one-dimensional concentration lemma that can be proved completely.

All three moves succeed in producing a theorem-sized restricted result.

## 5. The affine-circuit reduction

### Theorem A — exact circuit identity

Let

\[
K=\operatorname{conv}(v_1,\ldots,v_{n+2})\subset\mathbb R^n
\]

be full-dimensional, and suppose the `n+2` points form an affine circuit. Thus the unique affine dependence has all coefficients nonzero. Normalize it as

\[
\sum_{i=1}^{n+2}c_i v_i=0,\qquad
\sum_{i=1}^{n+2}c_i=0,
\tag{5.1}
\]

with

\[
\sum_{c_i>0}c_i=-\sum_{c_i<0}c_i=1.
\tag{5.2}
\]

Put `D=K-K`, `m=n+2`, and

\[
S(c):=\mathcal H^{n+1}\bigl([0,1]^m\cap c^\perp\bigr).
\tag{5.3}
\]

Then

\[
\boxed{
|K|\,|D^\circ|=\frac{n+1}{n!}\,\frac{S(c)}{\|c\|_2}.
}
\tag{5.4}
\]

#### Proof

Let `A` be the `(n+2) x (n+1)` matrix whose `i`th row is `(v_i^T,1)`. It has rank `n+1`, and `c^T A=0`. The signed cofactor vector of `A` spans the same one-dimensional left kernel, so there is `lambda>0` such that

\[
|\det A_{\widehat i}|=\lambda |c_i|,
\tag{5.5}
\]

where `A_hat i` deletes row `i`.

By Cauchy--Binet,

\[
J:=\sqrt{\det(A^TA)}
 =\left(\sum_i |\det A_{\widehat i}|^2\right)^{1/2}
 =\lambda\|c\|_2.
\tag{5.6}
\]

We also need the volume of the circuit polytope. Let `P={i:c_i>0}`. The simplices

\[
\Delta_i=\operatorname{conv}\{v_j:j\ne i\},\qquad i\in P,
\]

triangulate `K`. Indeed, if `x=sum theta_i v_i`, `theta_i>=0`, `sum theta_i=1`, choose

\[
t=\min_{i\in P}\frac{\theta_i}{c_i}
\]

and replace `theta` by `theta-tc`; all coordinates stay nonnegative and at least one positive-side coordinate becomes zero, so `x` lies in some `Delta_i`. Interiors of distinct `Delta_i,Delta_k` cannot overlap: two interior barycentric representations differ by a scalar multiple of `c`, while the zero at `i` forces that scalar to have the opposite sign from the zero at `k`. Thus, using (5.5) and (5.2),

\[
|K|=\sum_{i\in P}|\Delta_i|
=\frac{\lambda}{n!}\sum_{i\in P}c_i
=\frac{\lambda}{n!}.
\tag{5.7}
\]

Now consider the linear map

\[
T:\mathbb R^n\times\mathbb R\to c^\perp,
\qquad
T(y,r)=(\langle y,v_i\rangle+r)_{i=1}^{m}.
\tag{5.8}
\]

Its matrix is `A`, hence its `(n+1)`-dimensional Jacobian is `J`. For fixed `y`, the condition `T(y,r) in [0,1]^m` is

\[
-\min_i\langle y,v_i\rangle\le r
\le1-\max_i\langle y,v_i\rangle.
\]

The interval has length

\[
1-\bigl(\max_i\langle y,v_i\rangle-
\min_i\langle y,v_i\rangle\bigr)
=1-h_D(y),
\tag{5.9}
\]

and is nonempty exactly when `h_D(y)<=1`, i.e. `y in D^circ`. Therefore

\[
S(c)=J\int_{D^\circ}(1-h_D(y))\,dy.
\tag{5.10}
\]

Because `h_D` is the Minkowski gauge of `D^circ`, the sublevel set `{h_D<=t}` is `tD^circ`; layer-cake gives

\[
\int_{D^\circ}(1-h_D(y))\,dy
=|D^\circ|\int_0^1 t^n\,dt
=\frac{|D^\circ|}{n+1}.
\tag{5.11}
\]

Substitute `J=lambda||c||_2` from (5.6) into (5.10), then eliminate `lambda` with (5.7). This is exactly (5.4). `QED`.

## 6. The cube section is a weighted-uniform density

Reflect every cube coordinate for which `c_i<0`: `x_i -> 1-x_i`. This is an isometry of the cube. With

\[
w_i:=|c_i|,
\]

normalization (5.2) becomes

\[
0<w_i\le1,\qquad \sum_i w_i=2,
\tag{6.1}
\]

and the hyperplane `c dot x=0` becomes

\[
\sum_i w_i x_i=1.
\tag{6.2}
\]

Let `U_i` be independent `Unif[0,1]` and `W=sum_i w_i U_i`. The coarea formula for the linear map `x -> w dot x` gives

\[
S(c)=\|w\|_2 f_W(1)=\|c\|_2 f_W(1).
\tag{6.3}
\]

Consequently (5.4) simplifies to the exact probability identity

\[
\boxed{
|K|\,|(K-K)^\circ|
=\frac{n+1}{n!}\,f_W(1),
\qquad
W=\sum_i w_iU_i,\quad
\sum_iw_i=2,\quad w_i\le1.
}
\tag{6.4}
\]

Thus the entire circuit case of Makai reduces to `f_W(1)>=1`.

## 7. One-dimensional concentration lemma

### Lemma B

Let `w_1,...,w_m` be positive numbers with

\[
0<w_i\le1,\qquad \sum_iw_i=2.
\]

If `U_i` are independent `Unif[0,1]`, then the density of `W=sum_iw_iU_i` at its mean is at least one:

\[
\boxed{f_W(1)\ge1.}
\tag{7.1}
\]

#### Proof by merging widths

Center the variables. Write `X_a` for the uniform law on `[-a/2,a/2]`. We first prove the following peakedness step: for `a,b>0`,

\[
X_a+X_b \quad\text{is more peaked about zero than}\quad X_{a+b}.
\tag{7.2}
\]

Assume `a>=b`. For `0<=r<=(a-b)/2`,

\[
\mathbb P(|X_a+X_b|\le r)=\frac{2r}{a}
\ge\frac{2r}{a+b}
=\mathbb P(|X_{a+b}|\le r).
\tag{7.3}
\]

For `(a-b)/2<=r<=(a+b)/2`, put `d=a+b-2r`, so `0<=d<=2b`. The two tail triangles of the trapezoidal convolution give

\[
\mathbb P(|X_a+X_b|\le r)
=1-\frac{d^2}{4ab},
\]

whereas

\[
\mathbb P(|X_{a+b}|\le r)=1-\frac d{a+b}.
\]

Their difference is

\[
\frac{d\,[4ab-d(a+b)]}{4ab(a+b)}\ge0,
\tag{7.4}
\]

because `d<=2b` and `a+b<=2a`. Outside the common support both probabilities are one. This proves (7.2).

A convolution of centered uniform densities is symmetric and unimodal. If `g` is any symmetric unimodal density, its superlevel sets are centered intervals; layer-cake applied to (7.2) therefore yields

\[
\mathbb E g(X_a+X_b)\ge \mathbb E g(X_{a+b}).
\tag{7.5}
\]

Hence, whenever `a+b<=1`, replacing widths `a,b` by the single width `a+b` can only **decrease** the final convolution density at zero, while preserving both the total width `2` and the constraint that every width is at most `1`.

If at least four widths remain, the two smallest have sum at most one: each is at most the average `2/m`, so their sum is at most `4/m<=1`. We may therefore merge repeatedly until only two or three widths remain.

If two remain, each is at most one and their sum is two, so they are `(1,1)`. Their triangular convolution has density exactly one at zero.

If three remain, call them `a,b,c`. Then `a+b+c=2` and each is at most one. The standard inclusion-exclusion formula for a weighted sum of three uniforms at `1` gives

\[
f_W(1)=\frac{1-(1-a)^2-(1-b)^2-(1-c)^2}{2abc}.
\tag{7.6}
\]

Set

\[
x=1-a,\quad y=1-b,\quad z=1-c,
\qquad x+y+z=1.
\]

Then

\[
f_W(1)=\frac{xy+yz+zx}{(x+y)(y+z)(z+x)}.
\tag{7.7}
\]

But

\[
(x+y)(y+z)(z+x)
=(x+y+z)(xy+yz+zx)-xyz
=xy+yz+zx-xyz
\le xy+yz+zx.
\tag{7.8}
\]

Therefore `f_W(1)>=1`. Since every merge could only decrease the central density, the original density also satisfies (7.1). `QED`.

## 8. Dimension-free restricted Makai theorem

Combining (6.4) with Lemma B proves:

> **Theorem C.** Let `K subset R^n` be a full-dimensional convex polytope whose `n+2` vertices form an affine circuit. Then
> \[
> \boxed{|K|\,|(K-K)^\circ|\ge\frac{n+1}{n!}.}
> \]

This theorem is genuinely dimension-free and covers the entire affine-circuit parameter family; it is not finite sampling.

### Three-dimensional corollary

Every three-dimensional polytope with four vertices is a tetrahedron. A five-vertex polytope either has four coplanar vertices, in which case it is a quadrilateral pyramid and is covered by the preceding all-pyramids theorem, or has no four coplanar vertices, in which case its five vertices form an affine circuit and Theorem C applies. Hence:

> **Corollary D.** Every convex three-dimensional polytope with at most five vertices satisfies
> \[
> |K|\,|(K-K)^\circ|\ge\frac23.
> \]

This is the cleanest source-relevant milestone of the run. It still does **not** prove the source for arbitrary three-dimensional convex bodies.

## 9. Exact verification artifact, secondary to the proof

After the route and proof were written, I added

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T1234Z__makai_circuit_cube_slice_check.py`

at commit `aeeffebcfb820ae510e466b62b0cc519128e2d21` and executed the same exact-`Fraction` code. Its archived output is

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T1234Z__makai_circuit_cube_slice_check.out`

at commit `ac9dabc3aad8fd3a4425b19902537a04265ef2e2`.

The self-check verifies:

1. exact circuit cofactors for four rational triangular bipyramids;
2. `f_W(1)>=1` on **77,070** exact rational weight vectors with `m=3,...,7`, denominators through `10` and all coordinates in `(0,1]` summing to `2`;
3. the closed three-width formula on **5,365** exact rational cases;
4. the pair-peakedness comparison on **8,415** exact rational grid cases.

The output ends

`ALL_EXACT_CHECKS_PASS = True`.

These finite computations are labeled a self-check, not an exhaustive convex-body certificate. The theorem-sized claim rests on Sections 5--8.

## 10. What moved mathematically, and what did not

Source metric:

\[
d_{\rm Makai}:2\to2.
\]

So the first line correctly reports **NO MOVEMENT**.

Restricted-scope progress did move sharply:

- previous run: all positive-homothety prismoids/frusta in `R^3`;
- this run: **all affine-circuit polytopes with `n+2` vertices in every dimension**;
- in `R^3`: **all polytopes with at most five vertices**.

The simplest source-valid next frontier is therefore no longer a five-vertex polytope. For a polyhedral route in `R^3`, the first genuinely new vertex count is six; for the prismoid route, the unresolved planar inequality is the non-homothetic two-base formula from the preceding report.

## 11. Stagnation bookkeeping and next-run obligation

This is the third consecutive Makai run with the frozen source metric unchanged (`2 -> 2`): admission/all-pyramids, prismoid/frustum, and this affine-circuit theorem. Under Section I, the **next invocation is STUCK1** and must be a thinking/recovery run rather than another ordinary lemma run. It must record the exact remaining source blocker, all routes tried and why they do not yet cover arbitrary three-dimensional bodies, the simplest unproved case, the nearest solved analogue, and choose exactly one authorized recovery action with a fresh B-triple.

This run does not consume that future STUCK1 recovery prematurely.

## 12. Ledger delta

```text
track: HARD7-01
target: Makai Jr. polar difference-body volume-product conjecture
claim: operations/claims/MAKAI-POLAR-DIFFERENCE-BODY.md
metric: d_Makai
before: 2
after: 2
movement: NO MOVEMENT
status: PARTIAL / SOURCE OPEN / CLAIMED
new theorem: Makai bound for every affine-circuit n-polytope with n+2 vertices; in R^3 all polytopes with <=5 vertices
methods: B1 / B16 / B25
next: mandatory STUCK1 recovery run
shared RESULTS.md edit: none (P26/shared-root maintainer policy preserved)
```
