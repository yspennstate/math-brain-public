SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B19, 2026-09-23T01:12:54Z.
attacking: the current N3 compiler's first rank-one-tube obstruction and the newest grouped O3 interface; force genuinely transverse third curvature, pay the normalized-diffuse grouped branch, and remove pair-atomic R3 clustering.

# fleet02/B19 r23 — universal proof assembly

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly / SYNTHESIS  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target remains open: for arbitrary independent real coordinates with densities `0<=f_i<=1` and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal essential-density bound for `X^TAX`, or give a valid counterexample. No moments, support bounds, log-concavity, diagonal-basis independence, or post-rotation independence are introduced. Continuity is tracked separately.

## 1. Source graph actually consumed

Fresh brain control at invocation start was revision `2026-09-22.15`, QFORM-only. The live correction boundary includes the failures of arbitrary-joint rank-three coarea, conditional-cap-as-independence, law-uniform scalar quadratic-phase decay, perturbative deletion of small coefficients under unrestricted supports, a universal rank-three physical cross cut, and the more recent failures of extracting a robust `sigma_1 sigma_2` merely from low-order symmetric sums or localizing the N3 mixed-hub residue to one square/pair certificate before aggregation.

The owner-required source package `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` was read at its three files `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, `COUNTEREXAMPLE_SEARCH.md`. In particular I use its proved Theorem F exactly, not a stronger surrogate.

The newest completed designated-partner mathematics found during the run is fleet03/B19 r21, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260922T235209Z-fleet03-B19-QFORM-r21/REPORT.md`. Its source-valid compiler fixes `tau=2^-20`, reduces N3 after a paid diffuse D' branch to three states R1--R3, and explicitly leaves all three open. An earlier completed partner result, fleet03/B19 r20, gives a separate grouped `2+1` exact-rank-three source block with determinant loss `delta>1/6`; Section 3 below pays its normalized-diffuse part by Theorem F.

I also use fleet03/B19 r16 `QFORM-EXACT-CROSS-RANK-L2-v1`: if a disjoint original-coordinate cross bank `C` has exact rank three, then

`||p_Q||_infinity <= 3 e Pi_3(C)^(-1/3)`,

and when one active bank consists of exactly three original coordinates this improves to

`||p_Q||_infinity <= 3 sqrt(e) Pi_3(C)^(-1/3)`.

All these source theorems retain arbitrary same-bank quadratic phases and outside conditioning at their stated scope.

## 2. One conditional end-to-end proof graph

A correction-safe proof graph is now:

1. **Full target -> fixed-threshold N3.** Claude's completed geometric synthesis reduces the unrestricted theorem to one fixed `N3(tau)` class by its physical-pivot and Gaussian-padding argument. It is enough to take `tau=2^-20` as in the current partner.
2. **N3 -> a physical cut.** fleet03/B19 r21 chooses a physical bipartition with cross block `B` satisfying `||B||_F^2>2/3`.
3. **Large third cross-volume, diffuse orientation -> paid.** If `E_3(B)>=2^-36` and either natural three-volume orientation has maximum marginal at most `2/3`, the weighted D' theorem gives `||p_Q||_infinity<1645`.
4. **Otherwise partner r21 leaves exactly:**
   - R1: `E_2<=2^-20`, hence a `1/590` Frobenius tube around a rank-one cross bank with `sigma>4/5` and one diffuse leading singular vector;
   - R2: `E_2>2^-20`, `E_3<2^-36`, hence a `1/147` Frobenius tube around rank at most two, with the tail retained;
   - R3: `E_3>=2^-36` but both three-volume orientations are concentrated, yielding a four-coloured anchored packet of total squared-minor mass at least `2^-36/12` and at least `44914` nonzero witnesses.
5. **New in this run:** R1 is sharpened to genuine order-one curvature transverse to the rank-one cross span (Section 4); R3 is paid whenever its nonanchor row-pair or column-pair distribution has an atom at least `1/4` (Section 5). The residual R3 is therefore pair-diffuse. R2 remains unchanged.

The first end-to-end unpaid state in this ordering is still R1, but its exact missing mechanism is now substantially narrower and quantified in Section 4.

## 3. Completed source application: grouped O3 diffuse payment

This section applies the owner-required Theorem F to a real partner obstruction.

Fleet03/B19 r20 proves that in its exactly-one-internal-rank-two O3 survivor there is a choice of one rank-one companion bank `H_a` and the rank-two internal bank `G` such that, with

`A=RMR^T`, `R^TR=I_3`, `D=|det M|>=1`,

and `S=H_a union G`,

`H:=sum_(i in S) u_i u_i^T = I-lambda_b v_bv_b^T`,

with

`delta:=det H=1-lambda_b>1/6`.

Thus `H` has eigenvalues `1,1,delta`. Put

`Z=R_S H^(-1/2)`, so `Z^TZ=I_3`,

and

`K=H^(1/2) M H^(1/2)`.

Then the actual physical principal block is

`A_SS=Z K Z^T`,

its three nonzero eigenvalues are those of `K`, and

`|det K|=D delta>1/6`.

Diagonalizing `K` rotates only the deterministic spectral columns. The leverage of original coordinate `i in S` in the eigenspace of the actual block is invariant and equals

`ell_i=u_i^T H^(-1)u_i=||z_i||^2`.

Hence if

`max_(i in S) ell_i<=1/2`,

Theorem F from the required `e5f71d...` source applies after conditioning all original coordinates outside `S`: here the residual `B` in Theorem F is zero, so its `I=S` block is certainly diagonal. Uniformly in the affine terms generated by conditioning,

`||p_Q||_infinity <=12 |det K|^(-1/3)`
`                    <12*6^(1/3)`
`                    =21.805447113986... <21.806.`

This is `QFORM-O3-ROBUST-2PLUS1-DIFFUSE-PAYMENT-v1`. It closes the normalized-diffuse part of partner r20's first unpaid grouped `2+1` implication without any post-rotation independence claim.

If this branch fails, some original coordinate in `S` has `ell_i>1/2`. Since `sum ell_i=3`, there are at most five such coordinates. Also Cauchy--Binet gives the exact complete principal-triple mass through any such row:

`mu_i=sum_(j<k; j,k in S\{i}) |det A[{i,j,k},{i,j,k}]|`
`    =D delta ell_i`
`    >1/12.`

No single physical minor is selected.

A further finite-core payment is immediate. Let `H_*={i:ell_i>1/2}`, `m=|H_*|<=5`, and

`G_*=sum_(i in H_*) z_i z_i^T`.

If `lambda_min(G_*)>=eta>0`, then the original-row Gram on `H_*` satisfies

`R_H*^T R_H*=H^(1/2) G_* H^(1/2)>=delta eta I_3`.

Therefore the actual `m x m` principal block on `H_*` has three eigenvalues of modulus at least `delta eta`, and Claude's bounded-dimensional projected-gradient theorem pays it by

`||p_Q||_infinity <=2 sqrt(6 pi m)/(delta eta)`.

For `eta=1/16`, `delta>1/6`, `m<=5`, this is `<1864`. Thus the only remaining grouped high-leverage state has

`lambda_min(G_*)<1/16`,

so some normalized spectral direction carries less than `1/16` of its mass on the at-most-five-row heavy core and more than `15/16` on the light bank.

## 4. New theorem for the first N3 gap R1: third curvature is genuinely transverse

Partner R1 supplies

`B=sigma u v^T+E`,
`||E||_F<1/590`,
`sigma>4/5`,

where `u,v` are unit vectors and at least one is diffuse. Let

`S_0=diag(A[L,L],A[R,R])`,
`K_0=[[0,sigma u v^T],[sigma v u^T,0]]`,
`R_0=[[0,E],[E^T,0]]`.

Let `W=span{(u,0),(0,v)}` and `P=P_W`. The matrix

`K_0+P S_0 P`

is supported on the two-dimensional space `W`, hence has rank at most two. Since the target has `s_3(A)>=1`, the Eckart--Young characterization of the third singular value gives

`1<=||A-(K_0+P S_0 P)||_op`
` <=||S_0-P S_0 P||_op+||R_0||_op`.

Now `||R_0||_op=||E||_op<=||E||_F<1/590`, so

`boxed: ||S_0-P S_0 P||_op>589/590.`

Because `S_0` is block diagonal and `P` is the direct sum of the projections onto `u` and `v`, this is exactly

`boxed: max{`
` ||A[L,L]-(u^T A[L,L]u)uu^T||_op,`
` ||A[R,R]-(v^T A[R,R]v)vv^T||_op`
`} >589/590.`

This improves the partner's earlier conclusion that merely one same-side block has large norm: the large curvature cannot live entirely along the already-used rank-one cross span.

On the side realizing the maximum, write its self block relative to the corresponding cross singular vector `q` as

`C=[[a,b^T],[b,C_perp]]` on `span{q} direct_sum q^perp`.

Then

`C-aqq^T=[[0,b^T],[b,C_perp]]`,

and

`||C-aqq^T||_op <=||b||+||C_perp||_op`.

Therefore every R1 survivor satisfies the quantitative first-gap dichotomy

`boxed: ||P_(q^perp) C q||>589/1180`

or

`boxed: ||P_(q^perp) C P_(q^perp)||_op>589/1180.`

Numerically `589/1180=0.49915254237...`. This is `QFORM-N3-R1-TRANSVERSE-CURVATURE-v1`.

The first unpaid implication is now not “find a third direction”: an order-one transverse same-side slope or compression is already forced. What remains is to combine this exact transverse resource with the diffuse rank-one cross channel while retaining the full nonzero cross tail `E` and arbitrary same-side curvature. The `1/590` tail may not be deleted perturbatively.

## 5. New target-level R3 payment: pair-atomic anchored packets

Partner R3 provides a retained four-coloured packet of physical `3x3` cross minors with total squared determinant mass

`Z_A>E_3/12>=2^-36/12`.

Every retained minor contains the same physical row anchor and column anchor. Normalize the retained squared masses to a probability law.

Suppose the two nonanchor row indices equal one fixed physical pair with probability at least `rho>0`. Let `I_0` be the fixed row triple consisting of the anchor and that pair. By Cauchy--Binet on the **complete** `3 x |R|` physical cross bank,

`det(B[I_0,:] B[I_0,:]^T)`
` =sum_(|T|=3) det(B[I_0,T])^2`
` >=rho Z_A`.

Therefore this cross bank has exact rank three and

`Pi_3(B[I_0,:])>=sqrt(rho Z_A)`.

Apply the completed exact-cross-rank theorem with one active bank consisting of exactly three original coordinates:

`||p_Q||_infinity`
` <=3 sqrt(e) Pi_3^(-1/3)`
` <=3 sqrt(e) (rho Z_A)^(-1/6).`

The same argument applies when a fixed **column** pair has mass at least `rho`, after transposition. At the useful threshold `rho=1/4`,

`||p_Q||_infinity`
` <3 sqrt(e) (2^-36/48)^(-1/6)`
` =603.469524004344... <604.`

This proves `QFORM-N3-R3-PAIRATOM-PAYMENT-v1`.

Consequently every still-unpaid R3 state satisfies simultaneously:

- every nonanchor row-pair atom is `<1/4`;
- every nonanchor column-pair atom is `<1/4`;
- the total anchored packet mass is still at least `2^-36/12`;
- the original N3 entry and no-pivot bounds remain in force.

This removes the strongest clustered endpoint without selecting one physical `3x3` minor. The residual R3 is pair-diffuse but may still be one-vertex-heavy, which is the natural interface for the mixed-order minor theorem.

## 6. Exact first unpaid implication

After the current partner compiler and this run, the first end-to-end missing implication can be stated with exact quantifiers as follows.

`QFORM-N3-R1-TRANSVERSE-ABSORPTION-v1`:

> Fix `tau=2^-20`. There exists a universal finite `C` such that for every dimension, every symmetric target matrix `A` in `N3(tau)`, and every physical cut `L|R` supplied by fleet03/B19 r21 whose cross block admits
> 
> `A[L,R]=sigma u v^T+E`, `sigma>4/5`, `||E||_F<1/590`,
> 
> with one of `u,v` satisfying squared `l_infinity` norm `<1/296`, if on at least one side the corresponding self block `C` satisfies either
> 
> `||P_(q^perp)Cq||>589/1180`
> 
> or
> 
> `||P_(q^perp)CP_(q^perp)||_op>589/1180`,
> 
> then `X^TAX` has density cap at most `C` for every independent cap-one product input law, with the entire cross tail `E`, both self blocks, all signs and all extra spectrum retained.

The theorem in Section 4 proves that **every** partner-R1 state satisfies the premise, so paying this implication closes R1. R2 and the pair-diffuse remainder of R3 would still remain; hence no full-proof claim is made.

## 7. Verification

`VERIFY.py` checks the numerical constants and a deterministic regression of the grouped normalization `Z^TZ=I`, `R_S^TR_S=H`, and `|det(H^(1/2) M H^(1/2))|=delta |det M|`. The saved output is

`grouped_diffuse_constant=21.805447113986`
`r3_pairatom_constant=603.469524004344`
`heavy_core_eta_1_16_constant=1863.960876053471`
`r1_transverse=0.998305084746`
`r1_half_transverse=0.499152542373`
`QFORM_B19_R23_CHECK_PASS`.

The numerical regression is only a check; the proofs above are exact.

## 8. Status ledger

- Full unrestricted QFORM: **OPEN**.
- Fixed-threshold N3: **OPEN**.
- Current partner R1: structurally sharpened by `QFORM-N3-R1-TRANSVERSE-CURVATURE-v1`; analytic absorption still open.
- Current partner R2: open.
- Current partner R3: pair-atomic subbranch paid `<604`; pair-diffuse residual open.
- Partner r20 grouped `2+1`: normalized-diffuse subbranch paid `<21.806`; a quantitatively spanning at-most-five-row heavy core is paid `<1864` at `lambda_min>=1/16`; light-direction hybrid remains.
- No target-valid counterexample found.
- Independent end-to-end full-proof reviews: zero.
