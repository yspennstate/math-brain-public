SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-24T06:14:22Z.
attacking: the punctured near-coloop two-sheet endpoint; aggregate the full original-coordinate two-Jacobian before any reciprocal minor, and quantify exactly how the third square changes the rank-two logarithmic singular set from codimension one to codimension two.

# account03/B11 — puncture-stable full two-Jacobian currency

Programme: `QFORM-DENSITY-3EIG-20260922`.
Assignment: indefinite signatures `(2,1)` / `(1,2)`.
Status: **NEW SUPPORTING THEOREM / EXACT ORIGINAL-COORDINATE MINOR IDENTITY / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**.
Execution: **WITHOUT_VERIFIED_BRAIN**.
Regularity: the theorem below is an integrated coarea/Jacobian statement. It does **not** by itself prove a density, essential boundedness, or continuity on the remaining two-sheet branch. The designated partner theorem separately proves an essential-density bound on the one-sheet side; continuity is not claimed there.

The unrestricted owner conjecture remains OPEN / NOT PROVED / NOT DISPROVED.

The run label `r47` is part of this invocation's unique timestamped canonical ID. During the fresh source read I found the chronologically earlier published B11 run `20260924T023910Z-account03-B11-QFORM-r48`; it is therefore treated as a predecessor despite its larger suffix. No result from that run is overwritten or relabeled.

No Gaussianity, log-concavity, moment assumption, compact or connected support, independence after rotation, conditional-density-as-independence step, pointwise van-der-Corput decay, arbitrary-joint coarea theorem, or perturbative deletion of the puncture is used.

## 1. Fresh sources and the first unpaid implication

Fresh brain control was resolved from `yspennstate/math-research-brain` main, initially at

`db0d6dbe2a76fa54e663e4bcbe1a7acd0b2fc956`

and refreshed before publication. OWNER CONTROL remains revision `2026-09-22.15`; QFORM is the sole research target and the full target remains open.

The latest own mathematical predecessor consumed is

- repository `yspennstate/math-open-problems`,
- report-introducing commit `863bdb80ed0e334904d6232a6d6effafdb72f3fc`,
- path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260924T023910Z-account03-B11-QFORM-r48/REPORT.md`.

That run proved `QFORM-SAMEBANK-L3-L32-DEPENDENCE-BARRIER-v1`: even at arbitrarily small puncture, bounded same-bank joint and marginal densities plus the r46 `L^3` hyperbolic resource and an `L^(3/2)` square resource do not imply `L^infinity`. Its explicit nonlinear volume-preserving residual shear cancels the square and recovers the rank-two logarithmic singularity. It is not a QFORM counterexample because the residual triple is not an orthogonal **linear** projection of an independent product source.

A fresh compatible account02/B11 theorem further proves that a surviving fixed physical transverse Pluecker atom closes the exact-null branch; therefore a true hard sequence must become physically diffuse. That result is complementary to the aggregate identity below: here no individual minor is selected or inverted.

The completed designated partner used at an actual inequality is account04/B11,

- repository `yspennstate/math-open-problems`,
- commit `779d91b45aa70cd12c19ce04d951b306690358ad`,
- path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260924T051259Z-account04-B11-rough-one-sheet-r2/REPORT.md`.

Its rough anisotropic one-sheet theorem is applied in Section 6.

## 2. Exact punctured null-pivot normal form

Use the exact-rank-three normal form established in B11 r45. Let

`A=R M R^T`, `R^T R=I_3`,

and let

`s := min_j |lambda_j(M)| > 0`.

At a physical null pivot with leverage `q in (0,1]`, after an orthogonal spectral bookkeeping choice and a determinant-one shear in the residual `(V,W)` plane, the active quadratic form is

`Q = 2 a H W + 2 b T W + c (V')^2 + delta W^2`,             (2.1)

where

`a = kappa sqrt(q)`,
`b = kappa sqrt(1-q)`,
`a^2+b^2=kappa^2`,                                            (2.2)

`H` is one literal original independent coordinate, `(T,W,V)` is an orthonormal three-dimensional projection of the remaining original independent product bank, and

`V' = V + eta W`                                              (2.3)

for a deterministic real shear parameter `eta`. The determinant identity is

`kappa^2 |c| = |det M|`.                                     (2.4)

The puncture size is `b/a=sqrt((1-q)/q)` when `q<1`, but **no estimate below divides by `b`**. In particular all constants remain finite at the exact endpoint `b=0`.

Let the original residual coefficient vectors of `T,W,V` be `t,w,v`; thus

`||t||=||w||=||v||=1`,
`<t,w>=<t,v>=<w,v>=0`.                                      (2.5)

Write `x` for the residual original-coordinate vector, so `T=t.x`, `W=w.x`, `V=v.x`.

## 3. New theorem: exact full two-Jacobian identity

### Theorem 3.1 — `QFORM-PUNCTURE-FULL-TWOJACOBIAN-v1`

Define the two-output map on the **original independent coordinates**

`F(H,x) = ( W(x), Q(H,x) )`.                                 (3.1)

Its Euclidean two-Jacobian is

`J_2 F := | grad W wedge grad Q |`.

Then pointwise, with no probabilistic assumption,

`boxed:
 (J_2 F)^2 = 4 [ kappa^2 W^2 + c^2 (V')^2 ].
`                                                                  (3.2)

Equivalently,

`boxed:
 J_2 F = 2 sqrt( kappa^2 W^2 + c^2 (V')^2 ).
`                                                                  (3.3)

The identity is **independent of the puncture parameter `q`** except through the invariant `kappa`; in particular the potentially vanishing coefficient `b=kappa sqrt(1-q)` causes no loss.

### Proof

In the full coordinate space `R e_H direct_sum R^m`,

`grad W = (0,w)`.                                               (3.4)

From (2.1)-(2.3),

`partial_H Q = 2 a W`,                                         (3.5)

and the residual gradient is

`grad_x Q
 = 2 a H w
   + 2 b (W t + T w)
   + 2 c V' (v + eta w)
   + 2 delta W w`.                                             (3.6)

When wedged with `(0,w)`, every term parallel to `w` disappears. Hence

`grad W wedge grad Q
 = 2 a W (w wedge e_H)
   + 2 b W (w wedge t)
   + 2 c V' (w wedge v)`.                                     (3.7)

Because `e_H,t,w,v` are orthonormal in the full original-coordinate space, the three two-forms

`w wedge e_H`, `w wedge t`, `w wedge v`

are orthonormal in exterior square. Therefore

`|grad W wedge grad Q|^2
 = 4 a^2 W^2 + 4 b^2 W^2 + 4 c^2(V')^2
 = 4[kappa^2 W^2+c^2(V')^2]`,                                (3.8)

using `a^2+b^2=kappa^2`. QED.

### Literal original-coordinate minor form

The same proof can be written without exterior notation. For every residual physical coordinate `j`, the Jacobian minor on the literal pair `(H,x_j)` is

`D_(H,j) = -2 a W w_j`.                                      (3.9)

For every residual physical pair `j<k`,

`D_(j,k)
 = 2 b W (w_j t_k-w_k t_j)
   +2 c V' (w_j v_k-w_k v_j)`.                               (3.10)

Cauchy-Binet for the `2 x (m+1)` derivative matrix gives

`(J_2F)^2
 = sum_j D_(H,j)^2 + sum_(j<k) D_(j,k)^2`.                   (3.11)

Now

`sum_j w_j^2=1`,
`sum_(j<k)(w_j t_k-w_k t_j)^2=|w wedge t|^2=1`,
`sum_(j<k)(w_j v_k-w_k v_j)^2=1`,                             (3.12)

and

`sum_(j<k)(w_j t_k-w_k t_j)(w_j v_k-w_k v_j)
 = <w wedge t,w wedge v>=0`.                                 (3.13)

Substitution in (3.11) again yields (3.2).

This version matters for the fleet architecture: the curvature is aggregated over **literal original-coordinate minors before any reciprocal minor is taken**. There is no `max_(j,k)` and therefore no dimension loss merely because every individual Pluecker atom is small.

## 4. Product-law consequence: a puncture-uniform reciprocal Jacobian budget

The deterministic identity becomes quantitative because `(W,V')` retains original product-projection provenance.

The pair `(W,V)` is an orthogonal two-dimensional projection of the residual independent cap-one product source. The completed two-dimensional projection theorem used by account04/B11 gives it a joint density bounded by `2`. The shear

`(W,V) -> (W,V+eta W)=(W,V')`

has determinant one, so `(W,V')` also has a joint density bounded by

`M_2 <= 2`.                                                    (4.1)

### Lemma 4.1 — capped planar reciprocal ellipse

Let `(Y,Z)` have a probability density at most `M`. For `alpha,beta>0` and `0<p<2`,

`E (alpha^2 Y^2+beta^2 Z^2)^(-p/2)
 <= [2/(2-p)] (pi M/(alpha beta))^(p/2).`                    (4.2)

#### Proof

Set `u=alpha Y`, `z=beta Z`. The transformed probability density `h` has cap

`K=M/(alpha beta)`.                                          (4.3)

For `R=sqrt(u^2+z^2)`,

`P{R<r} <= min(1, pi K r^2)`.                                (4.4)

Use layer cake:

`E R^(-p)
 = int_0^infinity P{R^(-p)>y} dy
 = int_0^infinity P{R<y^(-1/p)} dy`.                         (4.5)

The two branches in (4.4) meet at

`y_0=(pi K)^(p/2)`.                                          (4.6)

Thus

`E R^(-p)
 <= y_0 + pi K int_(y_0)^infinity y^(-2/p) dy
 = [2/(2-p)] (pi K)^(p/2)`.                                 (4.7)

This proves (4.2). QED.

### Theorem 4.2 — `QFORM-PUNCTURE-JACOBIAN-NEGATIVE-MOMENTS-v1`

For the true product model (2.1), for every `0<p<2`,

`boxed:
 E (J_2F)^(-p)
 <= [2^(1-p)/(2-p)]
    ( pi M_2/(kappa |c|) )^(p/2).
`                                                                  (4.8)

Using `M_2<=2`,

`boxed:
 E (J_2F)^(-p)
 <= [2^(1-p)/(2-p)]
    ( 2 pi/(kappa |c|) )^(p/2).
`                                                                  (4.9)

Now the spectral hypothesis itself removes all dependence on the largest eigenvalue. Let

`L=max_j |lambda_j(M)|`.

Since `kappa=||M e_1||<=L` and the other two eigenvalue magnitudes are at least `s`,

`|det M| >= s^2 L`.                                           (4.10)

By (2.4),

`kappa |c| = |det M|/kappa >= s^2 L/kappa >= s^2`.           (4.11)

Therefore

`boxed:
 E (J_2F)^(-p)
 <= [2^(1-p)/(2-p)] (2 pi)^(p/2) s^(-p),
 0<p<2.
`                                                                  (4.12)

At the most relevant endpoint `p=1`,

`boxed:
 E 1/(J_2F) <= sqrt(2 pi)/s
 = 2.5066282746310002... / s.
`                                                                  (4.13)

There is also a uniform quadratic small-Jacobian tail:

`boxed:
 P{J_2F <= tau}
 <= min(1, pi tau^2/(2 s^2)).
`                                                                  (4.14)

Indeed (3.3) and the density cap give

`P{J_2F<=tau}
 <= M_2 * area{(w,v'): kappa^2w^2+c^2v'^2<=tau^2/4}
 = M_2 pi tau^2/(4 kappa|c|)`,                                  (4.15)

and then use `M_2<=2` and (4.11).

### Why this is exactly the third-direction gain

If the third square is deleted, `c=0`, then (3.3) collapses to

`J_2F=2 kappa |W|`.                                           (4.16)

For a perfectly legal rank-two control with a scalar density positive at the origin, `E 1/|W|` diverges logarithmically. For example centered unit uniform `W` gives the usual product-law logarithm in `2XY`.

With `c!=0`, the singular set is the **codimension-two point** `(W,V')=(0,0)`. The reciprocal kernel is now the planar Riesz kernel

`1/sqrt(kappa^2W^2+c^2(V')^2)`,                               (4.17)

whose first negative moment is integrable under the uniform two-dimensional product-projection cap. Equations (4.13)-(4.14) quantify this statement with a constant independent of puncture size, dimension, input supports, moments, and sign of `c`.

Thus the third direction removes the rank-two singularity at the level of the complete original-coordinate coarea Jacobian **even in the fully punctured same-bank geometry**.

## 5. What the new theorem does and does not buy

The result is stronger than a favorable-minor statement and weaker than the final density theorem.

It is stronger because (3.11) sums every literal physical `2 x 2` Jacobian minor before inversion. Hence a physically diffuse transverse frame, in which every individual determinant atom tends to zero, still has the invariant full currency (3.2).

It is weaker because a finite expectation of `1/J_2F` under the source law is an **integrated** statement. The coarea formula for the map `(W,Q)` involves fiber traces of the product density. A uniform bound for those traces does not follow from (4.13) alone. The live corrections explicitly forbid replacing an integrated product-law statement by an unrestricted fiber supremum or by an arbitrary-joint density cap. The r48 nonlinear cancellation example also shows that an inequality of the schematic form

`||p_Q||_infinity <= C E[1/J_2F]`                              (5.1)

cannot be asserted for arbitrary bounded joint laws.

The missing implication is therefore now very specific:

`QFORM-PRODUCT-COAREA-TWOJACOBIAN-COMPILER-v1`:

> for the map `F=(W,Q)` in (3.1), use the original independent-coordinate product structure together with the **aggregate** identity (3.11), before selecting any fiber or minor, to convert the puncture-uniform negative-moment budget (4.12) into a uniform linear interval estimate on the minority-sign/two-sheet side.

The likely valid mechanism must resemble the complete product-Fourier / Brascamp-Lieb aggregation already used elsewhere in the fleet: integrate the full physical minor bank or full product Fourier volume first, then spend the reciprocal singularity. It must not select a single tiny Pluecker atom and must not condition on a rotated variable and assume a conditional cap.

## 6. Designated account04/B11 result applied at an actual inequality

The freshest compatible designated partner theorem is account04/B11's rough anisotropic one-sheet estimate at commit

`779d91b45aa70cd12c19ce04d951b306690358ad`.

For any exact rank-three signature `(2,1)`, with same-sign eigenvalue magnitudes `lambda_1,lambda_2>0`, it proves on the one-sheet side

`P{Q in E} <= [2 pi/sqrt(lambda_1 lambda_2)] |E|`.             (6.1)

The r45/r48 null-pivot punctured model is an exact rank-three form and every nonzero eigenvalue magnitude is at least `s`. Hence

`sqrt(lambda_1 lambda_2) >= s`,                               (6.2)

so the partner theorem gives the actual inequality

`boxed:
 P{Q in I, Q>0} <= (2 pi/s)|I|
`                                                                  (6.3)

for signature `(2,1)`, after the standard homogeneous normalization of the critical value to zero. Equivalently,

`ess sup_(t>0) p_Q(t) <= 2 pi/s`.                              (6.4)

For signature `(1,2)`, negate the form; the same theorem gives

`boxed:
 P{Q in I, Q<0} <= (2 pi/s)|I|,
`                                                                  (6.5)

so the majority-sign/one-sheet half-line is already paid in both signatures.

This is a direct application to the current hard chamber, not a transfer of the X-ray argument to the opposite side. The partner report explicitly states that its method does **not** control the two-sheet side; the live correction `QFORM-TWOSHEET-XRAY-ONLY-FALSE` remains binding.

Combining (6.3)-(6.5) with Theorem 4.2 isolates the current B11 debt even further:

- one-sheet side: target-level linear interval bound `2 pi/s` is proved;
- two-sheet side: the complete original-coordinate Jacobian already has a puncture-uniform integrable reciprocal, but the final product-sensitive fiber aggregation is missing.

## 7. Opposite-sign rank-two benchmark retained

For centered independent unit uniforms `X,Y`,

`p_(2XY)(t)=log(1/(2|t|)), 0<|t|<1/2`.                       (7.1)

This is the correct control: a rank-two saddle alone has a codimension-one zero of the coarea Jacobian and an unavoidable logarithm. Theorem 3.1 shows exactly what changes when the third direction is present in the genuine rotated null-puncture model:

`rank two: J ~ |W|`,

`rank three: J ~ sqrt(kappa^2W^2+c^2(V')^2)`.                (7.2)

The determinant identity and spectral gate make the elliptic area scale `kappa|c|` uniformly at least `s^2`. Thus the third direction does not merely add a formal nonzero Hessian eigenvalue; it changes the local reciprocal singularity from one-dimensional nonintegrable `1/|w|` to two-dimensional integrable `1/sqrt(w^2+v^2)` at a quantitatively controlled scale.

This conclusion is symmetric under `c -> -c`, hence it applies to both signatures `(2,1)` and `(1,2)`.

## 8. Verification plan and scope summary

The companion `VERIFY.py` checks numerically on random orthonormal residual frames that

`sum physical 2x2 Jacobian minors^2
 =4[kappa^2W^2+c^2(V')^2]`

to floating-point precision, and checks the constants in (4.13)-(4.15). The numerical check is only a regression test; the proof above is exact.

Scope summary:

- `QFORM-PUNCTURE-FULL-TWOJACOBIAN-v1`: **PROVED exact deterministic identity**.
- `QFORM-PUNCTURE-JACOBIAN-NEGATIVE-MOMENTS-v1`: **PROVED product-law quantitative inequality**, uniform in puncture and both indefinite signatures.
- account04/B11 rough one-sheet theorem: **APPLIED** to obtain `2 pi/s` on the actual one-sheet half-line.
- two-sheet full `L^infinity`: **OPEN**.
- arbitrary additional nonseparable spectrum beyond the exact rank-three core: **OPEN bridge**.
- full-target continuity: **OPEN**; no new continuity claim in this run.
- full QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.

The next B11 mechanism should attack `QFORM-PRODUCT-COAREA-TWOJACOBIAN-COMPILER-v1` directly, using complete minor/product-Fourier aggregation. If that compiler fails, the failure should be preserved as an explicit product-law counterexample to the compiler, not replaced by another marginal-density abstraction.
