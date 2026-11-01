SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B08, 2026-09-23T18:16:56Z.
attacking: the r43 two-sided common-plane cycle: derive a product-preserving quantitative receiver or a sharp obstruction while retaining arbitrary same-bank curvature and the physical tail.

# fleet03/B08 r44 — diffuse two-arm path receiver and the exact vanishing-cycle endpoint

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case  
Status: `NEW SUPPORTING THEOREM / EXACT VANISHING-CYCLE ENDPOINT PAID / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Continuity: proved on the new theorem's exact path branch; full-target continuity remains open.

## 1. Scope and source pins

The owner target is unchanged: independent real original coordinates with probability densities bounded by one, arbitrary real symmetric `A`, at least three eigenvalues of modulus at least one, and one universal output-density bound. No Gaussianity, log-concavity, moments, compact support, connected support, post-rotation independence, arbitrary-joint coarea, or law-uniform pointwise quadratic decay is assumed.

Fresh owner control at startup was `QFORM` only, revision `2026-09-22.15`. The current B08 predecessor is

`yspennstate/math-open-problems@87f0f4b7b8a9b5dc4f1050ecef61e527dac7a541`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260923T172004Z-fleet03-B08-qform-diffuse-r43/REPORT.md`.

Its remaining exact common-plane state has two physical hubs, two disjoint product banks, two rank-two hub-to-bank arms, and a possible light-light common-plane edge plus a transverse tail. In its diffuse bisection branch, the two arm singular-volume products satisfy

`S_r=s_1(M_r)s_2(M_r) > L^2/(64 sqrt(896)), r=1,2`.

The current projected-density input used below is the orthonormal `r`-projection cap `2^(r/2)` recorded in the owner manuscript checkpoint

`yspennstate/math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6`

under `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`. In dimension two the cap is `2`.

The designated partner result actually applied is fleet04/B08

`QFORM-ANISOTROPIC-RANK1-E2-DIRECTSUM-RECEIVER-v1`,

source

`yspennstate/math-open-problems@abbec61f52e1f4b4d367fd67e73e4d2501ac9c74`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B08/20260923T091414Z-fleet04-B08-QFORM-r1/REPORT.md`.

It gives the exact localized anisotropic family a density bound `<7.251/L` after scaling by `L`.

## 2. Main analytic theorem: two independent arms through one diffuse hub

Let `H`, `X`, `Y` be mutually independent random blocks. Let `H` take values in `R^d`, `d>1`, with density `p_H` satisfying

`||p_H||_infinity <= M_0`.

Let `U=L_1 X` and `V=L_2 Y` be `R^d`-valued full-rank linear images whose marginal densities satisfy

`||p_U||_infinity <= M_1`,
`||p_V||_infinity <= M_2`.

Let `F_0,F_1,F_2` be arbitrary measurable real functions on their respective source blocks, finite almost surely. Define

`Q = F_0(H)+F_1(X)+F_2(Y)+2 H^T U+2 H^T V+c`.                 (2.1)

The internal functions may contain arbitrary quadratic and affine terms. No coordinate independence inside the projected vectors `U,V` is assumed.

### Theorem 2.1 — `QFORM-THREEBANK-TWOARM-PATH-v1`

The characteristic function of `Q` belongs to `L^1(R)`. Hence `Q` has a continuous density in `C_0(R)`, and

`boxed:
 ||p_Q||_infinity
 <= [d/(d-1)] M_0^(1/d) (M_1 M_2)^(1/(2d)).
`                                                                  (2.2)

For `d=2`,

`boxed:
 ||p_Q||_infinity <= 2 M_0^(1/2)(M_1M_2)^(1/4).
`                                                                  (2.3)

This theorem is an integrated-Fourier statement. It does not assert any law-uniform pointwise decay for a one-dimensional quadratic phase.

### Proof

Fix `t`. Push the complex measures

`exp(i t F_1(X)) dP_X`, `exp(i t F_2(Y)) dP_Y`

through `L_1,L_2`. Their Radon--Nikodym densities `a_t,b_t` satisfy

`|a_t(u)|<=p_U(u)`, `|b_t(v)|<=p_V(v)`,

and therefore

`||a_t||_2<=sqrt(M_1)`, `||b_t||_2<=sqrt(M_2)`.                (2.4)

Likewise

`c_t(h)=p_H(h) exp(i t F_0(h))`

obeys `||c_t||_infinity<=M_0`. Any affine terms are already inside the three arbitrary internal functions.

With Fourier convention

`hat a(xi)=int exp(i xi.u) a(u)du`,

independence of the three source blocks gives exactly

`phi_Q(t)=exp(i t c) int_(R^d) c_t(h)
                  hat a_t(2t h) hat b_t(2t h) dh`.             (2.5)

There is no rotated-independence assertion here: the only independence used is the original disjointness of the three source blocks.

By Holder in the form `L^infinity x L^2 x L^2` and Plancherel,

`|phi_Q(t)|
 <= M_0 ||hat a_t(2t .)||_2 ||hat b_t(2t .)||_2`
` <= M_0 (pi/|t|)^d sqrt(M_1M_2)`                              (2.6)

for `t!=0`, because

`||hat a_t(2t .)||_2
 = (2|t|)^(-d/2)(2pi)^(d/2)||a_t||_2
 = (pi/|t|)^(d/2)||a_t||_2`.                                  (2.7)

Together with `|phi_Q(t)|<=1`, set

`K=pi^d M_0 sqrt(M_1M_2)`.

For `d>1`,

`int_R min(1,K|t|^(-d))dt
 = 2 d/(d-1) K^(1/d)`.                                         (2.8)

Thus `phi_Q in L^1`, Fourier inversion gives a continuous `C_0` density, and

`||p_Q||_infinity
 <= (1/(2pi))||phi_Q||_1
 <= [d/(d-1)]M_0^(1/d)(M_1M_2)^(1/(2d))`,                     (2.9)

which is (2.2). QED.

## 3. Original-coordinate rank-two-arm corollary

Take `d=2` and let the hub `H=(H_1,H_2)` consist of exactly two original independent coordinates. Then its joint density cap is `M_0<=1`.

Let `M_r` be a `2 x m_r` physical hub-to-bank matrix of rank two, with

`S_r=s_1(M_r)s_2(M_r)>0`.

For a thin SVD `M_r=O_r Sigma_r R_r^T`, the orthogonal two-dimensional projection `R_r^T X_r` has density cap at most `2`. The invertible map `O_r Sigma_r` therefore gives

`||p_(M_r X_r)||_infinity <= 2/S_r`.                            (3.1)

Applying Theorem 2.1 gives the fully original-coordinate estimate

`boxed:
 ||p_Q||_infinity
 <= 2 sqrt(2) (S_1S_2)^(-1/4),
 p_Q in C_0(R).
`                                                                  (3.2)

Arbitrary same-bank quadratic-affine terms in the two arm banks and arbitrary hub-hub quadratic-affine terms are retained. Additional original coordinates may first be conditioned on; the envelope (2.6) is uniform in the conditioned values, so averaging preserves the same `L^1` Fourier envelope and the same continuity conclusion.

The only structural exclusion is a direct cross term between the two light banks. That exclusion is exact; a coefficient-small light-light tail is not deleted.

## 4. Actual r43 endpoint paid

In r43's diffuse two-sided bisection branch,

`S_1,S_2 > L^2/(64 sqrt(896)).`                                (4.1)

If the common-plane cycle edge and transverse light-light tail vanish exactly, the residual is precisely the two-arm path in Corollary 3.1. Hence

`||p_Q||_infinity
 < 2 sqrt(2) [L^4/(64^2*896)]^(-1/4)`
` = 16 sqrt(2) 896^(1/4) / L`
` = 123.797530897.../L`
` < 124/L`.                                                      (4.2)

The density is continuous and belongs to `C_0`.

This is a genuine closure of the **exact vanishing-cycle endpoint** of r43. It does not yet pay a nonzero physical light-light tail, however small in coefficient norm. Under the rough-input hypotheses such a tail cannot be thrown away perturbatively because inputs can be unbounded and have fragmented supports.

## 5. A target-valid diffuse family with vanishing physical coefficients

Let `m>=2`. Choose two `2 x m` matrices `R_1,R_2` with orthonormal rows; choose them diffuse, e.g. all row entries of order `m^(-1/2)`. On the original coordinates

`H=(H_1,H_2), X in R^m, Y in R^m`,

put

`Q_L=2L H^T R_1 X+2L H^T R_2Y`.                               (5.1)

The compressed matrix on the six active spectral coordinates is the direct sum, over the two hub directions, of

`[[0,L,L],[L,0,0],[L,0,0]]`.

Each `3 x 3` block has eigenvalues `sqrt(2)L,0,-sqrt(2)L`. Therefore the full matrix has

`{sqrt(2)L,sqrt(2)L,-sqrt(2)L,-sqrt(2)L,0,0}`                  (5.2)

plus ambient zeros. For `L>=1/sqrt(2)` this is a valid owner-target matrix with four eigenvalues of modulus at least one. Yet its individual hub-to-bank coefficients can be `O(L/sqrt(m))` and vanish with dimension.

Here `S_1=S_2=L^2`, so (3.2) gives, for every admissible product input law,

`boxed:
 ||p_(Q_L)||_infinity <= 2 sqrt(2)/L,
 p_(Q_L) in C_0(R).
`                                                                  (5.3)

At the threshold `L=1/sqrt(2)`,

`boxed: ||p_(Q_L)||_infinity <= 4.`                             (5.4)

This is an actual dimension-free diffuse-eigenvector estimate with no moment or support assumption.

## 6. Designated partner result applied at an actual inequality

The designated fleet04/B08 theorem treats the opposite, maximally localized anisotropic endpoint

`Q_(R,L)=L X_0^2+2LR U_1V_1+2L R^(-1)U_2V_2`, `R>=3`.          (6.1)

Scaling its proved `L=1` bound gives

`boxed: ||p_(Q_(R,L))||_infinity < 7.251/L.`                   (6.2)

This is used only at its exact source scope. It complements rather than extends Theorem 2.1: the partner pays a localized fixed-`E_2` direct sum with an outer square, while (5.3) pays two genuinely diffuse rank-two arms through a two-coordinate physical hub even when every individual arm coefficient tends to zero.

## 7. Why this route is correction-safe

The proof uses no one-dimensional pointwise van-der-Corput estimate. Its pointwise bound (2.6) comes from a **joint two-arm Plancherel identity after grouping two independent banks**, not from oscillatory decay of an arbitrary scalar density. No rotation of the original input vector is treated as preserving independence. Projected variables are used only through marginal density caps. No physical minor is selected or inverted. No small coefficient tail is discarded. No arbitrary-joint coarea theorem or fiber supremum is used.

## 8. Remaining implication

The current common-plane obstruction is now narrower.

`QFORM-R2-COMMONPLANE-NONZEROEDGE-OR-TAIL-RECEIVER-v1`:

starting from the r43 two-arm state, retain either

1. a nonzero common-plane light-light edge `M_1^T R M_2`, or
2. a nonzero transverse physical tail `T`,

while preserving arbitrary same-bank curvature and product provenance, and obtain a bound that stays finite as the extra edge/tail tends to zero, consistently recovering Theorem 2.1 at the exact zero endpoint.

The exact zero endpoint is therefore not singular in the output-density problem; the remaining difficulty is **uniform leakage stability**, not absence of smoothing at zero leakage.

The unrestricted conjecture remains OPEN. Full-target continuity remains OPEN.
