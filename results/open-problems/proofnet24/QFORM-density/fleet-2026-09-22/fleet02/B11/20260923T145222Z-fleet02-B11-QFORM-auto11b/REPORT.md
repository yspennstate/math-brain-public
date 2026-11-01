SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B11, 2026-09-23T14:52:22Z.
attacking: the approximate-null-ruling two-sheet survivor; build an actual original-coordinate cross cut while quarantining high-leverage rows on the unconstrained side.

# fleet02/B11 — asymmetric null-ruling cross-cut compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`  
**Continuity:** separate from the full target; the Fourier branches below actually give continuous densities at their stated scopes.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted QFORM conjecture remains OPEN / NOT PROVED / NOT DISPROVED.

## 1. First unpaid implication

The preceding B11 run left

`QFORM-NULL-RULING-TO-PRODUCT-CUT-v1`:

> In the exact-rank-three two-plane indefinite chamber, convert quantitative L2 proximity to the two null rulings on each spectral plane into an ACTUAL original-coordinate receiver, without replacing the random quadratic form by its projected-row approximation.

This run closes the diffuse part of that implication even when some original coordinates have arbitrarily large spectral leverage. The high-leverage coordinates are all put on the unconstrained side of Claude's decoupling theorem. Failure of the diffuse part is reduced to a finite heavy-spike null-ruling branch.

The early `CHECKPOINT.md` imposed a global tiny-leverage condition. That condition is sufficient but redundant with the already-paid Fresnel--Brascamp--Lieb Theorem F, so `CHECKPOINT_CORRECTION.md` explicitly withdraws it as a progress claim and replaces it by the asymmetric statement proved below.

## 2. Sources actually used

1. Required Claude package: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md` and `COUNTEREXAMPLE_SEARCH.md`.
   - Theorem D is applied below to the actual cross block at equation (5.5).
   - Theorem C is applied at equation (7.1) only on the ruled one-sheet half-line.
2. Predecessor fleet02/B11: `math-open-problems@8ae1a16002c77879645875d1e3b9a9d136365289`, same slot, run `20260923T141910Z-fleet02-B11-QFORM-auto11`. Its `QFORM-NULL-RULING-L1-TO-L2-v1` supplies the quantitative projected clusters used here.
3. Designated partner fleet03/B11 r32: `math-open-problems@28b5041d7a1147a167c4366e51e161ac34a9a8f7`, run `20260923T131406Z-fleet03-B11-QFORM-r32`. Its grouped four-ray compiler and its small-pivot obstruction are applied in Section 8.
4. Full-matrix cross-volume stability: `math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`. Its independent review is still pending; the corollary in Section 6 inherits that status.

No spectral projection is declared independent. Every cut below is a subset of original product coordinates.

## 3. Two-plane geometry and the predecessor null-ruling lemma

Write

`A=R M R^T`, `R^T R=I_3`, `s=min |eig(M)|>0`,

and use the two-plane decomposition

`R_S^T R_S=diag(1,rho,0)`,
`R_T^T R_T=diag(0,1-rho,1)`,
`0<rho<1`, `m_22=0`.                                                   (3.1)

Put `tau=min(rho,1-rho)`.

For S rows `(x_i,y_i,0)`,

`A_ii=x_i(m_11 x_i+2m_12 y_i)`,
`kappa_S=sqrt(m_11^2+4m_12^2)`,

and for T rows `(0,u_j,v_j)`,

`A_jj=v_j(2m_23 u_j+m_33 v_j)`,
`kappa_T=sqrt(4m_23^2+m_33^2)`.                                      (3.2)

Let

`D_S=sum_(i in S)|A_ii|`, `D_T=sum_(j in T)|A_jj|`,
`eps_S^2=D_S/kappa_S`, `eps_T^2=D_T/kappa_T`,
`eta_S=2sqrt(2)eps_S+eps_S^2`,
`eta_T=2sqrt(2)eps_T+eps_T^2`.                                       (3.3)

The predecessor theorem projects each original row to its nearest one of the two null lines in its physical plane. Denote the projected row by `r_i^*`. If `eta_S<=rho/2`, then the two projected S-line squared masses are each at least `rho/12` and their angle satisfies

`sin^2(theta_S)>=rho/9`.                                               (3.4)

If `eta_T<=(1-rho)/2`, the two projected T-line masses are each at least `(1-rho)/12` and

`sin^2(theta_T)>=(1-rho)/9`.                                          (3.5)

Moreover, on every subset of S or T the actual/projected Gram error is bounded by `eta_S` or `eta_T`, respectively. These statements are deterministic consequences of

`sum dist(r_i, null lines)^2 <= D_S/kappa_S + D_T/kappa_T`; no random perturbation is introduced.

## 4. New structural theorem

### Theorem 4.1 — `QFORM-NULL-RULING-LIGHT-CROSSCUT-v1`

Assume

`eta_S+eta_T <= tau^3/9216`.                                           (4.1)

Set

`gamma=tau^3/9216`, `h0=gamma/2=tau^3/18432`.                         (4.2)

Classify each original coordinate by which nearest projected null line it belongs to. Thus there are four clusters: two S-line clusters and two T-line clusters. In an S cluster call its bank parameter `b=rho`; in a T cluster put `b=1-rho`.

Assume that in each of the four clusters the projected squared mass carried by rows satisfying the ACTUAL spectral-leverage bound

`||r_i||^2 <= h0`                                                     (4.3)

is at least `b/48`.

Then there exist disjoint original-coordinate sets `I,J`, partitioning all coordinates, such that

`G_I=R_I^T R_I >= gamma I_3`,
`G_J=R_J^T R_J >= gamma I_3`,                                         (4.4)

and every row on the constrained side I satisfies

`r_i^T G_I^{-1} r_i <=1/2`.                                           (4.5)

Consequently, for arbitrary independent cap-one input densities,

`boxed: ||p_(X^T A X)||_infinity <= 55296 sqrt(e)/(s tau^3).`         (4.6)

This theorem allows arbitrarily high-leverage rows in J; hence it is not contained in the global-leverage hypothesis of Theorem F.

### Proof

For each of the four clusters use only rows satisfying (4.3). Greedily add such rows to I until their projected squared mass first reaches `b/96`. Every projected row norm is at most its actual row norm, so each added weight is at most `h0`. Since

`h0=tau^3/18432 <= b/96`,                                             (4.7)

the selected I-mass from that cluster lies in

`[b/96,b/48]`.                                                        (4.8)

Put every unselected coordinate, including every heavy coordinate, in J. By (3.4)-(3.5), the full projected cluster mass is at least `b/12`; therefore J retains at least

`b/12-b/48=b/16`                                                      (4.9)

on every null line.

Consider first the projected S-plane Gram on I. Its two line masses are at least `rho/96`, its line angle satisfies (3.4), and its trace is at most `rho/24` by (4.8). For two unit line vectors `u,v` with masses `a,b`,

`det(a uu^T+b vv^T)=ab sin^2(theta)`.

Thus

`det G_(I,S)^* >= (rho/96)^2 (rho/9)=rho^3/82944`,

and because `lambda_max<=trace<=rho/24`,

`lambda_min(G_(I,S)^*) >= rho^2/3456`.                                (4.10)

The reflected T estimate is

`lambda_min(G_(I,T)^*) >= (1-rho)^2/3456`.                            (4.11)

Since the S plane is `span(e1,e2)` and the T plane is `span(e2,e3)`, (4.10)-(4.11) imply

`G_I^* >= (tau^2/3456) I_3`.                                         (4.12)

For J, use the retained line masses `rho/16` and `(1-rho)/16`. The total projected trace in either physical plane is at most two, hence

`lambda_min(G_(J,S)^*) >= rho^3/4608`,
`lambda_min(G_(J,T)^*) >= (1-rho)^3/4608`,

so

`G_J^* >= (tau^3/4608) I_3`.                                         (4.13)

For either cut, the actual/projected Gram discrepancy is at most `eta_S+eta_T`. Since `tau<=1`, (4.12) is stronger than `tau^3/4608`, and (4.1), (4.12)-(4.13) yield exactly

`G_I,G_J >= [tau^3/4608-tau^3/9216]I_3=gamma I_3`.                   (4.14)

Every I row was selected from the light set, so

`r_i^T G_I^{-1}r_i <= ||r_i||^2/gamma <= h0/gamma=1/2`,              (4.15)

proving the structural statement.

## 5. Apply the required Claude theorem to the ACTUAL cross block

Let

`C=A[I,J]=R_I M R_J^T`.                                               (5.1)

Because (4.14) makes both restricted Grams positive definite, C has rank three. Put

`U=R_I G_I^{-1/2}`, `V=R_J G_J^{-1/2}`.

Then U and V have orthonormal columns and

`C=U B V^T`, `B=G_I^(1/2) M G_J^(1/2)`.                              (5.2)

Therefore the product of the three nonzero squared singular values of C is

`Z=e_3(C^T C)=det(B)^2=det(M)^2 det(G_I)det(G_J)`.                    (5.3)

Since `|det M|>=s^3` and both Gram determinants are at least `gamma^3`,

`Z>=s^6 gamma^6`.                                                     (5.4)

For rank-three C the squared-minor volume-sampling row marginal equals the ordinary column-space leverage:

`alpha_i=(P_range(C))_ii=r_i^T G_I^{-1}r_i`.

Indeed the squared 3-by-3 minors factor as `det(U_S)^2 det(B)^2 det(V_T)^2`, and Cauchy--Binet gives the determinantal marginal. Hence (4.15) is exactly Claude Theorem D's required `alpha_i<=1/2` gate.

Applying that completed theorem at `e5f71d79...` gives

`||p_Q||_infinity <=6 sqrt(e) Z^(-1/6)
                   <=6 sqrt(e)/(s gamma)
                   =55296 sqrt(e)/(s tau^3)`.                         (5.5)

Equation (5.5) is the required real application of the pinned source result. The theorem acts on the actual original-coordinate cross block (5.1); the projected rows were used only to construct the coordinate partition.

## 6. Full-matrix cross-tail stability corollary

The same cut survives a genuinely nonseparable additional spectrum when its contribution is small only on this cross block, with no random-variable perturbation argument.

Let

`A_full=R M R^T+H`, `E=H[I,J]`.                                       (6.1)

From (5.2),

`s_3(C)>=sqrt(lambda_min G_I) s sqrt(lambda_min G_J)>=s gamma`.       (6.2)

Also `max diag(P_range(C))<=1/2` by (4.15). Therefore, if

`||E||_op <= s gamma/16`,                                             (6.3)

the completed volume-stability theorem at `c2414ef6...` applies to the actual cross block `C+E` and yields

`boxed: ||p_(X^T A_full X)||_infinity < 23/(s gamma)
       =211968/(s tau^3).`                                            (6.4)

All same-side curvature, outside couplings and affine terms are arbitrary. The source proof is marked independent-review pending, so (6.4) inherits that review status. This does not handle a general large cross-tail.

## 7. Sign-specific ruled splice and the rank-two logarithm

For signature `(+, +, -)`, Claude's ruled Theorem C applies after dividing by s and gives

`boxed: p_Q(t)<=pi sqrt(2)/s,  t>=0.`                                 (7.1)

For signature `(+, -, -)`, reflection gives the analogous estimate on the negative majority-sign half-line. No X-ray-only inference is made on the opposite two-sheet side; that side is paid globally by (5.5) in the present chamber.

The opposite-sign rank-two failure is retained exactly. If independent `X,Y` are uniform on `[-1/2,1/2]`, then

`p_(2XY)(t)=log(1/(2|t|)),  0<|t|<1/2`.                              (7.2)

Thus two indefinite directions sit at the nonintegrable Fourier endpoint. In the present genuinely rotated branch, the third direction is recovered as the third singular direction of the ACTUAL source-coordinate cross block: (5.3)-(5.4) give three-volume, and Theorem D produces `|phi_Q(t)|=O(|t|^(-3/2))`, which is integrable. Dropping one cross direction would leave the `|t|^(-1)` endpoint consistent with (7.2). This is how the third direction removes the logarithm here; no post-rotation convolution is invoked.

## 8. Designated partner applied and why the new hypothesis is not cosmetic

Partner fleet03/B11 r32 proves for its exact grouped four-ray Parseval family

`||p_Q||_infinity <= (6*2^(4/3)/s) max(rho,1-rho)^(-1/3)
                   <= 6*2^(5/3)/s <19.049/s`.                         (8.1)

That family also proves the correction that tiny rowwise physical-pivot certificates do NOT force a rowwise or bank-L2 near-null split. In the symmetric stress instance the preceding B11 calculation gives

`D_S/kappa_S=1`, `D_T/kappa_T=1/sqrt(2)`,                             (8.2)

so (4.1) correctly fails even while the old local certificates tend to zero. I use (8.1) as the completed bound on that complementary exact four-ray obstruction, and (8.2) as a real obstruction to weakening (4.1) to a maximum-local-pivot assumption. The partner result is therefore applied, not merely cited.

## 9. Failure of the cross-cut compiler is a finite heavy-spike branch

Let

`H={i: ||r_i||^2>h0}`.                                                (9.1)

Since `sum_i||r_i||^2=tr(R^TR)=3`,

`|H| < 3/h0 =55296/tau^3`.                                           (9.2)

If the light-mass hypothesis of Theorem 4.1 fails in a cluster with bank parameter b, the total projected cluster mass is at least `b/12` but its light projected mass is below `b/48`. Therefore H carries projected mass more than

`b/12-b/48=b/16>=tau/16`                                             (9.3)

on that specific null-ruling cluster.

So the unpaid remainder is no longer a diffuse provenance problem. It is a **bounded-cardinality heavy-spike near-null branch** carrying macroscopic null-line mass. Scalar/pair completion pays any spike whose physical pivot or pair certificate is quantitative; what remains is the finite-spike interpolation when those pivots are genuinely near zero. This is the new first unpaid implication:

`QFORM-NULL-RULING-FINITE-SPIKE-INTERPOLATION-v1`.

One must either combine the finitely many heavy original coordinates with the residual diffuse banks through a product-preserving hub/pair receiver, or force an already-paid scalar/pair/disjoint-volume exit. Small nonzero pivots may not be replaced by exact zero, and arbitrary additional spectrum is only covered when the actual cross-tail satisfies (6.3).

## 10. Nonredundancy example

The theorem genuinely extends beyond the global low-leverage branch. At `rho=1/2`, take

`M0=[[0,1,1],[1,0,1],[1,1,0]]`, `spec(M0)={2,-1,-1}`.                (10.1)

Its S and T null lines are the coordinate axes in the two physical planes. Put one S/e1 physical row with squared leverage `0.6`, distribute the remaining S/e1 mass `0.4` among sufficiently many light original rows, and distribute the S/e2 mass `1/2`, T/e2 mass `1/2` and T/e3 mass `1` among sufficiently many light rows. Then `R^TR=I_3`, the projection error is zero, and every cluster has far more than the required light mass, while

`max_i ||r_i||^2=0.6>1/2`.                                           (10.2)

Thus the all-coordinate Theorem F leverage gate fails, but Theorem 4.1 applies by placing the heavy row in J. Negating M0 gives the opposite indefinite signature.

This is a covered target family, not a counterexample.

## 11. Scope

The full QFORM target remains open. This run closes the approximate-null-ruling branch only when every null-line cluster retains quantitative light source mass, and gives the small-cross-tail full-matrix extension (6.4). The remaining B11 debt is the finite-heavy-spike near-null interpolation plus the interface to arbitrary nonseparable spectrum with no small cross-tail certificate.

No moments, support bounds, log-concavity, identical laws, diagonal-basis assumption, post-rotation independence, FEI work, installation, benchmark, task mutation, notification/email, paid call, cross-account authentication, permission change, public release, or unrelated data are used.
