Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT in the frozen source metric `D_MI: 2 -> 2` (fifth consecutive run at the source metric). Methods tried: B1 / B3 / B20.**

# HARD7-01 — STUCK2 recovery: a five-dimensional Robin moment operator for 3D maximal-intersection uniqueness

**Status:** PARTIAL / source OPEN. This is the second and final allowed Section-I recovery cycle on the current maximal-intersection target. The run does **not** call the source problem solved and does **not** move `D_MI`.

## 1. Required state / source / collision read

I resumed the exclusive claim

`operations/claims/MAXIMAL-INTERSECTION-ELLIPSOID-UNIQUENESS.md`

rather than restarting admission. Before doing mathematics I reread the HARD7 control, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current claim, the newest own checkpoint, neighboring alias reports, and the `probability_1000_intake_*` root/intake inventory and source-alias search. Repository collision search again shows this exact source target owned by HARD7-01; R20's neighboring report explicitly treats the maximal-intersection question as occupied here. No claim was overwritten and no shared-root ledger was edited.

The exact source remains Shiri Artstein-Avidan and David Katzin, *Isotropic measures and maximizing ellipsoids: Between John and Loewner*, Proc. Amer. Math. Soc. 146 (2018), 5379--5390, DOI `10.1090/proc/14180`, arXiv:1612.01128, Section 4: for every centrally symmetric convex body and every prescribed intermediate radius `r_J<r<r_L`, is the maximum-intersection ellipsoid unique?

Fresh bounded literature checks used the exact title and aliases `maximal intersection ellipsoid`, `maximum intersection position`, `strong B equality`, and `uniform ball equality`:

- Artstein-Avidan--Katzin: https://arxiv.org/abs/1612.01128 .
- J. Bochi, https://arxiv.org/abs/1702.03808 , proves the planar case and describes the higher-dimensional question as open.
- D. Cordero-Erausquin--L. Rotem, https://arxiv.org/abs/2111.05110 , proves the strong `(B)` inequality for the rotationally invariant class containing the uniform Euclidean ball, but does not classify the needed uniform-ball equality cases.
- O. Herscovici--G. Livshyts--L. Rotem--A. Volberg, https://arxiv.org/abs/2305.17794 , treats equality/stability for the Gaussian strong `(B)` theorem and notes the geometric maximal-intersection question as a separate uniform-ball issue.
- E. Putterman, *Sharp stability for the (B)-theorem*, https://arxiv.org/abs/2608.08472 , submitted 2026-08-09 and updated 2026-08-11, gives Gaussian/1-log-concave stability and strong/functional extensions; its stated results do not supply the missing uniform-ball maximal-intersection uniqueness theorem.

The 2026 searches found no general-dimensional resolution. This is bounded negative evidence, not an exhaustive worldwide priority certificate.

### Frozen metric

`D_MI = largest d such that uniqueness is rigorously proved for every centrally symmetric K and every intermediate prescribed radius in every n<=d.`

Before: `D_MI=2` (Bochi). After: `D_MI=2`. **No movement.** The preceding run completed the full three-dimensional cube family, but that restricted theorem does not change this source metric.

## 2. Why this is a Section-I STUCK2 run

The source metric has now remained `2` for five consecutive current-target runs. The first recovery cycle succeeded in proving the full `3D` cube intermediate window, but did not move the all-body source metric. Hence I use the second allowed recovery choice: **port the equality-kernel idea from solved strong-`(B)` settings into a direct uniform-ball boundary operator, and identify exactly what strictness is still missing.**

The exact blocker is now:

\[
\boxed{\quad \lambda_{\min}(T_K)>0\quad\text{for every genuine intermediate maximal-intersection position }K\subset\mathbb R^3,\quad}
\]

where the operator `T_K` is derived below. Strong `(B)` gives only `T_K >= 0`. A proof of strict positivity, or an exact classification of its nullspace excluding nonzero trace-free quadratic modes in the intermediate regime, is what the existing routes do not contain.

Previous current-target routes and their precise limits:

- **B2/B5/B11:** found exact inactive-coordinate strong-`(B)` equality families and refuted the literal 2018 equality sentence, but those flat directions are not automatically global maximal-intersection positions.
- **B12/B15/B30:** proved a cube collar, but symmetry-specific cap disjointness stopped before the overlap layer.
- **B6/B18/B24:** obtained the switching-interface second variation, but its sign was not uniform for arbitrary angular contact sets.
- **B4/B14/B25:** completed the entire 3D cube window by hyperoctahedral reduction, but the reduction is not available for general bodies.
- **This run B1/B3/B20:** replaces general 3D geometry by an exact five-dimensional operator and proves a quantitative sufficient condition; it also proves that differentiating first-order isotropy only once cannot add information beyond the Hessian kernel.

What a full proof still needs, and none of the above has: a mechanism forcing a **strict spectral gap** for the uniform-ball equality operator at every intermediate MI position, including nonsmooth positions after approximation. The simplest structured unproved class isolated by this reduction is a smooth strictly convex centrally symmetric **body of revolution in R^3** in genuine intermediate MI position; axial symmetry block-diagonalizes the five-dimensional operator, but strict positivity of all blocks is not yet proved here.

The nearest solved problems are Bochi's full `n=2` uniqueness theorem and the Gaussian strong-`(B)` equality/stability theorems. The planar proof has one angular variable and lacks the five-dimensional degree-two harmonic kernel below; the Gaussian equality proofs have coercive spectral structure that does not directly survive the singular uniform-ball limit. That missing strict uniform-ball coercivity is exactly the gap.

## 3. Counterexample attack first: the obvious slab/product flat direction fails at maximality

The admission run produced a flat trace-zero strong-`(B)` equality segment by letting the deformation act only on constraints inactive on `B_2^3`. I first tried to promote that mechanism to an actual MI counterexample.

Consider the simplest product box

\[
K=[-a,a]\times[-b,b]^2
\]

and axis-aligned ellipsoids with semiaxes `(ell,m,n)` and fixed volume normalized by `ell*m*n=1`. In the regime where the `y,z` constraints are inactive (`m,n<=b`) and the `x` constraint clips (`ell>a`), the intersection is just a clipped ellipsoid, so exactly

\[
V(\ell)=\int_{-a}^{a}\pi mn\Bigl(1-\frac{x^2}{\ell^2}\Bigr)\,dx
 =\frac{2\pi a}{\ell}-\frac{2\pi a^3}{3\ell^3}.
\]

Hence

\[
V'(\ell)=-\frac{2\pi a(\ell^2-a^2)}{\ell^4}<0\qquad(\ell>a).
\]

But `m,n<=b` and `ell*m*n=1` force `ell>=1/b^2`. In the genuine clipped regime `a<1/b^2`, maximizing inside this putative slack family drives `ell` down to `1/b^2`, which forces `m=n=b`: both transverse constraints become active and the flat redistribution disappears. Thus the most direct inactive-coordinate equality template does **not** furnish a maximal-intersection plateau even in the axis-aligned box family. This does not prove the conjecture; it explains why the literal strong-`(B)` equality counterexamples found at admission do not automatically refute MI uniqueness.

## 4. B1 — change category: from ellipsoids to a 5x5 Robin moment operator

Work in `R^3` and affinely normalize a candidate MI position so that the unit ball `B=B_2^3` is a global maximum-intersection ellipsoid of the prescribed volume. For this derivation assume the gauge `g` of `K` is `C^2` near the switching set and transverse there. Put

\[
\Omega=\{\theta\in S^2:g(\theta)<1\},\qquad
\Gamma=\partial\Omega=\{g=1\},\qquad
h=|\nabla_{S^2}g|>0\ \text{ on }\Gamma.
\]

Let `H_2` be the five-dimensional Hilbert space of real symmetric trace-zero `3x3` matrices with Frobenius inner product, and for `A in H_2` write

\[
q_A(\theta)=\theta^T A\theta.
\]

### 4.1 First-order MI condition = degree-two isotropy

For the volume-preserving ellipsoid path `E_t=e^{tA}B`, the standard radial derivative is

\[
\frac{d}{dt}\Big|_{0}\operatorname{Vol}(K\cap E_t)
  =\int_{\Omega}q_A\,d\sigma.
\]

Since `B` is an MI maximizer, this vanishes for every `A in H_2`. Equivalently,

\[
\boxed{\int_{\Omega}\theta\theta^T\,d\sigma=\frac{|\Omega|}{3}I.}\tag{I2}
\]

### 4.2 Exact second variation including the switching boundary

For `a=q_A(theta)` and `b=theta^T A^2 theta`, the radial cube of `e^{tA}B` satisfies

\[
(\rho_{E_t}(\theta)^3)'_{t=0}=3a,\qquad
(\rho_{E_t}(\theta)^3)''_{t=0}=15a^2-6b.
\]

Differentiating the minimum of the body radial cube and ellipsoid radial cube, transversality gives the interface term `-a^2/h`. Therefore

\[
F_A''(0)
 =5\int_{\Omega}q_A^2\,d\sigma
  -2\int_{\Omega}\theta^TA^2\theta\,d\sigma
  -\int_{\Gamma}\frac{q_A^2}{h}\,d\ell.
\]

Using (I2),

\[
\boxed{
F_A''(0)=5\int_{\Omega}q_A^2\,d\sigma
 -\frac{2|\Omega|}{3}\operatorname{tr}(A^2)
 -\int_{\Gamma}\frac{q_A^2}{h}\,d\ell.}\tag{H}
\]

Polarization defines the symmetric bilinear form

\[
H_K(A,C)=5\int_{\Omega}q_Aq_C\,d\sigma
 -\frac{2|\Omega|}{3}\operatorname{tr}(AC)
 -\int_{\Gamma}\frac{q_Aq_C}{h}\,d\ell.
\]

Strong `(B)` for the uniform ball implies `H_K(A,A)<=0` at an MI position.

### 4.3 Operator form

Set

\[
V_\theta=\theta\theta^T-\frac13I\in H_2,
\]

so `q_A=<A,V_theta>`. Define operators on `H_2`

\[
M_\Omega=\int_\Omega V_\theta\otimes V_\theta\,d\sigma,
\qquad
B_\Gamma=\int_\Gamma \frac{V_\theta\otimes V_\theta}{h}\,d\ell.
\]

Then

\[
-H_K(A,C)=\langle A,T_K C\rangle,
\]

with the exact five-dimensional operator

\[
\boxed{
T_K=B_\Gamma+\frac{2|\Omega|}{3}I_{H_2}-5M_\Omega
   =B_\Gamma-5\left(M_\Omega-\frac{2|\Omega|}{15}I_{H_2}\right).}\tag{T}
\]

Strong `(B)` gives `T_K>=0`. The source uniqueness question in the smooth transverse `3D` normalization is therefore changed into a **strictness problem for a concrete 5x5 positive-semidefinite operator**.

There is also an exact trace identity. Since

\[
\|V_\theta\|_F^2=\frac23\quad(\theta\in S^2),
\]

we get

\[
\operatorname{tr}_{H_2}M_\Omega=\frac{2|\Omega|}{3},\qquad
\operatorname{tr}_{H_2}B_\Gamma=\frac23\int_\Gamma\frac{d\ell}{h},
\]

and the two bulk traces in (T) cancel:

\[
\boxed{\operatorname{tr}_{H_2}T_K=\frac23\int_\Gamma\frac{d\ell}{h}>0.}\tag{trace}
\]

Thus a counterexample cannot make the entire strong-`(B)` Hessian flat: it would require a **proper nonzero kernel direction** of `T_K`.

## 5. B3 — prove a stronger quantitative sufficient criterion

Formula (T) immediately yields a usable theorem that is stronger than merely checking a particular deformation.

### Theorem (design-defect versus boundary-collar criterion)

Under the smooth/transverse normalized `3D` hypotheses above, if

\[
\boxed{
\lambda_{\min}(B_\Gamma)
  >5\left\|M_\Omega-\frac{2|\Omega|}{15}I_{H_2}\right\|_{\rm op},}\tag{C}
\]

then `B_2^3` is the **unique global** maximum-intersection ellipsoid of its prescribed volume.

#### Proof

From (T), Weyl's elementary bound gives

\[
\lambda_{\min}(T_K)
\ge \lambda_{\min}(B_\Gamma)
 -5\left\|M_\Omega-\frac{2|\Omega|}{15}I\right\|_{\rm op}>0.
\]

Suppose a different equal-volume ellipsoid were also globally maximizing. It can be written `e^A B` with a nonzero symmetric trace-zero `A`. By the strong `(B)` theorem, `t mapsto Vol(K cap e^{tA}B)` is log-concave. Both endpoints `t=0,1` equal the global maximum, while no intermediate value can exceed that maximum, so the function is constant on `[0,1]`. Hence `F_A''(0)=0`. But (H)--(T) give

\[
F_A''(0)=-\langle A,T_KA\rangle<0,
\]

a contradiction. QED.

A clean corollary is the exact degree-four design case: if

\[
M_\Omega=\frac{2|\Omega|}{15}I_{H_2}
\]

and no nonzero trace-zero quadratic `q_A` vanishes on `Gamma` up to arclength-null sets, then `B_Gamma` is positive definite, (C) holds, and the MI ellipsoid is unique. This is a genuine all-deformation theorem for that smooth class, not finite sampling. I do **not** claim this condition covers every convex body or moves `D_MI`.

## 6. B20 — find why the natural isotropy algorithm fails

A tempting next step is: if two maximizers exist, the entire strong-`(B)` segment consists of maximizers; transform the body along that segment, differentiate its MI isotropy, and hope to obtain an extra equation. The exact computation shows that the first differentiation gives **precisely the same kernel equation and nothing more**.

Assume a hypothetical nonunique pair `B` and `e^A B`, `A!=0`, and set `K_t=e^{-tA}K`. Since the whole segment is maximizing, `B` is in MI position for every `K_t`. Let

\[
\Omega_t=K_t\cap S^2=\{\theta:g(e^{tA}\theta)<1\}.
\]

For every `C in H_2`, MI isotropy gives

\[
\int_{\Omega_t}q_C\,d\sigma=0.\tag{iso-t}
\]

Write `eta=grad_S g/h` for the outward normal of `Gamma` and

\[
X_A(\theta)=A\theta-q_A(\theta)\theta,
\]

the tangential spherical vector field generated by the linear deformation. The boundary velocity of `Omega_t` at `t=0` is

\[
V=-\frac{q_A}{h}-\eta\cdot X_A.
\]

The exact spherical identities are

\[
\operatorname{div}_{S^2}X_A=-3q_A,
\]

and

\[
\nabla_{S^2}q_C\cdot X_A
 =2\theta^TCA\theta-2q_Aq_C.
\]

Differentiate (iso-t), apply the spherical divergence theorem to `q_C X_A`, and use (I2). One obtains for every `C in H_2`

\[
\boxed{
\int_\Gamma\frac{q_Aq_C}{h}\,d\ell
 =5\int_\Omega q_Aq_C\,d\sigma
 -\frac{2|\Omega|}{3}\operatorname{tr}(AC).}\tag{KERNEL3}
\]

But (KERNEL3) is exactly

\[
T_KA=0.
\]

So **first-order differentiation of the moving isotropy condition is not a new rigidity equation**; it is merely the polarized zero-Hessian condition. This explains structurally why the route had stalled: another first derivative, another local MI Euler equation, or another checker for (H) cannot close the conjecture. Any continuation on this target would need either a second moving-isotropy derivative / curvature identity, or a strict equality classification imported from the underlying uniform-ball spectral proof.

This is the main negative-method result of the run.

## 7. Exact symbolic checker

Only after the operator route produced the concrete identities above did I build a checker. It verifies, with exact symbolic algebra for arbitrary symmetric trace-zero `A,C`, the two spherical polynomial identities used in the divergence calculation and the `H_2` frame identity `sum_i q_{E_i}(theta)^2=(2/3)|theta|^4` for a Frobenius-orthonormal trace-zero basis.

- checker commit: `e4bbcc01e034eac32adc7592b141f7c96f8722b4`
- archived output commit: `fd281259e7424e5c68a5f60f654ee2a823527ed0`
- output ends: `ALL_EXACT_CHECKS_PASS = True`

The checker is a self-check of the finite symbolic core only. The global uniqueness criterion and shape-derivative argument are proved on the page above; no simulation or finite sample is promoted to an asymptotic/general theorem.

## 8. Lifecycle consequence and handoff boundary

This run consumes the **second** allowed Section-I recovery on this source target. The source metric is still `D_MI=2`. Therefore, if a later execution again reaches the stuck condition without actually moving `D_MI`, CONTROL Section I requires a handoff/rotation rather than a third recovery on the same problem. The operator `(T)` and criterion `(C)` should be preserved for a future reassignment; a body-of-revolution block decomposition is the most concrete next special-class route, but it is not claimed here.

No closure audit is requested because the source remains PARTIAL/OPEN. No paper package is created.

## 9. Capability honesty

The available scheduler interface still exposes schedule/prompt/timing/enabled controls, not a model selector, reasoning-effort selector, authenticated runtime telemetry, or guaranteed run duration. GPT-6 maximum therefore remains prompt-requested only. The actual model visible here is GPT-5.6 Sol; reasoning level is UNVERIFIED.

The repository ledger records the historical `P26` permission error (`You cannot modify this task`) and also records that a later full P26 update succeeded from a different authorized context. I did not probe or modify P26 or any other schedule. The legitimate workaround for a genuinely nonmodifiable task is to use its authorized owning workspace/context or platform support/admin capability; duplicating/reactivating a task to bypass permissions is not allowed.

## 10. Ledger delta for coordinator consumption

- track: `HARD7-01`
- target: maximal-intersection ellipsoid uniqueness, Artstein-Avidan--Katzin Section 4
- fixed metric before: `D_MI=2`
- fixed metric after: `D_MI=2`
- movement: `NO MOVEMENT`
- supported unchanged count: `5`
- status: `PARTIAL / SOURCE OPEN / STUCK2 recovery consumed`
- methods: `B1, B3, B20`
- new theorem/reduction: exact smooth-transverse `3D` Robin moment operator `(T)`; global uniqueness under criterion `(C)`; nonuniqueness forces a proper kernel direction; first moving-isotropy derivative is exactly the same kernel equation
- exact finite self-check: PASS
- next lifecycle: on the next source-metric stuck episode, hand off/rotate rather than use a third recovery
