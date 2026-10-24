SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B12, 2026-09-23T00:55:56Z.
attacking: operator-norm stability of the two-large-directions plus collective-tail volume certificate, its exact minimax reserve, and a target-class obstruction to treating raw collective tail energy as stable under an arbitrary small high-rank tail.

# Thresholded collective-tail stability and its sharp operator-norm obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260923T005556Z-account02-B12-qform`.
Status: `PROVED_SUPPORTING_THEOREMS / PROVED_INTERMEDIATE_OBSTRUCTION / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and first unpaid implication

The full target remains OPEN: for arbitrary independent real `X_i` with probability densities bounded by one, and every real symmetric `A` having at least three eigenvalues of absolute value at least one, prove a universal essential density bound for `X^T A X`, or give a genuine counterexample.

This run proves a genuinely dimension-free way to stabilize the newest collective-tail cross-block certificate against an arbitrary high-rank operator-norm perturbation. The key is that the stable quantity is **not** the raw collective tail energy `T2`; it is a thresholded tail reserve which is exactly the minimax amount of `T2` that survives an operator-norm ball. The run also gives an exact QFORM target-class family showing that raw `T2`, and even the full third-volume `E3`, can collapse from order one to zero under perturbations whose operator norm tends to zero as dimension grows.

The first unpaid implication after the results below is therefore:

> In the remaining no-pivot / low-reserve class, force either a thresholded collective-tail reserve at a useful original-coordinate cut, a protected weighted determinant packet, or a physical/grouped star-pair mechanism, **before** paying reciprocal local curvature. Operator-norm smallness alone cannot preserve a collective-tail certificate when its energy is spread over singular values at the perturbation scale.

No step below treats a small matrix as a uniformly small random quadratic perturbation, and no rotated coordinates are declared independent.

## 2. Source pins actually used

### 2.1 Required newest-Claude package

Read all three required files at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`:

- `RESULTS.md`;
- `FOURIER_ROUTE_REPORT.md`;
- `COUNTEREXAMPLE_SEARCH.md`.

The completed result used at an equation below is the three-volume decoupling theorem D/D'.  For an ORIGINAL-coordinate cross block `M=A[I,J]`, if the three-volume row marginals satisfy `alpha_i<=h<3/4`, then

`||p_Q||_infinity <= 6 sqrt(e) (2h)^(-1/2) (3-4h)^(-1) E3(M^T M)^(-1/6)`       (2.1)

for `h>=1/2`, with the `h<=1/2` endpoint `6 sqrt(e) E3^(-1/6)`.  All self blocks, outside couplings, and affine terms are retained.  This is the main completed Claude result applied here.

### 2.2 Current volume-stability extension

The later source

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`

at

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/`

contains `REPORT.md` and `PEER_TAIL_EXTENSION.md`.  It records the exact three-volume marginal matrix, the inequality `T2 E2<=3E3`, and the sharper q-dependent Fourier coefficient

`3e/[(3-2q)sqrt(q)]`                                                   (2.2)

when `alpha_i<=q/2`, `1<=q<3/2`.  The proof is supplied there; independent review was still pending at this run.  I rederive the matrix part needed below, so the main stability statement also has the older completed D' coefficient (2.1) available independently of the sharper constant.

### 2.3 Fresh designated partner account03/B12

Fresh partner memory resolved to run `20260923T004313Z-qform-eigenvalue-r21`, canonical mathematics

`yspennstate/math-open-problems@dd754a0bfed889fd29c931b7112c8c3285fc83e8`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260923T004313Z-qform-eigenvalue-r21/REPORT.md`.

Two completed partner statements are applied below:

1. physical Schur elimination loses at most the pivot dimension from the count of eigenvalues above a fixed absolute threshold, with **no scale shrinkage**;
2. if a physical scalar completion has Schur remainder density cap `M`, then the full form obeys

`||p_Q||_infinity <= 4 sqrt(M/|a|)`.                                  (2.3)

The latter is dependence-safe and is not an independent-convolution assertion.

## 3. Deterministic minimax theorem for the collective tail

For a real rectangular matrix `M`, write its singular values as

`s_1(M)>=s_2(M)>=s_3(M)>=...>=0`,

and define

`T2(M)=sum_(j>=3) s_j(M)^2`.                                          (3.1)

This is the squared Frobenius distance from `M` to the rank-at-most-two matrices.

### Theorem 3.1 (`QFORM-TAIL-RESERVE-MINIMAX-v1`)

Let `M0` have singular values `sigma_j=s_j(M0)`.  For every `rho>=0`, define

`B_rho(M0)^2 = sum_(j>=3) (sigma_j-rho)_+^2`.                         (3.2)

Then

`inf_{||R||op<=rho} T2(M0+R) = B_rho(M0)^2`.                         (3.3)

Thus (3.2) is not merely a convenient perturbative lower bound: it is the **exact worst-case amount of collective tail energy that survives an arbitrary operator-norm perturbation of radius rho**.

#### Proof

For every `j`, singular-value Weyl gives

`s_j(M0+R) >= (sigma_j-||R||op)_+ >= (sigma_j-rho)_+`.

Squaring and summing over `j>=3` gives

`T2(M0+R)>=B_rho(M0)^2`.                                              (3.4)

For the reverse inequality, take an SVD

`M0=U diag(sigma_1,sigma_2,sigma_3,...) V^T`

and choose

`R_*=-U diag(0,0,min(rho,sigma_3),min(rho,sigma_4),...) V^T`.

Then `||R_*||op<=rho`, the first two singular values are unchanged, and all later diagonal singular values become exactly `(sigma_j-rho)_+`.  They remain below `sigma_2`, so no reordering affects the top-two/tail split.  Hence

`T2(M0+R_*)=B_rho(M0)^2`.

Together with (3.4) this proves (3.3). QED.

### Consequence

Any dimension-free theorem that tries to stabilize the collective-tail method under only `T2(M0)` and `||R||op` is missing the relevant information.  If many baseline tail singular values sit near `rho`, a single operator-norm-`rho` perturbation can lower all of them simultaneously.  The correct deterministic reserve is (3.2).

## 4. Three-volume marginal control from a protected row projection

The next lemma is the bridge from the minimax reserve to the required Claude D' theorem.

Let `M` have squared singular values

`lambda_j=s_j(M)^2`.

Put

`E2=e_2(lambda)`, `E3=e_3(lambda)`, `T2=sum_(j>=3)lambda_j`.

Volume-sample its nonzero `3x3` minors with weights proportional to their squared determinants, and let `alpha_i` be the row inclusion probability.  If

`M=U diag(s_j) V^T`,

the exact volume-marginal formula is

`alpha_i = [U diag(p_j) U^T]_ii`,

where

`p_j=lambda_j e_2(lambda without j)/E3`.                             (4.1)

Write

`W=U diag(p_j)U^T`.

### Lemma 4.1

For every orthogonal projection `P` on the row-index space, with

`ell_i=P_ii`, `epsilon=||(I-P)M||op`,

one has

`sqrt(alpha_i) <= sqrt(ell_i) + sqrt(3) epsilon/sqrt(T2) sqrt(1-ell_i)`  (4.2)

whenever `T2>0`.

#### Proof

First `0<=W<=I`, because

`E3=lambda_j e_2(lambda without j)+e_3(lambda without j)`

implies `0<=p_j<=1`.

Also `e_2(lambda without j)<=E2`, so from (4.1)

`W <= (E2/E3) M M^T`.                                                (4.3)

Now

`3E3 = sum_(p<q) lambda_p lambda_q sum_(r notin {p,q}) lambda_r`.

For every pair `p<q`, the inner sum is at least `T2=sum_(r>=3)lambda_r`: if `{p,q}={1,2}` this is equality; if one or both indices lie in the tail, replacing the removed tail eigenvalues by the larger omitted leading eigenvalues can only increase the sum.  Therefore

`T2 E2 <= 3E3`.                                                       (4.4)

Combining (4.3)-(4.4),

`W <= 3 M M^T/T2`.                                                    (4.5)

Finally

`sqrt(alpha_i)=||W^(1/2)e_i||
 <=||W^(1/2)Pe_i||+||W^(1/2)(I-P)e_i||`.

The first term is at most `||Pe_i||=sqrt(ell_i)` by `W<=I`.  By (4.5), the second is at most

`sqrt(3/T2)||M^T(I-P)e_i||
 <=sqrt(3) epsilon/sqrt(T2) sqrt(1-ell_i)`.

This is (4.2). QED.

## 5. Main stability theorem: thresholded collective tail under arbitrary small dense tails

### Theorem 5.1 (`QFORM-THRESHOLDED-COLLECTIVE-TAIL-STABILITY-v1`)

Let `A0` be any real symmetric matrix and let `I,J` be disjoint sets of ORIGINAL coordinates.  Put

`M0=A0[I,J]`, `a=s_2(M0)>0`.

Fix an orthogonal projection `P` on the I-row space such that

`max_i P_ii <= 1/2`,                                                  (5.1)

and set

`epsilon0=||(I-P)M0||op`.                                            (5.2)

Let the actual final symmetric matrix be

`A=A0+DeltaA`,

and write

`R=DeltaA[I,J]`, `rho=||R||op`.                                      (5.3)

Define the exact tail reserve

`B=B_rho(M0)
  =[sum_(j>=3)(s_j(M0)-rho)_+^2]^(1/2)`.                            (5.4)

Assume

`rho<a`, `B>0`.                                                       (5.5)

Put

`theta=(epsilon0+rho)/B`.                                            (5.6)

If

`theta < theta_* := (sqrt(3/2)-1)/sqrt(3)
                  =0.1297565119969...`,                              (5.7)

then the full final quadratic form, with arbitrary self blocks, arbitrary outside couplings and arbitrary affine terms, has a bounded continuous density.  More precisely, let

`h_theta=(1+sqrt(3)theta)^2/2 <3/4`.                                 (5.8)

The completed required-source D' theorem gives

`||p_Q||infinity
 <= C_D(theta) (a-rho)^(-2/3) B^(-1/3)`,                             (5.9)

where

`C_D(theta)
 =6sqrt(e)/[(1+sqrt(3)theta){3-2(1+sqrt(3)theta)^2}]`.               (5.10)

Using the sharper q-dependent coefficient in the current volume-stability package improves this to

`||p_Q||infinity
 <= C_sharp(theta) (a-rho)^(-2/3) B^(-1/3)`,                         (5.11)

with

`C_sharp(theta)
 =3e/[(1+sqrt(3)theta){3-2(1+sqrt(3)theta)^2}]`.                     (5.12)

The older D' coefficient (5.10) is the source-pinned completed result from the owner-required `e5f71d...` package, so the theorem has a valid completed-source version even if one withholds the sharper pending-review constant (5.12).

#### Proof

Let `M=A[I,J]=M0+R`.  By Theorem 3.1 / Weyl,

`s_1(M)>=a-rho`, `s_2(M)>=a-rho`, and `T2(M)>=B^2`.                  (5.13)

Also

`||(I-P)M||op <= epsilon0+rho = theta B
              <= theta sqrt(T2(M))`.                                (5.14)

Apply Lemma 4.1 to the **actual final cross block** `M`.  Since `P_ii<=1/2`, the function

`sqrt(x)+sqrt(3)theta sqrt(1-x)`

is increasing on `0<=x<=1/2` throughout the range (5.7).  Therefore every final three-volume row marginal satisfies

`sqrt(alpha_i)
 <=(1+sqrt(3)theta)/sqrt(2)`,

hence

`alpha_i<=h_theta<3/4`.                                               (5.15)

This verifies the marginal gate that cannot merely be assumed stable.

Now apply the owner-required completed D' theorem (2.1) to the actual final matrix.  Its three-volume is

`E3(M^T M)
 >=s_1(M)^2 s_2(M)^2 sum_(j>=3)s_j(M)^2
 >=(a-rho)^4 B^2`,                                                   (5.16)

because the subset of `E3` consisting of triples `{1,2,j}`, `j>=3`, is exactly the first product in (5.16).  Substitute (5.15)-(5.16) into D' to obtain (5.9)-(5.10).

For (5.11), choose in the sharper source theorem

`q=2h_theta=(1+sqrt(3)theta)^2`,

which lies in `[1,3/2)` by (5.7).  Its coefficient (2.2) becomes exactly (5.12), while the same lower bound (5.16) applies. QED.

### Simple numerical corollary

If

`theta<=1/15`,                                                       (5.17)

then the sharper coefficient in (5.12) is at most

`14.29394117441255...`,                                              (5.18)

because the denominator `x(3-2x^2)` decreases for `x>=1` and `x=1+sqrt(3)theta`.  Thus

`||p_Q||infinity
 <=14.294 (a-rho)^(-2/3)B^(-1/3)`.                                  (5.19)

The completed-source D' coefficient under the same `theta<=1/15` gate is at most

`17.33942714082004...`.                                              (5.20)

## 6. Arbitrary-rank dense tails and arbitrarily large signed spectral additions

The theorem is local to the final ORIGINAL-coordinate cross block, so it gives the required B12 perturbation control without saying that a quadratic random error is small.

Suppose

`DeltaA=T+L`,                                                        (6.1)

where `T` is any symmetric matrix of arbitrary rank and signs with

`||T||op<=delta`,                                                    (6.2)

and

`L=sum_r tau_r v_r v_r^T`                                           (6.3)

is any signed spectral addition, with orthonormal `v_r` and completely unrestricted `tau_r`.  Then compression and the rank-one operator norm give

`rho=||(T+L)[I,J]||op
 <=delta + eta_IJ(L)`,                                               (6.4)

where

`eta_IJ(L)
 :=sum_r |tau_r| ||(v_r)_I||_2 ||(v_r)_J||_2`.                       (6.5)

Thus Theorem 5.1 applies with any upper bound on the right side of (6.4).  The dense perturbation `T` may have full rank and arbitrary orientation.  The added spectral coefficients `tau_r` may be arbitrarily large and of either sign: they are charged only by their actual cross-bank footprint.  In particular, a spectral direction supported entirely away from one side of the protected cut costs zero, regardless of its magnitude.

If the `v_r` are eigenvectors of `A0` with eigenvalues `lambda_r`, choosing `tau_r=mu_r-lambda_r` literally replaces those eigenvalues by arbitrary real `mu_r`; the same bound remains valid whenever (6.4)-(6.5) keep the protected cross footprint inside the thresholded-reserve region.

This is the promised arbitrary smaller/larger-eigenvalue control in a nonseparable-tail regime.  It is a statement about the actual final matrix certificate, not about convolution with `X^T(T+L)X`.

## 7. Exact target-class obstruction: raw collective tail is not operator-norm stable

The minimax theorem permits a particularly sharp QFORM stress family.

Let `m` be a Hadamard order, put `N=m-2`, and let

`U=H_m/sqrt(m)`

be a normalized Sylvester Hadamard matrix.  Let

`d=N^(-1/2)`,

and write `P2` for the projection onto the first two columns of `U`.  Define

`M0=P2+d(I-P2)
   =U diag(1,1,d,...,d)U^T`.                                        (7.1)

Then

`s_1(M0)=s_2(M0)=1`,

and

`T2(M0)=N d^2=1`.                                                    (7.2)

Moreover, the third-volume satisfies

`E3(M0^T M0)>=s_1^2 s_2^2 T2=1`.                                  (7.3)

Because every entry of every Hadamard singular vector has squared modulus `1/m`, the exact marginal formula (4.1) gives

`alpha_i=(1/m) sum_j p_j=3/m`.                                      (7.4)

Hence for `m>=8` the original completed Theorem D already applies to the baseline cross block and gives the genuine inequality

`||p_(X^T A0 X)||infinity <=6sqrt(e) E3^(-1/6)<=6sqrt(e)`            (7.5)

for the symmetric block form

`A0=[[0,M0],[M0,0]]`,                                                (7.6)

and in fact for arbitrary self-block completion sharing this cross block.

Now add

`R=-d(I-P2)`,                                                        (7.7)

so

`||R||op=d=N^(-1/2)->0`,                                            (7.8)

but

`M=M0+R=P2`                                                         (7.9)

has rank exactly two.  Therefore

`T2(M)=0`, `E3(M^T M)=0`.                                           (7.10)

Embed the perturbation symmetrically:

`DeltaA=[[0,R],[R,0]]`.                                              (7.11)

Then

`||DeltaA||op=d->0`.                                                 (7.12)

Both before and after the perturbation the matrices lie in the exact QFORM spectral target.  Indeed the eigenvalues of `[[0,M],[M,0]]` are plus/minus the singular values of `M`; the final matrix has

`spec(A)={1,1,-1,-1,0,...,0}`.                                      (7.13)

The final matrix is also in a strict no-pivot class.  Its diagonal entries are zero.  Same-side physical `2x2` principal determinants vanish, while for a cross-side pair

`det A[{i,m+j},{i,m+j}]=-M_ij^2`.

Since

`|M_ij|=|(P2)_ij|<=2/m`,

we have

`|det A_pair|<=4/m^2<1/64`                                          (7.14)

for every Hadamard order `m>=32`.  Thus (7.13)-(7.14) put the final matrix directly inside the live `N3(1/64)` type of target family.

### What this refutes

This is **not** a QFORM counterexample.  It is a counterexample to the stronger stability claim

> a cross block with order-one raw `T2` or order-one `E3` retains a useful three-volume certificate after every operator-norm perturbation whose norm tends to zero.

That claim is false even when both the baseline and final full symmetric matrices remain exact target matrices, and even when the final matrix is no-pivot.  The failure is dimensional: all `N` weak tail directions of size `d=N^(-1/2)` are cancelled simultaneously by one perturbation of norm `d`.

The thresholded reserve detects the failure exactly:

`B_d(M0)=0`.                                                         (7.15)

More generally Theorem 3.1 shows that no larger universal reserve can be inferred from the baseline singular values and the operator-norm radius alone.

## 8. Applying the fresh account03/B12 partner: scalar-pivot plus collective-tail hybrid

The fresh partner theorem says physical Schur elimination loses eigenvalue **count** but not threshold.  If a target matrix `A` with at least three eigenvalues `|lambda|>=1` has a nonzero physical scalar pivot `a0=A_kk`, then its physical Schur complement `S` has at least two eigenvalues of modulus at least one.  This is a real target-level inheritance statement, not merely a citation.

Suppose additionally that this actual Schur remainder has a cross block fitting Theorem 5.1, with resulting density cap

`D_R=C(theta)(a-rho)^(-2/3)B^(-1/3)`.                               (8.1)

Apply the partner's dependence-safe scalar-square completion inequality (2.3).  It gives

`||p_Q||infinity
 <=4 sqrt(C(theta)) |a0|^(-1/2)
      (a-rho)^(-1/3) B^(-1/6)`.                                     (8.2)

Using the sharper coefficient and the simple gate `theta<=1/15`, (5.18) yields the explicit inequality

`||p_Q||infinity
 <=15.12293155412008...
      |a0|^(-1/2)(a-rho)^(-1/3)B^(-1/6)`.                           (8.3)

Using only the older completed-source D' coefficient gives instead the still-valid constant

`16.65625510891091...`.                                              (8.4)

This is `QFORM-SCALAR-PIVOT-THRESHOLDED-TAIL-HYBRID-v1`: one physical eigenvalue can be peeled without shrinking the surviving unit spectral threshold, while the remainder is paid by a thresholded collective-tail cross certificate.  The completed square and the Schur remainder are dependent through the original variables; (2.3) is precisely the partner result that handles this, so no independent convolution is inserted.

This does not say that every N3 matrix has such a scalar pivot/cross certificate.  In the strict no-pivot regime the scalar factor in (8.2) can itself be too small, which is why grouped pair/star routes remain necessary.

## 9. Relation to the fresh account03/B12 local-footprint theorem

The earlier partner run `20260922T234350Z-qform-eigenvalue-r20` proves stability of a protected physical triple or a protected weighted determinant packet under an arbitrary local perturbation footprint.  Theorem 5.1 is complementary rather than redundant:

- the protected-packet theorem starts from individual supported `3x3` minor gaps;
- Theorem 5.1 permits every individual tail singular value to be small and uses their **thresholded collective reserve**;
- The obstruction in Section 7 shows why the latter reserve cannot be replaced by raw `T2` under an operator-norm perturbation.

Hence a useful hybrid proof map is now: protected physical triple / weighted packet; otherwise thresholded diffuse collective tail; otherwise low-reserve or high-leverage star/bank geometry.

## 10. Why small matrix norm is still not a small quadratic random error

Nothing above estimates

`|X^T DeltaA X|`

by `||DeltaA||op` uniformly over the allowed laws.  Such an estimate is impossible without support or moment assumptions.  For example, for `DeltaA=delta e_1e_1^T` and `X_1` uniform on `[R,R+1]`, the density cap is one but

`X^T DeltaA X>=delta R^2`

almost surely.  The present method instead proves that a matrix-level certificate survives in the **actual final cross block**, using singular-value and marginal inequalities before invoking the product-law Fourier theorem.

## 11. What is and is not settled

**Proved in this run.** The thresholded tail reserve (3.2) is the exact minimax collective-tail energy under an operator-norm perturbation.  Combining that reserve with a fixed low-leverage row projection gives an explicit D' density bound for arbitrary high-rank dense perturbations and arbitrarily large signed low-footprint spectral additions.  The required `e5f71d...` D' theorem is applied at the inequality (5.9).  The latest partner account03/B12 scalar completion is applied at (8.2), and its threshold-preserving Schur theorem identifies the exact spectral inheritance after one pivot.  An exact Hadamard target family shows raw `T2`/`E3` certificate stability under small operator norm is false.

**Not proved.** The bare global condition `s_3(A)>=1` has not been shown to force the projection/reserve hypotheses of Theorem 5.1, nor a protected determinant packet, nor a usable physical pivot.  The general no-pivot statement N3 remains open.  Consequently the full QFORM conjecture remains OPEN / NOT PROVED / NOT DISPROVED.

**Next mathematical step.** In the low-reserve case `B_rho` small, the minimax theorem says the cross block is genuinely close, at the relevant operator scale, to rank two.  Combine that hard information with no-pivot entry bounds to force either (i) an aggregate physical-pair determinant budget that can be paid by the newest pair half-Riesz/square mechanisms, or (ii) a quantitatively singular star/grouped-bank structure.  The Section 7 family is the exact stress test: any claimed closure must remain uniform when a diffuse collective tail is cancelled all the way to a rank-two no-pivot target.

## 12. Source/control status

Fresh prepublication brain main was read after the early checkpoint; the owner control remained revision `2026-09-22.15`, QFORM remained the sole target, and the correction-inbox blob remained `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`.  No live correction used here conflicts with singular-value Weyl, volume marginals, the D' theorem, or the partner Schur/square-completion results.  Independent review of this run's new theorem has not yet occurred.

Execution context remains `WITHOUT_VERIFIED_BRAIN`: repository retrieval was used, but no authenticated native learned-memory retrieval plus receiver use occurred.
