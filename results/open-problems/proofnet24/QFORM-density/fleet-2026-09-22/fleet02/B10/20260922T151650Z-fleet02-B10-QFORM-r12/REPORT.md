# fleet02/B10 — rank-three coupled case: heavy-isotropic bank reduction and a flat-bank closure

**Run:** `20260922T151650Z-fleet02-B10-QFORM-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** fleet02/B10, `Rank-three coupled case`  
**Classification:** `ESSENTIAL_STEP_APPLIED` plus local `CANDIDATE_REFUTED`; full target **OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and source pins

The exact target remains: for independent real physical coordinates `X_i` with densities bounded by one and symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal density bound for `X^T A X`, or give a genuine counterexample. No rotation of the random vector is used below.


Completed named-partner result actually applied:

- fleet03/B10, `QFORM-RANK3-NONISOTROPIC-PIVOT-v1`, canonical report `yspennstate/math-open-problems@5ce98ee83b2fef75136f10cdd0e89741f017d3e0`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/fleet03-B10-20260922T141643Z-r11/REPORT.md`. For exact rank three, if physical row `u_i` has leverage `ell_i=||u_i||^2` and nonzero diagonal pivot `d_i=u_i^T Lambda u_i`, then

`||p_Q||_infinity < 97 [ |d_i| ell_i |det Lambda| ]^(-1/4)`.

The source also records the sharp product-linear marginal bound `||p_{sum b_j X_j}||_infinity <= sqrt(2)` for a unit coefficient vector `b`, via Ball--Rogozin.

Earlier fleet02/B10 theorem actually reused:

- `QFORM-HYPERBOLIC-SQUARE-v1`, canonical report `yspennstate/math-open-problems@1eba911614ef9f6683f8eacb5d6608a0f9a4b833`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260922T1147Z-qform-rank3-coupled-B10-r1/REPORT.md`. For independent cap-one `X,Y,Z`,

`T=2aXY+H(Y)+b(Z+theta(Y))^2`

has `||p_T||_infinity <= 4/sqrt(|ab|)`.

By scaling, if the three independent variables have density caps `K_X,K_Y,K_Z`, then the canonical form `2XY+Z^2` has

`||p||_infinity <= 4 K_Z sqrt(K_X K_Y)`.  
This scaling is used below with `K_X=K_Y=K_Z=sqrt(2)`.

## 2. First unpaid implication, sharpened immediately

For exact rank three write

`A=U Lambda U^T`, `U^T U=I_3`, `|lambda_r|>=1`.

For row `u_i`, define

`ell_i=||u_i||^2`, `d_i=A_ii=u_i^T Lambda u_i`,

and the off-diagonal row energy

`sigma_i^2 = sum_{j!=i} A_ij^2`.

### Lemma 2.1 — exact heavy-isotropic cross-energy identity

One has

`boxed( sigma_i^2 = u_i^T Lambda^2 u_i - d_i^2 >= ell_i-d_i^2 ).`

Hence, if `ell_i>1/32` and `|d_i|<1/8`, then `sigma_i>1/8`.

**Proof.** Since `A^2=U Lambda^2 U^T`,

`sum_j A_ij^2=(A^2)_ii=u_i^T Lambda^2 u_i`.

Subtract the `j=i` term `d_i^2`. Since every nonzero eigenvalue of `Lambda` has modulus at least one, `Lambda^2 >= I_3`, so `u_i^T Lambda^2 u_i>=ell_i`. Finally

`ell_i-d_i^2 > 1/32-1/64=1/64`.

### Lemma 2.2 — product-linear normal form in the hard branch

Assume `sigma_i>0` and define

`S_i = sigma_i^(-1) sum_{j!=i} A_ij X_j`.

Then `X_i` and `S_i` are independent, `S_i` has a density bounded by `sqrt(2)`, and exactly

`Q = d_i X_i^2 + 2 sigma_i X_i S_i + R_i(X_{bar i})`.

**Proof.** Independence is physical-coordinate independence. The coefficient vector `(A_ij/sigma_i)_{j!=i}` has Euclidean norm one by definition, so the partner source's Ball--Rogozin marginal bound gives `||p_{S_i}||_infinity<=sqrt(2)`. The displayed decomposition is simply the `i`th row expansion of `X^TAX`.

This gives a quantitative heavy-row dichotomy. If `ell_i>1/32` and `|d_i|>=1/8`, the named partner theorem and `|det Lambda|>=1` give the actual inequality

`||p_Q||_infinity < 97[(1/8)(1/32)]^(-1/4) = 388.`

If instead `|d_i|<1/8`, then the form contains an **original-product, uniformly strong hyperbolic coupling** `2 sigma_i X_i S_i` with `sigma_i>1/8` and `||p_{S_i}||_infinity<=sqrt(2)`. The only remaining obstruction is the correlation of `S_i` with the residual quadratic term `R_i`; replacing this by a conditional-density cap is invalid by the existing `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` correction.

Thus a current exact-rank-three end-to-end route is: diffuse-range theorem for the all-small-leverage branch; the partner nonisotropic-pivot theorem for a heavy row with `|d_i|>=1/8`; and the product-linear hard branch above when a heavy row is nearly isotropic. The first unpaid implication is now precisely to aggregate the residual product bank before losing its provenance.

## 3. Flat-bank heavy-isotropic family: single-edge and single-triple selection both fail, but the target density is uniformly bounded

The next construction is inside the exact target and lives exactly in the unpaid heavy-isotropic regime.

Fix `m>=1`. In a spectral basis `(e_+,e_-,e_2)` take

`Lambda = [[0,1,0],[1,0,0],[0,0,1]]`,

whose eigenvalues are `{1,-1,1}`. Define a Parseval frame with `1+3m` physical rows:

- one heavy row `u_0 = 2^(-1/2) e_+`;
- `m` plus-bank rows `u_{+,r}=(2m)^(-1/2)e_+`;
- `m` minus-bank rows `u_{-,r}=m^(-1/2)e_-`;
- `m` square-bank rows `u_{2,r}=m^(-1/2)e_2`.

Indeed the row outer products sum to `I_3`. Put `A_m=U Lambda U^T`. Then `A_m` has exact rank three and nonzero spectrum `{1,-1,1}`.

### 3.1 The heavy row is exactly isotropic but has constant total cross energy

For the heavy row,

`ell_0=1/2`, `d_0=A_00=0`.

Its only nonzero off-diagonal couplings are to the minus bank, with

`A_{0,-r}=1/sqrt(2m)`.

Therefore

`sum_{j!=0} A_0j^2 = 1/2`,

while

`max_{j!=0}|A_0j| = 1/sqrt(2m) -> 0`.

So constant hyperbolic row energy does **not** force one dimension-free physical cross edge.

The only nonzero diagonal physical pivots are the square-bank rows, where

`ell_{2,r}=1/m`, `d_{2,r}=1/m`.

Thus the best value of the partner pivot product is

`max_i |d_i| ell_i = 1/m^2`,

and the partner theorem, applied literally to any square-bank row, gives only

`||p_Q||_infinity < 97 sqrt(m)`.

This does not contradict the partner theorem; it shows that selecting one scalar pivot is dimensionally incomplete in the flat heavy-isotropic regime.

### 3.2 Every heavy-row physical triple also has vanishing determinant

For a physical triple `I`, exact rank three gives

`det A_{I,I} = det(Lambda) det(U_I)^2`.

A nonzero triple containing the heavy row must contain one minus-bank row and one square-bank row. For such a triple,

`|det U_I|=1/(sqrt(2)m)`,

hence

`|det A_{I,I}|=1/(2m^2)`.

All other triples containing the heavy row are singular. Consequently even heavy leverage does not force a single dimension-free principal triple determinant.

This is a source-valid counterexample to any attempted structural lemma of the form

`heavy isotropic row => one uniformly large cross edge or one uniformly large physical 3x3 determinant`.

It is **not** a counterexample to the density conjecture.

### 3.3 Exact bank decomposition and universal density bound 8

For arbitrary independent physical inputs with densities bounded by one, define the disjoint-bank linear forms

`Z_+ = X_0/sqrt(2) + (1/sqrt(2m)) sum_{r=1}^m X_{+,r}`,

`Z_- = (1/sqrt(m)) sum_{r=1}^m X_{-,r}`,

`Z_2 = (1/sqrt(m)) sum_{r=1}^m X_{2,r}`.

Because the three forms use disjoint physical coordinate sets, `Z_+,Z_-,Z_2` are independent. The quadratic form is exactly

`Q_m = 2 Z_+ Z_- + Z_2^2`.

Their marginal density caps are all at most `sqrt(2)`:

- `X_0/sqrt(2)` has density cap `sqrt(2)`, and convolution with the independent plus-bank sum cannot increase the `L^infinity` norm;
- the coefficient vectors of `Z_-` and `Z_2` have Euclidean norm one, so Ball--Rogozin gives cap `sqrt(2)`.

Scale the three variables in `QFORM-HYPERBOLIC-SQUARE-v1`. With `K_+=K_-=K_2=sqrt(2)`,

`||p_{Q_m}||_infinity <= 4 K_2 sqrt(K_+ K_-) = 8.`

This holds for every `m` and for **all** independent input laws with physical density cap one.

Therefore this family simultaneously proves two things:

1. the heavy-isotropic branch cannot be closed by selecting one cross coefficient, one scalar pivot, or one heavy-row principal triple before paying reciprocal local constants;
2. the same branch can nevertheless be uniformly closed when its product bank is aggregated first.

That is exactly the operator-order lesson suggested by the earlier Pluecker counterexamples, now realized in the previously unpaid heavy-isotropic geometry itself.

## 4. First remaining implication

### `QFORM-HEAVY-ISOTROPIC-BANK-AGGREGATION-v1`

In the arbitrary heavy-isotropic exact-rank-three branch, Lemma 2.2 supplies

`Q=d_iX_i^2+2 sigma_i X_i S_i+R_i`,

with `sigma_i>1/8`, `X_i independent of S_i`, and `S_i` a normalized linear form of the original independent residual coordinates with density cap at most `sqrt(2)`. Prove a dimension-free density bound by using the exact rank-three/Parseval constraints on the **joint product bank** generating `(S_i,R_i)` before reducing to conditional density caps or any reciprocal single-minor estimate.

The flat-bank construction proves this is plausible and identifies the right scale: complete bank aggregation can retain a constant even while every individual edge and heavy-row triple determinant tends to zero.

A sufficient next lemma would be a product-preserving decomposition of the residual coordinates into finitely many disjoint banks that keeps one square-like transverse direction with bounded marginal cap, or an operator inequality that achieves the same aggregation without an explicit partition. The existing nonlinear conditional-cap counterexample shows that any argument discarding linear-product provenance before this step cannot succeed.

## 5. Status

`ESSENTIAL_STEP_APPLIED` for the quantitative heavy-row reduction and the exact flat-bank closure; local `CANDIDATE_REFUTED` for single-edge/single-triple heavy-isotropic selection. The full arbitrary-rank-three case, and therefore the full arbitrary-matrix conjecture, remains OPEN.
