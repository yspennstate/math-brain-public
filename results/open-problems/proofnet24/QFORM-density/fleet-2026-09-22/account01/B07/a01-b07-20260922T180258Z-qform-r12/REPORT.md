SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B07, 2026-09-22T18:02:58.839638Z.
attacking: two-sided determinant-pattern selection for the partner O1 heavy-ridge branch, preserving aggregate minor mass without reciprocal single-minor selection.

# account01/B07 — two-sided heavy-ridge minor packet for O1

Programme: `QFORM-DENSITY-3EIG-20260922`.  Outcome: **ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN**.  Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Conditional end-to-end argument and first missing implication

The target is the unrestricted statement: independent real coordinates with densities bounded by one, arbitrary real symmetric A, and at least three eigenvalues of absolute value at least one imply a universal L-infinity bound for the density of X^T A X. Continuity is separate.

The completed account03/B07 theorem `QFORM-THIRD-COMPOUND-OVERLAP-REDUCTION-v1`, canonical `yspennstate/math-open-problems@685929d9daee92a164dbf6ba6f9305d2e6550826`, reduces every target matrix to one of the O0/O1/O2/O3 original-coordinate third-compound overlap packets. O0 has a completed diffuse ridge payment and a finite-heavy residual. The designated partner account02/B07 then treated O1 by the exact identity

`H_i = a_i C_2(B) - W_(u_i) B iota_(v_i)`

and, for a_i !=0, by the Schur identity

`H_i = a_i C_2(N_i)`,  `N_i=B-u_i v_i^T/a_i`,

with `W_i:=||H_i||_HS^2=a_i^2 E_i`, `E_i=e_2(N_i N_i^T)`.  Its canonical report is `yspennstate/math-open-problems@41ed0a3af4b1aec79c036031a00066b0f49a9a45`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260922T170237Z-b07-e559ca/REPORT.md`.

At the partner's calibrated scale gamma_i, the ridge kernel has trace 3/2, and the exact inequalities

`gamma_i^4 <= 2 E_i`,
`D_i:=det(I+N_i N_i^T/gamma_i^2) >= E_i/gamma_i^4`

hold.  The partner paid the branch with row or column ridge leverage <=1/2; if both failed it left at most two heavy rows and at most two heavy columns, but did not preserve a quantitative amount of determinant mass jointly on those two finite cores.

This run supplies that missing two-sided determinant packet.  It also enlarges the paid analytic branch from leverage 1/2 to leverage 29/40 by applying account03/B09 `QFORM-PIVOT-RIDGE-BILINEAR-v1` at a different parameter q.

A full proof would follow after the remaining O1 singular/near-zero packet and the finite bridge packets below are paid, together with the already isolated O0/O2/O3 residuals.  No subclass is promoted to the full theorem.

## 2. Source-pinned peer result actually applied

The assigned partner result actually used is account02/B07 `QFORM-O1-COMPOUND-SCHUR-FACTOR-v1` / `QFORM-O1-PIVOT-RIDGE-PAYMENT-v1`, canonical commit `41ed0a3af4b1aec79c036031a00066b0f49a9a45` at the path above.  In particular, this run uses its exact identities `W_i=a_i^2 E_i`, `gamma_i^4<=2E_i`, and `D_i>=E_i/gamma_i^4` in the final inequalities, not merely as background.

The analytic payment used is account03/B09 `QFORM-PIVOT-RIDGE-BILINEAR-v1`, canonical `yspennstate/math-open-problems@62bdcf30669c1037a3c7d87aee1fcb2bdcccd251`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/account03-B09-20260922T155042Z-qform12/REPORT.md`.  It permits every 1<=q<=2 and retains arbitrary self blocks, outside couplings, signs, extra spectrum, and the original product law.

No post-rotation independence, uniform pointwise Fresnel decay, conditional spectral-density cap, fiber-supremum estimate, or single-good-minor inference is used.

## 3. The two-sided joint regularized-minor law

Fix one nonzero-pivot O1 index i and abbreviate N=N_i, gamma=gamma_i.  Put

`M=N/gamma`,
`D=det(I+M M^T)`,
`K_L=M M^T(I+M M^T)^(-1)`,
`K_R=M^T M(I+M^T M)^(-1)`.

Both kernels have trace 3/2.  Define a probability law on pairs of equally sized physical row/column subsets by

`mu(R,S)=det(M[R,S])^2/D`,  `|R|=|S|`,

including the empty pair.  Cauchy--Binet and the principal-minor expansion give

`sum_(|R|=|S|) det(M[R,S])^2 = det(I+M M^T)=D`.                 (3.1)

The row marginal is the L-ensemble with L=M M^T and kernel K_L; the column marginal is the analogous L-ensemble with kernel K_R.  Thus for every physical row set H_L and column set H_R,

`mu(R cap H_L = empty)=det(I-K_L[H_L,H_L])`,
`mu(S cap H_R = empty)=det(I-K_R[H_R,H_R])`.                    (3.2)

This is the joint determinant currency needed to track both sides simultaneously.

## 4. Enlarged analytic payment

Take

`q=29/20`,  `tau=q/2=29/40`,  `r=39/20`.

For theta=3/2, the source exponent is

`beta=theta/(2q)=15/29`,  `beta r=117/116>1`,

so r is admissible in account03/B09.  If either

`max diag K_L <=29/40`  or  `max diag K_R <=29/40`,

swap the two banks if necessary and apply that theorem.  Its exact formula gives

`||p_Q||_infinity <= 103.883937 |a_i|^(-1/2) gamma^(-1/2) D^(-1/6)`.  (4.1)

Now apply the designated partner inequalities.  Since `D>=E_i/gamma^4`,

`gamma^(-1/2)D^(-1/6) <= gamma^(1/6) E_i^(-1/6)`.

Since `gamma^4<=2E_i`,

`gamma^(1/6)<=2^(1/24)E_i^(1/24)`.

Consequently

`boxed( ||p_Q||_infinity <107 |a_i|^(-1/2) E_i^(-1/8)
                         =107 (a_i^2 W_i)^(-1/8). )`             (4.2)

The conclusion here is essential boundedness; this source theorem does not supply the full continuity conclusion.

## 5. New theorem: two-sided heavy packet retains D/20

### Theorem `QFORM-O1-TWOSIDED-HEAVY-PACKET-v1`

Assume both 29/40 leverage gates in Section 4 fail.  Define

`H_L={j:(K_L)_jj>29/40}`,
`H_R={k:(K_R)_kk>29/40}`.

Then both sets are nonempty and

`1<=|H_L|,|H_R|<=2`.                                             (5.1)

Moreover, there are nonempty fixed subsets `T subset H_L`, `S subset H_R` such that

`boxed( sum_(R cap H_L=T, J cap H_R=S, |R|=|J|)
             det(M[R,J])^2 >= D/20. )`                           (5.2)

Equivalently in the partner variables,

`boxed( a_i^2 gamma_i^4 W_(i,T,S) >= W_i/20, )`                 (5.3)

where `W_(i,T,S)` denotes the dimensionless sum in (5.2), and `W_i=a_i^2E_i`.

### Proof

Because `tr K_L=tr K_R=3/2`, any set of diagonal entries strictly exceeding 29/40 has cardinality at most two, proving (5.1).

For a nonempty heavy set H, the contraction `I-K[H,H]` is positive semidefinite.  By Hadamard,

`det(I-K[H,H]) <= product_(j in H)(1-K_jj)
                < (11/40)^|H| <=11/40`.                         (5.4)

Using (3.2) on each side and a union bound under the *joint* law mu,

`mu(R hits H_L and J hits H_R)
 > 1-11/40-11/40 =9/20`.                                        (5.5)

There are at most

`(2^|H_L|-1)(2^|H_R|-1)<=9`

possible nonempty incidence pairs `(R cap H_L,J cap H_R)`.  Pigeonhole applied to (5.5) gives one pair of fixed nonempty patterns `(T,S)` with probability at least 1/20.  Multiplying by D proves (5.2).

Finally account02/B07 gives `D>=E_i/gamma_i^4`; hence

`a_i^2 gamma_i^4 W_(i,T,S)
 >= a_i^2 gamma_i^4(D/20)
 >= a_i^2E_i/20=W_i/20`,

which is (5.3).  This is the requested direct application of the partner result to an actual new inequality.  QED.

The theorem is aggregate: it does not select and reciprocate one tiny determinant.  If a collection of O1 indices all lies in this heavy branch, summing (5.3) preserves at least one twentieth of their total partner O1 mass after the natural `a_i^2 gamma_i^4` weighting.

## 6. Balanced patterns factor exactly through a <=2 by <=2 physical core

The selected heavy patterns have sizes 1 or 2 on each side.  Suppose first that `|T|=|S|=r` and the physical core `N[T,S]` is nonsingular.  Let `L_0=H_L^c`, `R_0=H_R^c` and define the light Schur cross block

`N_eff=N[L_0,R_0]-N[L_0,S] N[T,S]^(-1) N[T,R_0]`.               (6.1)

For every `I subset L_0`, `J subset R_0` with `|I|=|J|`, ordinary block determinant elimination gives

`det N[T union I,S union J]
 =det N[T,S] det N_eff[I,J]`.                                   (6.2)

Summing squares and using Cauchy--Binet gives the exact packet factorization

`boxed( W_(i,T,S)
 =gamma^(-2r) det(N[T,S])^2
   det(I+gamma^(-2)N_eff N_eff^T). )`                            (6.3)

Thus the surviving two-sided heavy obstruction is no longer a vague set of at most two rows and two columns.  On every balanced nonsingular pattern, the determinant currency splits multiplicatively into a <=2 by <=2 original-coordinate core and a regularized light residual.

The only genuinely new finite-core shapes left by this step are:

* imbalanced incidence `(1,2)` or `(2,1)`; or
* balanced incidence `(1,1)` or `(2,2)` with singular heavy core.

A positive packet in either case must use light coordinates to repair the row/column rank imbalance or the singular core.  These are finite bridge packets and are the next coordinate-minor target.

## 7. Exact checks

A pure exact-arithmetic check records two independent fixtures.

First take a diagonal regularized spectrum with

`y=(73/27,73/27,1/24)`,  `k=y/(1+y)=(73/100,73/100,1/25)`.

Then `sum k=3/2`, the first two coordinates are strictly heavier than 29/40, their avoidance probability is `729/10000<11/40`, and the corresponding diagonal joint row/column hit probability is `9271/10000>9/20`.

Second, for

`N=[[2,1,0],[1,3,2],[0,1,1]]`, `T=S={1}` (zero-based coordinate 0 in the checker),

the direct sum of squared minors with the fixed core pattern is exactly 54.  The Schur residual is

`[[5/2,2],[1,1]]`,

and the right side of (6.3) is also exactly 54.

The source constant calculation gives `beta r=1.008620689655...` and final coefficient `106.9279680849...<107`.

Terminal checker marker: `STATUS=QFORM_O1_TWOSIDED_HEAVY_PACKET_CHECK_PASS`.

## 8. Honest status and next implication

**Proved this run:**

1. `QFORM-O1-TWOSIDED-HEAVY-PACKET-v1`, equations (5.1)--(5.3).
2. Enlarged O1 pivot-ridge analytic payment (4.2) at leverage threshold 29/40.
3. Exact balanced-core factorization (6.3).

**Still open:** the full QFORM conjecture.  In particular, account02/B07's source-valid near-zero scalar-pivot family remains a real obstruction to paying O1 from `W_i` alone; the singular/hyperbolic packet is not removed by this theorem.  The first B07 implication to attack next is `QFORM-O1-FINITE-BRIDGE-PAYMENT-v1`: pay the imbalanced or singular <=2 by <=2 heavy-core packets under the original product law, preferably by the completed orientation-free rank-two affine half-Riesz theorem, while simultaneously retaining the near-zero inverse-free hyperbolic packet.  O2/O3 and the O0 finite core remain separate residuals.

Continuity is not claimed here; the new analytic branch establishes essential boundedness only.  No target-valid counterexample was found.
