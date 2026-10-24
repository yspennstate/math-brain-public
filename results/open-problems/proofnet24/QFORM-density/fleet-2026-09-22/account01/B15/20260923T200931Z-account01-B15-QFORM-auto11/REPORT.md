SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-23T20:09:31Z.
attacking: finite-Lp source-stability and exact separation of essential height from continuity, applying account02/B15's completed physical-triple and rough-regularity results.

# account01/B15 auto11 — finite-Lp rough-source stability from any paid height certificate

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T200931Z-account01-B15-QFORM-auto11`  
Status: **PROVED TARGET-LEVEL REGULARITY/STABILITY LEMMA / PARTNER RESULT APPLIED / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and source boundary

The full owner target remains OPEN: for independent real coordinates with probability densities `0<=f_i<=1` and a real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove one universal finite bound on the essential supremum of the density of `Q=X^TAX`.

This run keeps the regularity hierarchy separate:

1. qualitative absolute continuity is much weaker than the target height;
2. a finite essential height is the central quantitative target;
3. a continuous representative is a separate stronger regularity statement, already known instancewise for rank at least three but not used to manufacture a universal height.

Fresh owner/control source was read on `math-research-brain` main at `2ea138dc4d05b138b9b57f79057b64426a8ad749`, OWNER CONTROL revision `2026-09-22.15`. The live corrections against pointwise law-uniform quadratic Fourier decay, independence after spectral rotation, and projection/X-ray-only closure are retained.

The completed assigned-partner material actually used is account02/B15 at the current math source, in particular

- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260923T190353Z-account02-B15-qform-auto11/REPORT.md`, and
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260923T190353Z-account02-B15-qform-auto11/CONSTANT_SHARPENING.md`, blob `95e45723e41901ace9d95790b610f24546cf6fdd`.

The latter gives the uniform physical-triple height

`||p_Q||_infinity < 15.008/kappa`                                      (1.1)

whenever one original-coordinate principal `3x3` block has smallest singular value at least `kappa>0`, with arbitrary outside interactions and affine terms. The same partner run proves the Fisher rough-closure obstruction used in Section 5 below.

For qualitative continuity I use the completed source-pinned account02/B15 theorem at `5b2073a19b463978d5e0b10df035842a8f3e22ff`, which gives an individually bounded `C_0(R)` density for every fixed rank-at-least-three product quadratic. Its constants depend on a nonsingular physical `3x3` or `4x4` block and therefore are not the missing universal constant.

## 2. New abstract lemma: height plus total variation gives finite-Lp output stability

### Theorem 2.1 — finite-Lp pushforward stability

Let `mu` and `nu` be finite positive measures of the same mass on a measurable space, let `q` be any measurable map to `R`, and suppose the pushforwards

`q_#mu = p_mu(t) dt`, `q_#nu = p_nu(t) dt`

have densities satisfying

`||p_mu||_infinity<=M`, `||p_nu||_infinity<=M`.                       (2.1)

Put

`Delta = ||mu-nu||_TV,dens`,

where in the density setting below this means the `L1` norm of the signed input density, not the half-total-variation convention. Then for every `1<=r<infinity`,

`boxed{
 ||p_mu-p_nu||_r
 <= (2M)^(1-1/r) Delta^(1/r).
}`                                                                        (2.2)

No continuity, Fourier decay, moments, support bound, or smoothness is required.

### Proof

Pushforward contracts the total variation norm of a signed measure. Therefore

`||p_mu-p_nu||_1 <= Delta`.                                               (2.3)

The common height bound gives

`||p_mu-p_nu||_infinity <=2M`.                                            (2.4)

Writing `h=p_mu-p_nu`,

`||h||_r^r = integral |h|^r
 <= ||h||_infinity^(r-1) ||h||_1
 <= (2M)^(r-1) Delta`.

Taking the `r`th root proves (2.2). QED.

The endpoint `r=infinity` is intentionally absent. The factor `Delta^(1/r)` tends to one as `r->infinity`, so this lemma does not smuggle an `L1 -> L-infinity` closure statement into the proof. This is exactly the distinction needed in the current regularity programme.

## 3. Product-source specialization

Let

`F(x)=prod_{i=1}^n f_i(x_i)`, `G(x)=prod_{i=1}^n g_i(x_i)`

be probability product densities. The telescoping identity gives

`F-G = sum_{j=1}^n
        (prod_{i<j} f_i)(f_j-g_j)(prod_{i>j} g_i)`.

Integrating absolute values and using that every other factor has integral one yields

`boxed{
 ||F-G||_1 <= sum_{j=1}^n ||f_j-g_j||_1.
}`                                                                        (3.1)

Consequently, whenever one law-independent height certificate `M(A)` is valid for every cap-one product source for the same matrix `A`, Theorem 2.1 gives

`boxed{
 ||p_{F,A}-p_{G,A}||_r
 <= [2M(A)]^(1-1/r)
    [sum_j ||f_j-g_j||_1]^(1/r),
  1<=r<infinity.
}`                                                                        (3.2)

This is a genuinely rough-source statement: the two sets of marginals may be discontinuous, fragmented, unbounded in support, and unrelated except through their `L1` distances.

## 4. Actual application of the completed account02/B15 physical-triple theorem

Assume that `A` has an original-coordinate principal `3x3` block `B` with

`kappa=sigma_min(B)>0`.

The completed account02/B15 physical theorem (1.1) applies to every admissible cap-one product source, so in (3.2) we may take

`M(A)=15.008/kappa`.

Therefore, for every `1<=r<infinity`,

`boxed{
 ||p_{F,A}-p_{G,A}||_r
 < (30.016/kappa)^(1-1/r)
   [sum_j ||f_j-g_j||_1]^(1/r).
}`                                                                        (4.1)

In particular,

`boxed{
 ||p_{F,A}-p_{G,A}||_2
 < sqrt(30.016/kappa)
   [sum_j ||f_j-g_j||_1]^(1/2).
}`                                                                        (4.2)

This is an actual inequality obtained from the designated partner result; no spectral-coordinate independence or projection-only reduction is used. The block and all conditioning are in the original independent coordinates, exactly as in the partner theorem.

### Rough mollification corollary

If `f_j^(m)` are cap-preserving original-coordinate approximations with

`sum_j ||f_j^(m)-f_j||_1 ->0`,

then, for this fixed physical-block branch,

`boxed{
 p_m -> p in L^r(R) for every finite r.
}`                                                                        (4.3)

Thus smooth or analytic approximations may be removed strongly at every finite output `L^r` level once a uniform height receiver is already paid. No shrinking-window, desmoothing, or continuity argument is needed for (4.3).

The same conclusion holds for every fixed rank-at-least-three matrix using its matrix-dependent bounded-density certificate from the fixed-matrix B15 theorem. The constant is then instance-dependent and does not solve the universal problem.

## 5. Concrete comparison with the partner Fisher obstruction

Take the exact normalized target

`A = [[0,1,0],[1,0,0],[0,0,1]]`,

so

`Q=2X_1X_2+X_3^2`,

and the spectrum is `{1,-1,1}`. Here the whole matrix is an invertible physical `3x3` block with `kappa=1`.

Let `U_3=1_[0,1]^tensor3`, and let `F_m=prod_i f_{i,m}` be cap-one product densities with

`Delta_m=||F_m-U_3||_1 ->0`.

Equation (4.1) gives, for every finite `r`,

`boxed{
 ||p_m-p_U||_r
 < 30.016^(1-1/r) Delta_m^(1/r).
}`                                                                        (5.1)

For `r=2`,

`||p_m-p_U||_2 < sqrt(30.016) Delta_m^(1/2) <5.48 Delta_m^(1/2)`.          (5.2)

Now impose the additional Fisher regularity `sqrt(f_{i,m}) in H^1`. The latest account02/B15 theorem proves that whenever `Delta_m<=1/8`, the projected information for this exact target obeys

`boxed{
 J_E=I(f_{1,m})+I(f_{2,m})+I(f_{3,m}) >= 3/(4 Delta_m).
}`                                                                        (5.3)

Thus the same approximation can have **strong output convergence in every finite `L^r` while its Fisher budget necessarily diverges**. This cleanly identifies the regularity lesson:

- the physical height theorem is robust enough to pass to rough sources by total variation and finite-Lp interpolation;
- a Fisher-information certificate is not a uniform closure class for arbitrary cap-one sources;
- neither fact supplies the missing global matrix geometry needed for the unrestricted universal height.

For the limiting cube source itself, the partner's ruled-majority theorem even gives the sharper special inequality

`||p_U||_infinity <= pi sqrt(2)`,

because `2X_1X_2+X_3^2>=0` on `[0,1]^3`. This special positivity is not assumed in (4.1) or (5.1).

## 6. Exact regularity ledger

### Absolute continuity

If the joint input law is absolutely continuous and `A!=0`, then `X^TAX` is absolutely continuous. One may prove this by coarea away from `ker A`, or by original-coordinate conditioning on a nonconstant quadratic/affine fiber. The target assumptions are much stronger than needed for this qualitative conclusion.

### Bounded density

The central owner theorem is the missing uniform statement

`||p_Q||_infinity <= C/s_3(A)`                                               (6.1)

for one absolute `C` over the whole product class. Physical blocks, volume/ridge branches and the Gaussian-mixture branch pay substantial subclasses, but no supplied argument closes every matrix/source configuration.

### Continuous density

The source-pinned fixed-matrix B15 theorem gives `p_Q in C_0(R)` for every fixed rank-at-least-three matrix and every cap-one product source, with a finite matrix-dependent height. This qualitative continuity theorem is separate from (6.1).

If (6.1) is eventually proved, the already-existing continuous representative automatically satisfies the same pointwise bound because a continuous function cannot exceed its essential supremum at an isolated point:

`sup_t p_Q(t) = ess sup_t p_Q(t) <= C/s_3(A)`.                              (6.2)

No constant is lost in passing from the essential bound to the continuous representative. But continuity is not being used to prove the essential bound.

### No uniform continuity modulus

The completed B15 phase-aligned constructions already show that even for `A=I_3`, smooth compact cap-one sources can have uniformly bounded output heights but arbitrarily rapid output oscillation. Therefore neither (4.3) nor the fixed-matrix `C_0` theorem may be upgraded to a target-uniform modulus of continuity without extra hypotheses.

## 7. Target-level conditional stability consequence

The new lemma packages a useful consequence of the desired theorem itself. If the universal QFORM constant `C_*` exists, then for every fixed target matrix and every two admissible product sources,

`boxed{
 ||p_{F,A}-p_{G,A}||_r
 <= (2C_*/s_3(A))^(1-1/r)
    [sum_j ||f_j-g_j||_1]^(1/r),
  1<=r<infinity.
}`                                                                        (7.1)

This finite-Lp Hölder stability is therefore an automatic **corollary** of universal height, not an extra regularity premise needed to establish height. It is stable under arbitrary rough cap-one laws and is consistent with the known failure of any uniform continuity/Hölder modulus in the output variable.

## 8. Remaining implication

This run closes a regularity/approximation interface, not the structural matrix endpoint. The full conjecture still requires a universal height receiver when no uniformly conditioned physical triple exists, including the growing-dimension / degenerate-minor configurations covered only partially by aggregate ridge, grouped-coordinate, volume, projected-crossing, or Gaussian-mixture arguments.

The mathematical next step for B15 is to apply finite-Lp/TV closure only *after* a source-valid uniform height branch is paid, and to avoid trying to manufacture the missing height from Fisher approximation, qualitative continuity, target-uniform desmoothing, rotated independence, or generic projection information.
