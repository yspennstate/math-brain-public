SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B09, 2026-09-22T23:50:17Z.
attacking: the remaining one-strong-cross geometry: prove a product-preserving dichotomy between a second disjoint hyperbolic packet and a paid aligned/ridge exit.

# fleet03/B09 r20 — a null linear pivot supplies the missing half power at a rank-two cross-bank endpoint

Programme: `QFORM-DENSITY-3EIG-20260922`.  
Assignment: Bilinear block mechanism.  
Outcome: `NEW_SUPPORTING_THEOREM / TARGET-LEVEL BRANCH CLOSED / FULL_QFORM_OPEN`.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and correction boundary

The target remains the unrestricted conjecture: independent real original coordinates with marginal density caps one, arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, and one dimension/law-independent density bound. No moments, support regularity, log-concavity, post-rotation independence, arbitrary-joint coarea, conditional spectral-density moment, or pointwise law-uniform quadratic stationary-phase estimate is used.

The new mechanism addresses the rank-two cross-bank endpoint, where the ordinary bilinear Plancherel estimate alone has a `|t|^{-1}` tail. A genuinely independent **linear null pivot** contributes another `|t|^{-1/2}` in `L^2`, producing the integrable `|t|^{-3/2}` tail without squaring a small-ball probability and without requiring a square innovation.

Completed peer input actually applied: fleet02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical source

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

For every `k`-dimensional orthogonal projection of an original cap-one product source it gives density cap at most `exp(k/2)`. It is used below at an actual inequality for the two rank-two singular projections and for the scalar pivot-coupling projection. The designated fleet04/B09 current-QFORM handoff/root was absent at the fresh lookup, so no partner result is fabricated or awaited.

## 2. Analytic theorem

Let `X0`, `U=(U_i)_{i in I}`, and `V=(V_j)_{j in J}` be mutually independent blocks of original coordinates; all scalar coordinate densities are at most one. Let `B` be a real `|I| x |J|` matrix of exact rank `r>=2`, with nonzero singular values `sigma_1,...,sigma_r` and

`Delta_r(B)=prod_(k=1)^r sigma_k`.

Let `p in R^I` be nonzero, `a!=0`, and `d in R`. Let `F(U)` and `G(V)` be arbitrary measurable real functions, finite almost surely. Put

`T = F(U)+G(V)+2 U^T B V + 2 a X0 (p^T U+d)`.                 (2.1)

Write `E=range(B)` and `Fsp=range(B^T)`. Suppose the positive projection densities satisfy

`||rho_(P_E U)||_infinity <= M`,
`||rho_(P_Fsp V)||_infinity <= N`,
`||rho_(p^T U)||_infinity <= L`.                               (2.2)

### Theorem 2.1 — `QFORM-LINEAR-PIVOT-CROSSBANK-LINF-v1`

`T` has a bounded continuous density and

`boxed:
 ||p_T||_infinity
 <= [(r+1)/(r-1)] [ M N L / (|a| Delta_r(B)) ]^(1/(r+1)).
`                                                                  (2.3)

Consequently every interval `J0` satisfies the genuine linear estimate

`P(T in J0) <= [(r+1)/(r-1)] [MNL/(|a|Delta_r(B))]^(1/(r+1)) |J0|`. (2.4)

For the target source class, the completed fleet02/B06 theorem gives

`M,N <= exp(r/2)`,
`L <= exp(1/2)/||p||_2`.                                        (2.5)

Therefore

`boxed:
 ||p_T||_infinity
 <= [(r+1)/(r-1)] exp((r+1/2)/(r+1))
    [ |a| ||p||_2 Delta_r(B) ]^(-1/(r+1)).
`                                                                  (2.6)

At the critical rank-two endpoint,

`boxed:
 ||p_T||_infinity
 <= 3 e^(5/6) [ |a| ||p||_2 sigma_1(B)sigma_2(B) ]^(-1/3)
 < 6.903 [ |a| ||p||_2 sigma_1 sigma_2 ]^(-1/3).
`                                                                  (2.7)

### Proof

Take a thin SVD `B=P Sigma R^T`, with `P,R` having `r` orthonormal columns. Set

`Y=P^T U`, `Z=R^T V`.

For fixed `t`, disintegrate the two product laws over `Y` and `Z`. Let `phi_0` be the characteristic function of `X0` and define complex amplitudes

`A_t(y)=rho_Y(y) E[ exp(i t F(U)) phi_0(2 a t(p^T U+d)) | Y=y ]`,
`C_t(z)=rho_Z(z) E[ exp(i t G(V)) | Z=z ]`.                    (2.8)

No independence among coordinates of `Y` or `Z` is asserted. Jensen/Cauchy on the conditional probability measure gives

`|A_t(y)|^2
 <= rho_Y(y)^2 E[|phi_0(2at(p^TU+d))|^2 | Y=y]
 <= M rho_Y(y) E[|phi_0(2at(p^TU+d))|^2 | Y=y]`.               (2.9)

Integrating in `y`,

`||A_t||_2^2 <= M E |phi_0(2at(p^TU+d))|^2`.                    (2.10)

Since `S=p^T U` has density at most `L`,

`E |phi_0(2at(S+d))|^2
 <= L int_R |phi_0(2at(s+d))|^2 ds
 = [L/(2|at|)] int_R |phi_0(xi)|^2 dxi.                        (2.11)

By Plancherel and `0<=f_0<=1`, `int f_0^2<=1`, hence

`int_R |phi_0(xi)|^2 dxi <= 2 pi`.                              (2.12)

Thus

`||A_t||_2 <= [M L pi/(|a t|)]^(1/2).`                          (2.13)

Similarly `||C_t||_2<=N^(1/2)`.

The exact characteristic function is

`phi_T(t)=int int A_t(y) C_t(z) exp(2 i t y^T Sigma z) dy dz`.  (2.14)

The standard rank-`r` bilinear Plancherel calculation, with Fourier convention `hat h(xi)=int h(x)e^(i xi.x)dx`, gives

`|phi_T(t)|
 <= pi^(r/2) |t|^(-r/2) Delta_r(B)^(-1/2)
    ||A_t||_2 ||C_t||_2`.                                      (2.15)

Insert (2.13):

`|phi_T(t)|
 <= K |t|^(-(r+1)/2)`,                                         (2.16)

where

`K=pi^((r+1)/2) [MNL/(|a|Delta_r(B))]^(1/2)`.                  (2.17)

Together with `|phi_T(t)|<=1`, put `alpha=(r+1)/2>1` and use

`int_R min(1,K|t|^-alpha) dt
 =2 [alpha/(alpha-1)] K^(1/alpha)
 =2 [(r+1)/(r-1)] K^(2/(r+1)).`                                (2.18)

Hence `phi_T in L^1`; Fourier inversion gives a bounded continuous density and

`||p_T||_infinity
 <=(1/(2pi)) int |phi_T|
 <=[(r+1)/(r-1)] [MNL/(|a|Delta_r(B))]^(1/(r+1))`,             (2.19)

because the factor `pi` cancels exactly. This is (2.3). Equation (2.4) follows by integrating the density over an interval. Applying the peer projection theorem in dimensions `r,r,1` gives (2.5)--(2.7). QED.

## 3. Physical null-pivot corollary

Partition the original coordinates as `{0} union I union J union O`. Assume

`A_00=0`, `A_0J=0`, `p=A_0I !=0`,                              (3.1)

and the physical cross block `B=A_IJ` has rank `r>=2`. There is **no restriction** on `A_II`, `A_JJ`, `A_OO`, or the couplings involving `O`.

Condition on the original coordinates `X_O`. The term involving `X_0` becomes

`2 X_0(p^T X_I+d_O)`,                                          (3.2)

while all `I`-only and `J`-only quadratic/affine terms are absorbed into the arbitrary `F,G`; the `I-J` cross term remains `2X_I^T B X_J`. Therefore Theorem 2.1 applies uniformly in the conditioning, with `a=1`.

### Corollary 3.1 — `QFORM-NULLPIVOT-RANK2-CROSS-v1`

For rank two,

`boxed:
 ||p_(X^TAX)||_infinity
 < 6.903 [ ||A_0I||_2 sigma_1(A_IJ)sigma_2(A_IJ) ]^(-1/3).
`                                                                  (3.3)

The same coefficient times interval length bounds every interval probability. In the stated branch the density is continuous: the conditional characteristic functions share the integrable envelope (2.16), so averaging over `O` preserves Fourier inversion/continuity.

This is a different third-direction payment from the completed rank-two-cross-plus-square theorem: the missing half power comes from an untouched **linear null pivot**, not a quadratic square bank.

## 4. Diffuse target-valid stress family

Let `m>=2`. Choose orthonormal flat vectors `u_1,u_2 in R^m` and `v_1,v_2 in R^m` (for example a constant vector and a balanced sign vector when `m` is even). On coordinates `(x_0,X_I,X_J)` define

`A_0I=u_1^T`, `A_0J=0`,
`A_II=A_JJ=0`,
`A_IJ=u_1 v_1^T+u_2 v_2^T`.                                  (4.1)

The compressed matrix on `(x_0,u_1,u_2,v_1,v_2)` is

`[[0,1,0,0,0],
  [1,0,0,1,0],
  [0,0,0,0,1],
  [0,1,0,0,0],
  [0,0,1,0,0]]`.                                               (4.2)

Its spectrum is exactly

`{-sqrt(2),-1,0,1,sqrt(2)}`.                                   (4.3)

Thus it is a valid target family with four eigenvalues of modulus at least one. Meanwhile every `I-J` physical coefficient is `O(1/m)` and every pivot-to-`I` coefficient is `O(m^-1/2)`, so fixed local coefficients/minors vanish with dimension. Nevertheless

`||A_0I||=1`, `sigma_1(A_IJ)=sigma_2(A_IJ)=1`,                 (4.4)

and (3.3) gives uniformly over `m` and every admissible product input law

`boxed: ||p_Q||_infinity < 6.903.`                              (4.5)

This is aggregate-before-inversion and is not a local-minor theorem.

## 5. Structural implication and remaining debt

This run closes a real piece of the one-strong-cross/full-curvature residual: whenever a null physical pivot supplies a genuine independent linear innovation into one source bank and that bank has a quantitative rank-two cross interaction with a disjoint bank, arbitrary self-curvature on **both** cross banks is harmless. Analytically, the critical `|t|^-1` rank-two cross tail is upgraded to `|t|^-3/2` by the scalar linear pivot.

There is a useful structural routing observation. If a rank-two cross block `B=A_IJ` is present and the pivot coupling vector `p=A_0I` has a component `p_perp` outside `range(B)`, then the enlarged physical cross block `[p,B]` has rank three and

`Delta_3([p,B]) = Delta_2(B) ||p_perp||`.                       (5.1)

The already-completed rank-three cross theorem pays that case directly. Hence the genuinely new/null-pivot difficulty begins only when the pivot coupling is aligned with the rank-two cross range. Corollary 3.1 pays the aligned case when the opposite pivot coupling `A_0J` vanishes.

The first remaining B09 implication is therefore narrower:

`QFORM-ALIGNED-NULLPIVOT-TWOSIDED-COUPLING-v1` — given a null pivot and a quantitative rank-two physical cross block, handle the survivor in which **both** pivot coupling vectors lie in the corresponding rank-two cross ranges and both are nonzero, while retaining arbitrary same-bank curvature and product provenance. If either coupling has a transverse component, rank-three cross smoothing pays it; if one opposite coupling is zero, this run pays it. A viable next attack is a three-factor oscillatory operator estimate for

`2 y^T Sigma z + 2 x_0(p^T y+q^T z)`

with product-source amplitudes, seeking the same integrable `|t|^-3/2` decay without shearing the random coordinates.

The unrestricted QFORM conjecture remains **OPEN**. Full-target continuity remains **OPEN**; continuity is proved in the exact theorem/corollary scope above.

## 6. Finite checks

The exact stress spectrum follows by decomposing into a three-vertex path (`{-sqrt(2),0,sqrt(2)}`) and an independent edge (`{-1,1}`). Numerically, the peer-cap rank-two coefficient is

`3 e^(5/6)=6.902927672678475...`.

Using the sharper `2^(k/2)` product-marginal caps instead of the peer BL cap would improve the rank-two numerical coefficient to `3*2^(5/6)=5.345392308842036...`; the proof above intentionally records the completed peer theorem at the actual inequality required by this assignment.
