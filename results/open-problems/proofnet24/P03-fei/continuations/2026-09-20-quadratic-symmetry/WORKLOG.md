# Scientific worklog and continuation targets

20 September 2026. This records the mathematical results, tested routes, code, and limitations of this owner-requested FEI attempt. Full FEI was the target; it has not been proved here. This is a research record, not a claim about independent reviewers, hidden agents, or future scheduled execution.

## A. Starting point and decisions that changed the mathematics

The current P03 entrypoint and complete erasure reduction were read. The latest entrypoint already retires the all-coordinate absolute-overlap selector, the false pointwise erasure converse, all-constant resolvent shortcuts, and fixed-coefficient affine entropy-drift payments. None was reinstated.

The live all-dimensional target is a uniform weighted-erasure/entropy allocation bound. The first experiments retained the actual Fourier amplitudes of Boolean truth tables, rather than optimizing over unrestricted nonnegative spectral laws. Such a relaxation would lose the signed convolution identities arising from `f^2=1` and would admit elementary false countermodels.

The substantive new direction was to use invariance of the Boolean multiplicative derivatives. A quadratic phase turns the derivative correlation into one Fourier coefficient of the original derivative. Symmetry supplies a second equal coefficient, forcing each to have magnitude at most one half. This creates the quarter-influence payment proved in REPORT.md, rather than another unpaid local-entropy reformulation.

## B. Positive results obtained

The report proves `H((-1)^Q h) <= (12.04+log_2 d)J((-1)^Q h)` for arbitrary d-part-symmetric Boolean cores and arbitrary quadratic phases on the same variables. The mechanism is physical deletion of mixed quadratic rows, with a precise cost and a certified residual symmetry class.

It then proves the same result for a product of independently supported cores, with `d` replaced by the maximum number of parts in any one core, not the total number of cores. Cross-core quadratic rows have folded influence exactly one half. In particular, any number of symmetric factors with arbitrary quadratic coupling has the dimension-independent constant 12.04.

The constants are inherited from O'Donnell–Wright–Zhou, not numerically fitted. The unrestricted quadratic coupling is allowed to break the symmetry and factorization of the final function. Only the actual physical restriction leaves are assumed and proved to recover the certified structure.

The report also records the universal pair inequality `j_i(h)+j_i((-1)^Qh)>=1/2` for nonzero quadratic rows, and a precise low-folded-influence transfer criterion with an explicit leaf-certificate hypothesis. That criterion is conditional on those stated certificates, not a solution to their unrestricted existence.

## C. Initial local-entropy experiment

Files:

- `explore_local_entropy.py`: initial NumPy floating-point search, random seed 20260920.
- `explore_local_entropy_stdout.txt`: the actual original console output, including the maximizing witnesses encountered and the compression witness.

The script exhausts truth tables in dimensions two and three, then samples 4,000 tables per dimension from four through eight, using several negative densities. It computes spectral entropy, total influence, erasure entropy, the weighted logarithmic edge quantity, absolute overlaps, and coordinate entropy decrements.

The largest observed `B/I` was approximately 2.8835664 and the largest observed `K/I` approximately 1.1902175, both in the finite search. These are observations about the tested tables only. They are not upper bounds, optimality certificates, universal constants, or evidence that other function families have been ruled out. The largest observed minimum-coordinate decrement ratio was approximately 4.8676687. No FEI conclusion was inferred from these finite extrema.

The initial script first hit a printing error on a dimension with no positive `K/I` witness; its diagnostic print was corrected and the included version was rerun successfully. This did not change the formulas or select away a failed mathematical inequality.

## D. A rejected monotone-compression shortcut, with an exact witness

A possible route was to compress pairs of physical values into monotone order and hope to reduce influence without losing the entropy that must be bounded. The required entropy monotonicity is false.

For integers indexing bit strings with the first coordinate as the least significant bit, take

    f = (1,-1,-1,1,-1,1,-1,1).

Equivalently, `f(x)=(-1)^{x_1}g(x_2,x_3)` where `g` has values `(1,-1,-1,-1)`. The two-variable `g` has four squared Fourier coefficients equal to one quarter. Thus `H(f)=2`, and `I(f)=2`.

Sorting each first-coordinate pair into nondecreasing order gives

    compressed_f = (-1,1,-1,1,-1,1,-1,1) = -(-1)^{x_1}.

Its entropy is zero and its influence is one. Therefore this physical compression can decrease both influence and entropy and cannot, without a separate paid entropy loss, transfer an FEI upper bound on the compressed function back to the original. The exact integer checker verifies all four quantities. This does not rule out every compression-based method; it rules out the unpaid monotonicity shortcut tested here.

## E. A rejected fixed-q strengthening

An attempted stronger route was to seek a fixed `0<q<2` and fixed `rho>0` with

    sum_S |fhat(S)|^q rho^{|S|} <= 1

for all Boolean functions. This is false even for odd majority, so it cannot be used as a universal input from which to differentiate toward FEI.

For majority on `n=2m+1` variables, every singleton Fourier coefficient is

    a_m = 4^{-m} binom(2m,m).

To see the coefficient formula, average first over the selected input coordinate: its correlation with majority is one exactly when the sum of the other `2m` signs is zero, and is zero otherwise.

The elementary bound `a_m >= 1/(2 sqrt(m))` holds for `m>=1`. At `m=1` there is equality. The recurrence `a_(m+1)/a_m=(2m+1)/(2m+2)` is at least `sqrt(m/(m+1))`, since squaring reduces the assertion to `4m^2+4m+1 >= 4m^2+4m`. This proves the bound by induction.

Consequently, the singleton contribution alone is at least

    rho (2m+1)/(2 sqrt(m))^q,

which diverges as `m -> infinity` for every fixed `q<2`. This obstruction does not contradict FEI; it excludes the stronger finite-q bound. A nonuniform endpoint argument would need additional analysis and was not established. No priority claim is made for this elementary obstruction.

## F. Why a naive high-degree extension fails

For the rare monomial phase `(-1)^{x_1...x_m}` on `m+1` variables, every relevant folded influence is `2^(1-m)` and the last coordinate is irrelevant. The function is not invariant under exchanging that last coordinate with a relevant one. Thus arbitrary higher-degree perturbations of a symmetric seed can break symmetry while every relevant influence is arbitrarily small.

This prevents simply replacing “quadratic” by “arbitrary degree” in the fixed per-coordinate payment. It does not refute a more refined probability-weighted or structural payment and does not contradict FEI. The exact checker verifies the formulas for `m=4,...,10`; the formula itself has a direct proof in every dimension: flipping a relevant bit changes the output precisely when all the other `m-1` relevant bits are one.

This example can itself be handled by recognizing a more suitable symmetry block, so it does not show that every adaptive block-refinement strategy must fail. It shows that the particular fixed original-symmetry, fixed-cost extension would be invalid.

## G. Exact validation and one checker correction

`verify_quadratic_symmetry.py` uses no external packages. It verifies the main inequalities with exact integer Walsh transforms and rational logarithm enclosures; it does not accept inequalities by floating-point tolerance. The delivered `verification.json` was produced by that script.

The first exact run stopped at a valid entropy-deletion equality because the upper interval endpoint of the parent was slightly above the sum of the lower endpoints of the leaves. In the diagnostic case, `n=6` and the numerical enclosure excess was the rational `9/9671406556917033397649408`, entirely from using two independently rounded versions of the same logarithm. The mathematical bound had not failed.

The checker was corrected by expressing the relevant entropy difference as a rational linear combination of logarithms of odd primes and cancelling common terms exactly before enclosure. The subsequent complete run passed. This correction is retained in the code as `entropy_signature` and `certify_entropy_deletion`; the output records one symbolic cancellation certificate. The final run also includes the universal quadratic-pair checks added after the first successful class check.

Current output:

    graph / partition / factorization checks: 108506
    exhaustive symmetric-core / graph cases: 67732
    exhaustive partition / core / graph / linear cases: 29896
    random product / part-symmetric cases: 840
    restriction leaf tables: 171150
    universal quadratic pair function / graph cases: 2084
    universal quadratic pair coordinate checks: 4640
    symbolic entropy equality certificates: 1
    status: PASS

Case families overlap, and the sampled families are not exhaustive. The analytical proof, not these counts, supplies the all-dimensional result.

## H. Precise next research objective

The new positive class can serve as a stopping class for the already-established hereditary erasure program. The next useful extension would admit genuinely dependent, high-degree cores while controlling the allocation entropy or the physical recombination cost by actual influence. In such an extension, rare asymmetric defects must receive a probability-weighted cost, not a fixed cost per coordinate.

A universal bound on the surviving weighted-erasure quantity would finish FEI through the existing induction. It remains unproved here. No assertion is made that the new class covers every Boolean function, that the remaining gap is merely clerical, that a future worker has consumed this package, or that a percentage of the conjecture is solved.

Delivery should preserve all earlier valid constant-four and rare-control theorems with their own hypotheses. The present theorem is a complementary positive result, not an excuse to overwrite their stronger constants on their smaller stated classes.
