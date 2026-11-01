SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B10, 2026-09-24T05:34:42Z.
attacking: the exact-rank-three near-coloop two-sheet survivor; test whether the newest disjoint partner/hard-square certificate can be converted into a clean or regression-clean ORIGINAL source bank, while consuming the ruled one-sheet theorem rather than repeating it.

# fleet02/B10 — a harmonic near-coloop frame simultaneously defeats clean-square and exact-regression extraction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T053442Z-fleet02-B10-QFORM-auto11`  
Status: `NEW_STRUCTURAL_INTERFACE_COUNTEREXAMPLE / PARTNER_HARD_SQUARE_APPLIED / RULED_SIDE_PAID / ALL_FINITE_LP_CERTIFIED / FULL_EXACT_RANK3_OPEN / FULL_QFORM_OPEN`.

## 1. Source boundary and first unpaid implication


The latest compatible fleet03/B10 algebra is the r32 transverse-curvature calculation at

`yspennstate/math-open-problems@c97e404492dc02e28ee6c465c4328df3afe22d70`

with deterministic verifier/check output through `c1b9d3e30df05f6b27df2b0bc0431475448a0a57`. Its exact consequence for

`M=[[alpha,s,0],[s,b,k],[0,k,d]]`, `sigma_min(M)>=1`, `|alpha|<1`,

is

`(alpha^2+s^2-1)(d^2-1) >= (1-alpha^2)k^2`,                         (1.1)

hence `|d|>=1`. The newest completed full partner report used here is fleet03/B10 r29,

`yspennstate/math-open-problems@fa694dbcc9a8e70293a5120263fabe67e5f1465b`,

which in the diffuse near-coloop collar additionally supplies disjoint ORIGINAL banks `U,V` with

`||r_U||_2^2>1/202`, `||y_V||_2^2>=1/162`, and

`|d| ||r_U||_2^2 ||y_V||_2^2 >1/32724`.                              (1.2)

The first unpaid implication tested in this run is therefore sharply:

`QFORM-HARD-SQUARE-THREEWAY-CONTAMINATION-RECEIVER-v1`:

> Starting from the endpoint-stable partner/hard-square certificate (1.2), prove the two-sheet density bound while the square-heavy bank still carries genuinely non-negligible hub-partner and third-projection coefficients. Do not replace that same-bank overlap by independence, a fiber supremum, exact regression, or deletion of a small coefficient times an unbounded variable.

The calculation below shows that neither of the two obvious ways to discharge this implication — extracting a clean square bank or extracting an exact regression-clean reservoir — follows from the current deterministic geometry, even in a maximally regular diffuse Fourier frame.

## 2. Exact target-valid harmonic family

Fix an odd integer `m>122` and

`theta_j=2*pi*j/m`, `j=0,...,m-1`.

Define normalized leaf coefficient vectors

`r_j=sqrt(2/m) cos(theta_j)`,
`y_j=sqrt(2/m) sin(theta_j)`,
`z_j=sqrt(2/m) cos(2 theta_j)`.                                      (2.1)

Discrete Fourier orthogonality gives

`||r||_2=||y||_2=||z||_2=1`,
`r perpendicular y`, `r perpendicular z`, `y perpendicular z`.      (2.2)

For `0<rho<1/64`, put `c=1-rho` and take the physical spectral rows

`u_0=sqrt(c)e_1`,
`u_j=sqrt(rho) z_j e_1+r_j e_2+y_j e_3`, `0<=j<m`.                  (2.3)

By (2.2), the three columns of the resulting `(m+1) x 3` matrix `R` are orthonormal. Take

`M_0=[[0,1,0],[1,0,0],[0,0,1]]`.                                    (2.4)

Then

`A=R M_0 R^T`                                                        (2.5)

has exactly the three nonzero eigenvalues `{1,-1,1}`. Every leaf has transverse leverage

`r_j^2+y_j^2=2/m<1/61`,                                              (2.6)

so this lies in the genuinely diffuse near-coloop chamber. No projected variables are declared independent.

For arbitrary independent ORIGINAL inputs with densities at most one, write

`H=X_0`, `Z=z.X_L`, `L=r.X_L`, `V=y.X_L`.

The quadratic form is exactly

`boxed: Q=2(sqrt(c)H+sqrt(rho) Z)L+V^2.`                              (2.7)

Thus the longitudinal leakage, hub partner and hard square use three orthogonal coefficient vectors on the same ORIGINAL leaf bank.

In the fleet03/B10 adapted notation this family has

`alpha=0`, `s=1`, `b=k=0`, `d=1`, `gamma=theta=1`, `eta=0`.          (2.8)

Consequently the newest hard-square inequality (1.1) is attained at its exact endpoint:

`alpha^2+s^2-1=0`, `k=0`, `|d|=1`.                                  (2.9)

The r29 hub-pencil quantity is also completely nondegenerate:

`D_H=-s^2 det(M_0)/(d gamma^4)=1`.                                  (2.10)

So the family below is not exploiting a weak matrix coefficient. The only issue is source overlap.

## 3. Theorem — clean-square and exact-regression extraction fail simultaneously

### Theorem 3.1 — `QFORM-HARMONIC-SIMULTANEOUS-EXTRACTION-BARRIER-v1`

For the target family (2.3)-(2.7):

1. Every ORIGINAL subset `I` obeys the quantitative contamination inequality

   `boxed:
   ||r_I||_2^2+||z_I||_2^2
   >=(4 sqrt(2)-5)||y_I||_2^2.`                                    (3.1)

   Hence no nonempty square bank is clean in both the hub-partner and longitudinal directions. More strongly, any bank with

   `||y_I||_2^2>=1/162`

   necessarily satisfies

   `||r_I||_2^2+||z_I||_2^2
    >=(4sqrt(2)-5)/162
    >0.0040546.`                                                     (3.2)

2. If an ORIGINAL subset `I` is exact-regression-clean for the endpoint receiver, i.e. for some constants `gamma,eta`

   `sqrt(rho) z_j=gamma r_j+eta y_j` for all `j in I`,               (3.3)

   then `|I|<=4`. For its transverse Gram

   `G_I=sum_(j in I)(r_j,y_j)^T(r_j,y_j)`,                            (3.4)

   one has

   `boxed: det G_I <=16/m^2.`                                        (3.5)

Therefore, as `m->infinity`, every exact-regression-clean reservoir has vanishing two-dimensional transverse volume, while every square-heavy bank retains a fixed positive amount of the two forbidden contaminating directions.

#### Proof of (3.1)

Remove the common factor `2/m` from (2.1) and put `x=cos^2(theta_j)`. Then

`cos^2(theta_j)+cos^2(2theta_j)
 -(4sqrt(2)-5)sin^2(theta_j)`

`=x+(2x-1)^2-(4sqrt(2)-5)(1-x)`

`=4(x-(1-sqrt(2)/2))^2 >=0`.                                        (3.6)

Multiply by `2/m` and sum over `j in I`. This proves (3.1), and (3.2) is immediate.

#### Proof of the exact-regression bound

Since `rho>0`, (3.3) is equivalent after rescaling the constants to

`cos(2theta_j)=a cos(theta_j)+b sin(theta_j)` for every `j in I`.   (3.7)

The function

`F(theta)=cos(2theta)-a cos(theta)-b sin(theta)`                    (3.8)

is a nonzero real trigonometric polynomial of degree two. It cannot vanish identically because its second Fourier mode has nonzero coefficient, whereas the right side of (3.7) only has first modes. A nonzero degree-two trigonometric polynomial has at most four zeros in one period. The `theta_j` are distinct, so `|I|<=4`.

Finally `r_j^2+y_j^2=2/m` pointwise, hence

`tr G_I=2|I|/m<=8/m`.                                                (3.9)

For a positive semidefinite `2x2` matrix, `det G_I<=(tr G_I/2)^2`; therefore `det G_I<=16/m^2`. QED.

### Consequence for the two existing endpoint interfaces

The regression-clean receiver proved previously in fleet02/B10 has a cost proportional to `(det G_I)^(-1/2)`. On this family every legal exact-regression reservoir therefore forces that factor to be at least `m/4`, so the resulting estimate cannot be uniform in dimension.

Conversely, the clean-square / one-sided mixed-bank theorems require an ORIGINAL square bank on which both the hub-partner and longitudinal coefficients vanish. Equation (3.1) shows that the only such bank is empty. Even an attempted perturbative replacement is not produced by the partner bank extraction: at the partner threshold `||y_V||^2>=1/162`, the contamination stays above the fixed constant (3.2), independent of `m`.

This is a counterexample to those two **extraction implications**, not to QFORM.

## 4. Newest fleet03/B10 partner result applied at an actual obstruction

Apply the completed r29 disjoint-bank certificate (1.2) to the family (2.7). Because (2.8) identifies the partner frame exactly with the harmonic `(r,z,y)` frame, there are disjoint ORIGINAL banks `U,V` such that

`||r_U||_2^2>1/202`,
`||y_V||_2^2>=1/162`,
`|d|=1`.                                                             (4.1)

The new inequality (3.1) then forces on that **same guaranteed square bank**

`boxed:
 ||r_V||_2^2+||z_V||_2^2
 >=(4sqrt(2)-5)||y_V||_2^2
 >=(4sqrt(2)-5)/162.`                                                 (4.2)

Thus the newest partner theorem is genuinely consumed here: its hard square and disjoint source partner survive, but the theorem cannot be completed by silently upgrading `V` to a source-independent square bank. The obstruction is quantitative and endpoint-stable; it persists with `d=1`, `D_H=1`, and row leverage `2/m->0`.

The even newer r32 hard-curvature identity (1.1) is also spent at the exact family: (2.9) shows that the hard square is already at the sharp floor `|d|=1`. There is no hidden surplus `d^2-1` available to absorb (4.2).

## 5. Required pinned ruled-side theorem applied to the same family

At the required source pin

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`COUNTEREXAMPLE_SEARCH.md` proves the dimension-free ruled-level-set theorem for signature `(2,1)`: if the three spectral eigenvalue moduli are at least one, then on the majority-sign one-sheet side

`p_Q(s)<=pi sqrt(2)`.                                                  (5.1)

The family (2.5) has spectrum `{1,1,-1}` after ordering signs, so the completed source theorem gives the real target inequality

`boxed: p_Q(s)<=pi sqrt(2)<4.443 for every s>=0.`                    (5.2)

No part of (5.2) is reproved here. Its proof in the pinned source uses line integrals of genuine product-measure marginals and does not declare the spectral projections independent.

Therefore any remaining endpoint failure for this harmonic family is confined to the genuine two-sheet side `s<0`.

## 6. The family already has every finite Lp bound; only the endpoint remains

A useful compatible completed input is fleet01/B10's

`QFORM-INDEPENDENT-HYPERBOLIC-LP-ENDPOINT-v1`

at `yspennstate/math-open-problems@aa9a9649b577588afab22b1995f080bbd0478f7f`. It states that if `H` is independent of all nonhub variables, `Y` has density cap `K_Y`, and

`Q=alpha H Y+S`

with `S` an arbitrary measurable function of the nonhub variables, then for every `p>1`

`||p_Q||_p <=p [2K_H K_Y/|alpha|]^(1-1/p).`                          (6.1)

Apply this directly to (2.7) with

`alpha=2sqrt(c)`, `Y=L`,
`S=2sqrt(rho)ZL+V^2`, `K_H<=1`.                                     (6.2)

The coefficient vector `r` has Euclidean norm one, so the scalar product-marginal bound gives `K_L<=sqrt(2)`. Hence

`boxed:
 ||p_Q||_p
 <=p (sqrt(2)/sqrt(c))^(1-1/p),  p>1.`                              (6.3)

Since `c>63/64`, in particular

`||p_Q||_3<3.800`.                                                    (6.4)

The same theorem gives the uniform small-ball estimate

`P(Q in I)
 <= e A_0 |I| log(1/(A_0|I|))`,
`A_0=sqrt(2)/sqrt(c)<1.426`,                                        (6.5)

for sufficiently short intervals. Thus the harmonic survivor is already absolutely continuous with all finite `L^p` norms uniformly controlled. Combined with (5.2), the missing content is literally an `L^infinity` endpoint on `s<0`, not an absolute-continuity or power-law anti-concentration gap.

## 7. What is now genuinely unpaid

The simultaneous barrier (3.1)-(3.5) rules out the two most direct ways of converting the current partner geometry into an endpoint theorem:

- exact regression cannot retain a uniformly nondegenerate transverse Gram;
- a square-heavy source bank cannot be made clean, or even asymptotically clean in coefficient energy, by dimension growth.

The next implication should therefore be stated without either hidden simplification:

`QFORM-HARMONIC-THREE-DIRECTION-TWOSHEET-RECEIVER-v1`:

> For the exact-null near-coloop form
+> `Q=2(sqrt(c)H+sqrt(rho)Z)L+V^2`,
+> where `(r,z,y)` are orthonormal ORIGINAL leaf coefficient vectors, every physical transverse leverage is small, and the square bank may carry a fixed fraction of both `r` and `z` energy, prove a universal essential density bound on the two-sheet side using the original product law. The receiver must retain the three same-bank linear forms jointly; it may not demand exact regression, a clean square bank, post-rotation independence, a fiber supremum, finite moments/support, or a small-random-perturbation argument.

A proof of this statement for the harmonic family would attack the precise source-overlap phenomenon left after fleet03/B10 r29/r32. A counterexample with admissible cap-one sources would be a genuine QFORM counterexample, so no such claim is made here.

## 8. Status

- New theorem: `QFORM-HARMONIC-SIMULTANEOUS-EXTRACTION-BARRIER-v1`, equations (3.1)-(3.5).
- New actual partner obstruction: equation (4.2).
- Required pinned source theorem spent at the actual density inequality (5.2).
- Exact target family: arbitrary independent source densities `<=1`, exact nonzero spectrum `{1,-1,1}`, no moment/support/log-concavity assumption, no post-rotation independence.
- Full arbitrary exact-rank-three theorem: **OPEN**.
- Full owner QFORM theorem: **OPEN / not proved / not disproved**.
- Continuity: not claimed here beyond what cited completed results establish for their own scope.
