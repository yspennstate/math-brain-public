SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B13, 2026-09-22T20:34:07Z.
attacking: the final exact-rank-three mixed one-heavy/two-transverse-bank obstruction, by paying either genuine three-volume in a light bank or a non-null heavy Rayleigh coefficient before any reciprocal physical-minor selection.

# fleet03/B13 — two exact-rank-three closure collars from extremal product banks

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T203407Z-fleet03-B13-qform-r16`  
**Assignment:** Extremal product laws  
**Classification:** `ESSENTIAL_STEP_APPLIED / TWO TARGET-LEVEL SUBBRANCHES CLOSED / FULL-QFORM-OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and source-valid inputs

The full owner target remains OPEN: independent real physical coordinates have arbitrary probability densities bounded by one, and the symmetric matrix has at least three eigenvalues of modulus at least one. No support, moment, Gaussian, log-concavity, connected-support, finite-fragment, or post-rotation independence hypothesis is added. Continuity is tracked separately.

This report attacks the concrete exact-rank-three residual isolated by fleet01/B13 run `20260922T190849Z-fleet01-B13-qform-r17`, canonical report

`yspennstate/math-open-problems@01c524aa389abf1b9b58c852bfa11fc747ec5b59`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B13/20260922T190849Z-fleet01-B13-qform-r17/REPORT.md`.

In its final unpaid mixed branch one has

`A=R Lambda R^T`, `R^T R=I_3`, `min_j |lambda_j(Lambda)|>=1`,

one heavy original coordinate `i` with

`r_i=sqrt(c) u`, `c>3/10`, `||u||=1`,

and, after conditioning the other heavy original coordinates, two disjoint light physical banks `L_1,L_2`. Writing

`r_j=t_j u+p_j`, `p_j in u^perp`,

and

`G_a=sum_(j in L_a) p_j p_j^T`,

that report proves

`G_a >= kappa I_(u^perp)`, `kappa=7/800`, for `a=1,2`.       (1.1)

The high normalized transverse-leverage subbranch is already paid there; (1.1) is the final two-bank branch.

I use three completed analytic inputs at their exact scopes:

1. fleet03/B19 `QFORM-EXACT-CROSS-RANK-L2-v1`, canonical commit `9d55d9ca5a7beaed6f693a57bd32b5fc9949b981`: an exact-rank-three original-coordinate cross bank `C` has bounded continuous density with `||p_Q||_infinity <=3e Pi_3(C)^(-1/3)` in the general-bank case.
2. fleet01/B19 run `20260922T191359Z-b19-qform-r11`, `QFORM-EXACT-RANK2-CROSS-HALF-RIESZ-v1`: for two independent 2D banks with cap-one densities and invertible cross matrix `S`, `H_(1/2)<=4sqrt(2)|det S|^(-1/4)`; its proof is an L2 mixed-Hessian estimate and scales with the L2 norms of the two bank densities.
3. the two-dimensional product-projection theorem already source-pinned in fleet03/B13 r14: if a 2D original-coordinate coefficient map has Gram `G`, its projected density is at most `e/sqrt(det G)`.

The designated partner fleet04/B13 is also actually used below. Its latest completed report visible at this run is

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B13/20260922T201036Z-fleet04-B13-affine-bank-bangbang-r1/REPORT.md`,

theorem `QFORM-AFFINE-BANK-BANGBANG-WITNESS-v1`. It proves constant-preserving reduction of every bounded measurable affine-slab functional, including an outside-parameter average, from arbitrary cap-one product densities to fixed arbitrary unit-measure product indicators. Therefore every geometric slab inequality proved below for all extreme products transfers with exactly the same coefficient to all admissible product laws; the optimizing sets do not depend on the outside conditioning parameter.

The live corrections are retained: no arbitrary-joint rank-three coarea bound, no conditional positive projection-cap moment, no pointwise law-uniform quadratic-phase decay, no post-rotation independence, and no bounded-diameter/fixed-fragment reduction is used.

## 2. New structural currency: the missing longitudinal variance of each light bank

For bank `a`, define its full spectral Gram

`S_a=sum_(j in L_a) r_j r_j^T`.

Relative to the orthogonal splitting `R^3=span(u) direct_sum u^perp`, write

`S_a=[[tau_a,h_a^T],[h_a,G_a]]`.                              (2.1)

Since `G_a>=kappa I_2`, it is invertible. Define the Schur longitudinal variance

`rho_a := tau_a-h_a^T G_a^(-1)h_a >=0`.                       (2.2)

Equivalently,

`rho_a=min_(w in u^perp) sum_(j in L_a)(t_j-w dot p_j)^2`.     (2.3)

Thus `rho_a=0` exactly when every spectral row in bank `L_a` lies in one 2D graph plane over `u^perp`. Also

`det S_a=det G_a * rho_a >= kappa^2 rho_a`.                    (2.4)

This is a product-preserving geometric scalar: it measures whether a light bank genuinely carries the third spectral direction before any physical minor is selected.

## 3. First new theorem: genuine bank three-volume closes the branch directly

### Theorem 3.1 — `QFORM-RANK3-LIGHTBANK-FULLVOLUME-CUT-v1`

In the final mixed branch (1.1), if for either `a=1` or `2`

`rho_a >= eps >0`,                                               (3.1)

then the full exact-rank-three quadratic output has a bounded continuous density and

`boxed(
 ||p_Q||_infinity
 <=3e [kappa^2 sqrt(c eps)]^(-1/3)
 <=3e [kappa^2 sqrt((3/10)eps)]^(-1/3).
)`                                                              (3.2)

At `eps=1/100`,

`boxed(||p_Q||_infinity <505.697.)`                             (3.3)

The estimate is uniform in dimension, all input laws, all support geometry, and all conditioned affine leakage.

### Proof

Take the physical cut `I=L_a`, `J=I^c`, without rotating the physical input law. Its exact cross block is

`C=A[I,J]=R_I Lambda R_J^T`.                                    (3.4)

Put `T=R_J^T R_J=I_3-S_a`. The complement contains the heavy row `r_i=sqrt(c)u` and the other transverse bank `L_b`, `b!=a`. Therefore

`T >= c uu^T + S_b`.                                           (3.5)

Write `S_b` in the same block form. The determinant of the lower matrix is

`det(c uu^T+S_b)
 =det G_b [c+tau_b-h_b^T G_b^(-1)h_b]
 >=c det G_b
 >=c kappa^2`.                                                  (3.6)

Since determinant is monotone on positive-definite matrices under Loewner order,

`det T>=c kappa^2`.                                             (3.7)

By (2.4), `det S_a>=kappa^2 eps`. Both Grams are positive definite, hence the cross block (3.4) has exact rank three. Its nonzero singular-value product satisfies the exact identity

`Pi_3(C)^2
 =pdet(CC^T)
 =det(Lambda)^2 det(S_a)det(T)`.                                (3.8)

Indeed the three nonzero eigenvalues of `CC^T=R_I Lambda T Lambda R_I^T` equal those of the 3x3 positive matrix obtained after cyclic compression, whose determinant is the right-hand side. Since `|det Lambda|>=1`, (3.7)-(3.8) give

`Pi_3(C)>=kappa^2 sqrt(c eps)`.                                 (3.9)

Apply the completed exact-rank-three cross-bank theorem to (3.4). It gives a continuous density and

`||p_Q||_infinity<=3e Pi_3(C)^(-1/3)`,

which is (3.2). QED.

This theorem consumes the entire physical cross cut before inversion; it does not choose one tiny 3x3 physical minor.

## 4. A cap-scaled exact-rank-two half-Riesz lemma

The second closure collar needs a quantitative form of the completed exact-rank-two endpoint for 2D bank densities.

### Lemma 4.1

Let `Z_1,Z_2` be independent `R^2`-valued random variables with probability densities `g_a` satisfying

`||g_a||_infinity<=M_a`.

Let `S` be invertible symmetric `2x2`, and allow arbitrary quadratic-affine self terms on each bank:

`R=Z_1^T S Z_1+2Z_1^T S Z_2+Z_2^T S Z_2
   +ell_1 dot Z_1+ell_2 dot Z_2+c`.                             (4.1)

Then

`boxed(
 H_(1/2)(R):=sup_t E|R-t|^(-1/2)
 <=4sqrt(2)(M_1M_2)^(1/4)|det S|^(-1/4).
)`                                                              (4.2)

### Proof

For the characteristic function, absorb each self quadratic-affine phase into

`a_t(z)=g_1(z)e^{it(...)} , b_t(z)=g_2(z)e^{it(...)}`.

The rank-two mixed Fourier transform gives

`|phi_R(t)|
 <=pi |t|^(-1)|det S|^(-1/2)||a_t||_2||b_t||_2
 <=pi sqrt(M_1M_2)|t|^(-1)|det S|^(-1/2)`.                    (4.3)

Together with `|phi_R|<=1`, set

`A=pi sqrt(M_1M_2)|det S|^(-1/2)`.

The Abel half-Riesz identity used in the completed peer theorem gives

`H_(1/2)(R)
 <=sqrt(2/pi) int_0^infinity t^(-1/2)min(1,A/t)dt`.

The integral is exactly `4sqrt(A)`, yielding (4.2). QED.

No independence inside either 2D vector is assumed; only independence of the two disjoint physical banks is used.

## 5. Second new theorem: a non-null heavy Rayleigh coefficient closes the two-bank branch

Represent `Lambda` in the spectral orthonormal basis beginning with `u`:

`Lambda=[[a,b^T],[b,D]]`,
`a=u^T Lambda u`.                                               (5.1)

### Theorem 5.1 — `QFORM-RANK3-TWOBANK-NONNULL-RAYLEIGH-v1`

In the final mixed branch (1.1), if

`|a|>=delta>0`,                                                  (5.2)

then the exact-rank-three output has an essentially bounded density with

`boxed(
 ||p_Q||_infinity
 <=4sqrt(2) sqrt(e/kappa)c^(-1/2)
    |a|^(-1/4)|det Lambda|^(-1/4)
 <=K_0 delta^(-1/4),
)`                                                              (5.3)

where

`K_0=4sqrt(2)sqrt(800e/7)sqrt(10/3)
    =182.0361225384...`.                                       (5.4)

Thus at `delta=1/100`,

`boxed(||p_Q||_infinity<575.649.)`                              (5.5)

No longitudinal variance `rho_a` is required for this theorem.

### Proof

Condition on all heavy original coordinates except `X_i`. Their contribution becomes a deterministic spectral translation. For the two disjoint light banks define their spectral sums and transverse projections

`W_a=sum_(j in L_a) r_j X_j=s_a u+Z_a`, `Z_a in u^perp`.       (5.6)

The two `Z_a` are independent because the physical banks are disjoint. Whitening the coefficient map in each bank and applying the 2D product-projection theorem gives

`||p_(Z_a)||_infinity
 <=e/sqrt(det G_a)
 <=e/kappa=:M`.                                                 (5.7)

Let the conditioned fixed transverse translation be `z_0`; put `z=z_0+Z_1+Z_2`. The scalar spectral coordinate has the form `sqrt(c)X_i+s`, where `s` may depend arbitrarily on both banks. Since `a!=0`, complete the square in the ORIGINAL independent variable `X_i`:

`Q
 =ac [X_i+s/sqrt(c)+(b dot z)/(a sqrt(c))]^2
   + z^T S z`,                                                  (5.8)

where

`S=D-bb^T/a`,
`det S=det Lambda/a`.                                           (5.9)

The square shift in (5.8) may depend on all bank variables, but the cap-one square pushforward is translation-uniform. Hence

`||p_Q||_infinity
 <=|ac|^(-1/2) H_(1/2)(z^T S z).`                              (5.10)

Expanding `z^T S z` into the independent `Z_1,Z_2` gives exactly the form of Lemma 4.1, with arbitrary affine terms coming from `z_0`. By (5.7),

`H_(1/2)(z^T S z)
 <=4sqrt(2) M^(1/2)|det S|^(-1/4).`                            (5.11)

Use (5.9), `M=e/kappa`, `c>3/10`, and `|det Lambda|>=1` to obtain (5.3)-(5.5). QED.

The key point is that no conditional density of a spectral fiber is used. Each 2D transverse bank is aggregated in its own disjoint ORIGINAL coordinate set first; the rank-two mixed-Hessian estimate then pays the two bank vectors jointly.

Continuity is not asserted from this half-Riesz/square splice; the theorem proves absolute continuity and an essential L-infinity bound.

## 6. Designated-partner transfer to the exact extreme-product geometry

The two theorems above were derived using only cap-one facts and therefore can be run first on arbitrary extreme products `prod_j 1_(E_j)`, `|E_j|=1`. In that form they give the genuine geometric slab inequalities

`|{x in prod E_j: x^T A x in J}|<=C_cut(eps)|J|`              (6.1)

in Theorem 3.1's branch and

`|{x in prod E_j: x^T A x in J}|<=C_ray(delta)|J|`            (6.2)

in Theorem 5.1's branch, uniformly over the affine terms generated by conditioning the other heavy coordinates.

Now apply the completed designated-partner theorem `QFORM-AFFINE-BANK-BANGBANG-WITNESS-v1` to the *actual averaged slab functional* with the outside heavy coordinates included as the parameter. It selects fixed measure-one sets, independent of that parameter, and proves that the arbitrary-density slab probability is no larger than an extreme-product slab probability. Consequently (6.1)-(6.2) transfer with **zero constant loss** to every original cap-one product law. This is the partner theorem applied to the exact new inequalities, not merely cited as background.

No interval/centered-set extremality is claimed: the `E_j` may be unbounded and infinitely fragmented.

## 7. New exact-rank-three residual after this run

Combine fleet01/B13's exhaustive mixed reduction with Theorems 3.1 and 5.1. Fix, for example,

`eps=delta=1/100`.                                               (7.1)

Every final one-heavy/two-transverse-bank exact-rank-three state is now paid with a universal constant unless simultaneously

`boxed(
 |u^T Lambda u|<1/100,
 rho_1<1/100,
 rho_2<1/100.
)`                                                              (7.2)

Thus any surviving exact-rank-three counterexample sequence in this branch must approach a very specific codimension-three geometry:

1. the heavy spectral direction approaches the `Lambda`-null cone;
2. each light physical bank approaches a 2D graph plane over the same transverse spectral plane;
3. both banks nevertheless retain the quantitative transverse ellipticity `G_a>=7/800 I_2`.

This is much narrower than the previous generic one-heavy/two-bank obstruction. It also cleanly separates two mechanisms: genuine third-volume is paid by an exact rank-three physical cut; nonzero heavy Rayleigh is paid by a rank-two mixed-Hessian half-Riesz estimate behind the original scalar square.

The remaining exact-rank-three implication is therefore

`QFORM-RANK3-NEARNULL-TWOPLANAR-BANK-CLOSURE-v1`:

> Under (7.2) and `G_1,G_2>=7/800 I_2`, exploit the strong transverse coupling forced by `||Lambda u||>=1` to obtain a product-preserving grouped payment. The proof must remain stable as the two longitudinal Schur variances tend to zero, and must not condition on the entire spectral complement or select one tiny physical minor.

The exact simultaneous-null-pair endpoint from fleet03/B13 r12 and the aggregate zero-pair theorem from r14 remain useful controls, but neither by itself supplies this near-null/two-planar interpolation.

## 8. Constants check

With `kappa=7/800`, `c_0=3/10`, `eps=delta=1/100`:

`Pi_cut_lower=kappa^2 sqrt(c_0 eps)=4.1935008308989285e-6`,

`C_cut=3e Pi_cut_lower^(-1/3)=505.6967456841...`,

`K_0=4sqrt(2)sqrt(e/kappa)c_0^(-1/2)=182.03612253845...`,

`C_ray=K_0 delta^(-1/4)=575.6487636470...`.

The sibling checker records these values and the determinant identities on random positive-semidefinite Gram samples.

## 9. Status

- `QFORM-RANK3-LIGHTBANK-FULLVOLUME-CUT-v1`: **PROVED SUPPORTING TARGET-LEVEL THEOREM**.
- `QFORM-RANK3-TWOBANK-NONNULL-RAYLEIGH-v1`: **PROVED SUPPORTING TARGET-LEVEL THEOREM**.
- fleet04/B13 affine-bank bang-bang theorem: **APPLIED WITH ZERO LOSS TO (6.1)-(6.2)**.
- Full exact-rank-three problem: **still OPEN**, now narrowed in this mixed branch to (7.2).
- Full owner QFORM target: **OPEN / NOT PROVED**.
- Full continuity: **OPEN**; continuity is obtained in Theorem 3.1's cross-rank-three branch, but not asserted in Theorem 5.1's half-Riesz branch.
