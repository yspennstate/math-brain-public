# Early substantive checkpoint — rough star before the pair-log receiver

## QFORM-ROUGH-STAR-UNIFORM-SQRT-SMALLBALL-v1

Let `X` be one literal original coordinate with probability density `f_X<=1`, and let `Z` be a disjoint bank of original independent coordinates, each with density <=1.  Let `m!=0` be a real coefficient vector and let `G(Z)` be an arbitrary real measurable phase (in the QFORM application it is the entire quadratic-affine same-bank Schur curvature).  For arbitrary real `s,b,c`, put

`R=s X^2+2 X <m,Z>+b X+G(Z)+c`.

Then, for every `t!=0`,

`|phi_R(t)| <= 2^(1/4) sqrt(pi) ||m||_2^(-1/2) |t|^(-1/2)`.       (1)

Consequently, for every `rho>0`,

`sup_u P{|R-u|<=rho}
 <= exp(1/2) Gamma(1/4) ||m||_2^(-1/2) sqrt(rho)`.                 (2)

Both estimates are completely uniform in the scalar curvature `s` and in the arbitrary same-bank phase `G`; no moment, support or regularity assumption on the inputs is used.

### Proof of (1)

Let `L=<m,Z>`.  The reviewed one-dimensional product-projection estimate gives

`||p_L||_infinity <= sqrt(2)/||m||_2`.                            (3)

For each fixed `t`, push the complex measure `exp(it G(Z)) dP_Z` forward under `Z -> L`.  It has a complex density `b_t` satisfying pointwise `|b_t(l)|<=p_L(l)`, hence

`||b_t||_2^2 <= ||p_L||_infinity <= sqrt(2)/||m||_2`.             (4)

Set `g_t(x)=f_X(x) exp(it(sx^2+bx))`.  Because `0<=f_X<=1`,

`||g_t||_2^2=int f_X^2 <= int f_X=1`.                             (5)

With the angular Fourier transform `hat g(xi)=int g(x)exp(i xi x)dx`,

`phi_R(t)=unit_phase * int b_t(l) hat g_t(2t l) dl`.              (6)

Cauchy-Schwarz, the change of variables `xi=2t l`, and Plancherel give

`|phi_R(t)|
 <= ||b_t||_2 [ (1/(2|t|)) int |hat g_t(xi)|^2 dxi ]^(1/2)
 <= (2^(1/4)||m||^(-1/2)) [pi/|t|]^(1/2)`,                       (7)

which is (1).  The quadratic chirp `exp(itsx^2)` remains intact and costs nothing in (5); this is the key reason the estimate does not deteriorate as `s->0`.

### Proof of (2)

For `|y|<=rho`,

`1 <= exp(1/2) exp(-y^2/(2rho^2))`.                               (8)

The angular Fourier representation of the Gaussian is

`exp(-y^2/(2rho^2))
 =(rho/sqrt(2pi)) int exp(-rho^2 t^2/2) exp(ity) dt`.             (9)

Therefore (1) implies

`P{|R-u|<=rho}
 <= exp(1/2) rho/sqrt(2pi)
    int exp(-rho^2 t^2/2)|phi_R(t)|dt`.

Using

`int_0^infinity t^(-1/2) exp(-rho^2t^2/2)dt
 =rho^(-1/2) 2^(-3/4) Gamma(1/4)`,                               (10)

and substituting the coefficient in (1), all powers of `2` and `pi` cancel, yielding exactly (2).

## Immediate splice into the latest designated partner

The current account03/B09 Schur algebra completes an invertible indefinite literal physical pair `B` and leaves

`R=s X_k^2+2 X_k <m,Z>+beta X_k+G_1(Z)`,                         (11)

with `G_1` arbitrary.  Its completed pair-log theorem says that a remainder bound

`sup_u P{|R-u|<=rho} <= H0 sqrt(rho)`                             (12)

implies

`||p_Q||_infinity <=4 sqrt(2H0)
 (|det B| sigma_min(B))^(-1/4)`.                                 (13)

Applying (2) gives, for **every** scalar Schur coefficient `s`,

`||p_Q||_infinity
 <= 4 sqrt(2) exp(1/4) Gamma(1/4)^(1/2)
    [|det B| sigma_min(B) ||m||_2]^(-1/4)`                        (14)

with numerical prefactor `13.8305403219936...`.  This is already a final `O(|I|)` interval bound.  In particular, it removes the latest partner's exact-Schur-null restriction on every branch with a nonzero aggregate star `m`; the dense right-bank quadratic curvature stays inside `G_1` throughout.

The remaining B09 issue is not the scalar `s->0` transition on a nonzero star.  It is the degenerate routing where the relevant Schur star vanishes or the physical-pair conditioning itself degenerates, together with the still-live exact/near-rank-one physical-pair collar outside a quantitatively invertible indefinite pair.
