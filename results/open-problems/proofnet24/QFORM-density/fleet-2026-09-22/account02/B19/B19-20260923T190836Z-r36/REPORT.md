SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B19, 2026-09-23T19:08:36Z.
attacking: the finite-core physical rank-two Frobenius collar left by account03/B19 r38, by extracting a third literal leaf row when the light self-curvature leaves the anchored cross plane, and classifying the exact zero-height endpoint.

# account02/B19 r36 — leaf-transverse compiler and exact common-plane endpoint

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Universal proof assembly / SYNTHESIS / complementary constructions  
Status: **ESSENTIAL STEP APPLIED; full QFORM remains OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**.

## 1. Fresh frontier and correction boundary

The current owner continuation remains `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` under OWNER CONTROL revision `2026-09-22.15`; the unrestricted target is still open. The current account02/B20 login is healthy, so this B19 run performs no keeper or scheduler mutation.

The newest completed designated partner available at the mathematical start of this argument is account03/B19 r38,

`yspennstate/math-open-problems@f09b670173440c4c511985c9a89baf38f97e82c1`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T183023Z-account03-B19-QFORM-r38/REPORT.md`.

In the account01/B20 finite-core branch it starts from an original-coordinate heavy bank `H`, light bank `L=H^c`,

`|H| <= 124`, `C=A[H,L]`, `s_1(C)s_2(C)>1/480`,

and after the physical third-volume exit it has `s_3(C)<1/64`. Its theorem chooses two literal physical rows `T={a,b} subset H` such that, with

`M=C[T,L]`, `S=sqrt(det(MM^T))`,

`S > S_0 := 1/(480 sqrt(7626)) = 2.3856699607...*10^(-5)`.            (1.1)

Writing `Pi` for the projection onto `row(M)`, r38 pays the branch

`||C[H\T,L](I-Pi)||_F >= 1/64`

by a continuous density bound `<743`. Thus its still-unpaid rank-two packet lies in the two-row anchored Frobenius collar

`||C[H\T,L](I-Pi)||_F < 1/64`.                                    (1.2)

This run does not delete the small tail (1.2). Instead, for the next analytic test it conditions on the coordinates `H\T`. That is product-safe and turns every term containing those coordinates into affine data, while leaving two literal cap-one hub coordinates `X_T` and the whole product bank `X_L`. The conditional quadratic part is therefore

`Q_T(x_T,x_L)=x_T^T B x_T + 2 x_T^T M x_L + x_L^T D x_L + affine`, (1.3)

where `B=A[T,T]` and `D=A[L,L]`. The estimates below are uniform in all affine terms and hence survive averaging over the conditioned coordinates.

The live corrections are respected throughout: no independence after rotation, no arbitrary-joint coarea theorem, no uniform pointwise quadratic-phase decay, no worst conditional-density supremum, no moment/support assumption, and no deletion of a small coefficient as a small random perturbation.

## 2. A literal leaf-transverse third-row compiler

Let `m_i in R^2` denote column `i` of `M`, and put

`G=MM^T`, `ell_i=m_i^T G^{-1}m_i`.                               (2.1)

These are the normalized column leverages of the physical two-row cross block. They satisfy

`0<=ell_i<=1`, `sum_i ell_i=2`.                                  (2.2)

For `ell_i<1`, deletion of column `i` leaves rank two. Write

`M_{-i}=M[:,L\{i}]`,
`P_i=projection onto row(M_{-i}) in R^{L\{i}}`,
`r_i=||D[i,L\{i}](I-P_i)||_2`.                                  (2.3)

### Theorem 2.1 — `QFORM-TWOHUB-LEAF-TRANSVERSE-COMPILER-v1`

For every `i` with `ell_i<1` and `r_i>0`, the full ambient quadratic law has a continuous `C_0` density and

`boxed: ||p_Q||_infinity <= 3 sqrt(2) [S sqrt(1-ell_i) r_i]^(-1/3).` (2.4)

All same-bank curvature on both sides, all affine terms, the conditioned collar tail, and all extra spectrum are retained.

#### Proof

The matrix determinant lemma applied to `G-m_i m_i^T` gives the exact deletion identity

`det(M_{-i}M_{-i}^T)=det(G)(1-m_i^T G^{-1}m_i)
                    =S^2(1-ell_i)`.                              (2.5)

Now consider the **literal physical** crossing block from the three source coordinates `T union {i}` to the receiver bank `J=L\{i}`:

`B_i=A[T union {i},J]
    = [ M_{-i} ; D[i,J] ]`.                                      (2.6)

The third row has perpendicular height `r_i` over `row(M_{-i})`. Hence the base-times-height Gram identity gives

`det(B_i B_i^T)
 = det(M_{-i}M_{-i}^T) r_i^2
 = S^2(1-ell_i) r_i^2`.                                          (2.7)

Thus `B_i` has exact rank three and the product of its three nonzero singular values is

`Sigma_i=S sqrt(1-ell_i) r_i`.                                   (2.8)

Condition on all original coordinates outside `(T union {i}) union J` (there are none in `L`, and the already-conditioned `H\T` only changes affine terms). The source side consists of exactly three independent original coordinates, so after its orthogonal singular-vector rotation its three-dimensional density cap is `M_X<=1`. The receiver side is an orthogonal three-dimensional projection of an original-coordinate product law, whose density cap is `M_Y<=2^(3/2)`.

Apply the checked exact-rank crossing theorem in `NEW_PROJECTED_CROSSING.md`:

`||p_Q||_infinity <= 3 (M_X M_Y / Sigma_i)^(1/3)
                   <= 3 sqrt(2) Sigma_i^(-1/3)`,                  (2.9)

which is (2.4). The theorem gives Fourier integrability and therefore a continuous `C_0` density on this branch. QED.

### Numerical consequence in the live collar

Take the universal thresholds

`ell_i <= 3/4`, `r_i >= 1/64`.                                   (2.10)

Using (1.1),

`S sqrt(1-ell_i) r_i >= S_0/(128)`,

and (2.4) becomes

`boxed: ||p_Q||_infinity < 742.738818 < 743.`                     (2.11)

Therefore every survivor of both r38 and Theorem 2.1 obeys

`boxed: r_i<1/64 for every i with ell_i<=3/4.}`                   (2.12)

Since `sum ell_i=2`, at most two light coordinates can violate `ell_i<=3/4`. Hence the arbitrary light self-curvature in (1.3) has been reduced to a **rowwise common-plane collar outside at most two physical leaf coloops/heavy leaves**.

This is genuinely new information relative to (1.2): r38 controls transverse `H-to-L` crossing after two hub rows are selected, while (2.12) controls transverse `L-to-L` self-curvature relative to the same physical two-row plane.

## 3. Exact zero-height classification

The punctured estimate above identifies the correct exact endpoint algebraically.

### Theorem 3.1 — `QFORM-TWOHUB-EXACT-COMMONPLANE-CLASSIFICATION-v1`

Assume `M` has rank two and has **no exact coloop**, i.e. `ell_i<1` for every `i`. If

`r_i=0 for every i`,                                               (3.1)

then there exist a diagonal matrix `Delta` and a symmetric `2x2` matrix `K` such that

`boxed: D = Delta + M^T K M.`                                    (3.2)

#### Proof

Since `M_{-i}` has rank two and `r_i=0`, for each `i` there is a unique row vector `a_i in R^2` satisfying

`D_{ij}=a_i . m_j` for every `j!=i`.                              (3.3)

Let `A_0` be the matrix whose `i`-th row is `a_i`. Then `D-A_0M` is diagonal, because (3.3) matches every off-diagonal entry. Since `D` is symmetric, `A_0M` is symmetric as well:

`A_0M=M^T A_0^T`.                                                (3.4)

Put `N=M^T`, an `|L| x 2` full-column-rank matrix, and let `P_N` be projection onto `col(N)`. Left-multiplying (3.4) by `I-P_N` gives

`(I-P_N)A_0 M=0`.                                                (3.5)

Because `M` has full row rank, it has a right inverse, so (3.5) implies `(I-P_N)A_0=0`. Hence

`A_0=N K`                                                         (3.6)

for some `2x2` matrix `K`. Substituting into (3.4) gives

`N(K-K^T)N^T=0`; full column rank of `N` forces `K=K^T`. Therefore `A_0M=M^T K M`, proving (3.2). QED.

So in the exact no-coloop endpoint the entire light self-block is not arbitrary: modulo its physical diagonal it is rank at most two **in precisely the same two-dimensional coefficient plane as the hub crossing**.

If an exact coloop `ell_c=1` exists, the normalized Parseval-frame identity implies every other normalized column is orthogonal to the coloop direction; there can be at most two exact coloops. The row equations `r_i=0` for all non-coloops then leave only additional physical stars centred on those one or two coloop coordinates, plus a diagonal and the common-plane rank-two piece. Thus the exact exceptional set is finite-anchor/common-plane, not a new diffuse high-rank object. I do not claim a quantitative stability version of this final sentence here.

## 4. Two complementary endpoint facts

### 4.1 Pure two-hub star with arbitrary hub function is bounded

A useful positive endpoint, independent of any hub-block determinant, is the following.

Let `X=(X_1,X_2)` be two original independent cap-one variables, let `Y` be an independent original-coordinate product bank, let `M` be any rank-two `2xm` matrix with

`S=sqrt(det(MM^T))`,

and let

`Q=F(X)+2 X^T M Y + b^T Y + c`                                  (4.1)

for arbitrary measurable real `F` and arbitrary affine data. Then

`boxed: ||p_Q||_infinity <= sqrt(2 pi / S).}`                    (4.2)

Proof: for fixed `X=x`, the coefficient of the linear form in `Y` is `a(x)=2M^T x+b`. The scalar projection theorem for product cap-one laws gives conditional density cap `sqrt(2)/||a(x)||_2`. Decompose `b=b_parallel+b_perp`, choose `x_0` with `b_parallel=-2M^T x_0`, and write `G=MM^T`. Then

`||a(x)||^2 >=4 (x-x_0)^T G (x-x_0)`.                            (4.3)

Thus the conditional cap is at most

`1/[sqrt(2) |G^(1/2)(x-x_0)|]`.                                 (4.4)

The joint density of the two physical hubs is at most one. Under `u=G^(1/2)(x-x_0)`, its pushforward density is at most `1/S`. By the bathtub principle for the radially decreasing kernel `1/|u|`, among all probability densities bounded by `1/S` the largest integral is attained by the disk of area `S`; hence

`E |G^(1/2)(X-x_0)|^(-1) <=2 sqrt(pi/S)`.                        (4.5)

Averaging (4.4) gives (4.2). This proves existence of an essentially bounded density; continuity is not asserted from this argument.

At the live lower area `S_0`, (4.2) gives `<513.198`. Thus a nonzero or indefinite physical `2x2` hub block is **not itself** an obstruction when the light bank is purely linear; the unresolved endpoint requires curvature on both sides of the common two-plane (or the diagonal/tail/external third source).

### 4.2 Why the common-plane packet alone cannot be declared bounded

There is a source-valid rank-two logarithmic obstruction. Let `X_1,X_2,Y_1,Y_2` be independent `Uniform[-1/2,1/2]`, and let

`K=diag(1,-1)`, `M=I_2`,

`Q=X^T K X + 2 X^T Y + Y^T K Y
  =(X_1+Y_1)^2-(Y_2-X_2)^2`.                                    (4.6)

The matrix is exactly common-plane and has nonzero spectrum `{2,-2}`. The two variables

`U=X_1+Y_1`, `V=Y_2-X_2`

are independent and have triangular densities positive at zero. Hence the density of `U^2-V^2=(U-V)(U+V)` grows logarithmically as the level tends to zero and has infinite essential supremum. Concretely, in coordinates `a=U-V`, `b=U+V`, the joint density is bounded below on a neighbourhood of the origin, and the product-density formula contains

`int_{|q|/delta < |a| < delta} da/|a| ~ log(delta^2/|q|)`.        (4.7)

This is **not** a QFORM counterexample: the matrix has only two large eigenvalues. It proves, however, that no closure theorem may spend only the two-dimensional common-plane packet while allowing arbitrary same-plane curvature on both banks. The full target's genuinely third spectral resource must be located and spent jointly.

## 5. Required owner-source theorem applied at an equation

The requested source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` was reread (`RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, `COUNTEREXAMPLE_SEARCH.md`). A direct application of its proved **Theorem H** is available inside the exact collar:

if after conditioning to (1.3) the light block `D` is diagonal and every normalized cross leverage satisfies

`ell_i<=1/2`,                                                     (5.1)

then Theorem H with two physical hubs and no Fresnel square (`|H|=2,r=0`) gives

`|phi_Q(t)| <= 4 pi^2 S^(-1) |t|^(-2)`.                         (5.2)

Integrating `min(1,4 pi^2 S^(-1)t^(-2))` yields

`boxed: ||p_Q||_infinity <= 4 S^(-1/2).}`                        (5.3)

Using (1.1),

`boxed: ||p_Q||_infinity <818.946.}`                             (5.4)

This retains an arbitrary physical hub block `B` and arbitrary affine terms. It is an actual payment, not a citation-only use of the owner-required source.

As a separate already-paid high-rank exit from the same source, D5 says that any genuine physical cross block `N` with `s_5(N)>=1/64` has

`e_5(N^TN)>=64^(-10)` and therefore
`||p_Q||_infinity <=320 sqrt(2e)=746.126074...`.                 (5.5)

The present collar analysis is needed only after such fifth-volume exits have failed.

## 6. Updated proof graph and first unpaid gate

A compact compatible graph through the current finite-core branch is now:

1. Account01/B20 isolates the rank-`<=5` finite core, pays physical `s_3(A[H,L])>=1/64`, and leaves rank-one, rank-two, or two-light-bank strong-mode packets.
2. Account03/B19 r38 pays the rank-two packet whenever the selected two-row span has transverse `H-to-L` Frobenius residual at least `1/64`, leaving the literal two-row collar (1.1)-(1.2).
3. **This run conditions the already-small `H\T` tail rather than deleting it and pays every light coordinate whose self-row leaves the cross plane by the quantitative amount (2.4).** At the universal thresholds (2.10) that payment is again `<743`.
4. Hence, outside at most two high-leverage/coloop leaves, the surviving light self-curvature lies in a rowwise `1/64` common-plane collar. At exact zero height and with no coloop, it is exactly `diagonal + M^T K M` by Theorem 3.1.
5. The diffuse diagonal subendpoint (5.1) is paid by Theorem H; the purely linear light endpoint is paid by (4.2). The rank-two logarithmic example (4.6) proves that arbitrary two-sided common-plane curvature cannot be paid without the third spectral resource.

The first compatible unpaid implication is therefore sharpened to

`QFORM-FINITECORE-COMMONPLANE-THIRD-SOURCE-PAYMENT-v1`:

> In the finite-core two-row collar with `S>S_0`, after the leaf-transverse exits (2.4), spend the full target's third large spectral resource in the rowwise common-plane/at-most-two-coloop state, while retaining arbitrary diagonal light twists, arbitrary physical hub curvature, the conditioned affine data, the nonzero original Frobenius tail, the full operator residual, and all extra spectrum. Equivalently, either force a quantitative projected crossing/physical pivot already paid above, or prove a product-preserving receiver for the common-plane packet plus the actual third carrier.

The rank-two logarithmic model (4.6) shows why the words “plus the actual third carrier” cannot be removed.

The parallel account01/B20 rank-one tube and two-light-bank strong-mode branches remain separate gates. Arbitrary-extra-spectrum closure outside the finite-core compiler and global continuity also remain open. No full-proof claim is made, and there are not two independent end-to-end reviews.
