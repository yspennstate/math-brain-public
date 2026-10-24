SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B01, 2026-09-24T02:07:49Z.
attacking: rank-two cross half-Riesz via exact two-dimensional Plancherel, sharpening the scalar-square E2 receiver and transferring finite-leak Schur determinant currency.

# Rank-two cross: fractional potentials, near-linear small-ball, and a sharp scalar-square compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T020749Z-account01-B01-qform-auto11`  
Role: account01/B01, Oscillatory replacement  
Status: **PROVED SUPPORTING THEOREMS / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Control and correction boundary

The unrestricted owner target remains OPEN. Inputs are arbitrary independent real coordinates with densities bounded by one; no moments, compact support, log-concavity, connected support, Gaussianity, or post-rotation independence are assumed.

Fresh prepublication control was read at `yspennstate/math-research-brain@8ee5cc9b7170ce66c0e85c782cf7b0974a407345`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only. The live correction inbox was reread at blob `a884b835aba929c5376e6417ae5cfcd44c0f7a76`.

The phase-aligned fragmented-support counterexample to any law-uniform scalar quadratic estimate

`|E exp(itX^2)| <= C |t|^{-alpha}`, `alpha>0`,

is preserved. The estimates below are JOINT two-bank estimates created by a rank-two bilinear phase and two-dimensional Plancherel. They do not imply any pointwise decay for a single scalar quadratic phase.

Source inputs used at equations:

1. Exact-rank crossing theorem: `yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`, `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`. For two independent original-coordinate banks, an exact rank-r physical cross block `M=USV^T`, arbitrary same-bank measurable phases, and projected density caps `M_X,M_Y`, it proves

   `|phi(t)| <= min{1,(pi/|t|)^(r/2)(M_X M_Y)^(1/2)(s_1...s_r)^(-1/2)}`.

   In dimension two, the orthogonal product projections have density caps at most 2.

2. Previous B01 scalar-square plus E2 synthesis: `yspennstate/math-open-problems@0bbbd2e99a4d26b7a4380a9827d92596daeaf2a6`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260923T200355Z-account01-B01-qform-auto11/E2_SQUARE_SYNTHESIS.md`. It gives `8 e^(1/4)|a|^(-1/2) Z^(-1/8)` using the more general row-gate-free E2 theorem. The exact-rank-two argument below improves the constant to 8 and also gives the full fractional-potential scale `0<beta<1` plus a near-linear concentration bound.

3. Newest completed designated partner account02/B01: `yspennstate/math-open-problems@94f16e48c87819684efd69c01766d5dc11356dd6`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260924T003308Z-auto11-latentrank1/REPORT.md`. Its theorem `QFORM-LATENT-RANK1-GLOBAL-COMPILER-v1` pays every `A=D+R`, `rank R<=1`, `s_3(A)>=1` by `<195.01`; on `A_0=I_3-11^T` its physical-pair branch gives `<22.105`.

## 2. Main theorem: rank-two cross fractional potentials

Let `I,J` be disjoint original-coordinate banks and let `X_I,X_J` be independent. Let

`R = F(X_I) + 2 X_I^T M X_J + G(X_J)`,                              (2.1)

where `F,G` are arbitrary measurable real functions and `M` is an exact rank-two real matrix. Write its nonzero singular values as `s_1,s_2>0` and set

`Z = e_2(M^T M) = s_1^2 s_2^2 >0`.                                 (2.2)

Affine terms and arbitrary quadratic curvature internal to either bank are included in `F,G`.

### Theorem 2.1 — `QFORM-RANK2-CROSS-FRACTIONAL-POTENTIAL-v1`

For every `0<beta<1`,

`boxed:
 H_beta(R):=sup_u E|R-u|^(-beta)
 <= K_beta Z^(-beta/4),`                                           (2.3)

where

`K_beta = (2pi)^beta /
          [ Gamma(beta) cos(pi beta/2) beta(1-beta) ].`             (2.4)

In particular,

`boxed: H_(1/2)(R) <= 8 Z^(-1/8).`                                 (2.5)

The range `beta<1` is sharp in this scope; Section 5 gives an exact rank-two example with `H_1=infinity`.

### Proof

Take a thin SVD

`M = U diag(s_1,s_2) V^T`,                                         (2.6)

with two-column orthonormal frames `U,V`. Put

`Y=U^T X_I`, `W=V^T X_J`.                                          (2.7)

The source-valid product-projection theorem gives

`||p_Y||_infinity <=2`, `||p_W||_infinity<=2`.                     (2.8)

For each frequency `t`, push the complex measures

`exp(itF(X_I))dP_I`, `exp(itG(X_J))dP_J`                            (2.9)

through the maps in (2.7). Their densities `a_t,b_t` obey

`|a_t|<=p_Y`, `|b_t|<=p_W`,                                        (2.10)

so

`||a_t||_2<=sqrt(2)`, `||b_t||_2<=sqrt(2)`.                        (2.11)

With Fourier convention `hat f(xi)=int exp(i xi.x)f(x)dx`, the bilinear operator

`(T_t b)(y)=int exp(i2t y^T diag(s_1,s_2) w)b(w)dw`                 (2.12)

has exact two-dimensional Plancherel norm

`||T_t||_(2->2) = pi |t|^(-1) (s_1 s_2)^(-1/2).`                  (2.13)

Therefore

`|phi_R(t)|
 <= min{1, 2pi |t|^(-1)(s_1s_2)^(-1/2)}
 =  min{1, A/|t|},`                                                (2.14)

where

`A = 2pi Z^(-1/4).`                                                 (2.15)

This is JOINT bilinear decay. It is fully compatible with the scalar phase-alignment correction.

For `0<beta<1`, use the regularized one-dimensional Riesz identity

`|x|^(-beta)
 = [2 Gamma(beta) cos(pi beta/2)]^(-1)
   int_R exp(itx)|t|^(beta-1)dt`                                   (2.16)

and Tonelli after the usual Gaussian cutoff. Taking absolute values only after the joint estimate (2.14),

`H_beta(R)
 <= [2 Gamma(beta)cos(pi beta/2)]^(-1)
    int_R |t|^(beta-1) min{1,A/|t|}dt.`                            (2.17)

The integral is exact:

`int_R |t|^(beta-1)min{1,A/|t|}dt
 = 2 A^beta [1/beta + 1/(1-beta)]
 = 2 A^beta/[beta(1-beta)].`                                      (2.18)

Insert (2.15) to get (2.3)-(2.4). At `beta=1/2`, the constant simplifies exactly to 8. QED.

## 3. Near-linear distribution-function estimate

The same critical `t^-1` envelope gives a useful endpoint concentration estimate with only a logarithmic loss.

### Theorem 3.1 — `QFORM-RANK2-CROSS-LOG-SMALLBALL-v1`

Under (2.1)-(2.2), for every `epsilon>0`,

`boxed:
 sup_u P(|R-u|<=epsilon)
 <= min{1,
        pi^3 Z^(-1/4) epsilon
        [1+log_+( Z^(1/4)/(2pi epsilon) )] }.`                     (3.1)

### Proof

Let

`k_T(x)=(1/(2pi)) int_(|t|<=T)(1-|t|/T)e^(-itx)dt
       =2 sin^2(Tx/2)/(pi T x^2).`                                 (3.2)

For `|x|<=1/T`, the elementary `sin y>=2y/pi` on `0<=y<=1/2` gives

`k_T(x)>=2T/pi^3`.                                                  (3.3)

Hence, for every `u`,

`P(|R-u|<=1/T)
 <= (pi^2/(4T)) int_(-T)^T |phi_R(t)|dt.`                          (3.4)

Take `T=epsilon^(-1)` and use (2.14). If `T>A`,

`int_(-T)^T |phi_R(t)|dt
 <=2A[1+log(T/A)].`                                                 (3.5)

If `T<=A`, the right side of (3.1) after the outer minimum is already 1. Substituting `A=2pi Z^(-1/4)` gives (3.1). QED.

This is close to the correct critical behavior: exact rank-two indefinite forms can have logarithmically singular densities, so a universal no-log density estimate for `R` itself is impossible.

## 4. One original square closes the exact-rank-two cross endpoint

Let `X_0` be one further original coordinate, independent of the banks and with density at most one. Suppose exact completion gives

`Q = a (X_0+h(X_I,X_J))^2 + R`, `a!=0`,                            (4.1)

where `R` has the form (2.1) with exact rank-two cross block `M`; the shift `h` may depend arbitrarily on both banks.

### Corollary 4.1 — `QFORM-SCALAR-SQUARE-PLUS-EXACT-RANK2-CROSS-v1`

`boxed:
 ||p_Q||_infinity <= 8 |a|^(-1/2) Z^(-1/8).`                      (4.2)

This is an essential-supremum statement; continuity is not asserted for arbitrary merely measurable input densities.

Proof. Condition on both banks. Translation of `X_0` preserves the density cap, and the conditional density of `a(X_0+h)^2` is bounded by

`|a|^(-1/2)|v|^(-1/2)`                                             (4.3)

on the appropriate half-line. Therefore

`p_Q(s)
 <= |a|^(-1/2) E|s-R|^(-1/2)
 <= |a|^(-1/2) H_(1/2)(R).`                                       (4.4)

Apply (2.5). QED.

Compared with the previous general E2 receiver `8e^(1/4)|a|^(-1/2)Z^(-1/8)`, the exact-rank-two branch now has the sharper constant 8 and a complete explanation of the critical exponent.

### Strict target stress family

For `0<epsilon<=1`, take five original coordinates and

`Q_epsilon
 = epsilon X_0^2
 + 2 epsilon^(-1)(X_1 X_3 + X_2 X_4).`                             (4.5)

The symmetric coefficient matrix has spectrum

`{epsilon, +epsilon^(-1),+epsilon^(-1),-epsilon^(-1),-epsilon^(-1)}`,

so it has at least four eigenvalues of modulus at least one. The residual rank-two cross matrix is

`M=epsilon^(-1) I_2`,                                              (4.6)

hence

`Z=e_2(M^T M)=epsilon^(-4).`                                      (4.7)

Corollary 4.1 gives the exact cancellation

`boxed: ||p_(Q_epsilon)||_infinity <=8`                            (4.8)

for every admissible cap-one product law, uniformly as `epsilon->0`. The older E2 synthesis gave `8e^(1/4)` on the same scaling.

## 5. Critical sharpness: H_1 is false even with rank-two crossing

Let all four coordinates be iid `Uniform[-1/2,1/2]`. Write the two original banks as `Y=(Y_1,Y_2)` and `W=(W_1,W_2)` and set

`R=(Y_1-W_1)^2-(Y_2-W_2)^2.`                                      (5.1)

This has the form (2.1) with exact-rank-two cross block

`M=diag(-1,1)`, `Z=1`.                                             (5.2)

The differences `D_1=Y_1-W_1`, `D_2=Y_2-W_2` are independent triangular variables with densities `1-|d|` on `[-1,1]`, hence each density is at least `1/2` on `[-1/2,1/2]`. Therefore

`E|R|^(-1)
 >= (1/4) int_0^(1/2) int_0^(1/2)
       |x^2-y^2|^(-1) dx dy
 = infinity`,                                                      (5.3)

because the integral diverges logarithmically along `x=y`. Thus `H_1(R)=infinity`.

This is not a counterexample to the owner target: the quadratic matrix in (5.1) has only two nonzero spectral directions. It shows that Theorem 2.1 reaches the correct fractional endpoint: `beta<1` is possible, `beta=1` is not.

## 6. Exact Schur determinant transfer in diagonal-plus-rank-two geometry

The new compiler interacts cleanly with the fleet's remaining finite-leak state.

Let

`A = D + U C U^T`,                                                  (6.1)

where `D=diag(d_1,...,d_n)`, `U^T U=I_2`, and `C` is invertible symmetric `2x2`. Write `u_k=U^T e_k` for the k-th latent row and let

`a=A_kk=d_k+u_k^T C u_k !=0`.                                      (6.2)

After exact scalar completion of coordinate `k`, the Schur residual is

`A/k = D_(-k) + U_(-k) C_k U_(-k)^T`,                              (6.3)

with

`C_k = C - C u_k u_k^T C/a`.                                      (6.4)

The determinant lemma gives the exact identity

`boxed: det C_k = (d_k/a) det C.`                                  (6.5)

Now split remaining original coordinates into disjoint banks `I,J` and put

`G_I=U_I^T U_I`, `G_J=U_J^T U_J`.                                 (6.6)

If both are positive definite, the residual cross block

`M_k=U_I C_k U_J^T`                                                (6.7)

has exact two-volume

`boxed:
 e_2(M_k^T M_k)
 = (det C_k)^2 det(G_I)det(G_J)
 = (det C)^2(d_k/a)^2 det(G_I)det(G_J).`                           (6.8)

Combining (6.8) with Corollary 4.1 yields

`boxed:
 ||p_Q||_infinity
 <=8 |a|^(-1/4)|d_k|^(-1/4)|det C|^(-1/4)
      [det(G_I)det(G_J)]^(-1/8).`                                  (6.9)

This is the useful structural message: when a physical pivot `a` is small because it nearly cancels the diagonal-plus-latent decomposition coefficient `d_k`, the exact Schur cross determinant inflates by `|d_k/a|`; after spending the rank-two cross half-Riesz budget, the small-pivot cost improves from `|a|^-1/2` to `|a|^-1/4`. No random quadratic tail is discarded.

Equation (6.9) is still a scoped receiver, not a full proof: the bare three-large-eigenvalue hypothesis has not yet been shown to force `det(G_I)det(G_J)` and the other factors to stay at target scale, and the exact `a=0` endpoint must be routed without division.

## 7. Required designated-partner application

The newest completed account02/B01 theorem is applied to the concrete target matrix

`A_0 = I_3 - 11^T
     = [[0,-1,-1],[-1,0,-1],[-1,-1,0]].`                          (7.1)

It has spectrum `{1,1,-2}` and is globally diagonal plus rank one. The partner theorem gives

`boxed: ||p_(X^T A_0 X)||_infinity <195.01.`                       (7.2)

On this actual matrix every physical pair is `[[0,-1],[-1,0]]`, so the partner's source-pinned pair branch gives the sharper equation-level bound

`boxed: ||p_(X^T A_0 X)||_infinity
        <=3*400^(1/3)
        <22.105.`                                                  (7.3)

This also delineates the mechanisms cleanly: every original-coordinate cross cut of a global diagonal-plus-rank-one matrix has rank at most one, so the new exact-rank-two cross receiver is identically unavailable there; the partner theorem pays precisely that complementary branch.

## 8. Remaining implication

The first structural debt after this run is

`QFORM-W2ZERO-RANK2-EXACTCROSS-OR-COLLOOP-ROUTING-v1`:

> In the genuinely diagonal-plus-rank-two finite-leak survivor, force either (i) a nonzero original scalar pivot whose Schur residual contains an exact rank-two cross block with target-scale two-volume, paid by (4.2)/(6.9), or (ii) a quantitatively localized latent-coloop/finite-support state paid by the existing partner physical-pair, latent-wedge, three-square, grouped, or zero-diagonal receivers. The exact zero-pivot state and the nonzero collar must be retained rather than treated as negligible rough-law perturbations.

The analytic rank-two cross endpoint itself is now paid sharply enough for structural routing: it has all `H_beta`, `beta<1`, near-linear `epsilon log(1/epsilon)` concentration, and one source-disjoint original square gives an `L^infinity` density bound with constant 8.

Full QFORM remains **OPEN**. Full-target continuity remains **OPEN**. There are not two independent end-to-end reviews of the owner target.
