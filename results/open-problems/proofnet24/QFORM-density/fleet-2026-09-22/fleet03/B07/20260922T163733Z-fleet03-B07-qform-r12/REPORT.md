# fleet03/B07 — full-matrix third-compound overlap reduction and ridge payment

**Run:** `20260922T163733Z-fleet03-B07-qform-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Final owner-control revision used for mathematics:** `2026-09-22.7`  
**Assignment:** Coordinate minor selection  
**Classification:** `PROVED FULL-TARGET STRUCTURAL REDUCTION + PAID DISJOINT-RIDGE SUBBRANCH / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and correction discipline

For every dimension, independent real coordinates `X_i` with probability densities bounded by one, and every real symmetric `A` having at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has a density whose essential supremum is bounded by one universal finite constant, or give a valid counterexample. Continuity is a separate requested conclusion.

This run uses no post-rotation independence, no law-uniform pointwise van-der-Corput estimate, no naive fiber-supremum integral, and no claim that a single small coordinate minor is enough. The full arbitrary matrix is retained throughout, including all additional spectral components.

The previous B07 state was the exact-rank-three nested-heavy disjoint-bank collar at

`yspennstate/math-open-problems@494c999fc67d230fff7e2079b1867216253b35bc`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260922T154026Z-fleet03-B07-qform-r11/REPORT.md`.

The owner proof-first continuation asks B07-type workers to attack an exhaustive product-preserving combination of ridge-certified diffuse branches with low-cross-rank grouped-coordinate branches. This run therefore changes mechanism from the preceding rank-three nested-heavy normal form to a **full-matrix exterior-power decomposition**.

The designated partner `fleet04/B07` still had no completed QFORM handoff or canonical QFORM directory at the fresh source check; no result is fabricated. The completed supporting ridge theorem actually applied below is the owner-supplied `QFORM-RIDGE-DENSITY-v1`, canonical proof

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`,

with the spectral-window perturbation/MSS portion independently passed by fleet03/B04 at

`yspennstate/math-open-problems@093c15486c794a2e8b23978ca7b289feabf999a7`.

The completed fleet04 theorem retained as the compatible fleet04 fallback is `QFORM-SCHUR-PIVOT-SMOOTHING-v1`,

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`.

## 2. Third compound mass of the full matrix

For `S,T subset {1,...,n}` with `|S|=|T|=3`, write `A[S,T]` for the corresponding `3 x 3` submatrix and define

`M_3(A)=sum_{|S|=|T|=3} det(A[S,T])^2`.                         (2.1)

By the singular-value identity for the third compound matrix,

`M_3(A)=|| wedge^3 A ||_HS^2
      =sum_{i<j<k} lambda_i(A)^2 lambda_j(A)^2 lambda_k(A)^2`.   (2.2)

Because at least three eigenvalues have absolute value at least one,

`boxed( M_3(A)>=1. )`                                            (2.3)

This already incorporates every extra eigenvalue and every sign.

Partition (2.1) by overlap size

`M_r = sum_{|S|=|T|=3, |S intersect T|=r} det(A[S,T])^2`,

for `r=0,1,2,3`. Then

`M_0+M_1+M_2+M_3=M_3(A)>=1`,                                    (2.4)

so at least one overlap class has mass at least `1/4`.

## 3. New theorem: dimension-free overlap-group selection

### Theorem 3.1 — `QFORM-THIRD-COMPOUND-OVERLAP-REDUCTION-v1`

For every real symmetric `A` satisfying the target spectral hypothesis, at least one of the following four coordinate-valid alternatives holds.

**O0: disjoint cross-volume.** There is a bipartition of the original coordinates `L disjoint_union R` such that, for `B=A[L,R]`,

`boxed( E_3(B):=sum_{S subset L,T subset R, |S|=|T|=3}
                 det(A[S,T])^2 >= 1/256. )`                     (3.1)

Equivalently `E_3(B)=e_3(s_1(B)^2,s_2(B)^2,...)`.

**O1: one-shared-coordinate aggregate.** There is a three-color partition `C,L,R` of the original coordinates such that

`boxed( sum_{i in C}
             sum_{S subset L, |S|=2}
             sum_{T subset R, |T|=2}
        det A[{i} union S,{i} union T]^2 >= 1/972. )`            (3.2)

**O2: two-shared-coordinate aggregate.** There is a three-color partition `C,L,R` such that

`boxed( sum_{I subset C, |I|=2}
             sum_{j in L}
             sum_{k in R}
        det A[I union {j}, I union {k}]^2 >= 1/324. )`           (3.3)

**O3: principal aggregate.** The full principal-triple mass obeys

`boxed( sum_{|S|=3} det A[S,S]^2 >= 1/4. )`                     (3.4)

All four alternatives are statements about original coordinates; no random-variable rotation is used.

### Proof

By (2.4), choose `r` with `M_r>=1/4`.

If `r=0`, color every coordinate independently `L/R` with probability `1/2`. Every ordered disjoint pair `(S,T)` uses six distinct coordinates and lands with `S subset L,T subset R` with probability `2^-6=1/64`. Hence the expected left side of (3.1) is `M_0/64>=1/256`; some deterministic bipartition attains at least that value.

If `r=1`, color every coordinate independently with one of `C,L,R`. An ordered pair `(S,T)` with one shared coordinate uses five distinct coordinates. The shared coordinate must receive color `C`, the two row-only coordinates color `L`, and the two column-only coordinates color `R`, a probability `3^-5=1/243`. Hence some partition has mass at least `M_1/243>=1/972`.

If `r=2`, the union has four distinct coordinates. The two shared coordinates must be in `C`, the row-only coordinate in `L`, and the column-only coordinate in `R`, probability `3^-4=1/81`. Thus some partition has mass at least `M_2/81>=1/324`.

If `r=3`, (3.4) is exactly `M_3>=1/4`. QED.

### Why this avoids the known cross-minor correction

The live correction `QFORM-CROSSMINOR-ALONE-FALSE` rules out promoting one cross minor to a universal certificate. Theorem 3.1 does not do that. It keeps the **entire squared determinant mass** in the selected overlap class. In particular, the singleton-plus-two-banks family may fall into O1/O2/O3 rather than being falsely forced into O0.

## 4. Direct attack on O0: regularized determinant payment from aggregate minors

The O0 branch is already compatible with the completed ridge theorem because the selected `L,R` are disjoint original-coordinate groups. Let `s_j` be the singular values of `B=A[L,R]`, let

`E=E_3(B)=e_3(s_j^2)>=1/256`,                                   (4.1)

and for `gamma>0` define

`K_gamma = B B^T (gamma^2 I + B B^T)^(-1)`,

`theta(gamma)=tr K_gamma`,

`D(gamma)=det(I+B B^T/gamma^2)`.                                (4.2)

Because `E>0`, `rank B>=3`, and `theta(gamma)` decreases continuously from `rank B` to zero. Therefore there is a unique positive `gamma_*` with

`theta(gamma_*)=8/3`.                                            (4.3)

### Lemma 4.1 — effective-rank cubic lower bound

Let

`k_j=s_j^2/(gamma_*^2+s_j^2)`.

Then `0<=k_j<1`, `sum k_j=8/3`, and

`boxed( e_3(k)>=2/3. )`                                          (4.4)

Proof: take independent Bernoulli variables `xi_j` with means `k_j` and put `N=sum xi_j`. Then

`e_3(k)=E[ binom(N,3) ]`.

For every integer `m>=0`, `binom(m,3)>=m-2`. Hence

`e_3(k)>=E[N]-2=8/3-2=2/3`. QED.

Put `y_j=s_j^2/gamma_*^2`. Since `y_j=k_j/(1-k_j)>=k_j`,

`E/gamma_*^6=e_3(y)>=e_3(k)>=2/3`,                               (4.5)

so

`gamma_*^6 <= (3/2) E`.                                          (4.6)

Also, by the Cauchy-Binet expansion of the regularized determinant,

`D(gamma_*)=prod_j(1+y_j)
 >= e_3(y)=E/gamma_*^6`.                                         (4.7)

### Theorem 4.2 — `QFORM-O0-RIDGE-PAYMENT-v1`

Assume in addition that the physical row ridge leverages satisfy

`max_{i in L} (K_gamma*)_ii <=1/2`.                              (4.8)

Then the completed `QFORM-RIDGE-DENSITY-v1` theorem applies with `q=1` and `theta=8/3`, giving a **continuous** density and

`||p_Q||_infinity
 <= e/(sqrt(2) gamma_*) * [theta/(theta-2)] * D^(-1/(2theta))`

` = (4e)/(sqrt(2) gamma_*) D^(-3/16).`                           (4.9)

Use (4.7):

`D^(-3/16) <= (gamma_*^6/E)^(3/16)`.

Hence

`||p_Q||_infinity
 <= (4e/sqrt(2)) gamma_*^(1/8) E^(-3/16).`                       (4.10)

From (4.6),

`gamma_*^(1/8) <= [(3/2)E]^(1/48)`,

and therefore

`boxed(
 ||p_Q||_infinity
 <= 2 sqrt(2) e (3/2)^(1/48) E^(-1/6).
)`                                                               (4.11)

With the O0 guarantee `E>=1/256`,

`boxed( ||p_Q||_infinity < 19.54. )`                             (4.12)

Thus an entire full-matrix overlap class is paid without selecting any one tiny minor.

## 5. Exact residual when O0 is not paid: a ridge-heavy physical row

If (4.8) fails, there is an original coordinate `i in L` with

`(K_gamma*)_ii>1/2`.                                             (5.1)

This has an exact determinant-weight interpretation. Let

`Lmat=B B^T/gamma_*^2` and `D=det(I+Lmat)`.

Define a determinantal row-subset law by

`P(S)=det(Lmat[S,S])/D`.

Cauchy-Binet gives

`det(Lmat[S,S])
 = gamma_*^(-2|S|)
   sum_{T subset R, |T|=|S|} det(B[S,T])^2`.                    (5.2)

The standard L-ensemble marginal identity gives

`P(i in S)=(K_gamma*)_ii>1/2`.                                  (5.3)

So failure of the ridge payment does not return an arbitrary tiny coordinate minor: it returns a **specific original physical coordinate carrying more than half of the entire regularized determinant weight**. This is exactly the source-valid input required by heavy-row / grouped-coordinate mechanisms.

The newest compatible grouped-coordinate peer result, fleet02/B01 `QFORM-CONDITION-ONE-HEAVY-ROW-v1` at

`yspennstate/math-open-problems@007d06d8118bc87becd247676c7a63ae336755c9`,

shows that in the rank-two-plus-independent-square normal form, conditioning one heavy residual row and whitening the remaining frame gives

`||p_Q||_infinity
 <= 2*3^(1/4)*sqrt(pi e)
    |d|^(-1/2)[(1-c)|det Gamma|]^(-1/4)`                         (5.4)

whenever the whitened remaining rank-two frame has row leverage at most `1/2`. Equation (5.3) supplies the correct kind of heavy physical coordinate, but the missing full-target implication is to convert the **ridge-DPP heavy row of a general cross block** into the precise rank-two-plus-square grouped normal form of (5.4), or into one of the O1/O2 overlap branches, without discarding arbitrary self blocks.

The completed fleet04/B18 theorem separately discharges any resulting physical triple with minority-sign scalar pivot `a` and definite Schur complement:

`||p_Q||_infinity <= 2 sqrt(pi)(|a det B_3|)^(-1/4)`.             (5.5)

This is retained as the exact pivot payment; no lower bound for `|a det B_3|` is asserted from (5.3).

## 6. Smallest conditional end-to-end deduction

Theorem 3.1 converts the full target, with arbitrary additional spectrum, into four source-valid aggregate overlap classes. O0 is completely paid by (4.12) whenever its calibrated ridge kernel is diffuse. Therefore a full proof follows if the following three implications are established with universal constants:

1. **O0-heavy reduction:** from (5.3), pass a ridge-DPP-heavy physical row to a completed grouped-coordinate payment, or show it transfers a fixed fraction of third-compound mass into O1/O2/O3 after conditioning.
2. **O1/O2 payments:** control the one-shared and two-shared determinant aggregates directly by product-preserving grouped-coordinate smoothing, without reciprocal selection of one vanishing minor.
3. **O3 payment:** control the aggregate principal-triple branch, again without assuming one principal triple has a dimension-free determinant.

The first unpaid implication is (1). It is now quantitative: the heavy row has regularized determinant inclusion probability strictly greater than `1/2` at a scale where the effective rank is exactly `8/3`, while the total disjoint third-minor mass is at least `1/256`.

## 7. Status and limitations

* `QFORM-THIRD-COMPOUND-OVERLAP-REDUCTION-v1`: **PROVED**, full-matrix structural theorem.
* `QFORM-O0-RIDGE-PAYMENT-v1`: **PROVED conditional analytic payment**, using the completed ridge theorem under its exact row-leverage gate.
* O0 ridge-heavy branch and O1/O2/O3 aggregate payments: **OPEN**.
* Full universal QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
* Continuous density: **proved only on the O0 ridge-paid subbranch through the ridge theorem; not proved for the full target**.

No schedule, enabled/paused state, notification setting, email, Drive, public workflow, paid model/API/Codex, credentials, cross-account authentication or unrelated data is used or changed by this report.
