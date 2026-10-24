SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B12, 2026-09-24T05:56:37.723323Z.
attacking: finite anti-accretive-index stability — convert the partner relative-resonance factorization into a five-mode criterion controlled by the Hermitian numerical range, then apply the source-pinned D5 theorem to an actual original-coordinate cross block after an arbitrary dense tail.

# account02/B12 — finite anti-accretive-index carrier stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control / complementary constructions  
Run: `20260924T055637Z-account02-B12-QFORM-auto11`  
Status: **PROVED SUPPORTING STABILITY THEOREM / FULL QFORM OPEN**  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and first unpaid implication

The owner target remains the unrestricted product-law problem: independent ORIGINAL coordinates with scalar densities bounded by one, and an arbitrary real symmetric coefficient matrix with at least three eigenvalues of modulus at least one. No moments, bounded support, connected support, log-concavity, iid assumption, diagonal-basis law, or post-rotation independence is used below. Continuity is stated only on branches whose receiver proves it.

The first unpaid implication is structural. From the bare condition `s_3(A)>=1`, one still has to force either a bounded ORIGINAL-coordinate carrier with at least five quantitatively non-antipodal *relative* directions, or an already-paid projected-crossing / grouped-bank / hub / ridge / physical-core / physical-pair / Schur / common-plane / Pluecker exit. Nothing below asserts that a universal carrier scale follows automatically from `s_3(A)>=1`.

The latest compatible designated partner is account03/B12 r50, canonical report `yspennstate/math-open-problems@e5c25693bac41b18a8258b6c76f5c7c41eac085b`, theorem `QFORM-RELATIVE-RESONANCE-DROP-STABILITY-v1`. It proves an exact orthogonal relative-action factorization and, for every singular index, a lower bound through `s_j(I+M^dagger E P)`. The present result compiles that mechanism into a criterion involving only the eigenvalue count of a symmetric whitened relative action. This does not improve the partner's exact identity; it supplies a new checkable sufficient condition that survives arbitrarily large skew and accretive action and can remain useful when a low-rank-plus-small-tail approximation is impossible.

The required source-pinned result is the completed fifth-volume theorem in `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `FOURIER_ROUTE_REPORT.md`: for an ACTUAL disjoint ORIGINAL-coordinate cross block `B=A[I,J]`,

`||p_(X^T A X)||_infinity <= 5 sqrt(2e) e_5(B^T B)^(-1/10)`

with no row-marginal condition. It keeps arbitrary same-bank quadratic terms, outside couplings and affine terms. I apply it below to a literal final cross block, not to spectral coordinates.

A live correction important for this application is `QFORM-BIINDEPENDENT-SPECTRAL-MODES-NOT-CROSS-VOLUME-v1`: common spectral independence on two sides does not imply a nonzero D5 volume. The example below therefore computes the actual physical cross singular values directly; no spectral-mode-to-cross-volume inference is used.

## 2. Relative numerical-range theorem

Let `H` be a literal ORIGINAL-coordinate bank of size `m`, and let

`P:R^m -> R^n`

be its coordinate embedding. Let `A_0=A_0^T` be a baseline matrix and put

`M=A_0 P`, `G=M^T M`, `g=s_m(M)>0`.

Let `S=S^T` be an arbitrary signed addition, with no rank, norm, sign, inertia, or spectral-orientation restriction, and put `N=SP`. Define the whitened relative action

`K = G^(-1/2) M^T N G^(-1/2)`

and its symmetric part

`H_K = Sym(K)=(K+K^T)/2`.

Write the eigenvalues of `H_K` decreasingly as

`mu_1 >= ... >= mu_m`.

### Theorem 2.1 — `QFORM-RELATIVE-NUMERICAL-RANGE-MODE-SHIELD-v1`

For every `j=1,...,m`,

`boxed: s_j((A_0+S)P) >= g [1+mu_j]_+.`                      (2.1)

If a further arbitrary symmetric dense tail `T` satisfies

`||T||op <= delta`,

then for `A=A_0+S+T`,

`boxed: s_j(A P) >= [ g [1+mu_j]_+ - delta ]_+.`              (2.2)

Equivalently, by symmetry,

`boxed: sqrt(lambda_j((A^2)[H,H])) >= [g[1+mu_j]_+-delta]_+.`  (2.3)

No probabilistic perturbation argument is used.

### Proof

Set

`U=M G^(-1/2)`.

Then `U^T U=I_m` and `Pi=UU^T` is the orthogonal projection onto `Ran(M)`. The in-range piece factors exactly as

`M+Pi N = U (I+K) G^(1/2)`.                                  (2.4)

The transverse piece

`Z=(I-Pi)N`

is orthogonal to `Ran(M)`, hence

`(M+N)^T(M+N)
 = G^(1/2)(I+K)^T(I+K)G^(1/2) + Z^T Z`.                       (2.5)

Since `G>=g^2 I`, singular-value product monotonicity and the positive term `Z^T Z` give

`s_j(M+N) >= g s_j(I+K)`.                                     (2.6)

This is the whitened version of the partner r50 relative-resonance factorization.

It remains to lower-bound `s_j(I+K)` without controlling `||K||`. Let `W_j` be the span of the top `j` eigenvectors of `H_K`. For every unit `x in W_j`,

`x^T(I+K)x = 1 + x^T H_K x >= 1+mu_j`.

When `1+mu_j>0`, Cauchy-Schwarz gives

`||(I+K)x|| >= |x^T(I+K)x| >= 1+mu_j`.

The max-min characterization of singular values therefore yields

`s_j(I+K) >= [1+mu_j]_+`.                                     (2.7)

Combining (2.6) and (2.7) proves (2.1). Finally

`||TP||op <= ||T||op <= delta`,

so singular-value Weyl gives (2.2). Since

`(AP)^T(AP)=P^T A^2 P=(A^2)[H,H]`,

(2.3) follows. QED.

## 3. Five-mode anti-accretive-index corollary

Take `m>=5`. Suppose for some `eta in (0,1]` that

`mu_5 >= -1+eta`.                                             (3.1)

Equivalently, at most `m-5` eigenvalues of the symmetric whitened relative action lie below `-1+eta`. Then after an arbitrary dense symmetric tail of norm at most `delta`,

`boxed: sqrt(lambda_5((A^2)[H,H])) >= [g eta-delta]_+.`        (3.2)

Thus as many as `m-5` relative directions may be completely anti-accretive or worse, while the remaining five need only stay a fixed distance from the antipodal value `-1`. Arbitrarily large skew-symmetric action is invisible to (3.1), and arbitrarily large positive/accretive action can only help.

Whenever

`r:=g eta-delta>0`,

the completed account03/B12 r47/r50 five-square-mode compiler applies directly to the final physical carrier and gives

`boxed:
 ||p_(X^T A X)||_infinity
 <= sqrt(24*pi*m+K3^2)/r,`                                    (3.3)

where

`K3=3*2^(4/3)*exp(1/3)`.

That receiver supplies a continuous `C_0(R)` density. All conditioning in that receiver is on ORIGINAL coordinates.

The structural obstruction has a useful contrapositive. If a baseline carrier of scale `g` is crushed below `epsilon g` before the dense tail, then (2.1) forces

`mu_5 < -1+epsilon`                                             (3.4)

whenever five-mode survival fails. So destruction of five quantitative carrier modes requires at least `m-4`? No: more precisely it requires the fifth-largest symmetric-relative eigenvalue to be near `-1`, i.e. fewer than five relative directions remain uniformly non-antipodal. Large packet norm alone is not the obstruction.

## 4. Why this differs from a low-rank-plus-small-tail budget

The partner r50 exact theorem is stronger when `s_5(I+M^dagger SP)` can itself be evaluated. Its finite-codimension corollary instead assumes

`M^dagger SP = K_0+F`, `rank(K_0)<=m-5`, `||F||op<1`.

The numerical-range criterion can succeed even when no such decomposition exists: a full or high-rank skew action may have large singular values but zero symmetric part. In particular, no small operator-norm residual need remain after spending `m-5` directions.

The theorem therefore identifies a different invariant: **anti-accretive relative index**, not numerical rank and not perturbation norm.

## 5. Exact hostile-spectrum family

Take two disjoint ORIGINAL-coordinate banks

`H={h_1,...,h_9}`, `J={j_1,...,j_9}`,

and on `H union J` let

`A_0 = [[0, 2 I_9], [2 I_9, 0]].`                              (5.1)

For the carrier `P=P_H`,

`M=A_0P=[0;2I_9]`, `G=4I_9`, `g=2`.

Let

`R=[[0,1],[-1,0]]`, `J_4=diag(R,R)`,

and for any `c>=2` define

`K_c=diag(-I_4, c J_4, 0)`.                                    (5.2)

Now add the symmetric signed packet

`S_c = [[0, 2 K_c^T], [2 K_c, 0]].`                            (5.3)

Because `G=4I`, the whitened relative action of `S_c` is exactly `K_c`. Its symmetric part is

`Sym(K_c)=diag(-I_4,0_4,0)`,                                   (5.4)

so

`mu_5=0`.

The theorem therefore gives

`boxed: s_5((A_0+S_c)P_H) >= 2`                                (5.5)

for every `c`, even as `c -> infinity`.

This is not a small addition. The symmetric matrix `S_c` has signed eigenvalues `+2c,-2c` on four large modes (and fixed signed modes coming from the `-I_4` block); its operator norm is `2c`. Thus the extra spectrum can become arbitrarily large in both signs.

The relative low-rank-plus-small-tail corollary cannot certify this family at its required strict threshold. The singular values of `K_c` are

`c,c,c,c,1,1,1,1,0`.

By Eckart-Young, after subtracting any rank-four matrix, the smallest possible operator-norm residual is

`s_5(K_c)=1`.

Hence there is no decomposition with `rank(K_0)<=4=m-5` and `||F||op<1`. The exact partner theorem still applies if one computes `s_5(I+K_c)` directly; the point is that the new numerical-range gate extracts this survival from a different, orientation-sensitive datum and does not require a rank-tail approximation.

In fact the physical cross block is explicit:

`B_c=(A_0+S_c)[H,J]=2(I_9+K_c^T)`.                             (5.6)

Its singular values are four copies of `2 sqrt(1+c^2)`, one copy of `2`, and four zeros. Therefore

`boxed: s_5(B_c)=2`                                             (5.7)

exactly for all `c>=2`.

## 6. Arbitrary spectator spectrum and arbitrary dense tail

Append an arbitrary-dimensional symmetric spectator block `Theta`, with arbitrary eigenvalue signs, multiplicities, magnitudes and internal mixing. It is a direct-sum completion and is not restricted in norm.

Now add **any globally dense symmetric** matrix `T_dense` satisfying

`||T_dense||op <= 1/64`.                                       (6.1)

The final actual ORIGINAL-coordinate cross block is

`B_final=A[H,J]`.

Physical compression cannot increase operator norm, hence

`||T_dense[H,J]||op <= 1/64`.

By singular-value Weyl and (5.7),

`boxed: s_5(B_final) >= 2-1/64 = 127/64.`                      (6.2)

This is the only use of dense-tail smallness in the D5 branch. No assertion is made that the random variable `X^T T_dense X` is small; on unbounded inputs that assertion would be false.

The source-pinned fifth-volume theorem now applies to the **actual final physical cross block**. Since

`e_5(B_final^T B_final) >= s_5(B_final)^10
                         >= (127/64)^10`,                      (6.3)

we get the required real inequality

`boxed:
 ||p_(X^T A X)||_infinity
 <= 5 sqrt(2e)/(127/64)
 = 5.875008457567557... .`                                     (6.4)

There is no row-marginal gate. Same-bank quadratic pieces, the spectator spectrum, outside couplings generated by the dense tail, and affine terms remain in the theorem's ambient form. This D5 branch also yields a continuous `C_0` representative by Fourier inversion.

The recent bi-independent-mode correction is respected: (6.3) is derived from the explicit final cross singular value (6.2), not from spectral independence or common modes.

## 7. Exact-target verification

Before `T_dense`, the eighteen-coordinate core has the symmetric off-diagonal form

`[[0,B_c],[B_c^T,0]]`.

Its nonzero eigenvalues are

`+s_1(B_c),..., +s_5(B_c), -s_1(B_c),..., -s_5(B_c)`.

By (5.7), all ten of these have modulus at least two. The arbitrary direct-sum spectator block cannot remove those singular directions. After the dense tail, Weyl gives

`s_10(A_final) >= 2-1/64 = 127/64 >1`.                         (7.1)

Because the final matrix is symmetric, its singular values are the absolute values of its eigenvalues. Hence every member of the family has at least three eigenvalues of modulus at least one. It lies literally in the owner's exact target class for every `c>=2`, every spectator `Theta`, and every allowed dense tail.

## 8. What this pays and what remains

This run removes another false source of instability: **large relative action is not destructive unless its symmetric numerical range approaches `-1` in enough directions.** Skew relative action can be arbitrarily large and full/high rank without consuming a five-mode carrier. Positive/accretive action is likewise free.

What remains unpaid is global extraction. Starting from only `s_3(A)>=1`, prove that either some bounded ORIGINAL-coordinate carrier has five relative directions satisfying a universal version of (3.1), or the near-antipodal failure geometry forces one of the already-paid projected-crossing, grouped-bank, hub, ridge, core, physical-pair, Schur, common-plane or Pluecker exits. The full QFORM conjecture is therefore still `OPEN / NOT PROVED / NOT DISPROVED`.

No rotation of the random vector is used; every probabilistic receiver acts on original product coordinates. No hidden support, moment, log-concavity or regularity hypothesis is introduced.
