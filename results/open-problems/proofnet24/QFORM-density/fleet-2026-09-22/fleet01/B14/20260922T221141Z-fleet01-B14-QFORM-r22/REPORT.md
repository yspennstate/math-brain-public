SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B14, 2026-09-22T22:11:41Z.
attacking: translation-uniform rank-one log-star smoothing by combining the indefinite-pair logarithmic envelope with the partner's radial leakage localization on a whole independent coordinate bank.

# fleet01/B14 — pair plus rank-one bank localization

**Run:** `20260922T221141Z-fleet01-B14-QFORM-r22`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Translations and localization  
**Status:** `ESSENTIAL_STEP_APPLIED / SUPPORTING TARGET-LEVEL THEOREM`; full QFORM remains OPEN.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact sources and corrections used


Assigned partner result actually used: fleet02/B14 r21, `QFORM-RADIAL-LEAKAGE-BATHTUB-v1`, canonical proof

`yspennstate/math-open-problems@2ca523ac73b814a97e846de8d37a932c127eecfb:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260922T220604Z-fleet02-B14-QFORM-r21/REPORT.md`.

For independent cap-one coordinates X, rank-d L, G=LL^T, arbitrary a, `Y=G^{-1/2}(LX-a)`, and nonincreasing Borel psi,

`E psi(|Y|) <= e^(d/2) d v_d int_0^{e^(-1/2)v_d^(-1/d)} psi(r) r^(d-1) dr.`

Second dependency: the completed physical-pair logarithmic envelope

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f:proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

If B is an invertible indefinite physical 2x2 block, `D=|det B|`, `kappa=sigma_min(B)`, and after completing this pair the random critical value is R, then for every r>0,

`p_Q(t) <= 2 sqrt(2)/r + D^(-1/2) E log_+(2r^2/(kappa |t-R|)).`      (1.1)

The live corrections were respected: no law-uniform pointwise Fourier decay, arbitrary-joint coarea, positive conditional-projection moment, post-rotation independence, bounded support diameter, fixed fragment count, single-good-packet extraction, or three-bank cross-core-with-arbitrary-leakage closure is used.

## 2. Explicit one-dimensional logarithmic localization from the partner theorem

Let Z have independent cap-one coordinates, let `L` be a nonzero row vector, put `ell=||L||_2`, and let a be arbitrary. Applying the partner theorem with d=1 and `v_1=2` to

`Y=(LZ-a)/ell`

gives for `psi(r)=log_+(rho/r)`

`E log_+(rho/|Y|) <= 2 sqrt(e) int_0^(1/(2sqrt(e))) log_+(rho/r) dr.`

The integral is explicit. If `rho<=1/(2sqrt(e))`, the right side is `2 sqrt(e) rho`; if `rho>=1/(2sqrt(e))`, it is `1+log(2sqrt(e)rho)`. Therefore, after rescaling,

`boxed: E log_+(R/|LZ-a|) <= 1 + log_+(2 sqrt(e) R/ell).`             (2.1)

This bound is uniform in the translation a and in every support feature of the input laws. It needs no moment, centering, radius, connectedness or fragment-count assumption. The sharper small-R branch is

`E log_+(R/|LZ-a|) <= 2 sqrt(e) R/ell` whenever `2sqrt(e)R<=ell`.      (2.2)

Thus the critical reciprocal singularity in one leakage dimension is indeed nonintegrable, but the logarithmic singularity is uniformly integrable with an explicit translation-free constant.

## 3. New log-star compiler

### Theorem — `QFORM-INDEPENDENT-LINEAR-LOG-STAR-COMPILER-v1`

Let W=(W1,W2) have independent cap-one coordinates and let Z be an independent vector of cap-one coordinates. Let B be a fixed invertible indefinite symmetric 2x2 matrix and set

`D=|det B|`, `kappa=sigma_min(B)`.

Suppose that after completing the B-pair the quadratic expression has the exact form

`Q=(W+m(Z))^T B (W+m(Z)) + LZ+d`,                              (3.1)

where `m` is arbitrary measurable, `L` is a nonzero row vector and d is arbitrary. Put `ell=||L||_2`. Then Q has an essentially bounded density and

`boxed: ||p_Q||_infinity <= D^(-1/2) [3 + log_+(8 sqrt(e) D/(kappa ell))].`  (3.2)

### Proof

Apply (1.1) with `R=LZ+d`. Equation (2.1), with `R0=2r^2/kappa`, yields

`p_Q(t) <= 2sqrt(2)/r + D^(-1/2)[1+log_+(4sqrt(e)r^2/(kappa ell))].`   (3.3)

This is uniform in t and in the arbitrary correlated pair shift m(Z). Choosing `r=sqrt(2D)` gives (3.2). QED.

The point is not the numerical constant: a rank-one heavy-star branch becomes payable as soon as its conditional pair singularity has been softened to logarithmic order in one genuinely independent linear image. This is precisely the positive mechanism suggested by the partner's r21 rank-one obstruction.

## 4. New target-level bank theorem

The previous theorem has a quadratic-form realization which is directly useful under the three-large-eigenvalue target.

Partition the original coordinates into two singleton coordinates P={i,j}, a disjoint bank G, and outside coordinates R. Let u be a unit vector supported on G and let `U=[e_i,e_j,u]`. Assume

`A_SS = U M U^T`,   `A_SR=U C`,                                  (4.1)

where `S=P union G`, M is a nonsingular symmetric 3x3 matrix, C is arbitrary, and `A_RR` is arbitrary. Let B be the leading 2x2 principal block of M and assume B is invertible indefinite. Put

`D=|det B|`, `kappa=sigma_min(B)`, `s=sigma_min(M)`.

Then for arbitrary independent cap-one input laws,

`boxed: ||p_(X^T A X)||_infinity <= 8 (2e)^(1/4) (D kappa s)^(-1/4).`   (4.2)

Numerically the leading constant is `8(2e)^(1/4)=12.2157772909...`.

### Proof

Condition only on the outside original coordinates R. The active variables are the two physical coordinates and the bank scalar

`Y=u^T X_G`.

They are mutually independent. Apply the partner radial theorem at d=1 with indicator kernels (or its density-cap corollary): Y has density at most `sqrt(e)`, uniformly under translations and with no support assumptions.

Write M in block form

`M=[[B,v],[v^T,m33]]`.

Completing the physical B-pair leaves the bank Schur coefficient

`lambda=m33-v^T B^(-1)v`.

Since M and B are invertible,

`1/lambda=(M^(-1))_33`,

so

`|lambda| >= sigma_min(M)=s`.                                  (4.3)

All outside couplings in (4.1) become affine terms in the three bank variables. The pair shift may depend arbitrarily on Y and on the conditioned outside coordinates, which is allowed by the pair-log theorem. Completing the remaining scalar square gives a critical-value remainder

`R_z=lambda (Y-a(z))^2+c(z)`.

For every rho>0, the preimage in Y of an interval of radius rho under this square has total Lebesgue length at most

`2 sqrt(2rho/|lambda|)`.

Since `||p_Y||_infinity<=sqrt(e)`, uniformly in z and t,

`P(|R_z-t|<rho) <= [2 sqrt(2e)/sqrt(|lambda|)] sqrt(rho).`        (4.4)

The general small-ball smoothing form of the pair-log theorem says that a remainder satisfying `P(|R-t|<rho)<=H sqrt(rho)` yields

`||p_Q||_infinity <= 4 sqrt(2H) (D kappa)^(-1/4)`.

Insert `H=2sqrt(2e)/sqrt(|lambda|)` and use (4.3):

`||p_Q||_infinity <= 8(2e)^(1/4) (D kappa |lambda|)^(-1/4)
                   <= 8(2e)^(1/4) (D kappa s)^(-1/4).`

The bound is uniform in the outside conditioning, so averaging proves (4.2). QED.

This theorem strictly enlarges the earlier physical-third-coordinate pair-log branch in one useful direction: the third rank-one Schur direction may be an arbitrarily diffuse linear combination of an entire disjoint original-coordinate bank. All distant fragments and unbounded supports stay inside the whole bank law; no fragment normalization occurs.

## 5. Exact localization status

The preceding fleet01/B14 r20 theorem already proved that the exact worst-case interval small-ball coefficient over all cap-one product laws is unchanged when every marginal is restricted to a bounded finite union of intervals of total measure one. Therefore (3.2) and (4.2), although proved directly for arbitrary laws, also survive the extreme-product localization with exactly the same constants and transfer back with zero tax. This is compatible with the corrections ruling out a uniform support diameter or a uniform fragment-count cap.

A useful regularity strengthening follows by mollification: the same supremum is unchanged if each marginal is restricted to `C_c^infinity` cap-one densities, and also if restricted to strictly positive real-analytic Schwartz cap-one densities. Indeed, convolving a finite-union indicator with a positive compact mollifier or a Gaussian preserves mass one and the cap one, converges in L1, and the product-density error is at most the sum of the marginal L1 errors. Thus rough supports are not a necessary source of extremality, but no uniform moment or support-radius bound follows.

## 6. What remains unpaid

Full QFORM remains OPEN. The structural implication still missing is to show that every matrix with `s_3(A)>=1` enters one of the already-paid aggregate branches. The present result closes a specific rank-one heavy-star interface whenever the surviving logarithmic singularity lands on a genuinely independent bank image and closes the two-singleton-plus-one-bank exact rank-three factorization when the physical pair is quantitatively usable.

It does **not** handle the difficult case in which the linear innovation and quadratic leakage live in the same original-coordinate bank, and it does not imply that a good indefinite physical pair exists under the bare spectral hypothesis. Those are matrix/product-structure debts, not law-localization debts.

Next recipient should combine (4.2) with the structural heavy/diffuse split: either expose a usable physical indefinite pair plus a rank-one disjoint Schur bank, or route the remaining same-bank leakage to the positive-copy/ridge/cross-block mechanisms without imposing false conditional independence.
