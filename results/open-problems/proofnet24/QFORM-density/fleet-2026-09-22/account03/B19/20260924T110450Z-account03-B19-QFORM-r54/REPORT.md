SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B19, 2026-09-24T11:04:50Z.
attacking: the r51 BL-compatible robust rank-two survivor; replace dimension-many rowwise alignment errors by a setwise aggregate third-volume compiler and a finite seven-packet curvature collar.

# account03/B19 r54 — setwise aggregate third-volume compiler and seven-packet collar

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Universal proof assembly / quantitative inequalities and rigorous computations  
Run: `20260924T110450Z-account03-B19-QFORM-r54`  
Status: **NEW TARGET-LEVEL PAYMENT + DIMENSION-FREE SETWISE COLLAR / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**. Repository access is not native learned-memory receiver ingestion.

All sets below are literal ORIGINAL-coordinate sets. Orthogonal transformations are used only inside deterministic coefficient-space proofs. No random coordinate is rotated. No Gaussian, log-concavity, moment, compact-support, connected-support, iid, arbitrary-joint coarea, conditional-density-cap, fiber-supremum, pointwise van-der-Corput, or small-coefficient-means-small-random-variable assumption is used. Every nonzero coefficient tail remains in the actual quadratic form.

## 1. Source-pinned frontier and conditional proof assembly


The immediate same-slot input is r51:

- `yspennstate/math-open-problems@bcb36a7573a7e9f23f1ea78792e0b72bc8bb0d9c`
- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260924T060028Z-account03-B19-QFORM-r51/REPORT.md`.

It starts from an ultra-thin actual physical rank-two crossing `N=A[R,C]` with top-two approximation `N_2=U Sigma V^T`,

`||N-N_2||_F < tau`, `tau=2^-16`,                               (1.1)

`sigma_2(N)>=1/64`,                                                (1.2)

and peels at most six leverage-heavy coordinates per bank. In its robust branch, with literal light banks `L_R,L_C`, the rank-two restriction

`M_0=N_2[L_R,L_C]`                                                 (1.3)

has

`sigma_2(M_0)>=1/112`,                                             (1.4)

while the actual light-light crossing

`M=A[L_R,L_C]`                                                     (1.5)

satisfies

`sigma_2(M)>1/112-2^-16=4089/458752`.                              (1.6)

The normalized restricted right coefficient plane has an orthonormal physical frame `Vtilde` on `L_C` with

`Vtilde^T Vtilde=I_2`, `max_j ||Vtilde_j||^2<=1/2`.                (1.7)

The transposed statement holds on the left bank. r51 supplied a full-law `H_{1/4}` resource but not an `L^infinity` endpoint because arbitrary same-bank curvature and the genuine tail in (1.1) remained.

r49 organized that same-bank curvature into finite latent/hub structure plus diffuse residuals, but its first common-plane step still originated from one-coordinate deletion estimates. The present run changes mechanism: it deletes an arbitrary **set** of total top-plane leverage at most one half and spends the **aggregate Frobenius transverse curvature of the entire set at once**. This directly removes the dimension-summation defect.

The completed physical-third-volume receiver used below is `QFORM-CROSS-E3-MARGINALFREE-L1-v1`: for a literal disjoint physical cross block `K=A[I,J]`, if

`E_3(K):=e_3(KK^T)>0`,                                           (1.8)

then the FULL ambient quadratic law has a continuous `C_0` density and

`||p_Q||_infinity <= C_E3 E_3(K)^(-1/6)`,                         (1.9)

where

`C_E3=3*2^(4/3)*exp(1/3)=10.550168831164775...`.                  (1.10)

Thus arbitrary self blocks, outside couplings, affine terms, signatures and extra spectrum remain present.

A fresh fleet reduction from account03/B12 is also recorded for the global proof tree:

- `yspennstate/math-open-problems@9bcbbbdb12483a06b15d7923ec4324422924d781`.

It proves that **189 or more** eigenvalues of absolute value at least one already imply a continuous universal density bound; hence the global target may be reduced to 3--188 target-scale eigenvalues. This is not used in the algebra below, but it removes the unbounded-large-spectrum branch from the final assembly.

## 2. Aggregate promoted-row identity

The first new lemma is purely deterministic.

### Lemma 2.1 — `QFORM-AGGREGATE-PROMOTED-ROWS-E3-v1`

Let `M` be an `r x c` real matrix with singular values

`s_1(M)>=s_2(M)>0`,                                                (2.1)

and let `W=V_2(M)` be any top-two right singular subspace. Let `D` be a `k x c` real matrix and stack

`K=[M; D]`.                                                        (2.2)

Then

`boxed: E_3(K) >= [s_1(M)s_2(M)]^2 ||D P_(W^perp)||_F^2.`         (2.3)

Repeated top singular values cause no problem: any orthonormal top-two singular pair may be used.

#### Proof

Take an SVD of `M` and rotate only its coefficient row space, leaving the rows of `D` untouched. Since `E_3(K)` is the squared Hilbert--Schmidt norm of the third compound, it is invariant under this block-orthogonal row operation. The first two transformed rows of the `M` block are

`s_1 v_1^T`, `s_2 v_2^T`,                                        (2.4)

for orthonormal `v_1,v_2` spanning `W`.

Fix a row `d_alpha^T` of `D`. Sum the squares of all `3x3` minors using precisely the two rows in (2.4) and this one row of `D`. By Cauchy--Binet / the exterior-product norm identity, that sum is

`||s_1 v_1 wedge s_2 v_2 wedge d_alpha||^2
 =s_1^2 s_2^2 ||P_(W^perp)d_alpha||^2`.                           (2.5)

These minors are a subset of the nonnegative terms defining `E_3(K)`. Summing (2.5) over all rows of `D` gives (2.3). QED.

This is the setwise form of the earlier one-promoted-row inequality: an arbitrarily large packet of physical rows is paid by its **total transverse Frobenius energy**, not by a dimension-dependent sum of rowwise density estimates.

## 3. Set deletion preserves the robust rank-two crossing

Return to the r51 robust branch. Write the rank-two restriction in orthonormal-frame form

`M_0=Utilde H Vtilde^T`,                                          (3.1)

where `Utilde,Vtilde` have orthonormal columns and, by (1.4),

`sigma_2(H)>=1/112`.                                               (3.2)

Let `S subset L_C` be any literal set satisfying the **aggregate leverage budget**

`sum_(j in S) ||Vtilde_j||^2 <=1/2`,                              (3.3)

and put

`J=L_C\S`.                                                         (3.4)

Then

`Vtilde_J^T Vtilde_J
 =I_2-Vtilde_S^T Vtilde_S
 >=[1-tr(Vtilde_S^T Vtilde_S)]I_2
 >=(1/2)I_2`.                                                      (3.5)

Hence the restricted rank-two approximant satisfies

`sigma_2(M_0[:,J])>=1/(112 sqrt(2))`.                             (3.6)

The actual block is

`M_S:=A[L_R,J]=M_0[:,J]+F[:,J]`,                                  (3.7)

where `||F[:,J]||_op<=||F||_F<2^-16`. Weyl gives

`boxed:
 sigma_2(M_S)>b_*:=1/(112 sqrt(2))-2^-16
                 =0.006298194614388817... .`                     (3.8)

This is a literal physical crossing, and no coefficient tail has been deleted.

## 4. Main target-level payment: any setwise transverse packet is terminal

Because `L_R`, `S` and `J` are pairwise disjoint original-coordinate sets, the stacked matrix

`K_S:=A[L_R union S,J]
    =[ M_S ; A[S,J] ]`                                             (4.1)

is a genuine physical cross block. Let

`W_S=V_2(M_S)`,                                                    (4.2)

and define its aggregate same-bank transverse currency

`Delta(S):=||A[S,J] P_(W_S^perp)||_F
         =dist_F(A[S,J], {matrices whose rowspace is in W_S}).`    (4.3)

Lemma 2.1 and (3.8) give

`E_3(K_S)>=b_*^4 Delta(S)^2`.                                     (4.4)

Combining with the full-ambient physical-`E3` receiver proves:

### Theorem 4.1 — `QFORM-R51-SETWISE-TRANSVERSE-E3-PAYMENT-v1`

For every `S subset L_C` satisfying (3.3), if `Delta(S)>0`, then the full target law has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity
 <=C_E3 [b_*^4 Delta(S)^2]^(-1/6)
 =C_E3 [b_*^2 Delta(S)]^(-1/3).`                                 (4.5)

At the concrete gate

`Delta(S)>=zeta_0:=2^-12`,                                        (4.6)

this becomes

`boxed: ||p_Q||_infinity <4949.584 <4950.`                        (4.7)

The transposed theorem holds for sets on the left bank.

This is an actual endpoint for arbitrary signs, degeneracies outside the displayed positive singular values, arbitrary independent cap-one laws, arbitrary same-bank curvature not contained in `A[S,J]`, arbitrary outside couplings, and arbitrary affine terms. Continuity is proved on this paid branch.

The contrapositive is the important structural output. Every r51 robust state that is still unpaid at constant 4950 must satisfy, **simultaneously for every leverage-budget set S**,

`boxed: Delta(S)<2^-12.`                                         (4.8)

Unlike the earlier one-coordinate condition, (4.8) controls the Frobenius transverse error of a whole physical set with one dimension-free number.

## 5. At most seven packets suffice to cover the whole light bank

The row leverages

`ell_j=||Vtilde_j||^2`                                             (5.1)

satisfy

`0<=ell_j<=1/2`, `sum_j ell_j=2`.                                 (5.2)

### Lemma 5.1 — seven-bin leverage partition

The coordinates can be partitioned into

`L_C=S_1 disjoint_union ... disjoint_union S_m`,                  (5.3)

with

`m<=7`, `sum_(j in S_g) ell_j<=1/2` for every g.                  (5.4)

#### Proof

Use the next-fit bin rule of capacity `1/2`: append coordinates to the current bin until the next coordinate would make the leverage sum exceed `1/2`, then open a new bin. Every coordinate individually fits by (5.2).

Whenever a new bin opens, the load of the previous bin plus the first item of the new bin is strictly greater than `1/2`. Therefore, pairing consecutive bins `(1,2),(3,4),...`, the total leverage in each pair is strictly greater than `1/2`. Eight bins would contain four such pairs and hence total leverage strictly greater than `2`, contradicting (5.2). Thus `m<=7`. QED.

Apply Theorem 4.1 to every `S_g`. In every still-unpaid state there is a rank-at-most-two matrix `L_g` on the directed block `S_g x (L_C\S_g)` such that

`||A[S_g,L_C\S_g]-L_g||_F<2^-12`.                                (5.5)

Summing the squared errors gives the dimension-free packet bound

`boxed:
 sum_(g=1)^m ||A[S_g,L_C\S_g]-L_g||_F^2
 <7*2^-24.`                                                       (5.6)

No factor depending on `|L_C|` appears.

### Corollary 5.2 — finite-rank inter-packet collar

Let `O` denote the matrix obtained from `A[L_C,L_C]` by zeroing every within-packet block `S_g x S_g`; thus `O` contains exactly the inter-packet same-bank curvature. Form the nonsymmetric matrix `L` whose row block on `S_g` is `L_g` on `L_C\S_g` and zero on `S_g`. Then

`rank L<=2m<=14`,                                                 (5.7)

and by (5.6)

`||O-L||_F<sqrt(7)2^-12`.                                        (5.8)

Since `O=O^T`, define

`K_inter=(L+L^T)/2`.                                               (5.9)

Then

`rank K_inter<=28`,                                               (5.10)

and

`boxed: ||O-K_inter||_F<sqrt(7)2^-12
                    =0.000645935... .`                           (5.11)

Indeed

`||O-K_inter||_F
 <=[||O-L||_F+||O-L^T||_F]/2
 =||O-L||_F`.                                                      (5.12)

Thus the previously dimension-many common-plane errors have been replaced by a finite object:

> at most seven literal self-curvature chambers, plus one symmetric rank-at-most-28 inter-chamber carrier, plus a genuine Frobenius tail below `sqrt(7)2^-12`.

The within-chamber matrices `A[S_g,S_g]` are retained **exactly**; they are not declared small or discarded. The same construction applies independently on the `L_R` bank.

Combining both banks, the still-unpaid r51 robust branch has at most fourteen literal self-curvature chambers; all curvature joining distinct chambers on the same side is absorbed into rank at most 56 plus Frobenius error below `sqrt(14)2^-12`, while the original actual `R--C` crossing and its nonzero tail remain untouched. This is a deterministic compiler, not yet a full density theorem.

## 6. Designated account04/B19 result applied at the new deleted-set scale

The latest completed designated-partner theorem is the corrected

`QFORM-FINITECARRIER-CURVED-R2-TERMINAL-v1`,

from

`yspennstate/math-open-problems@97c4f5328da327cae4249c40253e466603b2ba5c`,

with the canonical correction addendum in the partner r5 run. For an exact literal packet

`[[0,B,0],[B^T,C,h],[0,h^T,a]]`,                                  (6.1)

with arbitrary symmetric `C`, arbitrary `h`, `a!=0`, and `sigma_2(B)>0`, it proves

`||p_Q||_infinity
 <=min{2sqrt(pi)/sqrt(sigma_1(B)sigma_2(B)),
       4sqrt(2)/sqrt(|a|sigma_1(B))}.`                             (6.2)

The new set-deletion estimate (3.8) supplies an actual numerical scale for the first term whenever a subsequent structural router produces this partner theorem's **exact** packet with `B=M_S`. Since `sigma_1(M_S)>=sigma_2(M_S)>b_*`,

`boxed:
 ||p_Q||_infinity
 <2sqrt(pi)/b_*
 =562.8451... <563.`                                              (6.3)

This is strictly inside the partner theorem's proved scope. No merely small self block is set to zero, and this report does not claim that every seven-packet survivor automatically has form (6.1). Equation (6.3) is the concrete terminal once the exact zero-self-side packet is genuinely manufactured.

## 7. Compact conditional proof assembly after r54

The current end-to-end map is now:

1. The diagonal branch is paid by the elementary same-sign pair argument; general rotated `C=pi` is not asserted.
2. Existing principal-block, pair-log, affine half-Riesz, grouped-square/star, ridge-window, physical-E3 and finite-carrier receivers pay their exact source-valid branches.
3. Fresh account03/B12 closes every state with at least 189 target-scale eigenvalues, leaving only 3--188 globally.
4. r47--r51 funnel one major singular-pair chamber into a robust physical rank-two crossing with BL-compatible coefficient planes, or into explicit finite hub/star alternatives.
5. The present r54 theorem pays **any** aggregate same-bank packet whose transverse Frobenius currency exceeds `2^-12`, with continuous density `<4950`.
6. Therefore every unpaid robust-rank-two state satisfies the simultaneous setwise collar (4.8). A whole light bank is representable by at most seven overlapping rank-two packets, equivalently by at most seven exact self-curvature chambers plus a rank-28 inter-chamber carrier and the explicit small Frobenius tail (5.11). The bilateral state has at most fourteen chambers.
7. Whenever this finite packet geometry produces the exact account04/B19 curved-rank-two packet, the partner terminal (6.3) pays it below 563.

The first essential missing implication on this route is now

`QFORM-FOURTEEN-CHAMBER-SYMMETRY-GLUE-OR-EXACT-PACKET-ENDPOINT-v1`:

> exploit symmetry and the overlaps among the at-most-seven setwise rank-two packets on each bank to merge the remaining exact within-chamber self curvature into a finite latent/hub carrier, or force an already-paid exact physical pair / finite-carrier / E3 / ridge endpoint. The new Frobenius errors are dimension-free and must remain in the actual coefficient matrix; the within-chamber blocks are not small and may not be discarded.

This is a strictly smaller debt than r49's dimension-many rowwise alignment problem. The giant near-rank-one crossing, small-Pluecker aggregate branch, and hub-star branch remain parallel global debts and are not renamed as solved.

## 8. Exact finite checks

A reproducible checker in this run verifies three deterministic identities/inequalities:

1. 3,000 random noncommuting rectangular instances of Lemma 2.1: minimum observed `E_3/RHS = 0.9999999999999974`, zero violations.
2. 4,109 admissible random set deletions with row leverage at most `1/2`: minimum observed margin above `b_*` was `4.0693789e-5`, zero violations.
3. 10,000 random leverage arrays produced at most seven next-fit bins; 2,000 random symmetric packet systems verified the symmetrization inequality (5.12), maximum error/packet-residual ratio `1.0000000000000002` (floating roundoff), zero mathematical violations.

These computations are diagnostics only; Sections 2--5 contain exact proofs.

## 9. Quantifiers, signs, degeneracies and regularity

The new coefficient inequalities are sign-free. Repeated singular values are allowed. Exact zero transverse currency is retained as the collar branch; it is never divided by. The probabilistic endpoint invokes only the source-valid physical-E3 theorem on a literal disjoint original-coordinate cross block, so it retains arbitrary independent densities `0<=f_i<=1`, arbitrary same-bank curvature, arbitrary outside couplings, arbitrary affine terms and extra signed spectrum.

Full QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full universal continuity: **OPEN**.  
Continuity: **proved on the new setwise-E3 paid branch; not proved on the seven-packet survivor as a whole**.
