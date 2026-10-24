# account01/B08 auto11 — independent multiplicity-nine replacement and the exact multiplicity-eight obstruction

Run: `20260924T144535Z-account01-B08-fixedmult-audit-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Baseline manuscript: `7c0d6e60946b19423e6400a12d34b473cf0591e2`, source blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Status: **independent B08 mathematical PASS for multiplicity nine; multiplicity eight remains open.** This report does not claim the unrestricted three-eigenvalue conjecture or global continuity.

## 1. Replacement theorem at multiplicity nine

### Theorem `QFORM-FIXED-MULTIPLICITY-9-B08-v1`

Let `X_1,...,X_n` be independent real random variables with densities bounded by `K<infinity`. Let `A=A^T` be arbitrary, and let `b,c` be arbitrary. If

` s_9(A)>=s>0`,

then

`Q=X^TAX+b^TX+c`

has an essentially bounded density. A self-contained constant ledger from the baseline plus the independently reconstructed marginal-free crossing compilers gives

`boxed: ||p_Q||_infinity <5338 K^2/s.`

The no-pivot branch has a continuous `C_0` density. Global continuity is not asserted for the pivot branches.

### Proof: normalize `K=s=1`

Keep the manuscript parameters

`eta=1/100`, `kappa=1/80^2`.

#### 1.1 No physical pivot

If `A` has no `eta`-pivot, apply the audited baseline spectral-to-volume proposition with order `k=3`. Its multiplicity requirement is exactly

`4k-3=9`,

so

`V_3(A)>=kappa^3`.

A fair original-coordinate cut captures each ordered disjoint three-minor with probability `4^-3`, hence there is a literal physical crossing block `M` with

`E_3(M)=e_3(MM^T)>=4^-3 kappa^3`.

I independently reconstructed the grouped product-Fourier promotion proof used in the current nine-eigenvalue candidate. For an arbitrary literal crossing it gives the row-marginal-free estimate

`||p_Q||_infinity <= C_3 E_3(M)^(-1/6)`,

where the conservative fully derived coefficient is

`C_3=3 sqrt(2) e (9/2)^(1/6)<14.819`.

The proof uses only original-coordinate banks. A heavy physical crossing row is promoted as an actual original-coordinate hub; the exact Gram--Schmidt identities are

`J_i=||w||^2 e_2(CC^T)`

and, after a second promotion,

`H_ij=det(PP^T)||C_2||_F^2`.

When no row is heavy, weighted Holder over determinant-squared subsets gives the entropy factor

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`,

obtained by uniformly ordering the sampled `ell`-subset and applying entropy subadditivity. Product-projection density bounds and Plancherel then give an integrable `|t|^{-3/2}` envelope. No post-rotation independence is used.

Since

`(4^-3 kappa^3)^(-1/6)=160`,

this branch satisfies

`||p_Q||_infinity <160*14.819<2372`.

It has a `C_0` density.

#### 1.2 Scalar pivot

Suppose `|A_hh|>=eta`. Complete the square only in the original coordinate `X_h`. By the audited Schur count, its principal Schur complement `S` retains at least eight eigenvalues of modulus at least one.

If `S` has no `eta`-pivot, then `s_5(S)>=1`. Apply the baseline volume theorem at order two and a fair physical cut:

`E_2(M_S)>=4^-2 kappa^2`.

The independently reconstructed row-marginal-free critical order-two compiler gives

`sup_a E|R-a|^(-1/2) <= C_2 E_2(M_S)^(-1/8)`,

with the conservative coefficient

`C_2=8 sqrt(e) 2^(-1/8)<12.096`.

Hence this half potential is `<153`.

If `S` has an `eta`-pivot, use the baseline pivot proof but retain its exact displayed constants instead of rounding to `600`. With

`L_0=4+4 log16`,

the three pivot subbranches satisfy

- scalar: `H<=10(8+3L_0)=200+120 log16`;
- definite pair: `H<=40 pi`;
- indefinite pair: `H<=10(32+4 log16)+4/e`.

The scalar quantity is the largest. Therefore the truncated half potential obeys

`H<200+120 log16`,

and adding the outside kernel tail `<=1` gives the full bound

`sup_a E|R-a|^(-1/2) <201+120 log16 <533.711`.

The scalar-square profile contributes `eta^-1/2=10`, so the outer scalar-pivot branch gives

`||p_Q||_infinity
 <10(201+120 log16)
 =2010+1200 log16
 =5337.106466...<5338.`

This is the bottleneck in the present B08 constant ledger.

#### 1.3 Definite pair pivot

If a physical principal two-by-two pivot is definite and has determinant modulus at least `eta`, the direct two-dimensional calculation gives

`||p_Q||_infinity <=pi/sqrt(eta)=10pi<32`.

#### 1.4 Indefinite pair pivot

If the physical pair is indefinite and has determinant modulus at least `eta`, the Schur complement retains at least seven eigenvalues of modulus at least one and in particular operator norm at least one. The audited hyperbolic-pair/quarter-power logarithmic-potential proof gives

`||p_Q||_infinity<251`.

These four alternatives are exhaustive, proving the normalized theorem.

### Scaling

Set `Y=KX` and

`Qtilde=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c=(K^2/s)Q`.

The coordinates of `Y` have density cap one and `s_9(A/s)>=1`. Therefore

`||p_Q||_infinity <5338 K^2/s`.

No Gaussianity, log-concavity, moment, bounded-support, connected-support, sign, diagonal-basis, identical-law or post-rotation-independence assumption entered.

## 2. Independent check of the grouped Fourier compiler

For completeness, the analytic step used above was not accepted from a headline. I reconstructed its key identities.

Let `w_T=d_T/Z_ell` be the determinant-squared law on `ell`-subsets, with inclusion marginals `alpha_i`. The exact exponent identity

`prod_i g_i = prod_T (prod_(i in T) g_i^(1/alpha_i))^(w_T)`

permits weighted Holder whenever `alpha_i<=1/2`. For a terminal subset `T`, the map consisting of the promoted hub directions together with the residual projected rows has Gram determinant

`S^2 d_T`.

The audited product-projection theorem gives density cap

`e^(d/2)/(S sqrt(d_T))`, `d=k+ell`,

and the scalar Fourier-power estimate at exponent `1/alpha_i` gives

`int |psi_i(2t(y+u))|^(1/alpha_i)dy
 <=pi sqrt(2e alpha_i)/|t|`.

The geometric mean of determinant denominators is exactly

`Z_ell^(-1/2) exp(H(w)/2)`,

while marginal powers contribute

`exp((1/2)sum alpha_i log alpha_i)`.

Ordering a sampled subset gives

`H(w)+log(ell!) <=ell H(alpha/ell)
 =-sum alpha_i log alpha_i+ell log ell`,

so there is no dimension factor. Together with the hub Plancherel step this yields

`|phi(t)|<=min(1,K_(k,ell)|t|^(-d/2))`

with the stated compiler constant. Promotion uses actual physical rows; SVDs are deterministic Jacobian/projection devices only. This closes the interfaces needed at `(k,ell)=(0,3),(1,2),(2,1)` and at the critical order-two tree.

## 3. Why the B08 rank mechanism stops at nine

The interpolation audit gives simultaneously sharp bounds

`rank R<=3r`, `rank R[L,L]<=r`.

At order-three volume, the terminal bad seed has `r=2`. With `s_9(A)>=1`, global rank subtraction forces three large diagonal entries of `D`, and restricted rank two cannot accommodate the resulting strictly diagonally dominant `3x3` block. With only `s_8(A)>=1`, the same argument forces only two large diagonal entries; a rank-two restricted block can accommodate a nonsingular `2x2` block, so the contradiction disappears.

The direct-sum family

`(1/200)[[0,1,1],[1,0,1],[1,1,1]]`

shows that both rank bounds are attained simultaneously in the no-pivot algebraic class. Thus multiplicity eight cannot be obtained merely by retuning the rank bookkeeping or asserting a hidden symmetry improvement of the nonsymmetric interpolant.

## 4. Current multiplicity-eight endpoint

I also checked the newest terminal-collar reduction available during this run. It does **not** prove multiplicity eight. In the only unpaid no-pivot `s_8(A)>=1` chamber it now extracts a literal two-coordinate anchor `H` with robust outside crossing

`det(A[H,H^c]A[H,H^c]^T)>=0.3649442658...`,

while the principal self-block remains in the small/no-pivot regime. The exact-zero self-block is paid continuously; for an invertible near-singular self-block, the order-two Schur half-potential pays the moving logarithmic singularity, but the current hyperbolic route still leaves the nonlogarithmic term proportional to

`6/sqrt(|det A[H,H]|)`.

This is a genuine unresolved endpoint, not a license to pass through determinant zero by coefficient continuity. A uniform product-preserving near-singular two-anchor receiver, or an equivalent argument removing that nonlogarithmic determinant term while retaining arbitrary complement curvature, is still required.

I therefore do **not** claim `s_8`.

## 5. Validation status

- Exact 17-eigenvalue baseline: **PASS** in the companion full B08 audit.
- Multiplicity-nine replacement: **PASS mathematically in this independent B08 reconstruction**.
- I observed separate repository review artifacts of the nine-eigenvalue argument, but this report does not self-award owner-level release/validation status; canonical integration remains an owner/release-gate action.
- Multiplicity eight: **OPEN** at the explicit near-singular robust two-anchor endpoint above.
- Global continuity for the nine-eigenvalue theorem: **OPEN outside the Fourier-integrable no-pivot branch**.
- Unrestricted three-eigenvalue conjecture: **OPEN**.