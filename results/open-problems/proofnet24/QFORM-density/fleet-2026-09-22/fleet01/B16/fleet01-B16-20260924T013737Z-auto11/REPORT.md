SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B16, 2026-09-24T01:37:37Z.
attacking: the innovation-free shared-square endpoint after the hub-phase and cross-square receivers; derive a source-preserving nonlinear Fourier/TT* inequality that stays uniform when the transverse puncture vanishes, and apply the newest completed fleet02/B16 result to an actual target inequality.

# fleet01/B16 — arbitrary cross-rank two-bank Fresnel receiver with exact hub-innovation currency

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `fleet01-B16-20260924T013737Z-auto11`  
**Role:** Projection-product interaction  
**Status:** `NEW SUPPORTING THEOREM + NEW SOURCE-GEOMETRIC EXIT + NEWEST PARTNER APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Regularity:** the new theorem gives a continuous density vanishing at infinity on its scope. Global continuity remains separate.

## 1. Source boundary and live corrections

Fresh owner control keeps the unrestricted quadratic-form problem as the sole target. The full statement remains **OPEN / NOT PROVED / NOT DISPROVED**: arbitrary independent original-coordinate inputs with densities at most one, arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, no moment/support/iid/log-concavity/smoothness assumptions, and no independence after spectral rotation.

The actual bounded-density projection theorem used below is the owner-pinned product-projection input already used by B16: for a full-row-rank `k x n` matrix `T` and an independent cap-one product vector `X`,

`||p_(T X)||_infinity <= 2^(k/2) / sqrt(det(T T^T)).`              (1.1)

The newest completed designated-partner artifact read before this report is fleet02/B16

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B16/20260924T012413Z-fleet02-B16-QFORM-auto11/REPORT.md`,

whose new theorem `QFORM-PHYSICAL-HUB-DEFINITE-DISCRIMINANT-v1` is applied at an actual target inequality in Section 7.

The corrections are retained throughout. In particular:

- no coordinate independence is inferred after projection;
- no arbitrary-joint indefinite coarea estimate is used;
- no conditional projection-density cap is inferred from a marginal cap;
- the authentic fleet03/B16 r38 hub-first half-trace divergence is respected;
- the projected density cap is spent only as a Hilbert `L^2` energy **before** nonlinear Fresnel integration.

## 2. New rank-r two-bank theorem

Let `r>=1`. Let `H`, source bank `A`, and source bank `B` be mutually independent. For `i=A,B`, let

`Y_i=(L_i,V_i) in R x R^r`

be a linear projection of bank `i`, with joint density `g_i` satisfying

`||g_i||_infinity <= M_i`.                                        (2.1)

Let `R_H(H)`, `R_A(X^A)`, and `R_B(X^B)` be arbitrary real measurable functions of their respective original source blocks. Let `Gamma` be an invertible symmetric `r x r` matrix and let `alpha!=0`. Put

`L=L_A+L_B`, `V=V_A+V_B`,

and consider

`Q = R_H(H) + 2 alpha H L + V^T Gamma V + R_A + R_B + affine`.     (2.2)

Assume the hub density satisfies `||f_H||_infinity<=L_H`.

### `QFORM-TWOBANK-RANKR-FRESNEL-HILBERT-v1`

The law of `Q` has a continuous density vanishing at infinity and

`boxed:
 ||p_Q||_infinity
 <= ((r+2)/r)
    [ L_H^2 M_A M_B / (alpha^2 |det Gamma|) ]^(1/(r+2)).
`                                                                    (2.3)

For `r=1`, (2.3) is exactly the preceding two-bank cross-square constant

`3 [L_H^2 M_A M_B/(alpha^2 |lambda|)]^(1/3)`.

The point of the theorem is not the formal higher-dimensional Fresnel identity by itself. The nontrivial source interface is that `L_i` may be arbitrarily dependent on every coordinate of `V_i`; the only independence is between the two **original source banks** and the physical hub.

## 3. Proof

For fixed outer Fourier time `t`, phase-weight source bank `i` and push it to `(L_i,V_i)`:

`h_(i,t)(l,v)
 = g_i(l,v) E[ exp(i t R_i) | L_i=l, V_i=v ].`                    (3.1)

Therefore

`|h_(i,t)| <= g_i`,                                               (3.2)

and, since `g_i` is a probability density,

`||h_(i,t)||_2^2 <= int g_i^2 <= M_i`.                            (3.3)

Define the `(r+1)`-dimensional Fourier transform

`Phi_(i,t)(eta,xi)
 = int exp(i eta l + i xi dot v) h_(i,t)(l,v) dl dv`.             (3.4)

Plancherel gives

`||Phi_(i,t)||_2 <= (2pi)^((r+1)/2) sqrt(M_i)`.                    (3.5)

Hence Cauchy--Schwarz supplies the dependence-safe product energy

`int_(R^(r+1)) |Phi_(A,t)(eta,xi) Phi_(B,t)(eta,xi)| d eta d xi
 <= (2pi)^(r+1) sqrt(M_A M_B).`                                   (3.6)

No projected coordinate has been declared independent.

For `t!=0`, the `r`-dimensional Fresnel representation is

`exp(i t v^T Gamma v)
 = c_(t,Gamma) (4pi|t|)^(-r/2) |det Gamma|^(-1/2)
   int_(R^r) exp[-i xi^T Gamma^(-1) xi/(4t)] exp(i xi dot v) d xi`, (3.7)

with `|c_(t,Gamma)|=1`. It may be obtained with a Gaussian regulator and then passed to the limit; (3.6) is an integrable dominating quantity for the resulting frequency integral.

Insert (3.7) into the characteristic function of (2.2). Independence of the two original banks factors their phase-weighted transforms. Taking absolute values only **after** that factorization gives

`|phi_Q(t)|
 <= (4pi|t|)^(-r/2)|det Gamma|^(-1/2)
    int_R int_(R^r) f_H(h)
      |Phi_(A,t)(2 alpha t h,xi) Phi_(B,t)(2 alpha t h,xi)|
    d xi d h.`                                                     (3.8)

The arbitrary hub phase has modulus one. Use `f_H<=L_H` and set

`eta=2 alpha t h`, `dh=deta/(2|alpha t|)`.                         (3.9)

Then (3.6) yields

`boxed:
 |phi_Q(t)|
 <= pi^(1+r/2) L_H sqrt(M_A M_B)
    |alpha|^(-1) |det Gamma|^(-1/2)
    |t|^(-(1+r/2)).
`                                                                    (3.10)

The exponent

`s=1+r/2=(r+2)/2`                                                  (3.11)

is strictly larger than one. Let

`C=pi^s L_H sqrt(M_A M_B)|alpha|^(-1)|det Gamma|^(-1/2)`.

Combining `|phi_Q(t)|<=1` with (3.10), split at `T=C^(1/s)`:

`int_R |phi_Q(t)| dt
 <= 2 C^(1/s) [1+1/(s-1)]
 = 2 C^(1/s) s/(s-1).`                                            (3.12)

Fourier inversion therefore gives

`||p_Q||_infinity
 <= [s/(pi(s-1))] C^(1/s)
 = ((r+2)/r)
   [L_H^2 M_A M_B/(alpha^2|det Gamma|)]^(1/(r+2)),`                (3.13)

because `pi^s` cancels exactly. Since `phi_Q in L^1`, the inverse Fourier transform is a continuous function vanishing at infinity. QED.

This is the required projection-product interaction: the projected density bound appears only through (3.3)-(3.6), an `L^2` energy that is paired across independent source banks before the nonlinear quadratic oscillation is integrated. It is not a direct level-set estimate for a dependent projected law.

## 4. Source-invariant cross-block corollary

The theorem has a useful original-coordinate form. Suppose, after conditioning only on outside original coordinates, the active variables are one fresh hub `H` and two disjoint original source banks `X_A,X_B`, and

`Q = R_H(H)
    +2H(a^T X_A+b^T X_B)
    +2 X_A^T C X_B
    +R_A(X_A)+R_B(X_B)+affine`,                                    (4.1)

where `rank(C)=r>=1`. Take a thin SVD

`C=U Sigma V^T`,

with `U^T U=V^T V=I_r` and singular values `sigma_1,...,sigma_r>0`. Define the true hub innovations transverse to the crossing spaces by

`delta_A = ||(I-UU^T)a||_2`,
`delta_B = ||(I-VV^T)b||_2`.                                      (4.2)

Assume `delta_A delta_B>0`. Put

`Z_A=U^T X_A`, `Z_B=V^T X_B`,
`L_A=a^T X_A`, `L_B=b^T X_B`.

The cross interaction has the exact identity

`2 X_A^T C X_B
 = (Z_A+Z_B)^T Sigma (Z_A+Z_B)
   -Z_A^T Sigma Z_A-Z_B^T Sigma Z_B`.                             (4.3)

The last two terms are same-bank phases and are absorbed into `R_A,R_B`.

The row Gram of the projection `(L_A,Z_A)` is

`G_A=[[||a||^2,a^T U],[U^T a,I_r]]`,

so the Schur complement gives

`det G_A=delta_A^2`; similarly `det G_B=delta_B^2`.                (4.4)

Now use the **actual product-projection theorem** (1.1):

`M_A <= 2^((r+1)/2)/delta_A`,
`M_B <= 2^((r+1)/2)/delta_B`.                                     (4.5)

Applying (2.3) with `alpha=1`, `Gamma=Sigma` gives the source-geometric exit

### `QFORM-TWOBANK-CROSSRANK-HUB-INNOVATION-v1`

`boxed:
 ||p_Q||_infinity
 <= ((r+2)/r) 2^((r+1)/(r+2))
    [ L_H^2 /
      (delta_A delta_B product_(j=1)^r sigma_j) ]^(1/(r+2)).
`                                                                    (4.6)

The density is continuous and in `C_0` on this branch.

The denominator is a genuine product-source currency:

`Omega = delta_A delta_B product_j sigma_j`.                       (4.7)

It is invariant under orthogonal changes inside either bank. The crossing singular values measure the nonlinear cross volume, while `delta_A,delta_B` measure exactly the hub information that is **not already trapped inside the crossing row/column spaces**.

For rank two this reads

`boxed:
 ||p_Q||_infinity
 <= 2^(7/4)
    [L_H^2/(delta_A delta_B sigma_1 sigma_2)]^(1/4),
`                                                                    (4.8)

where `2^(7/4)=3.3635856610...`.

For rank one it gives

`3*2^(2/3)[L_H^2/(delta_A delta_B sigma_1)]^(1/3)`,                (4.9)

which is the invariant form of the exact-zero-puncture cross-square theorem from the preceding fleet01/B16 run.

## 5. Strict owner-target family paid by the new rank-two theorem

Take one fresh cap-one coordinate `H` and two disjoint cap-one product banks. In each bank choose three orthonormal coefficient vectors and denote the projections by

`(L_A,V_A1,V_A2)`, `(L_B,V_B1,V_B2)`.

For arbitrary `theta in R`, define

`Q_theta
 = theta H^2
  +2H(L_A+L_B)
  +2 V_A1 V_B1 +2 V_A2 V_B2.`                                    (5.1)

Here the cross block has rank `r=2`, singular values `1,1`, and the hub coefficient directions are orthogonal to the crossing spaces, so

`delta_A=delta_B=1`.                                              (5.2)

Equation (4.8) gives

`boxed:
 ||p_(Q_theta)||_infinity
 <= 2^(7/4)
 =3.3635856610...,
`                                                                    (5.3)

uniformly in `theta` and in all cap-one original input laws. The density is continuous and vanishes at infinity.

This family is genuinely in the owner's spectral target. Each physical cross pair contributes the exact `2x2` block

`[[0,1],[1,0]]`,

so four eigenvalues are exactly `+1,-1,+1,-1`, independently of `theta`. The remaining `H`--symmetric-`L` block is

`[[theta,sqrt(2)],[sqrt(2),0]]`.

Thus every `Q_theta` has at least four eigenvalues of modulus at least one. No projected-coordinate independence is used; each three-dimensional bank projection may be strongly dependent.

Any additional independent quadratic block on disjoint original coordinates may be convolved afterward without increasing the density height, while the four displayed target eigenvalues remain present by direct sum.

## 6. What the new theorem pays in the current majority-sign endpoint

The newest fleet02/B16 report proves that a nonzero physical hub with the majority spectral sign has an **indefinite** literal-hub discriminant, and that a bounded planar projected density alone cannot control the resulting positive half-trace. Fleet03/B16 r38 strengthens this with an authentic product-source logarithmic divergence of the hub-first positive trace.

The new theorem supplies a sign-free Fourier exit that does not touch that failed interface: for any two-bank physical partition whose leaf cross block has rank `r>=1`, if

`delta_A delta_B product_j sigma_j >= omega_0>0`,                  (6.1)

then (4.6) gives a universal bound depending only on `omega_0`, regardless of the discriminant sign and regardless of arbitrary same-bank quadratic phases or the hub square.

This cleanly identifies why the authentic r38 stress family survives. There

`Q_a=aY^2+4YU+V^2`, `Y=sqrt(c)X_0+S`.

For the natural `S`--`U` cross bank, the rank-one crossing direction is exactly `S` on one side and `U` on the other, while the physical-hub star also points exactly along those same two directions. Consequently

`delta_A=delta_B=0`.                                              (6.2)

So r38 is not a small-value failure of (4.6); it lies on the **exact innovation-free boundary** where the Hilbert variable change loses a full dimension on both banks. This sharpens the remaining B16 endpoint from a vague “hyperbolic discriminant” to a concrete source-geometric degeneracy.

## 7. Newest fleet02/B16 result applied to an actual target inequality

The newest completed partner theorem, `QFORM-PHYSICAL-HUB-DEFINITE-DISCRIMINANT-v1`, states that for a fresh cap-one hub `H`, a two-dimensional orthonormal product projection `Z=(U,V)` of a disjoint source bank, and

`Q=(H,U,V)^T B(H,U,V)+affine`,

if the physical hub diagonal `a=B_11` obeys

`a det B>0`,

then

`||p_Q||_infinity <= 2 sqrt(2pi) (a det B)^(-1/4).`               (7.1)

Apply it to

`B_*=[[-2,1,0],[1,2,0],[0,0,2]].`                                (7.2)

Its spectrum is

`spec(B_*)={-sqrt(5),sqrt(5),2}`,                                 (7.3)

so this is a strict three-large-eigenvalue target. Moreover

`a=-2`, `det B_*=-10`, `a det B_*=20>0`.                          (7.4)

Therefore, for arbitrary independent cap-one originals producing the fresh `H` and the orthonormal projected pair `(U,V)`, the genuinely coupled quadratic

`Q_*=-2H^2+2HU+2U^2+2V^2`                                       (7.5)

satisfies the actual inequality

`boxed:
 ||p_(Q_*)||_infinity
 <= 2 sqrt(2pi) 20^(-1/4)
 =2.3706226576... .
`                                                                    (7.6)

This is a literal application of the newest partner result. It uses only the genuine pair projection cap `<=2`; it does **not** assert that `U` and `V` are independent. The partner theorem is a height certificate; its continuity conclusion is not used or inferred here.

## 8. First remaining B16 implication

The new theorem pays every two-bank crossing packet with a positive quantitative currency `Omega` in (4.7). The newest partner pays the minority-sign physical-hub discriminant by a genuine projected pair cap. The authentic r38 construction shows that the majority-sign positive-trace fallback is nonuniform and simultaneously sits at `Omega=0`.

Thus the first remaining implication is now:

**`QFORM-INNOVATIONFREE-MAJORITY-HUB-TTSTAR-v2` (OPEN).**  
In the exact-rank-three true-near-coloop survivor after all existing projected-crossing/volume exits, treat the source partition for which the physical hub-star vectors lie in (or quantitatively collapse into) the left/right crossing spaces, so that `delta_A delta_B product sigma_j` cannot be bounded below. The proof must keep the common physical-hub frequency and original product phases through a TT*/Hilbert pairing. It cannot first replace the remaining bank by an arbitrary bounded projected density and take a positive hyperbolic half-trace.

A useful structural next step is a deterministic dichotomy: from the surviving rank-three frame, force either one physical two-bank partition with `Omega>=omega_0` (then (4.6) closes it), the already-completed punctured fleet02/B16 receiver, or an explicitly aligned innovation-free normal form. The final aligned normal form is the only genuinely new analytic receiver still demanded by this B16 route.

## 9. Status

`QFORM-TWOBANK-RANKR-FRESNEL-HILBERT-v1`: **PROVED SUPPORTING THEOREM**.  
`QFORM-TWOBANK-CROSSRANK-HUB-INNOVATION-v1`: **PROVED SOURCE-GEOMETRIC COROLLARY**.  
Strict rank-two target family (5.1): **PROVED**, continuous `C_0`, density height `<=2^(7/4)<3.364`.  
Newest fleet02/B16 definite-discriminant theorem: **APPLIED** to the actual strict target inequality (7.6).  
Full unrestricted QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**. Global universal continuity remains separate.
