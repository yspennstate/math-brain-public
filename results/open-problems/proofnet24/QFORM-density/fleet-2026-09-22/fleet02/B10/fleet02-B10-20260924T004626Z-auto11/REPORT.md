SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B10, 2026-09-24T00:46:26Z.
attacking: the exact-rank-three hybrid/near-null physical direction, specifically the remaining bidirectional mixed-bank contamination while preserving original-coordinate product provenance after projection.

# fleet02/B10 auto11 — regression-clean endpoint receiver and a diffuse harmonic survivor

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: rank-three coupled case / complementary constructions and source-valid counterexamples  
Status: `NEW SUPPORTING THEOREM + NEW STRUCTURAL OBSTRUCTION / FULL EXACT-RANK3 OPEN / FULL QFORM OPEN`.


The live correction boundary is retained throughout: no independence after spectral rotation, no arbitrary-joint coarea cap, no worst conditional-density supremum, no law-uniform pointwise quadratic-phase decay, no moment/support/log-concavity assumption, and no deletion of a small random quadratic term on rough unbounded laws.

## 1. Sources actually consumed

Required pinned source:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

I use its completed ruled-level-set Theorem C below at an actual density inequality; I do not reprove it. Its exact statement gives, for signature `(2,1)` and the majority-sign side,

`p_Q(s) <= pi sqrt(2)` when all three nonzero eigenvalue magnitudes are at least one.

The current designated partner input is fleet03/B10 commit

`70f02a787a432edc745fa632b80ecfff0cc2ef11`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/20260923T221626Z-fleet03-B10-QFORM-r25/REPORT.md`.

I use three proved facts from that report: in the near-coloop collar the physical leaves have

`sum t_i^2=rho`, `sum t_i p_i=0`, `sum p_i p_i^T=I_2`, `rho<1/64`,

with unpaid transverse row leverages `<1/61`; the nonzero-hub discriminant loses all longitudinal leakage exactly; and its legal conditioning contraction can leave transverse Gram `lambda_min>=2/81` while removing a fixed fraction of longitudinal energy. The partner explicitly leaves the null endpoint with same-bank contamination open.

Finally I audited the real-variable single-hub receiver at the current source

`proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/single_hub_core/REPORT.md`

(blob `31ed40e83dffd5988f54883da317dedebac340a5`). Its Theorem 3.2 proof only uses a maximal slice quantity after the hub is retained jointly with one square. I reproduce the exact part needed below, so no extension is taken on faith.

## 2. Exact-null partner normal form

At the true null endpoint of the adapted hub Rayleigh coefficient, rotate only the deterministic transverse spectral basis so that the cross vector is `(r,0)`. This does **not** rotate the random source coordinates. The exact-rank-three form is

`M = [[0,r,0],[r,a,b],[0,b,d]]`,

and, with one ORIGINAL physical hub `H` and ORIGINAL leaf coefficient vectors `t,y,w`,

`Q = 2 r (sqrt(c) H + T) Y + a Y^2 + 2 b Y W + d W^2`,                 (2.1)

where

`T=sum_i t_i X_i`, `Y=sum_i y_i X_i`, `W=sum_i w_i X_i`,

`sum t_i^2=rho=1-c`, `t perpendicular y,w`, `||y||_2=||w||_2=1`, `y perpendicular w`, and `c>63/64`.

Because `sigma_min(M)>=1`,

`|r|>=1`.                                                            (2.2)

Also `|d|>=1`: for `x=(-b/r,0,1)`, `M x=(0,0,d)`, hence `|d|=||Mx||>=||x||>=1`. This elementary observation is useful because the receiver below pays only `r,d`, never `rho`.

## 3. New theorem: an exact regression-clean transverse reservoir pays bidirectional leakage

### Theorem 3.1 — `QFORM-REGRESSION-CLEAN-RESERVOIR-ENDPOINT-v1`

Assume (2.1). Suppose there are real numbers `gamma,eta` and a set `I` of ORIGINAL leaf indices such that

`t_i = gamma y_i + eta w_i` for every `i in I`,                        (3.1)

and the transverse Gram on those same physical indices,

`G_I = sum_(i in I) (y_i,w_i)^T (y_i,w_i)`,

has

`delta := det G_I > 0`.                                               (3.2)

Then for arbitrary independent input densities bounded by one,

`||p_Q||_infinity
 <= 1/(2 |r| sqrt(c))
    + 16 delta^(-1/2) (|r| sqrt(c))^(-1/2) |d|^(-1/2)`                (3.3)

and therefore, using (2.2),

`boxed: ||p_Q||_infinity <= 1/(2 sqrt(c)) + 16 delta^(-1/2)c^(-1/4).` (3.4)

No moment, support, regularity, post-rotation independence, or separation between `T,Y,W` is assumed.

### Proof

Put

`q = t - gamma y - eta w`, `Z=sum_i q_i X_i`.

By (3.1), `q_i=0` on `I`; hence `Z` is a function only of the disjoint ORIGINAL coordinates `I^c`. The identity

`T = gamma Y + eta W + Z`

turns (2.1) into

`Q = 2 r sqrt(c) H Y + 2r ZY + a'Y^2 + 2b'YW + dW^2`,                (3.5)

where `a'=a+2r gamma` and `b'=b+r eta`. This is an exact algebraic shear; no random coordinate is split into independent pieces.

Condition on all ORIGINAL variables in `I^c`. The remaining random pair `(Y_I,W_I)` is the linear image of the product law on `I` with coefficient Gram `G_I`. Whitening by `G_I^{-1/2}` gives a two-dimensional orthogonal projection of a product density. The Ball/Livshyts-Paouris-Pivovarov two-dimensional marginal bound used in the pinned ruled theorem is at most `2`; scaling back gives

`||p_(Y_I,W_I)||_infinity <= 2/sqrt(delta)`.                           (3.6)

Since `(Y,W)` is only translated after the `I^c` variables are fixed, disintegration over `Z` yields, when `Z` is nonconstant,

`rho_(Y,W,Z)(y,w,z) <= (2/sqrt(delta)) p_Z(z)` a.e.                    (3.7)

and therefore

`M := sup_y int sup_w rho_(Y,W,Z)(y,w,z) dz <= 2/sqrt(delta).`         (3.8)

If `Z` is constant, the same argument is the `k=0` version with `M=sup_(y,w)rho_(Y,W)<=2/sqrt(delta)`.

For completeness, here is the exact single-hub receiver needed from this point. Let

`S = 2 H Y + lambda W^2 + 2W g(Y,Z)+F(Y,Z)`                            (3.9)

with the hub `H` independent of the other ORIGINAL coordinates and density at most one, and suppose (3.8) holds. On a slice `Y=y,Z=z`, complete the square in `W`. For any Borel set `B` and any `R>0`, the contribution from the fold `|W-W_0(y,z)|<=R` is at most `2RM`; outside the fold each of the two branches has derivative at least `2|lambda|R`, so its push-forward contribution is at most `M |B|/(|lambda|R)`. Taking `R=(|B|/(2|lambda|))^(1/2)` gives the square-root profile

`mu_y(B) <= 2 sqrt(2) M (|B|/|lambda|)^(1/2)`.                        (3.10)

The hub bathtub calculation of `single_hub_core`, Lemma 3.1 with `theta=1/2`, then gives

`||p_S||_infinity <= 1/2 + 8 M |lambda|^(-1/2).`                      (3.11)

This derivation uses only (3.8), so it is valid for the possibly nonorthogonal statistic `Z` produced by the exact regression shear.

Now divide (3.5) by `kappa=|r|sqrt(c)` and, if needed, reflect `H` to make the coefficient of `HY` positive. Equation (3.9) holds with

`|lambda|=|d|/(|r|sqrt(c))`.

Insert (3.8) into (3.11) and scale the density back by `kappa^{-1}`. This is exactly (3.3). QED.

### Corollary 3.2 — a uniform 30-row residual chamber

Suppose additionally every transverse leaf leverage satisfies

`ell_i=y_i^2+w_i^2 < 1/61`,                                           (3.12)

as in the current fleet03/B10 unpaid chamber, and suppose the nonregressible residual `q=t-gamma y-eta w` is supported on at most 30 physical leaves. Take `I=supp(q)^c`. Since the full transverse Gram is `I_2`,

`G_I = I_2-G_supp(q)`,

and

`lambda_min(G_I) >= 1-sum_(q_i!=0) ell_i > 1-30/61 =31/61`.

Hence `delta>(31/61)^2`, and (3.4) gives

`boxed: ||p_Q||_infinity < 1/2 sqrt(64/63)
       +16(61/31)(64/63)^(1/4) <32.12.`                               (3.13)

The earlier one-clean-bank theorem required an entire independent transverse square bank. The present result is strictly broader: both transverse coordinates may be contaminated by the same longitudinal leaves; it is enough that after one exact transverse regression there remains a source-disjoint two-dimensional transverse reservoir.

## 4. Required ruled-side theorem spent on the same geometry

For the exact-null matrix (2.1), `det M=-r^2 d`, while the leading `2x2` principal block is indefinite. Thus if `d>0` the signature is `(2,1)`, and if `d<0` it is `(1,2)`. Applying the pinned ruled-level-set theorem to `Q` or `-Q` gives the actual inequality

`boxed: p_Q(s) <= pi sqrt(2) whenever sign(d) s >=0.`                  (4.1)

In the canonical target family below `d=1`, so the entire one-sheet side `s>=0` is already paid by (4.1). The remaining issue is genuinely the two-sheet side, not the ruled side.

## 5. New obstruction: aggregate partner curvature does not manufacture an exact clean reservoir

Theorem 3.1 is useful but cannot be the final gluing principle. There is an explicit target-valid, fully diffuse harmonic family in which the partner's aggregate geometry is strong while every exact regression-clean reservoir has determinant tending to zero.

Fix an odd integer `m>122`, `0<rho<1/64`, `c=1-rho`, and

`theta_j=2 pi j/m`, `j=0,...,m-1`.

Use the Parseval rows

`u_0=sqrt(c)e_1`,

and, for `j=0,...,m-1`,

`t_j = sqrt(2rho/m) cos(2 theta_j)`,
`y_j = sqrt(2/m) cos(theta_j)`,
`w_j = sqrt(2/m) sin(theta_j)`,
`u_j=(t_j,y_j,w_j)`.                                                  (5.1)

Discrete Fourier orthogonality gives exactly

`sum t_j^2=rho`, `sum y_j^2=sum w_j^2=1`,
`sum t_j y_j=sum t_j w_j=sum y_j w_j=0`.

Therefore the matrix `R` with rows `u_0,u_j` has `R^T R=I_3`. Every transverse leaf leverage is

`y_j^2+w_j^2=2/m<1/61`.                                               (5.2)

Take

`M_0=[[0,1,0],[1,0,0],[0,0,1]]`, `A=R M_0 R^T`.                      (5.3)

Then `A` has exactly the three nonzero eigenvalues `{1,-1,1}` and is an exact target instance. In ORIGINAL coordinates,

`Q=2(sqrt(c)H+T)Y+W^2`.                                               (5.4)

Now let `gamma,eta` be arbitrary. An index lies in an exact regression-clean set only if

`t_j=gamma y_j+eta w_j`,

or equivalently

`sqrt(rho) cos(2 theta_j)=gamma cos(theta_j)+eta sin(theta_j)`.         (5.5)

The left minus right side is a nonzero trigonometric polynomial of degree two. It has at most four zeros on one period. Hence **every** exact regression-clean set `I` has

`|I|<=4`.                                                             (5.6)

Moreover, by Cauchy-Binet,

`det G_I = sum_{i<j in I} (y_i w_j-y_j w_i)^2`.

Here

`|y_i w_j-y_j w_i|=(2/m)|sin(theta_j-theta_i)|<=2/m`,

so (5.6) implies

`boxed: det G_I <= 24/m^2.`                                           (5.7)

Thus no choice of the exact regression shear in Theorem 3.1 has a uniformly nondegenerate clean reservoir in this family. Its bound necessarily deteriorates at least through the factor `delta^{-1/2} >= m/sqrt(24)`.

This remains true after conditioning on **any** subset of ORIGINAL leaves: conditioning only deletes sample points `theta_j`; equation (5.5) still has at most four surviving zeros. In particular, apply the current fleet03/B10 contraction theorem to this same family. It guarantees a legal conditioning set which contracts longitudinal energy while leaving a remaining transverse Gram with `lambda_min>=2/81`. Nevertheless, every exact regression-clean subset of that remaining bank still obeys (5.6)-(5.7). Therefore

> strong aggregate transverse curvature plus a fixed-factor leakage contraction does **not** imply a uniformly nondegenerate exact regression-clean reservoir.

This is a counterexample to that proposed proof interface, not to QFORM.

The required pinned source theorem simultaneously pays the ruled side of this very family:

`p_Q(s)<=pi sqrt(2)` for every `s>=0`.                                 (5.8)

So the hard survivor exposed by (5.1)-(5.8) is sharply located on the two-sheet side `s<0`, with fully diffuse ORIGINAL-coordinate overlap and no good exact-regression reservoir.

## 6. Near-null puncture and why the gluing debt is real

The same physical frame can be kept while replacing (5.3) by

`M_alpha=[[alpha,sqrt(1+alpha),0],[sqrt(1+alpha),0,0],[0,0,1]]`,       (6.1)

for `0<=alpha<1/16`. Its nonzero spectrum is exactly

`{1+alpha,-1,1}`.                                                      (6.2)

Thus (6.1) is a target-valid punctured collar converging to (5.3). The current partner's exact discriminant cancellation applies for `alpha>0` and yields an absolute-root payment of order `alpha^(-1/4)`; at `alpha=0` that route degenerates to rank one. The new Theorem 3.1 supplies a finite endpoint receiver only when a quantitatively nondegenerate exact regression-clean reservoir exists, and (5.7) shows that its constant can simultaneously deteriorate with `m` in a fully diffuse target family.

Hence the two already-valid mechanisms do not yet glue to a universal endpoint estimate. The obstruction is not small matrix error: the laws have arbitrary unbounded/fragmented support, so a small coefficient cannot be discarded as a small random perturbation.

## 7. First unpaid implication

The first unpaid B10 implication is now

`QFORM-DIFFUSE-REGRESSION-DENSE-TWOSHEET-RECEIVER-v1`:

> In the exact-rank-three near-coloop collar, after using the partner's legal conditioning contraction, prove a two-sheet density bound that uses the **aggregate** ORIGINAL-coordinate transverse Gram while retaining nonzero same-bank longitudinal contamination on every large transverse reservoir. The bound must remain uniform as the hub Rayleigh coefficient tends to zero and may not pass through an exact-regression zero set, a worst conditional density, post-rotation independence, a moment/support assumption, or an absolute discriminant expectation.

The harmonic frame (5.1) is a canonical source-valid test family for this implication: it satisfies the partner's `<1/61` diffuse gate, has exact spectrum `{1,1,-1}`, has the ruled side already paid by the pinned theorem, and defeats exact clean-reservoir extraction quantitatively while preserving the full product provenance.

## 8. Scope and status

What is proved here:

1. the regression-clean endpoint theorem (3.3)-(3.4) for arbitrary cap-one product laws;
2. the uniform `<32.12` corollary when the nonregressible residual occupies at most 30 diffuse leaves;
3. the explicit harmonic exact-rank-three family (5.1)-(5.4);
4. the exact obstruction (5.6)-(5.7) to deriving a universal clean reservoir from aggregate diffuse geometry;
5. the actual ruled-side inequality (4.1)/(5.8) from the required pinned source.

What is **not** proved: the arbitrary rough fully overlapping two-sheet endpoint, the punctured-to-null uniform gluing, the unrestricted exact-rank-three theorem, or full QFORM. No counterexample to the conjecture was found.
