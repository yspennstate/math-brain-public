SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B08, 2026-09-23T01:41:46.365492Z.
attacking: a mixed exterior-power conservation law across a balanced physical cut, to quantify the genuine one-/two-direction hybrid without deleting arbitrary spectral remainder.

# fleet01/B08 r22 — mixed compound conservation across a physical cut

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** diffuse eigenvector case  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_STRUCTURAL_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The full owner target remains open. Throughout, `A` is an arbitrary real symmetric `n x n` matrix and the original coordinates are independent with densities bounded by one. No moment, compact-support, Gaussian, log-concavity, connected-support, iid, or post-rotation independence assumption is used. The main theorem below is purely deterministic matrix algebra and therefore survives arbitrary input laws and arbitrary spectral remainder. A continuous-density conclusion is claimed only in the explicit cross-ridge corollary, where a completed Fourier theorem supplies it.

## 1. First unpaid implication attacked

The fresh designated partner `fleet02/B08` proves that for three genuinely diffuse full-matrix eigenvectors, a balanced **original-coordinate** cut has an exact hybrid ledger: if one physical child retains `k=0,1,2` substantial actual eigenvalues, then the true physical cross block carries respectively `3,2,1` substantial singular directions. The partner also gives a Hadamard family showing the `k=1,2` hybrid is real and cannot be removed by stronger selected-frame delocalization.

The missing compiler is therefore not another dichotomy claiming that either the child or the cross block alone has all three directions. The right object should retain **mixed exterior grades**: three child directions, two child plus one cross, one child plus two cross, or three cross directions.

This run proves exactly such a conservation law, directly from the restricted eigen-equation. It is an identity/inequality on the actual principal child and actual cross block; no component of `A` is discarded.

## 2. Setup and notation

Let `R in R^(n x 3)` have orthonormal columns and consist of three genuine eigenvectors of the full matrix:

`A R = R Lambda`, `R^T R = I_3`, `min_j |lambda_j| >= L`.

No assumption is made on the rest of the spectrum of `A`.

Take an original-coordinate partition `I sqcup J=[n]` and define

`G_I=R_I^T R_I`, `G_J=R_J^T R_J=I_3-G_I`.

Assume the cut is balanced at level `alpha in (0,1/2]`:

`alpha I_3 <= G_I,G_J <= (1-alpha) I_3`.

Set

`rho = sqrt(alpha/(1-alpha))`.

Whiten the selected frame on the two physical sides:

`U_I=R_I G_I^(-1/2)`, `U_J=R_J G_J^(-1/2)`.

Then `U_I,U_J` have orthonormal columns. Let

`A_I=A[I,I]`, `B=A[I,J]`,

and define their selected three-dimensional compressions

`C=U_I^T A_I U_I`, `H=U_I^T B U_J`.

For any matrix `M`, let

`D_1(M)=||M||_F`,
`D_2(M)=||wedge^2 M||_HS`,
`D_3(M)=||wedge^3 M||_HS`.

For a `3 x 3` matrix these are

`D_1(M)=||M||_F`, `D_2(M)=||cof M||_F`, `D_3(M)=|det M|`.

For a real symmetric physical child,

`D_k(A_I)=sqrt(e_k(A_I^2))`,

and for the rectangular cross block

`D_k(B)=sqrt(e_k(B B^T))`.

## 3. Exact restricted-eigenvector identity

Restrict `A R=R Lambda` to the rows in `I`:

`A_I R_I + B R_J = R_I Lambda`.

Using `R_I=U_I G_I^(1/2)` and `R_J=U_J G_J^(1/2)`, then left multiplying by `U_I^T`, gives

`C G_I^(1/2) + H G_J^(1/2) = G_I^(1/2) Lambda`.       (3.1)

Right multiply by `G_I^(-1/2)` and put

`T=G_J^(1/2) G_I^(-1/2)`.

Then

`C + H T = G_I^(1/2) Lambda G_I^(-1/2)`.              (3.2)

Taking determinants yields the exact invariant identity

`det(C+HT)=det Lambda`.                                 (3.3)

In particular,

`|det(C+HT)| >= L^3`.                                   (3.4)

The balancing bounds give

`||T||_op <= sqrt((1-alpha)/alpha)=rho^(-1)`.           (3.5)

This is the key step: the selected large spectral volume appears as the determinant of **child compression + true cross compression times an explicitly controlled transfer matrix**.

## 4. The mixed compound conservation theorem

### Theorem 4.1 — `QFORM-DIFFUSE-MIXED-COMPOUND-CONSERVATION-v1`

Under the setup above,

`L^3 <= D_3(A_I)
       + rho^(-1) D_2(A_I) D_1(B)
       + rho^(-2) D_1(A_I) D_2(B)
       + rho^(-3) D_3(B)`.                              (4.1)

Equivalently, at least one of the following four actual physical certificates holds:

1. `D_3(A_I) >= L^3/4`;
2. `D_2(A_I) D_1(B) >= rho L^3/4`;
3. `D_1(A_I) D_2(B) >= rho^2 L^3/4`;
4. `D_3(B) >= rho^3 L^3/4`.

The same statement holds with `I,J` interchanged.

### Proof

For arbitrary `3 x 3` matrices `M,N`, column multilinearity of determinant gives the exact grade decomposition

`det(M+N)
 = det M + <cof M,N>_F + <M,cof N>_F + det N`.          (4.2)

The four terms correspond respectively to choosing `0,1,2,3` columns from `N`. Therefore Cauchy--Schwarz gives

`|det(M+N)|
 <= D_3(M)+D_2(M)D_1(N)+D_1(M)D_2(N)+D_3(N)`.           (4.3)

Apply (4.3) with `M=C`, `N=HT`. From (3.5) and functoriality of exterior powers,

`D_1(HT) <= rho^(-1) D_1(H)`,
`D_2(HT) <= rho^(-2) D_2(H)`,
`D_3(HT) <= rho^(-3) D_3(H)`.                           (4.4)

Because `U_I,U_J` are isometries, exterior-power compression is Hilbert--Schmidt contractive:

`wedge^k C=(wedge^k U_I)^T (wedge^k A_I)(wedge^k U_I)`,

`wedge^k H=(wedge^k U_I)^T (wedge^k B)(wedge^k U_J)`.

Hence for `k=1,2,3`,

`D_k(C)<=D_k(A_I)`, `D_k(H)<=D_k(B)`.                   (4.5)

Combine (3.4), (4.3), (4.4), and (4.5) to obtain (4.1). If all four displayed physical terms were strictly below the listed quarter thresholds, their weighted sum would be below `L^3`, contradiction. QED.

### Scope guard

This theorem does **not** by itself prove a density bound. In particular, `D_2(A_I)D_1(B)` is an aggregate two-child/one-cross certificate and `D_1(A_I)D_2(B)` is an aggregate one-child/two-cross certificate; a product-preserving analytic receiver for those mixed grades is still needed. The theorem does, however, show that the hybrid is controlled by an exact conservation law rather than by a qualitative case split.

## 5. Explicit diffuse constants at leverage 1/48

The completed diffuse physical partition used by the designated partner gives, under selected-frame row leverage

`mu=max_i ||R_{i,*}||^2 <=1/48`,

a cut with

`G_I,G_J >= (3/8) I_3`.

Thus we may take

`alpha=3/8`, `rho=sqrt(3/5)`.

Theorem 4.1 yields the completely explicit four-way ledger

`D_3(A_I) >= (1/4)L^3`, or

`D_2(A_I)D_1(B) >= [sqrt(3/5)/4] L^3
                  =0.1936491673103708... L^3`, or

`D_1(A_I)D_2(B) >= (3/20)L^3
                  =0.15 L^3`, or

`D_3(B) >= [(3/5)^(3/2)/4] L^3
          =0.1161895003862225... L^3`.                  (5.1)

These constants are independent of `n`, the unselected spectrum, signs, moments, and input laws.

## 6. Designated partner applied to actual mixed inequalities

The designated completed partner is `fleet02/B08` r18, `QFORM-DIFFUSE-ACTUAL-SPECTRAL-GATE-v1`, canonical source

`yspennstate/math-open-problems@9fb59f9549a85af6173ade505fd53bc035c611ba`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/20260923T004036Z-fleet02-B08-qform-diffuse-r18/REPORT.md`.

At the same `mu<=1/48` cut set

`c=(L/2)sqrt(3/5)`,
`beta=(3/16)sqrt(3/5)L`.

Let `k_I` be the number, capped at three, of actual eigenvalues of the physical child `A_I` with modulus at least `c`. The partner proves

`k_I<3 => s_(3-k_I)(B)>beta`.                            (6.1)

This gives an actual inequality in every hybrid state:

- `k_I=3`: `D_3(A_I)>=c^3`;
- `k_I=2`: `D_2(A_I)>=c^2` and `D_1(B)>beta`, hence
  `D_2(A_I)D_1(B)>c^2 beta`;
- `k_I=1`: `D_1(A_I)>=c` and `s_2(B)>beta`; since `s_1>=s_2`,
  `D_2(B)>=s_1s_2>beta^2`, hence
  `D_1(A_I)D_2(B)>c beta^2`;
- `k_I=0`: `s_3(B)>beta`, hence
  `D_3(B)>=s_1s_2s_3>beta^3`.

At `L=1`,

`c=0.3872983346207417...`,
`beta=0.1452368754827781...`,

and the four corresponding certified grades are respectively

`c^3                 =0.0580947501931113...`,
`c^2 beta            =0.0217855313224167...`,
`c beta^2            =0.00816957424590627...`,
`beta^3              =0.00306359034221485...`.           (6.2)

Thus the partner's actual spectral gate is converted into the same four exterior grades appearing naturally in Theorem 4.1. This is the promised partner application; it is not merely a citation.

## 7. A paid continuous-density endpoint from the cross grade

The new fleet03/B08 r25 theorem `QFORM-CROSS-E3-RIDGE-v1` states: for an original-coordinate cross block `B`, if one side of `range(B)` has coordinate leverage at most `q/2`, `1<=q<3/2`, and

`Delta_3=e_3(BB^T)=D_3(B)^2`,

then the full quadratic form has a continuous `C_0` density and

`||p_Q||_inf
 <= [e/(6 sqrt(2q))]
    Beta(1/6,1/(4q)-1/6)
    Delta_3^(-1/6)`.                                     (7.1)

Apply this with `q=1` to the **fourth branch of Theorem 4.1**. There

`D_3(B)>=rho^3 L^3/4`,

so

`Delta_3>=rho^6 L^6/16`.

If one-side cross-range leverage is at most `1/2`, then

`||p_Q||_inf
 <= [e/(6 sqrt2)] Beta(1/6,1/12)
    16^(1/6) rho^(-1) L^(-1)`

` =11.5905034452964... / L`.                              (7.2)

This is a genuine end-to-end density estimate for one branch of the new conservation law, retaining arbitrary same-side blocks and arbitrary additional spectrum. Continuity follows from the cited cross-E3 ridge theorem.

For comparison, applying the same receiver directly to the designated partner's `k_I=0` estimate `D_3(B)>beta^3` gives, under the same range-leverage gate,

`||p_Q||_inf <38.9416513856214... / L`.                   (7.3)

So Theorem 4.1 materially strengthens the all-cross endpoint whenever its pure cross grade wins.

## 8. What remains unpaid

The first missing implication is now more precise:

`QFORM-MIXED-COMPOUND-RECEIVER-v1`.

Prove a product-preserving analytic receiver for either

`D_2(A_I)D_1(B) >= c_1 L^3`

or

`D_1(A_I)D_2(B) >= c_2 L^3`,

with universal fixed positive `c_1,c_2`, while allowing arbitrary remaining same-side curvature, arbitrary extra cross rank, arbitrary spectral signs, and only original-coordinate independence. The scalar contractions in the exact determinant expansion (4.2), before Cauchy--Schwarz, encode the required transversality and should be kept in the next attempt; replacing them by one selected minor risks the already-recorded aggregation losses.

A second route is a multiscale recursion on the `D_3(A_I)` branch. A naive recursive use loses a fixed spectral scale at each generation and is not yet dimension-free. Any recursion therefore needs to charge the lost determinant volume to mixed/cross grades before descending.

The full QFORM conjecture and global continuity statement remain OPEN.

## 9. Checks

The adjacent `CHECKS.py` verifies the exact 3x3 determinant grade identity on deterministic test matrices and verifies all constants in Sections 5--7. `CHECKS.txt` records the passing output.
