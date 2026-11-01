SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B18, 2026-09-23T12:59:02Z.
attacking: a rank-two physical cross bank plus one independent scalar-to-bank slope, using LPP projection caps and two exact Plancherel gains to obtain an integrable |t|^{-3/2} characteristic-function envelope; then apply fleet04/B18 square smoothing.

# fleet03/B18 r29 — rank-two cross plus scalar-slope Fresnel closure

Status: **SUPPORTING TARGET-LEVEL THEOREM PROVED / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**.

Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact theorem

Let

- `Z` be a real random variable with a probability density `f_0` satisfying `0<=f_0<=1`;
- `X=(X_i)_(i in I)` and `Y=(Y_j)_(j in J)` be two finite, disjoint banks of independent real random variables, independent also of `Z`, with every one-dimensional density bounded by one;
- `F:R^I->R` and `G:R^J->R` be arbitrary measurable real functions (in the QFORM application they are arbitrary quadratic-plus-affine polynomials);
- `a,b in R`, `c in R^I\{0}`;
- `B:R^J->R^I` have rank exactly two, with nonzero singular values `sigma_1,sigma_2`, and set `Delta=sigma_1 sigma_2`.

Consider

`Q = a Z^2 + b Z + 2 Z c^T X + F(X) + G(Y) + 2 X^T B Y.`                 (1.1)

Then `Q` has a continuous density vanishing at infinity and

`boxed:
 ||p_Q||_infinity <= 3*2^(5/6) ( ||c||_2 Delta )^(-1/3).
`                                                                            (1.2)

Numerically `3*2^(5/6)=5.345392308842036...`.

Equivalently, its characteristic function satisfies for every `t!=0`

`|phi_Q(t)| <= 2^(5/4) pi^(3/2)
               ||c||_2^(-1/2) Delta^(-1/2) |t|^(-3/2).`              (1.3)

The theorem is uniform in `a,b,F,G`. In particular, arbitrary same-side quadratic curvature in both banks survives. It makes no pointwise claim about a one-dimensional quadratic phase alone.

### Ambient conditioning form

The same estimate holds after conditioning on any further original coordinates, provided the active conditional quadratic polynomial has the form (1.1) with the same `c,B`: outside couplings only change `b,F,G` and the additive constant. Thus the estimate can be inserted literally into a larger quadratic-form proof whenever this product-preserving packet occurs.

## 2. Primary literature input, with hypotheses matched

Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889; arXiv:1507.07949, proves that if

`f(x)=prod_i f_i(x_i)`, `int f_i=1`, and `||f_i||_infinity<=1`,

then every `k`-dimensional orthogonal marginal has density bounded by `2^(k/2)`.

Only this theorem is imported. Its hypotheses match the owner target exactly: product independence and one-dimensional density caps. It assumes no Gaussianity, log-concavity, moments, compact support, connected support, smoothness, centering, or identical distribution.

Two consequences used below are:

1. if `S=c^T X`, then

`||p_S||_infinity <= sqrt(2)/||c||_2`;                                  (2.1)

2. for every matrix `P` with two orthonormal columns, the density of `P^T X` is at most `2`, and likewise for a two-dimensional orthogonal projection of `Y`.       (2.2)

No rotated coordinates are asserted independent. The theorem is used only to bound their joint projection densities.

## 3. First Plancherel gain: arbitrary scalar quadratic phase plus a random slope

For fixed `t!=0`, define

`A_t(s)=int_R f_0(z)
        exp(i t [a z^2+b z+2 z s]) dz.`                                  (3.1)

Let `h_t(z)=f_0(z) exp(i t[a z^2+bz])`. With Fourier convention

`hat h(xi)=int exp(i xi z) h(z) dz`,

we have `A_t(s)=hat h_t(2ts)`. Plancherel gives

`int_R |A_t(s)|^2 ds
 = (1/(2|t|)) int_R |hat h_t(xi)|^2 dxi
 = (pi/|t|) ||h_t||_2^2
 <= pi/|t|`,                                                            (3.2)

because `|h_t|=f_0`, `f_0<=1`, and `int f_0=1`, hence `||f_0||_2^2<=1`.

Now `S=c^T X` has density cap (2.1), so

`E_X |A_t(c^T X)|^2
 <= (sqrt(2)/||c||_2) int |A_t(s)|^2 ds
 <= pi sqrt(2)/( |t| ||c||_2).`                                          (3.3)

Therefore

`(E_X |A_t(c^T X)|^2)^(1/2)
 <= 2^(1/4) pi^(1/2) ||c||_2^(-1/2) |t|^(-1/2).`                 (3.4)

This is an averaged `L^2` statement. The live phase-aligned-support correction forbids replacing it by a law-uniform pointwise van-der-Corput bound, and no such replacement is made.

## 4. Second Plancherel gain: the rank-two cross bank

Take a thin singular-value decomposition

`B=P Sigma R^T`,

where `P` and `R` have two orthonormal columns and

`Sigma=diag(sigma_1,sigma_2)`.

For fixed `t`, push the complex measure

`exp(i t G(y)) prod_(j in J) f_j(y_j) dy`

through `v=R^T y`; denote its complex density by `k_t(v)`. Its total variation is pointwise dominated by the ordinary projection density `p_(R^T Y)`. Hence by (2.2)

`|k_t(v)|<=p_(R^T Y)(v)`,
`||k_t||_1<=1`, `||k_t||_infinity<=2`, and therefore `||k_t||_2^2<=2`.  (4.1)

Define

`Y_t(x)=E_Y exp(i t [G(Y)+2 x^T B Y]).`                                 (4.2)

Then

`Y_t(x)=hat k_t(2t Sigma P^T x).`                                       (4.3)

Let `U=P^T X`. Its joint density is at most `2` by (2.2). Two-dimensional Plancherel and the change of variables `xi=2t Sigma u` therefore give

`E_X |Y_t(X)|^2
 <= 2 int_(R^2) |hat k_t(2t Sigma u)|^2 du`
` = [2/(4 t^2 Delta)] int_(R^2) |hat k_t(xi)|^2 dxi`
` = [2/(4 t^2 Delta)] (2pi)^2 ||k_t||_2^2`
` <= 4 pi^2/(t^2 Delta).`                                               (4.4)

Thus

`(E_X |Y_t(X)|^2)^(1/2)
 <= 2 pi |t|^(-1) Delta^(-1/2).`                                        (4.5)

This step preserves arbitrary `G`; its phase appears only in `k_t` and has modulus one.

## 5. Joint characteristic-function bound

Integrate first in `Z` and `Y`. Since the remaining factor `exp(i t F(X))` has modulus one,

`phi_Q(t)
 = E_X [ exp(i t F(X)) A_t(c^T X) Y_t(X) ].`                             (5.1)

Cauchy--Schwarz in the ORIGINAL `X` bank, followed by (3.4) and (4.5), gives

`|phi_Q(t)|
 <= 2^(5/4) pi^(3/2)
    ||c||_2^(-1/2) Delta^(-1/2) |t|^(-3/2).`                            (5.2)

Write

`K=2^(5/4) pi^(3/2) ||c||_2^(-1/2) Delta^(-1/2).`

Together with `|phi_Q|<=1`,

`int_R |phi_Q(t)| dt
 <= int_R min(1,K|t|^(-3/2)) dt
 = 6 K^(2/3).`                                                          (5.3)

The crossover is `|t|=K^(2/3)`. Fourier inversion gives

`||p_Q||_infinity
 <= (1/(2pi)) 6 K^(2/3)
 = 3*2^(5/6) (||c||_2 Delta)^(-1/3),`                                   (5.4)

which is (1.2). Since `phi_Q in L^1`, Fourier inversion supplies a continuous representative in `C_0(R)`. QED.

## 6. Diffuse strict-no-pair target family paid uniformly

The theorem is not merely a fixed small-dimensional example. For any integer `m>=1`, take an `X` bank and a `Y` bank, each of size `2m`, split into two disjoint groups of size `m`. Let

`p_1=1_(I1)/sqrt(m)`, `p_2=1_(I2)/sqrt(m)`,
`r_1=1_(J1)/sqrt(m)`, `r_2=1_(J2)/sqrt(m)`,

so each pair is orthonormal. Set

`c=p_1`,
`B=p_1 r_1^T + p_2 r_2^T`,
`a=b=0`, `F=G=0`.

Then `||c||_2=1`, the two nonzero singular values of `B` are `1,1`, and therefore `Delta=1`. The active physical matrix, restricted to the orthonormal aggregate basis `(Z,p_1,p_2,r_1,r_2)`, is

`[[0,1,0,0,0],
  [1,0,0,1,0],
  [0,0,0,0,1],
  [0,1,0,0,0],
  [0,0,1,0,0]].`                                                       (6.1)

Its characteristic polynomial is

`lambda(lambda-1)(lambda+1)(lambda^2-2)`,

so the nonzero spectrum is exactly

`{-sqrt(2),-1,1,sqrt(2)}`.                                               (6.2)

Thus the owner target is satisfied (indeed four eigenvalues have magnitude at least one), for every `m`.

All physical diagonals are zero. A `Z-X` entry has magnitude at most `m^(-1/2)` and every `X-Y` entry has magnitude at most `m^(-1)`. Hence every physical `2x2` principal determinant has magnitude at most `1/m`. Given any prescribed `tau>0`, choosing `m>1/tau` places the family in an arbitrarily strict no-large-pair chamber, yet (1.2) gives the dimension-free continuous-density bound

`boxed: ||p_Q||_infinity <= 3*2^(5/6) < 5.346.`                           (6.3)

This is precisely an aggregate-before-selection effect: no uniformly large physical pair is needed.

## 7. Designated partner fleet04/B18 applied at an actual inequality

I read the underlying partner proof at

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`.

Its proved lemma `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1` states: if a residual `R` has density cap `M`, and conditionally on `R=r` a translated physical pivot variable has a density cap at most one, then

`R+d V_R^2`

has density cap at most

`2 sqrt(M/|d|)`,                                                        (7.1)

with no independence assumption between `R` and the translated pivot after completion of the square.

Apply (7.1) when a nonzero outer physical Schur pivot `d` has a residual of the form (1.1). Equations (1.2) and (7.1) give the concrete compiler

`boxed:
 ||p_Q||_infinity
 <= 2 sqrt(3*2^(5/6))
    |d|^(-1/2) (||c||_2 Delta)^(-1/6).
`                                                                            (7.2)

The numerical prefactor is `4.624020894780661...`.

A literal target-valid example is

`Q = W^2 + 2 W Z + 2 Z X_1 + 2 X_1 Y_1 + 2 X_2 Y_2.`                   (7.3)

Completing only the ORIGINAL physical pivot `W` gives

`Q=(W+Z)^2 + R`,
`R=-Z^2+2ZX_1+2X_1Y_1+2X_2Y_2.`                                       (7.4)

The residual has `a=-1`, `||c||=1`, `Delta=1`, hence (1.2) gives

`||p_R||_infinity<=3*2^(5/6)`.

Because `W` is independent of all residual variables, conditioning on the scalar `R` makes `W+Z` a mixture of translations of the cap-one density of `W`; this is exactly the partner lemma's hypothesis. Therefore

`boxed: ||p_Q||_infinity <= 2 sqrt(3*2^(5/6)) < 4.625.`                  (7.5)

The physical matrix in the order `(W,Z,X_1,X_2,Y_1,Y_2)` has characteristic polynomial

`(lambda-1)^2 (lambda+1) (lambda^3-3lambda-1).`                           (7.6)

Its eigenvalues are approximately

`{-1.5320888862,-1,-0.3472963553,1,1,1.8793852416}`,

so five eigenvalues have magnitude at least one. This verifies that the partner application is inside the exact owner target, not merely an auxiliary model.

The partner wrapper proves an essentially bounded density. I do **not** promote continuity through (7.1), because the partner lemma proves absolute continuity and an `L^infinity` bound but does not state continuity under its dependence-safe mixture hypothesis. The residual theorem itself does prove a continuous `C_0` density.

## 8. Relation to existing fleet results and remaining debt

A fresh repository check found related but different mechanisms:

- fleet01/B01's pair-wedge theorem obtains `|phi(t)|=O(|t|^-1)` from a two-coordinate random linear slope and then an `L^3`/fractional-potential square lift;
- fleet03/B09's grouped two-slope/one-Fresnel theorem obtains stronger decay when a rank-two cross bank coexists with a specific same-side rank-one curvature and a determinant-distributed basis certificate.

The theorem here has a different literal interface: an **independent scalar-to-one-bank linear slope** contributes the third half-power by one-dimensional Plancherel, while the rank-two cross bank contributes the other full power by two-dimensional Plancherel. It allows arbitrary `a,b,F,G` and requires neither a large physical minor nor a leverage/disjoint-basis condition. This report does not claim external novelty from the absence of an exact repository duplicate.

The unrestricted conjecture remains **OPEN / NOT PROVED**. The structural debt is to force or aggregate such a packet from the bare condition `s_3(A)>=1`, or route its failure to already-paid hub/ridge/grouped/near-coloop branches. In a general matrix the selected scalar may couple to both sides of a rank-two cross bank; (1.1) does not silently absorb that additional coupling. Arbitrary extra spectrum also remains part of the global compiler problem.

Full-target continuity remains open; continuity is proved only for theorem (1.1)'s stated scope.

## 9. Source integrity

Primary external theorem used:

Galyna Livshyts, Grigoris Paouris, Peter Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel Journal of Mathematics 216 (2016), 877--889, arXiv:1507.07949, DOI 10.1007/s11856-016-1431-5.

Designated partner theorem used:

`QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, fleet04/B18, immutable scientific source `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, exact report path given in Section 7.

No Gaussian/log-concavity/moment/support/iid assumption, post-rotation independence, arbitrary-joint coarea bound, conditional-cap-as-independence step, fixed-good-minor extraction, or law-uniform pointwise quadratic-phase decay is used.
