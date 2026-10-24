SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B01, 2026-09-23T12:29:22Z.
attacking: overlap-one exterior mass at a common physical hub, converting it into an averaged-frequency one-hub plus rank-one-leaf certificate before any tiny 3x3 minor is inverted.

# account01/B01 — overlap-one exterior star -> mixed-Fresnel density compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T122922Z-account01-B01-qform-auto11`  
Assignment: oscillatory replacement  
Status: **NEW EXACT STRUCTURAL BRIDGE + CONTINUOUS-DENSITY SUPPORTING THEOREM / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source and correction boundary

Fresh control was read from `yspennstate/math-research-brain` main; immediately before publication main was `4a6ac0f331a8c084566bf20dfba255890845edaf`, OWNER CONTROL remained revision `2026-09-22.15`, all research remained QFORM-only, and no B01 stop/pause was present. The live correction inbox was reread. In particular:

* bounded one-dimensional input densities do **not** imply any positive-power law-uniform pointwise decay for a scalar quadratic phase;
* spectral rotation does not preserve independence;
* arbitrary-joint coarea and positive conditional-density-moment shortcuts are unavailable;
* tiny individual coordinate minors may not be inverted before aggregate product structure is spent.

The phase-aligned fragmented-support counterexample therefore remains fully preserved. The result below uses a joint two-dimensional Fresnel/Brascamp--Lieb integral and yields an `L^1(dt)` characteristic-function envelope only after the hub and a rank-one leaf direction are treated together.

The analytic source used below is Theorem MF from the pinned Fourier package

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.

The designated partner result actually applied is account02/B01 r42,

`yspennstate/math-open-problems@2aa47367766e1b63306bec723c42fcd2899ca6ac`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260923T120442Z-account02-B01-qform-r42/REPORT.md`,

whose new exterior-overlap decomposition isolates `W_1` as a genuine remaining channel and computes the exact strict-N3 hub-square model with

`(W_0,W_1,W_2,W_3)=(0,(1-1/m)^2,2(m-1)/m^2,1/m^2)`.

## 2. Scoped setup

Fix one ORIGINAL physical coordinate `h`, a disjoint original-coordinate leaf bank `L`, and condition on all remaining original coordinates `K`. The conditioning creates only affine/constant terms in `(X_h,X_L)`, which will be kept arbitrary.

Assume that the quadratic block on `L` has the form

`A[L,L] = D + lambda z z^T`,                                      (2.1)

where `D` is an arbitrary real diagonal matrix, `lambda != 0`, and `||z||_2=1`. Put

`a=A_hh`, `b=A[L,h]`, `R=[b,z]` (an `|L| x 2` matrix),
`Gamma=R^T R`, `E=det Gamma`.                                     (2.2)

No condition is imposed on `a`, the entries of `D`, their signs/sizes, any conditioning-generated affine terms, or any coefficients wholly inside the conditioned bank.

Assume `E>0`. For row `r_i=(b_i,z_i)` define the normalized rank-two leverage

`ell_i = r_i^T Gamma^{-1} r_i`.                                   (2.3)

The analytic branch proved below assumes

`max_i ell_i <= 1/2`.                                              (2.4)

This is a product-coordinate diffuseness condition on the **augmented hub-slope/rank-one-square frame**, not an eigenvector rotation.

## 3. Exact overlap-one border-minor identity

For an unordered physical pair `P={p,q} subset L`, define

`theta_P = b_p z_q - b_q z_p`.                                    (3.1)

By Cauchy--Binet,

`boxed: E = det(R^T R) = sum_{|P|=2} theta_P^2.`                   (3.2)

Now take disjoint physical pairs `P,Q subset L`. Because `P cap Q` is empty, the diagonal block `D[P,Q]` vanishes identically, so

`A[P,Q] = lambda z_P z_Q^T`                                       (3.3)

has rank one. Expanding the bordered `3 x 3` determinant gives the exact identity

`boxed:
 det A[{h} union P, {h} union Q]
 = -lambda theta_P theta_Q.`                                      (3.4)

In particular the hub diagonal `a=A_hh` cancels completely from every overlap-one disjoint border minor in this class.

Define the ordered overlap-one star localized at `(h,L)` by

`W1(h;L) = sum_{P,Q subset L, |P|=|Q|=2, P cap Q=empty}
             det A[{h} union P,{h} union Q]^2.`                    (3.5)

Then

`boxed:
 W1(h;L)=lambda^2 sum_{P cap Q=empty} theta_P^2 theta_Q^2
        <= lambda^2 E^2.`                                         (3.6)

Thus a large overlap-one exterior star forces large **aggregate** mixed hub/square area `|lambda|E`, without selecting one physical 3x3 minor:

`boxed: |lambda| E >= sqrt(W1(h;L)).`                              (3.7)

There is also an exact probability identity. If

`p_P=theta_P^2/E`

is the natural rank-two volume law on leaf pairs, its row marginals are exactly the leverages `ell_i`, and for independent `P,Q~p`,

`boxed:
 W1(h;L)/(lambda^2 E^2)
 = P(P cap Q=empty)
 = 1 - sum_i ell_i^2 + sum_P p_P^2.`                               (3.8)

This identity records precisely what the still-unpaid heavy-leverage endpoint means inside the overlap-one channel.

## 4. Self-contained mixed-Fresnel estimate

For one original leaf density `f_i<=1`, write its twisted transform

`g_i(s,tau)=int f_i(y) exp(i s y^2+i tau y) dy.`                    (4.1)

The pinned source proves uniformly in `s` that for every real `p>=2`,

`int_R |g_i(s,tau)|^p d tau <= 4 pi/sqrt(p).`                      (4.2)

Condition on `X_K=k`. Suppress the resulting affine shifts. Regularized Fresnel linearization of the rank-one term gives, after taking absolute values,

`|phi_k(t)|
 <= (4 pi |t lambda|)^(-1/2)
    int f_h(x) int_R prod_{i in L}
       |g_i(t d_i, c_i(t,k)+2t b_i x+z_i xi)| dxi dx.`             (4.3)

The hub self-phase `exp(it a x^2)` and all hub affine phases have modulus one and disappear only **after** the exact product representation (4.3) is formed.

Put `u=2tx`; since `f_h<=1`,

`|phi_k(t)|
 <= (4 pi |t lambda|)^(-1/2)(2|t|)^(-1)
    int_R2 prod_i |g_i(t d_i,c_i+<r_i,(u,xi)>)| du dxi.`           (4.4)

Normalize the two-dimensional row system by `Gamma`. The rows

`rtilde_i = r_i Gamma^(-1/2)`

satisfy

`sum_i rtilde_i rtilde_i^T=I_2`, `||rtilde_i||^2=ell_i`.           (4.5)

By (2.4), `1/ell_i>=2` whenever `ell_i>0`. Apply geometric Brascamp--Lieb with exponents `ell_i`; after rescaling the one-dimensional arguments, (4.2) gives

`int_R2 prod_i |g_i(...)| du dxi
 <= (4 pi)^2 E^(-1/2).`                                            (4.6)

Indeed each one-dimensional BL factor is at most

`ell_i^(-1/2) int |g_i|^(1/ell_i)
 <= ell_i^(-1/2) 4 pi sqrt(ell_i)=4 pi`,                           (4.7)

and `sum_i ell_i=2`.

Combining (4.4)-(4.6), uniformly in the conditioned outside coordinates,

`boxed:
 |phi_k(t)| <= 4 pi^(3/2) (|lambda|E)^(-1/2)|t|^(-3/2).`           (4.8)

Averaging over `K` preserves the same bound. Together with `|phi_Q(t)|<=1`,

`boxed:
 |phi_Q(t)| <= min{1,
   4 pi^(3/2) (|lambda|E)^(-1/2)|t|^(-3/2)}.`                      (4.9)

Using (3.7) gives the purely overlap-one form

`boxed:
 |phi_Q(t)| <= min{1,
   4 pi^(3/2) W1(h;L)^(-1/4)|t|^(-3/2)}.`                          (4.10)

This is the new averaged-frequency replacement. It is a joint packet estimate; it says nothing like `|E exp(itX^2)|<=C|t|^-1/2` for an arbitrary one-dimensional cap-one law.

## 5. Density theorem and exact constant

For `B>0`,

`int_R min(1,B|t|^(-3/2)) dt = 6 B^(2/3).`                         (5.1)

Fourier inversion applied to (4.9) therefore yields a bounded continuous density vanishing at infinity and

`||p_Q||_infinity
 <= (3/pi)[4 pi^(3/2)]^(2/3)(|lambda|E)^(-1/3)`
` = 3*2^(4/3)(|lambda|E)^(-1/3).`                                  (5.2)

Using (3.7):

### Theorem 5.1 — `QFORM-W1-HUB-RANK1-LEAF-FRESNEL-v1`

Under (2.1)-(2.4), including arbitrary hub self-curvature, arbitrary diagonal leaf curvature, arbitrary outside conditioning and arbitrary induced affine terms,

`boxed:
 ||p_Q||_infinity
 <= 3*2^(4/3) W1(h;L)^(-1/6)
 = 7.559526299369239... W1(h;L)^(-1/6).`                            (5.3)

Moreover `phi_Q in L^1(R)`, so this theorem proves a **continuous `C_0` density**, not merely an essential bound.

Scaling check: every bordered `3x3` determinant scales cubically in `A`, hence `W1` scales as `|c|^6`; the exponent `-1/6` gives the required density scale `|c|^-1`.

## 6. Actual application of the designated partner r42 result

Account02/B01 r42 constructs the strict-N3 family

`Q_m = 2 X_0(a^T Y) + (z^T Z)^2`,                                 (6.1)

where `Y,Z` are disjoint size-`m` original-coordinate banks and `a,z` are flat unit vectors. It proves

`W0=0`, `W1=(1-1/m)^2`, `W2=2(m-1)/m^2`, `W3=1/m^2`,              (6.2)

while the nonzero spectrum is exactly `{-1,1,1}`.

Apply Theorem 5.1 with hub `h=0`, leaf bank `L=Y union Z`,

`b=(a,0)`, `ztilde=(0,z)`, `lambda=1`, `D=0`.                     (6.3)

Then

`Gamma=I_2`, `E=1`, and every augmented leverage equals `1/m`.     (6.4)

Thus for every `m>=2` the direct mixed-Fresnel currency gives

`boxed: ||p_(Q_m)||_infinity <= 3*2^(4/3)=7.55952629937...`        (6.5)

for every admissible independent cap-one input law, with a continuous `C_0` density.

Using **only the partner's overlap-one exterior value** in (6.2), (5.3) independently gives

`boxed:
 ||p_(Q_m)||_infinity
 <= 3*2^(4/3)(1-1/m)^(-1/3).`                                     (6.6)

For example, for `m>=8` this is `<7.904`. Equation (6.6) is an actual application of the completed designated-partner r42 structural result to a new inequality. It also verifies that the r42 `W1`-dominated endpoint is exactly the type of exterior currency measured by Theorem 5.1.

## 7. What this does and does not close

The partner r42 decomposition shows that after the already-paid disjoint-volume branch, a genuine global survivor may satisfy

`W1+W2+W3 > 3/4`.

Theorem 5.1 now completely pays the following nontrivial overlap-one subclass:

* a common original physical hub `h`;
* after conditioning all other coordinates, the active leaf curvature is `diagonal + rank one`;
* the augmented hub-slope/rank-one-square frame has leverage at most `1/2`.

No individual overlap-one `3x3` minor is required to be large; the theorem spends their whole squared star through (3.6).

The first unpaid implication is therefore sharpened to

`QFORM-W1-HEAVY-LEVERAGE-OR-HIGHER-LEAF-RANK-v1`:

starting from large global `W1`, either route a constant fraction into a common-hub star whose leaf Schur/Fresnel remainder is diagonal plus rank one with augmented leverage <=1/2 (now paid), or show that heavy augmented leverage / higher leaf rank quantitatively enters an already-paid pair, ridge, grouped-source, volume, or near-coloop receiver. The new exact diagnostic (3.8) should be retained in that routing; it identifies the heavy-row obstruction without selecting a tiny `3x3` minor.

This report does **not** prove that every `W1`-heavy matrix has the rank-one-leaf structure or the leverage condition. It therefore does not close the unrestricted conjecture.

## 8. Finite algebra check

A direct symbolic expansion gives

`det [[a,c1,c2],[b1,lambda p1 q1,lambda p1 q2],[b2,lambda p2 q1,lambda p2 q2]]
 = -lambda (b1 p2-b2 p1)(c1 q2-c2 q1)`,                           (8.1)

which is (3.4). Seeded random matrix checks also verified to machine precision:

* the determinant identity (3.4);
* `E=sum theta_P^2=det(R^T R)`;
* the probability identity (3.8).

These checks are sanity evidence only; the proof above is algebraic/analytic.

## 9. Status

Full QFORM: **OPEN**.  
This theorem: **proved supporting theorem in its stated original-coordinate scope**.  
Continuity: **proved in this scope** via the uniform `L^1` characteristic-function bound.  
Phase-aligned pointwise counterexample: **preserved**.  
Native brain ingestion: **not verified; repository retrieval/writeback only**.