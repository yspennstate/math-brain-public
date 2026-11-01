SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B14, 2026-09-23T05:13:53Z.
attacking: mass-preserving localization before fragment normalization; then coarsen aligned product banks before selecting a bank or paying reciprocal curvature.

# fleet01/B14 r30 — sharp fragment-mass localization and coarsen-before-condition application

Programme: `QFORM-DENSITY-3EIG-20260922`. Role: translations and localization. Status: **NEW SUPPORTING LOCALIZATION LEMMA + TARGET-VALID PROOF-ORDER APPLICATION; FULL QFORM REMAINS OPEN.** Execution: `WITHOUT_VERIFIED_BRAIN`. Continuity is separate.

## 1. Sources actually used


The assigned partner result actually applied below is `fleet02/B14` r26:

`yspennstate/math-open-problems@5704e7da5b6134fc8e3bdde6caedc7358a666f65`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260923T050751Z-fleet02-B14-QFORM-r26/REPORT.md`.

It proves the disjoint-multibank compiler. In the one-bank specialization, if `B=B^T` on `U in R^3` has a unit kernel vector `k`, the two eigenvalues of `B|_(k^perp)` have moduli at least `nu`, the bank statistic is `W=a^T V` with certified density cap `eta`, and the `U`-bank cross block is `gamma k a^T`, then after the cap-one scaling the leakage coefficient is `r=gamma/eta` and

`||p_Q||_inf <= C4/min(nu,|r|)`,

with

`C4=1000(8+log 4)=9386.294361119892...`,

uniform in arbitrary affine terms, arbitrary bank-square coefficient, arbitrary rough/unbounded support and arbitrary translations.

I also use the completed partner r24 whole-law localization principle and its warning against normalizing thin pieces first:

`yspennstate/math-open-problems@8c74cde9c5de560923027d3af8debe2da5c79bc4`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260923T025915Z-fleet02-B14-QFORM-r24/REPORT.md`.

No arbitrary-joint coarea bound, post-rotation independence, bounded-diameter localization, fixed fragment-count reduction, moment assumption, or law-uniform pointwise quadratic Fourier decay is used.

## 2. Sharp tensor fragment-mass localization

The correct way to pass from a whole cap-one marginal to finitely many distant fragments is to keep every fragment as an **unnormalized subprobability** until the singular/curvature estimate has been paid.

Let, for `1<=i<=m`,

`E_i = disjoint_union_{j=1}^{N_i} I_{ij}`,

where the `I_{ij}` are intervals of lengths

`ell_{ij}=|I_{ij}|`,   `sum_j ell_{ij}=1`.

Let `mu_i(dx)=1_{E_i}(x) dx` and `mu=otimes_i mu_i`. For a multi-index `alpha=(alpha_1,...,alpha_m)`, let

`nu_alpha = otimes_i (1_{I_{i,alpha_i}}(x_i) dx_i)`

be the corresponding **unnormalized** rectangle measure. Its mass is

`w_alpha = prod_i ell_{i,alpha_i}`,

and

`mu = sum_alpha nu_alpha`.

### Theorem 2.1 — tensor fragment-mass compiler

Suppose that for every component `alpha` and every interval `J`, after any component-dependent recentering/translation of the rectangle, one has

`nu_alpha{F in J} <= C |J| prod_i ell_{i,alpha_i}^{gamma_i}`            (2.1)

with fixed exponents `gamma_i>=1`. Then

`boxed: mu{F in J} <= C |J|`.                                          (2.2)

The same constant `C` is preserved. No fragment position, support diameter, moment, or translation parameter appears.

### Proof

Sum (2.1) over `alpha`:

`mu{F in J} <= C |J| sum_alpha prod_i ell_{i,alpha_i}^{gamma_i}`

`= C |J| prod_i (sum_j ell_{ij}^{gamma_i})`.

Because every `ell_{ij}<=1` and `gamma_i>=1`,

`ell_{ij}^{gamma_i} <= ell_{ij}`,

so every factor is at most `sum_j ell_{ij}=1`. This proves (2.2). Component-dependent translations do not enter the argument. QED.

### Sharpness for this proof interface

The exponent threshold `gamma_i=1` is exact. If one coordinate has `gamma_i<1`, split its unit mass into `N` equal fragments of length `1/N`. Then

`sum_{j=1}^N ell_j^{gamma_i} = N^(1-gamma_i) -> infinity`.             (2.3)

Thus a normalize-pieces-then-sum proof cannot be fragment-uniform if it leaves less than one full power of the unnormalized mass in any independently fragmented coordinate.

This is the ordinary-coordinate tensor analogue of fleet02/B14 r24's sharp overlap-power threshold for conjugate sum/difference fibers.

## 3. Equivalent normalized-cap criterion

Normalize each rectangle piece to probability. Its i-th marginal density cap is

`M_i = ell_i^(-1)`.

Suppose a downstream theorem applied to the **normalized** component has a density/small-ball certificate of the form

`C prod_i M_i^{beta_i}`.                                                (3.1)

Multiplying back by the component mass `prod_i ell_i` turns (3.1) into the unnormalized bound

`C prod_i ell_i^{1-beta_i}`.                                           (3.2)

Therefore Theorem 2.1 gives a fragment-uniform compiler exactly when

`boxed: beta_i <= 0 for every independently normalized fragment coordinate.` (3.3)

For this summation mechanism the criterion is also necessary: if some `beta_i>0`, equal `N`-fragment splitting produces an unavoidable factor

`N^{beta_i}`.                                                          (3.4)

The conclusion is not that a theorem with positive cap homogeneity is false. The conclusion is that one must apply it **before** independently normalizing arbitrary fragments, or retain additional cancellation/aggregation that restores a full mass power.

This is the precise localization rule relevant to arbitrary distant fragments and unbounded-support approximation.

## 4. Apply the completed partner theorem to an actual target inequality

Let `d>=1`, let

`r=(1,...,1)/sqrt(d) in R^d`,

and let

`U_1,U_2,U_3,Y_1,...,Y_d`

be independent real variables with densities at most one. Put

`W = r^T Y`.

For arbitrary `h in R`, consider

`Q_{d,h} = U_1^2 - U_2^2 + 2 U_3 W + h W^2`.                          (4.1)

### 4.1 The matrix is genuinely in the full target

On `span(U_1,U_2)` the eigenvalues are `+1,-1`. On `span(U_3,r)` the matrix is

`[[0,1],[1,h]]`,

whose two eigenvalues have product `-1`. Hence at least one of them has modulus at least one. Every direction in `r^perp` is null. Therefore the full matrix of (4.1) has at least three eigenvalues of modulus at least one for every `d` and every real `h`.

### 4.2 Coarsen the entire Y-bank before conditioning

Treat all `Y_1,...,Y_d` as **one original-coordinate bank** with bank vector `a=r`. The completed product-projection estimate used in partner r26 gives

`||p_W||_inf <= sqrt(2)/||r||_2 = sqrt(2)`.                            (4.2)

In partner r26 take

`B=diag(1,-1,0)`, `k=e_3`, `nu=1`, `gamma=1`, `a=r`, `eta=sqrt(2)`.

Thus the cap-one scaled bank variable has leakage coefficient

`|r_*| = gamma/eta = 1/sqrt(2)`.

Equation (2.1) of the completed partner theorem gives the actual target-level inequality

`boxed: ||p_{Q_{d,h}}||_inf <= sqrt(2) C4 < 13274.225.`                (4.3)

This is uniform in `d`, `h`, every choice of cap-one marginal laws, arbitrary translations of any coordinate, arbitrarily remote fragments, and unbounded supports. No moment bound is present.

The numerical constant is not intended as sharp; the point is the exact **dimension/support/translation independence**.

## 5. Remote-fragment stress test: the same theorem loses N if fragments are normalized first

Now specialize every `Y_j` to the remote-fragment density

`1_{E_N}`,   `E_N=union_{q=1}^N [4^q,4^q+1/N]`.                       (5.1)

Each marginal still has density cap one and total mass one. The whole-bank argument in Section 4 is unchanged, so (4.3) remains valid with no `N` dependence.

Instead, condition first on the fragment label of **every** `Y_j`. On each conditional component, every scalar `Y_j` is uniform on an interval of length `1/N`, hence has normalized density cap `N`.

Scale the conditional vector by

`Y'_j = N Y_j`.

The `Y'_j` are independent cap-one variables, and

`W = (1/N) r^T Y'`.

Thus the conditional aggregate `W` has the product-projection cap

`||p_{W | labels}||_inf <= sqrt(2) N`.                                (5.2)

Applying exactly the same partner r26 one-bank compiler after this normalization uses

`eta_N=sqrt(2)N`,   `r_{*,N}=1/(sqrt(2)N)`,

and gives only

`boxed: ||p_{Q_{d,h} | labels}||_inf <= sqrt(2) C4 N.`                (5.3)

Averaging over the fragment labels does not remove the factor `N`, because (5.3) is a normalized conditional probability bound. Hence the proof order

`condition on interval labels -> normalize -> pay reciprocal bank coefficient -> average`

loses a factor exactly of order `N`, while

`coarsen the whole product bank -> project -> pay curvature`

has the dimension- and fragment-free bound (4.3).

This is precisely Theorem 2.1 with normalized-cap exponent `beta=1`: the unnormalized component mass carries exponent `1-beta=0`, below the sharp safe threshold one.

The support locations `4^q` show that no recentering or bounded-diameter hypothesis repairs this loss. Translating each interval to the origin merely moves the lost scale into affine coefficients; partner r26 is already uniform in those affine coefficients.

## 6. A second proof-order comparison: select one fine bank versus coarsen first

There is another loss in the same family even without interval fragmentation.

If the `Y_j` themselves are treated as `d` separate partner-r26 banks, their exact caps are one and the leakage coefficients are

`gamma_j = 1/sqrt(d)`.

The one-bank selection step then yields only

`||p_{Q_{d,h}}||_inf <= C4 sqrt(d)`.                                  (6.1)

But the quadratic dependence on all `Y_j` in (4.1) factors through the single statistic `W=r^T Y`. Coarsening that entire aligned bank **before** bank selection produces (4.3), namely `sqrt(2) C4`, independent of `d`.

If one makes both bad choices—first fragment-normalize and then select one fine coordinate bank—the same compiler deteriorates to order `N sqrt(d)`.

Thus localization has two independent safe-order rules:

1. keep finite-fragment pieces unnormalized until after a mass-proportional estimate is obtained;
2. coarsen every exactly aligned disjoint product bank before selecting a weak individual bank.

Neither rule uses moments or bounded support.

## 7. Relation to whole-law extreme localization

Fleet02/B14 r24 proves that for convex TV-lower-semicontinuous output functionals, the supremum over cap-one product laws is unchanged when each marginal is restricted to an indicator of a compact finite union of intervals of total length one, simultaneously over arbitrary affine parameter families.

Theorem 2.1 supplies the missing operational warning for using that reduction: **the finite union is the localized object**. One is not entitled to normalize its component intervals separately and then apply a cap-homogeneous theorem unless the resulting unnormalized estimate retains exponent at least one in every fragment mass.

Therefore arbitrary unbounded laws may be approximated/localized with zero constant loss, but the proof must keep whole localized marginals or whole aligned banks through the reciprocal-curvature/volume step.

## 8. What remains unpaid

This run does not solve N3 or the full conjecture. The remaining matrix-structural problem is unchanged in substance but the localization interface is sharper:

* when a surviving heavy-star/no-pivot matrix factors through a bounded number of **disjoint aligned aggregate banks**, coarsen first and use the partner multibank/fixed-core theorem;
* when curvature genuinely uses several overlapping aggregate directions on the same original-coordinate bank, those statistics cannot simply be declared independent or conditioned on separately;
* any decomposition into remote fragments or conjugate thin fibers must retain one full unnormalized mass power through reciprocal curvature/volume payment, or aggregate before normalization.

The first unpaid implication is therefore to obtain an exhaustive product-preserving structural reduction from `s_3(A)>=1` into existing volume/ridge/mixed-hub exits or a bounded number of disjoint aligned aggregate banks **without** first normalizing arbitrary small pieces.

Full QFORM remains OPEN. No unrestricted continuity claim is made.
