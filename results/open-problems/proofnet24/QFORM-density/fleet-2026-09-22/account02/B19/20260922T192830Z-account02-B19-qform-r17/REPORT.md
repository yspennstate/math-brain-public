SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B19, 2026-09-22T19:28:30Z.
attacking: the O0 aligned-E2 / near-singular two-heavy splice by a different mechanism — pass through an exact scalar Schur complement, descend one exterior degree, and aggregate its full second compound before any reciprocal local-pair payment.

# account02/B19 — scalar-Schur second-compound reduction

**Run:** `20260922T192830Z-account02-B19-qform-r17`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly / SYNTHESIS  
**Latest owner control used before this report:** revision `2026-09-22.15`  
**Classification:** `ESSENTIAL_STEP_APPLIED` with a local `CANDIDATE_REFUTED`; **full target OPEN**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and correction discipline

The target is unchanged: for arbitrary independent real coordinates with one-dimensional densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite essential bound for the density of `Q=X^TAX`, or give a valid target counterexample.

This run uses no moment/support/log-concavity hypothesis, no post-rotation independence, no arbitrary-joint rank-three coarea cap, no positive conditional spectral-projection moment, no worst conditional spectral/core density supremum, and no inference of one good local minor from an aggregate determinant bank. The live corrections, including the failure of single-Schur rank-two local extraction and the same-square one-heavy-row shortcut, are retained.

The immediate incoming B19 debt was the aligned/near-singular O0 splice from r16. Instead of pushing the same aligned-E2 local selector again, this run changes mechanism: every genuine scalar pivot is converted into its exact physical Schur complement, then the **entire second compound** of that Schur complement is decomposed by physical overlap before any local reciprocal determinant is selected.

## 2. Source-pinned inputs actually used

1. **Current named partner account03/B19 r17.** Canonical mathematics `yspennstate/math-open-problems@9989e8640c2933ba54cd8de88723ac5c223be3b1`, report `proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260922T190100Z-account03-B19-QFORM-r17/REPORT.md`. It closes every O0 state with at least three `3/4`-heavy rows by an exact three-row cross-bank payment, with continuous density `<12 sqrt(e)<19.785`. Hence any unpaid O0 heavy-row branch has at most two such rows.

2. **Prior account02/B19 r16.** Canonical mathematics `yspennstate/math-open-problems@89a0197f2e9ed58383cdd516eedcc2ecd2145407`, report `proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260922T190733Z-account02-B19-qform-r16/REPORT.md`. It proves the two-heavy raw factor, exact Schur-projection inheritance, the R0 scalar `GOOD3/ALIGNED2` split, the R1 moderate-row/diffuse payment, and the definite physical-pair payment. Its first unpaid implication is the aligned/near-singular splice.

3. **account03/B03 determinant-bank half-Riesz theorem.** Canonical `yspennstate/math-open-problems@924b3c4c70f86a64402863fe228f641bf3db60b2`, report `proofnet24/QFORM-density/fleet-2026-09-22/account03/B03/20260922T175531Z-account03-B03-QFORM-r17/REPORT.md`. For a physical residual cross block `B`, if `E_2(B)=e_2(BB^T)>0` and one selected side has range leverage at most `1/2`, then

`H_(1/2)(R):=sup_y E|R-y|^(-1/2)
 <= 7.673759290384858 E_2(B)^(-1/8)`.                         (2.1)

It also proves the scalar-pivot transducer

`Q=a(X_i+h(Z))^2+R(Z)  =>  ||p_Q||_infinity<=|a|^(-1/2) H_(1/2)(R)`. (2.2)

4. **Newest compatible affine-hyperbolic fractional trace.** account01/B02, canonical `yspennstate/math-open-problems@960599513eef0d6048af1e0e1d279650d2d67e75`, report `proofnet24/QFORM-density/fleet-2026-09-22/account01/B02/20260922T192922Z-account01-B02-qform-auto11/REPORT.md`. If `R=2a XU+H(X,V)` with `X,U,V` on genuinely independent original-coordinate banks, cap-one `X`, cap-`M` `U`, and **no hidden U-curvature in H**, then

`H_(1/2)(R)<=4 sqrt(2) sqrt(M/|a|)`.                           (2.3)

I use (2.3) only as a paid subcase of the shared-overlap branch below; I do not extend it across the live same-square correction.

## 3. First new theorem: a scalar pivot preserves two large singular directions in the exact Schur residual

Permute a physical coordinate `i` first and write

`A = [[a, v^T],[v,C]],    a=A_ii !=0`,                         (3.1)

and let

`S=C-vv^T/a`                                                   (3.2)

be the exact Schur complement. Completing only the ORIGINAL coordinate `X_i` gives

`Q=a(X_i+a^(-1)v^T Z)^2+Z^T S Z`,                              (3.3)

where `Z` still consists of independent original coordinates.

### Theorem 3.1 — `QFORM-SCALAR-SCHUR-S2-INHERITANCE-v1`

If `s_3(A)>=1`, then

`boxed(s_2(S)>=1).`                                             (3.4)

Consequently

`boxed(e_2(SS^T)>=1).`                                          (3.5)

#### Proof

Set `D=diag(0,S)` and `w=(1,v/a)^T`. Then

`A=D+a w w^T`,                                                   (3.6)

so `rank(A-D)<=1`. The rank-one singular-value interlacing inequality gives

`s_3(A)<=s_2(D)=s_2(S)`.                                        (3.7)

This proves (3.4). Since `s_1(S)>=s_2(S)>=1`,

`e_2(SS^T)=sum_(p<q) s_p(S)^2 s_q(S)^2 >=s_1(S)^2s_2(S)^2>=1`. (3.8)

QED.

This is useful because it is magnitude-stable: no lower bound on `|a|`, no bound on `||v||`, and no local cross-rank assertion is required. The price of a small `|a|` appears only later in the scalar square transducer.

## 4. Main new theorem: second-compound physical-overlap reduction

For a symmetric matrix `S`, define its full second-compound mass

`M_2(S)=sum_{|I|=|J|=2} det S[I,J]^2
      = ||wedge^2 S||_F^2
      = e_2(SS^T).`                                             (4.1)

Partition it by overlap size

`M_r=sum_{|I|=|J|=2, |I intersect J|=r} det S[I,J]^2`,
`r=0,1,2`.                                                       (4.2)

Under (3.5), one of `M_0,M_1,M_2` is at least `1/3`.

### Theorem 4.1 — `QFORM-SCHUR-S2-OVERLAP-REDUCTION-v1`

For every exact scalar Schur complement `S` satisfying `s_2(S)>=1`, at least one of the following ORIGINAL-coordinate alternatives holds.

**S0 — disjoint two-volume bank.** There is a bipartition `L disjoint_union R` of the residual coordinates such that, for `B=S[L,R]`,

`boxed(E_2(B):=e_2(BB^T)>=1/48.)`                               (4.3)

**S1 — one-shared-coordinate bank.** There is a three-color partition `C0,L,R` such that

`boxed(sum_{k in C0} sum_{i in L} sum_{j in R}
 det S[{k,i},{k,j}]^2 >=1/81.)`                                 (4.4)

**S2 — principal-pair determinant bank.** One has

`boxed(sum_{i<j} det S[{i,j},{i,j}]^2 >=1/3.)`                  (4.5)

#### Proof

If `M_0>=1/3`, independently color every residual coordinate `L/R` with probability `1/2`. Every ordered disjoint pair of 2-sets `(I,J)` lands with `I subset L, J subset R` with probability `2^-4=1/16`. Therefore

`E E_2(S[L,R])=M_0/16>=1/48`,                                   (4.6)

and some deterministic bipartition satisfies (4.3).

If `M_1>=1/3`, independently color every coordinate `C0,L,R` with probability `1/3`. For an ordered pair `I={k,i}`, `J={k,j}` with unique shared coordinate `k`, the event `k in C0,i in L,j in R` has probability `3^-3=1/27`. Hence some partition satisfies (4.4).

If `M_2>=1/3`, then `I=J` and (4.5) is exactly that class. QED.

This reduction is the one-degree-lower analogue of the full third-compound O0/O1/O2/O3 decomposition. It is performed **after** the scalar Schur completion, so it directly attacks the object needed by the half-Riesz transducer and does not pretend that a projected raw bank is already physical.

## 5. Immediate target-level payment of the diffuse S0 branch

Assume S0 and suppose one side of the physical cross block `B=S[L,R]` has maximum range leverage at most `1/2`. Apply the account03/B03 theorem (2.1):

`H_(1/2)(Z^T S Z)
 <=7.673759290384858 * 48^(1/8)
 =12.449827293333545... .`                                      (5.1)

Then (2.2) and the exact physical completion (3.3) give

`boxed(||p_Q||_infinity
 <12.450 |a|^(-1/2).)`                                          (5.2)

In particular, if the chosen physical scalar pivot satisfies `|a|>=1/4`,

`boxed(||p_Q||_infinity <24.900.)`                               (5.3)

This retains every residual same-side quadratic term, every additional eigenvalue, every sign, and the original product law. No conditional spectral projection is used.

Thus a scalar-pivot survivor is no longer an undifferentiated aligned-E2 problem: its exact Schur residual either has a paid diffuse two-volume bank, or it enters one of only three concrete debts — high-leverage S0, shared-overlap S1, or principal-pair aggregate S2.

## 6. Exact interpretation of S1: shared minors are scalar-Schur edges or zero-self stars

For distinct `i,j,k`, let `d_k=S_kk`. The shared minor is

`det S[{k,i},{k,j}]=d_k S_ij-S_ik S_kj`.                        (6.1)

If `d_k!=0`, let `S^(k)` be the scalar Schur complement after pivoting physical coordinate `k`. Then exactly

`boxed(det S[{k,i},{k,j}]=d_k S^(k)_ij.)`                       (6.2)

If `d_k=0`, then instead

`boxed(det S[{k,i},{k,j}]=-S_ki S_kj.)`                         (6.3)

Hence S1 is not mysterious exterior algebra: it is an aggregate bank of genuine **second scalar-Schur edges**, together with exact zero-self two-edge stars. This preserves the critical distinction demanded by the live near-zero/same-square corrections: exact zero is treated as zero, while a merely small nonzero diagonal remains a genuine Schur pivot and is not replaced by the zero-self formula.

The newest account01/B02 fractional-trace theorem (2.3) immediately pays any S1 subpacket that, after this exact physical reduction, actually exposes a curvature-free affine hyperbolic variable on an independent bank. Arbitrary hidden curvature in that bank remains unpaid and is not discarded.

## 7. Source-valid adversary: S2 cannot be closed by selecting one physical pair

The aggregate S2 branch itself does **not** imply one physical pair with a universal determinant. There is a simple target-class family showing this sharply.

For integer `m>=3`, put

`S_m = direct_sum_(r=1)^m (J_m/m)`,                              (7.1)

where `J_m` is the all-ones `m x m` matrix. Then `S_m` has eigenvalue `1` with multiplicity `m` and all remaining eigenvalues zero, so

`s_2(S_m)=1`.                                                    (7.2)

For any two physical coordinates:

* if they lie in the same block, the principal `2 x 2` determinant is zero;
* if they lie in distinct blocks, the principal block is `diag(1/m,1/m)`, hence its determinant is `1/m^2`.

Therefore

`max_(i<j) |det S_m[{i,j},{i,j}]| = 1/m^2 ->0`,                 (7.3)

while the whole S2 bank is

`sum_(i<j) det S_m[{i,j},{i,j}]^2
 = binom(m,2)m^2 * m^(-4)
 = (m-1)/(2m) >=1/3`.                                          (7.4)

Thus the natural implication

`S2 aggregate >=1/3  =>  one principal pair has |det|>=c>0`

is false in the exact target geometry. Any local pair half-Riesz estimate paying `|det|^(-1/4)` loses like `sqrt(m)` on this family.

This is **not** a QFORM counterexample. Embed it as

`A_m = [1] direct_sum S_m`.                                     (7.5)

Then `A_m` has at least `m+1` eigenvalues equal to one. Moreover each block contribution is

`Y_r^2,   Y_r=m^(-1/2) sum_(j in block r) X_j`,                  (7.6)

and the `Y_r` are independent across disjoint ORIGINAL-coordinate blocks. The completed one-dimensional product-projection theorem gives `||p_(Y_r)||_infinity<=sqrt(e)`. Two same-sign squares therefore have convolution density at most `pi e`, and convolution with the other independent block contributions cannot increase that bound. So this family is uniformly paid by **bank aggregation**, exactly while every local principal-pair determinant vanishes asymptotically.

Classification of (7.3)-(7.6): `CANDIDATE_REFUTED` for the one-pair selector, not for QFORM.

## 8. Application of the current named partner and compact conditional proof map

The current named partner account03/B19 r17 is used upstream, not merely cited. Its three-heavy O0 closure removes every O0 state with at least three `3/4`-heavy physical rows. In the remaining at-most-two-heavy O0 state, prior B19 r16 produces the raw R0/R1/R2 alternatives and exact physical Schur inheritance. Whenever one of those surviving states exposes a nonzero scalar pivot, Theorems 3.1 and 4.1 now replace the local aligned selector by the exhaustive exact-Schur trichotomy S0/S1/S2. The diffuse S0 branch is paid by (5.2).

A correction-safe conditional end-to-end route is therefore:

1. Apply the completed low-offdiagonal / ridge / third-compound structural reductions at their exact source scopes.
2. In O0, use the current named partner to pay `>=3` heavy rows; only `<=2` heavy rows survive.
3. Use r16 to obtain physical Schur-compatible scalar/two-row packets without identifying raw orthogonal residuals with Schur blocks.
4. At every nonzero scalar pivot, use Theorem 3.1: the exact residual has `s_2>=1`.
5. Use Theorem 4.1 on that exact residual. Pay diffuse S0 by (5.2). Pay any S1 packet that truly meets the affine-hyperbolic provenance hypotheses by account01/B02. Do **not** select one pair from S2; (7.1)-(7.6) proves that shortcut false.
6. The remaining scalar-pivot debt is aggregate payment of high-leverage S0, curved S1, and diffuse S2 before reciprocal atom loss. The prior R2 indefinite/singular pair state and O1/O2/O3 remain separate obligations when no usable scalar pivot is available.

## 9. First unpaid implication with exact quantifiers

`QFORM-SCHUR-S2-AGGREGATE-HALFRIESZ-v1` (OPEN):

> There exists a universal finite `C_H` such that for every dimension `d`, every real symmetric `S` with `s_2(S)>=1`, every independent real `Z_1,...,Z_d` with densities at most one, every affine vector `ell`, and every constant `c`,
>
> `sup_t E |Z^T S Z + ell^T Z + c - t|^(-1/2) <= C_H`.          (9.1)

By Theorem 4.1 it is enough to prove (9.1) on the three source-valid aggregate branches S0/S1/S2. The diffuse S0 subbranch is already paid with constant `12.450`; the first genuine debt is therefore:

* high-leverage S0: `E_2(B)>=1/48` but both usable physical sides are leverage-heavy;
* curved S1: shared-minor mass `>=1/81` after excluding the exact affine-hyperbolic packets paid by (2.3);
* S2: principal-pair squared determinant mass `>=1/3`, paid **collectively**, not through one pair.

If (9.1) is proved, then every target form possessing a physical scalar pivot `|A_ii|>=alpha>0` has immediately

`||p_Q||_infinity <= C_H alpha^(-1/2)`                         (9.2)

by the exact completion (3.3). The complementary all-small-diagonal regime is then a pure high-offdiagonal/zero-self structural problem and can be routed through the existing overlap/ridge/hyperbolic machinery rather than through a fictitious local pair.

This is a strictly cleaner first missing implication than the incoming aligned-E2 local selector: it has exact quantifiers, arbitrary extra spectrum, exact original-product provenance, and an explicit aggregate counterexample showing why local pair selection cannot finish it.

## 10. Status

- `QFORM-SCALAR-SCHUR-S2-INHERITANCE-v1`: **PROVED**.
- `QFORM-SCHUR-S2-OVERLAP-REDUCTION-v1`: **PROVED**.
- Diffuse S0 scalar-pivot branch: **PAID**, `||p_Q||_infinity<12.450|a|^(-1/2)`.
- Exact S1 scalar-Schur/zero-star identity: **PROVED**.
- One-pair extraction from S2 aggregate: **REFUTED** by the exact target-class family (7.1)-(7.6).
- Full QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
- Continuity: not claimed for the new half-Riesz branch.

No numerical experiment is used as proof; a small checker beside this report records only the displayed arithmetic and finite-matrix sanity checks for the explicit S2 adversary.