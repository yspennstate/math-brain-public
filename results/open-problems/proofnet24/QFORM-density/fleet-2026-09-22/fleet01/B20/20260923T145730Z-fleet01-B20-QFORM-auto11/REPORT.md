SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B20, 2026-09-23T14:47:00Z.
attacking: the fresh absolute rank-two physical cross tube, converting its spectral R1/R2 survivors into original-coordinate source-bank packets without deleting the singular tail.

# fleet01/B20 — absolute-rank-two tube to physical-bank compiler

**Status:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL QFORM OPEN`.  
Full-target continuity remains **OPEN**.  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and correction discipline

The target remains: for every dimension, every family of independent real random variables with densities bounded by one, and every real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove a universal finite essential bound for the density of `Q=X^T A X`, or give a valid counterexample. Continuity is tracked separately.

No Gaussianity, moment, iid, compact-support, log-concavity, spectral-coordinate independence, law-uniform pointwise quadratic oscillatory decay, arbitrary-joint rank-three coarea cap, worst-fiber supremum, random-tail deletion, or one-good-minor inference is used below.

## 2. Fresh completed partner result actually consumed

The designated completed partner is fleet02/B20 run

`20260923T142651Z-fleet02-B20-QFORM-auto11`,

with source-pinned handoff in `yspennstate/math-research-brain` and canonical mathematics refreshed through

`yspennstate/math-open-problems@a996362199678ee069db30c5ab31a44b2d3d29d6`.

Together with its fresh fleet03/B20 dependency, the current physical cross block `N=A[J,K]` in `N3(1/64)` satisfies

`E:=||N||_F^2 > E0:=11907/16384`,

and every still-unpaid strong-top-four state lies in one of the two source-valid alternatives

**R1**

`s2 <= s1/16`,  `sum_(r>=2) s_r^2 < s1^2/36`,

or

**R2**

`sum_(r>=3) s_r^2 < (3/64)E`,  `s1*s2 > delta:=726327/33554432`.

The new fleet02/B20 closure further proves, for every still-unpaid state in these alternatives,

`boxed: s3(N)<1/64`.                                                   (2.1)

This run applies (2.1) to the actual coordinate-restriction inequality

`dist_op(N[L,R], rank<=2)`
` <= ||N[L,R]-N_2[L,R]||_op`
` <= ||N-N_2||_op`
` = s3(N) <1/64`                                                       (2.2)

for **every literal physical subblock** `N[L,R]`, where `N_2` is the deterministic best rank-two SVD truncation. Equation (2.2) is coefficient geometry only; no rotated random variable is introduced.

## 3. Physical entry cap in N3(1/64)

For every original-coordinate cross entry `N_ij=A_ij`, the defining physical `1x1/2x2` N3 inequalities give

`|A_ii|<1/64`, `|A_jj|<1/64`,
`|A_ii A_jj-A_ij^2|<1/64`.

Therefore

`A_ij^2 <= |A_ii A_jj|+|A_ii A_jj-A_ij^2|`
`         <1/4096+1/64=65/4096`,

so

`boxed: |N_ij| < eta:=sqrt(65)/64`.                                  (3.1)

This source-coordinate cap is the key extra input for the rank-one tube.

## 4. R1: one singular side is quantitatively diffuse

Assume R1. Write the top singular decomposition

`N=s1 u v^T+R`, `||R||_op=s2<=s1/16`,

with `||u||_2=||v||_2=1`. Since

`E=s1^2+sum_(r>=2)s_r^2 < (37/36)s1^2`,

we have

`s1^2 > (36/37)E0 =107163/151552`
`                  =169/256 +7115/151552`,

hence

`boxed: s1>13/16`.                                                     (4.1)

Let

`alpha=max_i |u_i|`, `beta=max_j |v_j|`.

Choose physical indices attaining these maxima. By (3.1),

`s1 alpha beta`
` <= |N_ij|+|R_ij|`
` < eta+s1/16`,

so, using (4.1),

`alpha beta < eta/s1+1/16`
`            < sqrt(65)/52+1/16`
`            <7/32`.                                                   (4.2)

The final strict inequality is elementary: it is equivalent to
`32 sqrt(65)<260`, whose square is `66560<67600`.

Since `min(alpha^2,beta^2)<=alpha beta`, (4.2) proves

`boxed: min(max_i u_i^2, max_j v_j^2)<7/32`.                          (4.3)

Thus at least one top singular side is genuinely diffuse in the **original physical indexing**.

### 4.1 Two strong disjoint physical source banks

Suppose for definiteness that `max_i u_i^2<7/32`; the column case is symmetric. The weights `u_i^2` sum to one and each is `<7/32`. Greedily collect a physical subset `J1` until its mass first reaches `25/64`. Because the last added weight is `<7/32`,

`25/64 <= ||u_{J1}||_2^2 <25/64+7/32=39/64`.

With `J2=J\J1`, both banks satisfy

`boxed: ||u_{Jq}||_2^2 >=25/64, q=1,2`.                              (4.4)

Test each actual subblock `N[Jq,K]` against the physical-coordinate vector `v`:

`||N[Jq,K]||_op`
` >= ||N[Jq,K]v||_2`
` >= s1||u_{Jq}||_2-||R[Jq,K]v||_2`
` >= (5/8)s1-s2`
` >= (9/16)s1`
` >117/256`.                                                          (4.5)

Combining (4.5) with the completed partner inequality (2.2), each of the two **disjoint original-coordinate source banks** obeys

`boxed: ||N[Jq,K]||_op>117/256,`
`boxed: dist_op(N[Jq,K], rank<=2)<1/64, q=1,2`.                       (4.6)

In relative terms the inherited absolute rank-two error is below

`(1/64)/(117/256)=4/117<0.035`                                       (4.7)

of each subblock's operator norm.

This is a strict narrowing of the R1 tube: it is no longer merely a spectral near-rank-one statement. It contains two strong, disjoint, literal source-coordinate banks on one side, each coupled to the opposite bank, and each remains in the partner's absolute rank-two tube.

## 5. R2: a four-bank physical second-volume packet

Assume R2. By Cauchy--Binet,

`e2(N^T N)=sum_(|S|=|T|=2) det N[S,T]^2`
`          =sum_(r<s)s_r^2 s_s^2`
`          >=s1^2 s2^2`
`          >delta^2`.                                                 (5.1)

Independently two-color the original row indices and original column indices. Any fixed row pair is separated with probability `1/2`, and any fixed column pair is separated with probability `1/2`. Hence the expected mass of minors whose two rows and two columns are both separated is one quarter of (5.1). Therefore there are literal partitions

`J=J1 disjoint_union J2`, `K=K1 disjoint_union K2`

such that

`P2:=sum_(i in J1,k in J2,j in K1,l in K2)`
`       det[[N_ij,N_il],[N_kj,N_kl]]^2`
`   >delta^2/4`
`   =527550910929/4503599627370496`
`   =1.17139833595e-4`.                                               (5.2)

This spends the **aggregate** second volume before localizing any individual minor.

For each determinant, `(ad-bc)^2<=2(a^2d^2+b^2c^2)`. Put

`E_pq=||N[Jp,Kq]||_F^2`.

Summing this elementary inequality over (5.2) gives

`P2 <=2(E11 E22+E12 E21)`.                                           (5.3)

Consequently one of the two opposite matchings satisfies

`boxed: max(E11 E22,E12 E21)>delta^2/16`
` =527550910929/18014398509481984`
` =2.92849583988e-5`.                                                 (5.4)

Again the completed partner theorem is inherited **on every one of the four actual physical blocks** through (2.2):

`boxed: dist_op(N[Jp,Kq], rank<=2)<1/64, p,q in {1,2}}`.              (5.5)

No inference from (5.2)--(5.4) to a single good coefficient or a single good minor is made. The resource remains aggregate, exactly as required by the live corrections.

## 6. New compiler and what it closes

The preceding arguments prove the following source-valid structural theorem.

### Theorem — `QFORM-N3-ABS-RANK2-TUBE-PHYSICAL-BANK-COMPILER-v1`

For the current strong-top-four physical cross survivor with

`E>11907/16384`

and the completed fleet02/B20 closure `s3(N)<1/64`, every unpaid state satisfies one of two strictly narrower physical-coordinate packets:

1. **R1 two-source-bank packet.** On one side the top singular vector has maximum squared physical coordinate `<7/32`; that side splits into two disjoint original-coordinate banks, each having cross operator norm `>117/256` to the opposite bank and absolute distance `<1/64` from rank at most two.

2. **R2 four-bank matching packet.** There are original-coordinate row/column bipartitions whose separated `2x2` minor mass is `>delta^2/4`, and one opposite matching of physical cross blocks has Frobenius-energy product `>delta^2/16`; every such block remains within operator distance `<1/64` of rank at most two.

This converts the newest **spectral** obstruction into literal product-source bank currencies. The full conjecture is not claimed.

## 7. First remaining implication

The first remaining closure edge is now

`QFORM-N3-PHYSICAL-R1-TWOSOURCE-OR-R2-FOURBANK-PAYMENT-v1`:

> Pay the two-source-bank R1 packet or the four-bank R2 matching packet while retaining arbitrary same-bank quadratic curvature, the full singular tail, and all outside couplings.

Two existing receivers are now directly adjacent:

- fleet02/B20's augmented-three-volume identity/D' payment can be applied as soon as an actual hub or same-bank arm has fixed transverse mass to the current top-two cross span and the resulting three-volume marginals are diffuse;
- fleet01/B09's physical indefinite-pair-plus-one-Schur-cross theorem can be applied as soon as one of these physical bank packets supplies a quantitative invertible indefinite pair and surviving Schur cross resource.

The unresolved work is precisely the complementary aligned/concentrated case. In particular, (5.4) must **not** be replaced by a false claim that one universally large physical pair/minor exists.

## 8. Arithmetic checks

`E0 =11907/16384 =0.72674560546875`.

`(36/37)E0 =107163/151552 =0.707103832347973... >169/256`.

`eta=sqrt(65)/64 =0.125972777317...`.

The sharper numerical value in (4.2), using the exact lower bound on `s1`, is `<0.212309`; the proof uses the clean rational threshold `7/32=0.21875`.

`117/256=0.45703125`, and `(1/64)/(117/256)=4/117=0.0341880...`.

`delta=726327/33554432=0.0216462314129...`.

`delta^2/4=1.17139833595e-4` and `delta^2/16=2.92849583988e-5`.

## 9. Scope/status

The completed partner result was consumed at the actual coordinate-restriction inequality (2.2), not cited decoratively. The new theorem is deterministic/source-coordinate geometry layered on the fresh R1/R2 packet. It proves a quantitative supporting implication satisfying the B20 closure assignment, but **does not yet prove the full QFORM theorem** and does not establish global continuity.
