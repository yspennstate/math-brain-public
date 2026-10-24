SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B04, 2026-09-23T11:19:30Z.
attacking: pay the non-coloop fractional third-volume support defects with exact-rank-three product Plancherel, then compare volume and ridge on one tetrahedral physical matrix.

# account02/B04 — the strict fractional-volume support defect is completely paid

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement / complementary constructions  
Status: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / TARGET-VALID EXPLICIT ESTIMATE`  
Full unrestricted QFORM target: **OPEN**.  
Independent review: **pending**.  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication, updated early

The preceding B04 theorem `QFORM-THIRDVOLUME-FRACTIONAL-BASEPACKING-v1` gave the exact support threshold

`h_*(N)=max_{A subset E, r(A)<3} (3-r(A))/|E\A|`

for probability weights on supported physical 3x3 minors. Hence failure of every strict D' gate `h<3/4` occurs only through one of three row-matroid geometries:

1. a physical row is a coloop;
2. all but two active physical rows lie in a rank-one flat;
3. there are at most four active physical rows.

This run pays **all three exact support-defect geometries**. The first unpaid implication is therefore no longer support feasibility. It is now

`QFORM-QUANTITATIVE-COMPOUND-HUB-HIGHER-RANK-PAYMENT-v1`:

> when a strict fractional-volume support weight exists but every such weight has poor determinant/entropy currency, use the bounded compound row/column hubs supplied by account03/B04 r31 and pay the genuinely higher-rank retained packets without multiplying by arbitrarily tiny extra singular values. Exact-rank-three retained packets are already paid by account03/B04 r32.

## 2. Sources actually used and forbidden premises excluded

Pinned Claude/e5 source, at the requested immutable commit:

- `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`
- `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`
- `.../FOURIER_ROUTE_REPORT.md`
- `.../COUNTEREXAMPLE_SEARCH.md`.

Theorem D gives `6 sqrt(e) Z^(-1/6)` for third-volume `Z=E3(M)` when the constrained-side row marginals are at most `1/2`. Its proved D' extension permits a cap `h<3/4`, with coefficient

`6 sqrt(e) (2h)^(-1/2) (3-4h)^(-1)`.

The newest compatible designated partner is account03/B04 r32, read from the fresh master snapshot containing

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/20260923T105123Z-account03-B04-qform-auto11-r32/REPORT.md`.

Its `QFORM-EXACT-CROSS-RANK-PLANCHEREL-v1` says that for two disjoint original-coordinate product banks with exact physical cross rank `r>=3`, arbitrary same-bank measurable phases/curvature, and nonzero cross singular values `sigma_j`,

`||p_Q||_infinity <= [r/(r-2)] (M_X M_Y)^(1/r) (product sigma_j)^(-1/r)`,

where `M_X,M_Y` are density caps of the two orthogonal product projections. In particular the product-marginal bound gives

`||p_Q||_infinity <= [2r/(r-2)] (product sigma_j)^(-1/r)`,

and for exact rank three

`||p_Q||_infinity <= 6 E3(M)^(-1/6)`.

The proof is a joint product-space Plancherel/rearrangement estimate on complex projected densities. No law-uniform pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint coarea bound, conditional projection-cap moment, or worst-fiber supremum is used here.

## 3. New theorem — every exact strict-D' support defect has an exact-rank-three exit

### Theorem 3.1 — `QFORM-FRACTIONAL-SUPPORT-DEFECT-COMPLETE-EXIT-v1`

Let `I,J` be disjoint original-coordinate banks of a full quadratic form and let `M=A[I,J]`. Assume

`Z=E3(M)=e3(M^T M)>0`.

Suppose no probability law on the supported physical 3x3 minors has every constrained-side row marginal strictly below `3/4`. Then the full ambient quadratic form, with arbitrary self-blocks, outside coefficients and induced affine terms, has a continuous density and

`boxed: ||p_Q||_infinity <= 6 * 4^(1/6) * Z^(-1/6).`                         (3.1)

If the support defect is a coloop or a rank-one-flat-plus-two-transverse-rows geometry, the sharper bound

`boxed: ||p_Q||_infinity <= 6 Z^(-1/6)`                                      (3.2)

holds.

#### Proof

Use the preceding exact support classification.

**Coloop.** Let row `i0` belong to every supported rank-three row basis. If `rank(M_{I\{i0},*})>=3`, three rows not using `i0` would form a supported row basis, contradiction. Hence

`rank(M_{I\{i0},*})<=2`.

Adding one row increases rank by at most one, so `rank(M)<=3`. Since `Z>0`, `rank(M)>=3`; therefore `rank(M)=3` exactly. Partner r32 applies directly and yields (3.2).

**Rank-one flat plus two transverse active rows.** The row span has dimension at most `1+2=3`. Again `Z>0` forces exact rank three, and partner r32 gives (3.2).

**At most four active rows.** Then `rank(M)<=4`. If the rank is three, partner r32 again gives (3.2). If the rank is four, for each physical row triple `S` put

`z_S = sum_{|T|=3} det(M_{S,T})^2 = E3(M_{S,*})`.

Cauchy-Binet gives

`Z = sum_{|S|=3} z_S`.

There are at most four row triples, so some `S_*` has `z_{S_*}>=Z/4`. Condition on every original coordinate of the row bank outside `S_*`. This is legitimate original-coordinate conditioning and preserves independence of all retained source coordinates. The retained cross block

`B=M_{S_*,*}`

has `E3(B)=z_{S_*}>0` and only three rows, hence exact rank three. All couplings from the conditioned rows become allowed affine/same-bank terms in the partner theorem. Therefore

`||p_Q||_infinity <= 6 z_{S_*}^(-1/6) <= 6*4^(1/6) Z^(-1/6)`.

Averaging the uniform conditional density bound proves (3.1). The partner characteristic-function proof is integrable, so the same branch supplies a continuous `C_0` representative. QED.

### Consequence

The exact support obstruction from the full proved third-volume fractional window is now **completely removed**. A strict D' support failure does not require a new endpoint theorem: it automatically collapses to exact rank three, except for the four-row rank-four case, where one original-coordinate conditioning exposes an exact-rank-three packet losing only the factor `4^(1/6)`.

The remaining obstruction is quantitative, not combinatorial support feasibility.

## 4. Boundary stress matrix: globally optimal volume weights still hit h=3/4

Take the regular tetrahedral frame

`U=(1/2)*[[ 1, 1, 1],
           [ 1,-1,-1],
           [-1, 1,-1],
           [-1,-1, 1]]`,

and put

`M=2U=[[ 1, 1, 1],
       [ 1,-1,-1],
       [-1, 1,-1],
       [-1,-1, 1]]`.

Then `U^T U=I_3`, every physical row leverage equals `3/4`, every physical cross coefficient is nonzero, and the singular values of `M` are exactly `(2,2,2)`.

There are four physical row triples. Their determinants are `4,-4,4,-4`, so every squared determinant is `16` and

`Z=E3(M)=64`.

Every supported minor law is determined by `p_i`, the probability that row `i` is omitted. Row `i` then has marginal

`alpha_i=1-p_i`,

with `sum_i p_i=1`. Consequently

`max_i alpha_i >= 3/4`,

and equality holds only when `p_i=1/4` for all four rows. Thus the exact global support optimum is

`boxed: h_*=3/4.`                                                        (4.1)

Because all supported squared determinants are equal, the entropy-adjusted volume currency is

`G(w)=16 exp(H(w)) = 64 exp(-KL(w||unif_4)) <=64`,

with equality exactly at the uniform law. So the same uniform law is also the global entropy optimum at the boundary.

This applies the pinned e5 results to an actual obstruction: e5 Theorem D cannot apply for **any** weighting because `h_*>1/2`; its D' extension also cannot apply because it requires the strict threshold `h<3/4`. The fifth-volume theorem has `E5(M)=0` because the block has exact rank three. This is an obstruction to those intermediate Fourier certificates, not to QFORM.

## 5. Direct ridge also has no certificate on the same matrix

For the completed direct ridge family let

`K_gamma=MM^T (gamma^2 I+MM^T)^(-1)`.

Since `MM^T=4 U U^T`, write

`kappa=4/(4+gamma^2)`.

Then

`K_gamma=kappa U U^T`,

`L_gamma=max_i (K_gamma)_ii=3kappa/4`,

`theta_gamma=tr K_gamma=3kappa`.

The direct ridge gate requires

`L_gamma <= q/2` and `theta_gamma>2q`.

The first inequality forces `q>=3kappa/2`, while the second forces `q<3kappa/2`. Therefore

`boxed: the completed direct ridge theorem has no certificate at any gamma or q on this physical cross block.`  (5.1)

Thus this matrix sits exactly on the strict fractional-volume support wall and simultaneously outside the direct ridge gate.

## 6. Partner r32 gives a strong product-space estimate anyway

Apply account03/B04 r32 to this actual inequality. The cross block has exact rank three and

`D=product sigma_j=8`.

The right singular frame can be chosen as the physical identity on the three-coordinate `J` bank, so its projected joint density is the original product density and has cap

`M_Y<=1`.

On the four-coordinate left bank, the three-dimensional orthogonal product marginal has cap

`M_X<=2^(3/2)`.

The parameterized partner inequality therefore gives

`||p_Q||_infinity
 <= 3 (2^(3/2))^(1/3) 8^(-1/3)
 = 3 sqrt(2)/2
 = 2.121320343559642... .`                                      (6.1)

The coarser symmetric product-marginal substitution would give `3`; (6.1) uses the actual physical dimensions and is stronger.

## 7. A dense genuinely rotated indefinite target matrix

To make the same-matrix example physically dense, include nonzero same-bank curvature:

`A_* = [[J_4/10, M],
        [M^T,    J_3/10]]`,                                     (7.1)

where `J_k` is the all-ones `k x k` matrix. Every entry of `A_*` is nonzero. It is not diagonal in the independent coordinates, and both source banks carry self-quadratic curvature.

Let

`A_0=[[0,M],[M^T,0]]`.

Because the singular values of `M` are all two,

`spec(A_0)={2,2,2,-2,-2,-2,0}`.

The perturbation

`A_*-A_0=diag(J_4/10,J_3/10)`

has operator norm `max(4/10,3/10)=2/5`. Weyl's inequality therefore leaves three positive and three negative eigenvalues with modulus at least

`2-2/5=8/5>1`.

Hence `A_*` is genuinely rotated, indefinite, and satisfies the exact target hypothesis with six eigenvalues of modulus at least one. The partner theorem permits the two arbitrary same-bank quadratic blocks, so for every admissible independent cap-one product law,

`boxed: ||p_{X^T A_* X}||_infinity <= 3 sqrt(2)/2 < 2.122.`        (7.2)

The partner Fourier estimate also supplies a continuous density for this displayed family. No continuity claim is made for the unrestricted conjecture.

A finite exact/numerical check gives the eigenvalues of (7.1) as approximately

`(-2,-2,-1.85561711,0.4,2,2,2.15561711)`,

consistent with the rigorous Weyl certificate; the proof uses only the rigorous `8/5` bound.

## 8. Proof-map consequence

On one target-valid dense rotated indefinite matrix:

- the globally optimized physical third-volume support threshold is exactly `h_*=3/4`, so pinned e5 D and strict D' have **no admissible weighting**;
- the direct ridge gate fails at **every** regularization scale and exponent;
- exact-rank-three product Plancherel gives `||p||_infinity <=3 sqrt(2)/2`.

Thus the routing rule “fractional third-volume or direct ridge” is not exhaustive. The missing complementary mechanism is exactly the product-space exact-rank theorem, and Theorem 3.1 shows it removes the entire **exact** support-defect branch rather than merely this example.

The genuinely unpaid branch is now quantitative: support-feasible cross blocks for which every admissible entropy-balanced third-volume law has too little determinant currency. Account03/B04 r31 compresses that failure into a bounded compound hub, while r32 pays retained patterns of exact rank three. What remains is to handle the retained rank `>=4` patterns without paying the product of arbitrarily small extra singular values.

## 9. Finite checks

Exact symbolic checks used only rational matrices:

- `U^T U=I_3`;
- each of the four 3x3 determinants of `M` has square `16`;
- `E3(M)=64`;
- `spec([[0,M],[M^T,0]])={2^3,-2^3,0}`;
- `6*4^(1/6)=7.559526299369239...`;
- `3 sqrt(2)/2=2.1213203435596424...`.

These arithmetic checks support, but do not replace, the proofs above.
