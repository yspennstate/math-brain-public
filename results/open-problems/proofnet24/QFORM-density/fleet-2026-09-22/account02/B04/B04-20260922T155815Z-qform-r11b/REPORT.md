# account02/B04 — square-assisted ridge rearrangement below the direct L1 threshold

Run: `B04-20260922T155815Z-qform-r11b`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
Assignment: Product Fourier rearrangement  
Outcome: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED_FROM_SOURCE-PINNED_INPUTS / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and first unpaid implication

The full target remains: for every dimension, independent real coordinates with probability densities bounded by one, and every real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove a universal finite bound for the density of `X^T A X`, or give a valid counterexample. No moment, support, sign, diagonal-basis or post-rotation-independence hypothesis is added.

The first unpaid B04 implication after the preceding elementary-symmetric aggregation run was to survive **small full-rank tails** without paying ordinary range leverage. The fresh ridge-window proof gives a product-space characteristic envelope at one regularization scale, but its direct density criterion needs effective ridge dimension `theta>2q`. The completed account03/B04 square-assisted mechanism only needs an `L^(3/2)` characteristic-function budget. The step proved here is that the two mechanisms combine at the strictly weaker threshold

`theta > 4q/3`.

Thus a genuine original-coordinate square can close ridge-effective dimensions between `4q/3` and `2q`, a region where direct Fourier inversion does not apply.

## 2. Source-pinned dependencies and status

1. Fresh free-regularizer/ridge proof: `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`, path `proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`. Its Sections 4-5 prove that for an original-coordinate cross block `B`, with

   `K_gamma = BB^T (gamma^2 I + BB^T)^(-1)`,

   `theta = tr K_gamma`, `D = det(I+BB^T/gamma^2)`, and `max_i (K_gamma)_ii <= q/2`, one has for the residual quadratic form `R`

   `|phi_R(t)| <= D^(-1/(4q)) [L_q/(2 gamma |t|)]^(theta/(2q))`,

   where `L_q = pi e sqrt(2/q)`. That source supplies a complete proof but, at this run's source read, its new extension was still awaiting the specifically requested independent review. This report does not upgrade that review status.

2. Named partner account03/B04: `yspennstate/math-open-problems@f447c650e04ef27d14be3380ac541c1cec60ab0`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/B04-20260922T145033Z-r12/REPORT.md`. The completed theorem `QFORM-SQUARE-ASSISTED-L32-v1` records the source-valid coarea/Riesz step

   `||p_[a(X+m(Y))^2+R(Y)]||_inf <= H_3 |a|^(-1/2) ||p_R||_3^(3/4)`,

   `H_3 = 8 sqrt(2)/3^(3/4)`,

   for one untouched original coordinate `X` of density cap one, with an arbitrary measurable shift `m(Y)` finite almost surely.

3. The same partner report records sharp inverse Hausdorff--Young in the present Fourier convention with

   `C_HY = 3^(1/6) 2^(-1/3)`.

Corrections consumed before publication: law-uniform pointwise scalar quadratic-phase decay is false; fiber-sup arguments can lose dimension; spectral rotation does not preserve independence; a single cross minor, scalar Schur rank-two extraction, generic conditional cap, uniformly good small principal block, and a single physical triple with bounded reciprocal determinant cost are not universally forced. No refuted premise is used below.

## 3. New theorem: `QFORM-SQUARE-ASSISTED-RIDGE-L32-v1`

Let `Y` consist of independent original coordinates with densities bounded by one, let `R(Y)` be an arbitrary real quadratic form, and choose disjoint original-coordinate sets `I,J` with physical cross block `B`. Let `X` be one further original coordinate, independent of `Y`, with density bounded by one. Fix `a!=0`, a measurable `m(Y)` finite almost surely, `gamma>0`, and `1<=q<=2`.

Put

`K_gamma = BB^T (gamma^2 I+BB^T)^(-1)`,

`theta = tr K_gamma`,

`D = det(I+BB^T/gamma^2)`.

Assume

`max_i (K_gamma)_ii <= q/2`                                      (3.1)

and

`theta > 4q/3`.                                                   (3.2)

Then

`Q = a (X+m(Y))^2 + R(Y)`

has an essentially bounded density and

`||p_Q||_inf <= C_ridge(q,theta) D^(-1/(4theta)) / sqrt(|a| gamma)`,  (3.3)

where

`C_ridge(q,theta)
 = 8 * 3^(-5/8) * sqrt(e) * q^(-1/4)
   * sqrt( 3 theta / (3 theta - 4q) ).`                           (3.4)

Since `log D >= theta`, there is also the simpler bound

`||p_Q||_inf
 <= 8 * 3^(-5/8) * e^(1/4) * q^(-1/4)
    * sqrt(3theta/(3theta-4q)) / sqrt(|a| gamma).`               (3.5)

The ordinary range projection of `B` may be the identity; `B` may have arbitrary rank and arbitrarily small nonzero singular values of either provenance. The theorem makes no rotated-coordinate independence assumption.

### Proof

Write

`beta = theta/(2q)`.

The source-pinned ridge envelope gives

`|phi_R(t)| <= min(1,(t_0/|t|)^beta)`,                            (3.6)

with

`t_0 = [L_q/(2gamma)] D^(-1/(2theta))`.                          (3.7)

Indeed raising `t_0` to `beta` reproduces the determinant factor because `4q beta=2theta`.

The condition `theta>4q/3` is exactly `3beta/2>1`. Hence

`I := int_R |phi_R(t)|^(3/2) dt`

is finite, and direct integration of (3.6) gives

`I <= 2 t_0 [1 + 1/(3beta/2-1)]`

`   = 2 t_0 * 3theta/(3theta-4q).`                               (3.8)

Thus `phi_R in L^(3/2)`. Sharp inverse Hausdorff--Young gives an `L^3` density `p_R` satisfying

`||p_R||_3 <= (2pi)^(-2/3) C_HY I^(2/3).`                       (3.9)

Apply the completed account03/B04 square/coarea theorem:

`||p_Q||_inf <= H_3 |a|^(-1/2) ||p_R||_3^(3/4)`

`<= H_3 (2pi)^(-1/2) C_HY^(3/4) |a|^(-1/2) I^(1/2).`            (3.10)

Substitute (3.7)-(3.8). Since

`H_3 = 8 sqrt(2) 3^(-3/4)`,

`C_HY^(3/4)=3^(1/8)2^(-1/4)`,

and `L_q=pi e sqrt(2/q)`, the constants simplify to

`H_3 (2pi)^(-1/2) C_HY^(3/4) sqrt(L_q)
 = 8 * 3^(-5/8) * sqrt(e) * q^(-1/4).`

This is exactly (3.3)-(3.4). The scalar inequality `log(1+x)>=x/(1+x)` summed over the singular values gives `log D>=theta`, hence (3.5). QED.

### Why the threshold is genuinely new

The direct ridge-density theorem requires `theta>2q`, because it needs `phi_R in L^1`. Here only `phi_R in L^(3/2)` is required and the fresh physical square performs the final smoothing. Therefore the interval

`4q/3 < theta <= 2q`

is newly covered by this combination. At `q=1` it includes effective ridge dimension just above `4/3`, even when ordinary range leverage is one.

## 4. Explicit full-rank rotated indefinite target form

Take two banks of eight original coordinates each and one further original coordinate `X`. Let `H` be any normalized real `8x8` Walsh matrix. Put

`Sigma = diag(2,2,0.02,0.02,0.02,0.02,0.02,0.02)`,

`B = H Sigma H^T`,

and define the residual matrix

`S = [[0,B],[B,0]].`

Thus the residual eigenvalues are `+2,+2,-2,-2` together with twelve eigenvalues of modulus `0.02`. In particular the residual is indefinite, and its spectral directions are Walsh-rotated in the original product coordinates. The physical cross block `B` is full rank, so its ordinary range projection is the identity and the old `q=1` range-leverage gate fails maximally.

Let `h_1` be the first Walsh column in the first bank and take the linear shift

`m(Y)=0.1 <h_1,Y_I>`.

Define

`Q = 2 (X+m(Y))^2 + Y^T S Y`.                                   (4.1)

This is a genuinely coupled quadratic form in 17 independent original coordinates. To verify the target spectrum, compare its matrix with `diag(2,S)`. The coupling perturbation acts only on the span of `X` and the unit vector defining `m`, and has operator norm

`delta_A = (2/2) [0.1^2 + 0.1 sqrt(0.1^2+4)]`

`        = 0.210249843945... .`                                  (4.2)

The unperturbed matrix has three top eigenvalues all equal to `2`; Weyl therefore leaves three eigenvalues at least

`2-delta_A > 1.78975 >1`.                                       (4.3)

So (4.1) lies inside the exact target and is indefinite.

Now choose `gamma=1`, `q=1`. Since every normalized Walsh entry has squared modulus `1/8`, every ridge diagonal is `theta/8`, where

`theta = 2*(4/5) + 6*(0.02^2/(1+0.02^2))`

`      = 1.6023990403838466... .`                                (4.4)

Hence

`max diag K_gamma = 0.2002998800479808... <1/2`,

while

`4/3 < theta < 2`.                                                (4.5)

Thus the direct ridge `L^1` theorem does **not** apply at this certificate, while Theorem 3 does. Moreover

`D = 25*(1.0004)^6 = 25.060060032009595... .`                    (4.6)

Substituting `a=2`, `gamma=1` into (3.3) yields the explicit target-level estimate

`boxed: ||p_Q||_inf <= 6.9296917991.`                             (4.7)

For comparison, the preceding unconditional `q=2,k=3` elementary-symmetric route on the same cross singular values gives about `21.916`; the new one-scale ridge/square combination does not pay the six tiny full-rank directions through an `E_3` reciprocal.

## 5. Structural consequence for the full problem

The fresh spectral-window theorem already closes the branch in which

`P = 1_{|A|>=1/64}`

has `max_i P_ii<=1/32`, with density `<64`. If this fails, choose `i` with `P_ii>1/32`. Then

`||A e_i||_2^2 = sum_alpha lambda_alpha^2 |u_alpha(i)|^2
               > 1/(64^2*32) = 1/131072.`                       (5.1)

Writing `a=A_ii` and `b=A[i, i^c]`, (5.1) implies the exact original-coordinate dichotomy

`boxed: max(|a|, ||b||_2) >= 1/512.`                              (5.2)

Indeed if both were `<1/512`, then `a^2+||b||_2^2<2/512^2=1/131072`, contradiction.

So, after the diffuse spectral-window branch, every unresolved matrix supplies either a quantitatively nontrivial physical square or a quantitatively heavy physical off-diagonal bank. The new Theorem 3 says that in the square branch it is enough to find a residual physical cross block whose **ridge** leverage is admissible and whose effective dimension is only `>4q/3`; one no longer needs ordinary range leverage or direct-ridge effective dimension `>2q`.

The first unpaid implication is therefore sharpened to

`QFORM-RIDGE-SQUARE-OR-HEAVY-BANK-ROUTING-v1`:

> Starting from the heavy-window coordinate furnished by (5.2), prove that either its nontrivial scalar square can be paired with a residual physical cut satisfying the Theorem 3 ridge certificate at a universal scale, or the heavy off-diagonal bank can be converted by the already completed aggregate hyperbolic/fresh-square mechanisms into a universal density bound. A source-valid counterexample to such an exhaustive routing would also be decisive.

This is a structural, not analytic, remaining step. Full QFORM remains OPEN.

## 6. Exact computation used

The following code was used only to evaluate the constants in Section 4 and the comparison value.

```python
import math

q=1.0
a=2.0
s=2.0
eps=0.02
gamma=1.0
m=8
delta=0.1

theta = 2*s*s/(gamma*gamma+s*s) + (m-2)*eps**2/(gamma*gamma+eps**2)
D = (1+s*s/gamma**2)**2 * (1+eps**2/gamma**2)**(m-2)
ridge_diag = theta/m

C0 = 8 * 3**(-5/8) * math.sqrt(math.e) * q**(-1/4)
ratio = math.sqrt(3*theta/(3*theta-4*q))
fine = C0 * D**(-1/(4*theta)) * ratio / math.sqrt(abs(a)*gamma)
coarse = (8 * 3**(-5/8) * math.e**0.25 * q**(-1/4)
          * ratio / math.sqrt(abs(a)*gamma))

perturb_norm = a/2*(delta**2 + delta*math.sqrt(delta**2+4))
weyl_large_eig_lower = 2 - perturb_norm

print(f"theta={theta:.15f}")
print(f"ridge_diag={ridge_diag:.15f}")
print(f"D={D:.15f}")
print(f"threshold_4q_over_3={4*q/3:.15f}")
print(f"direct_L1_threshold_2q={2*q:.15f}")
print(f"fine_bound={fine:.15f}")
print(f"coarse_bound={coarse:.15f}")
print(f"coupling_perturbation_norm={perturb_norm:.15f}")
print(f"weyl_large_eigenvalue_lower={weyl_large_eig_lower:.15f}")

assert ridge_diag < 0.5
assert theta > 4*q/3
assert theta <= 2*q
assert fine < 6.93
assert weyl_large_eig_lower > 1
```

Output:

```text
theta=1.602399040383847
ridge_diag=0.200299880047981
D=25.060060032009595
threshold_4q_over_3=1.333333333333333
direct_L1_threshold_2q=2.000000000000000
fine_bound=6.929691799078116
coarse_bound=8.920803819056266
coupling_perturbation_norm=0.210249843945008
weyl_large_eigenvalue_lower=1.789750156054992
```

No simulation or histogram is used as proof. No full-solution, continuity, novelty, or independent-review claim is made.
